/* ForecastData.tsx — Overlay chart (all series) + table, with hardcoded id filter (Z/C/B) + Hide Legend toggle */

import React from "react";
import { Table, Typography, Tag, Space, Divider, Select, Switch } from "antd";
import { fetchForecasts } from "../api";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
} from "recharts";

// -------- Types --------
type HistoryPoint = { term: string; value: number | null; isPred: boolean };
type SeriesItem = {
  key: string;                 // e.g., "B", "C", "UNIV"
  kind: "department" | "overall" | string;
  title: string;               // label to show
  history: HistoryPoint[];
  next_point?: HistoryPoint | null;     // {term: nextTerm, value, isPred:true}
  department_letter?: string;
  department_title?: string;
};
type MetaBlock = {
  metric: string;
  terms: string[];
  next_term: string;
  units: string;
  agg?: string;
  dept_letter?: string;
  generated_at?: string;
};
type ForecastResponse = { meta: MetaBlock; series: SeriesItem[] };

const kindColor = (k?: string) => {
  switch ((k || "").toLowerCase()) {
    case "department": return "blue";
    case "overall":    return "purple";
    default:           return "default";
  }
};
const fmt = (v?: number | null, digits = 3) =>
  v == null || Number.isNaN(v) ? "-" : Number(v).toFixed(digits);

// ---- Helpers to build per-series datasets for overlay lines ----
function buildSeriesDatasets(terms: string[], s: SeriesItem) {
  const actual = terms.map((t) => {
    const hp = s.history.find(h => h.term === t && !h.isPred);
    return { term: t, value: hp?.value ?? null, title: s.title, key: s.key };
  });

  let pred: { term: string; value: number | null; title: string; key: string }[] = [];
  if (s.next_point?.term) {
    let lastVal: number | null = null;
    let lastTerm: string | null = null;
    for (let i = terms.length - 1; i >= 0; i--) {
      const t = terms[i];
      const hp = s.history.find(h => h.term === t && !h.isPred && h.value != null);
      if (hp) { lastVal = hp.value!; lastTerm = t; break; }
    }
    if (lastTerm != null) {
      pred = [
        { term: lastTerm, value: lastVal, title: s.title, key: s.key },
        { term: s.next_point.term, value: s.next_point.value ?? null, title: s.title, key: s.key },
      ];
    }
  }
  return { actual, pred };
}

function computeYDomain(allActual: any[][], allPred: any[][]) {
  const vals: number[] = [];
  for (const arr of [...allActual, ...allPred]) {
    for (const d of arr) {
      const v = d?.value;
      if (v != null && !Number.isNaN(v)) vals.push(v);
    }
  }
  if (!vals.length) return [0, 1];
  const lo = Math.min(...vals), hi = Math.max(...vals);
  const pad = Math.max(0.05, (hi - lo) * 0.1);
  return [lo - pad, hi + pad];
}

const PALETTE = [
  "#1677ff", "#52c41a", "#fa8c16", "#eb2f96", "#722ed1",
  "#13c2c2", "#a0d911", "#f5222d", "#2f54eb", "#faad14"
];

// -------- Overlay chart component --------
const OverlayChart: React.FC<{
  meta: MetaBlock | null;
  series: SeriesItem[];
  showLegend?: boolean;
}> = ({ meta, series, showLegend = true }) => {
  const baseTerms = meta?.terms ?? [];
  const terms = meta?.next_term ? [...baseTerms, meta.next_term] : baseTerms;

  const [hidden, setHidden] = React.useState<Record<string, boolean>>({});

  const perSeries = series.map((s) => {
    const ds = buildSeriesDatasets(baseTerms, s);
    return { key: s.key, title: s.title, actual: ds.actual, pred: ds.pred };
  });

  const visible = perSeries.filter(s => !hidden[s.key]);
  const yDomain = computeYDomain(visible.map(v => v.actual), visible.map(v => v.pred));

  const legendPayload = series.map((s, idx) => ({
    value: s.title,
    color: PALETTE[idx % PALETTE.length],
    id: s.key,
    type: hidden[s.key] ? "line" : "plainline" as any
  }));

  const onLegendClick = (e: any) => {
    const id = e?.payload?.id as string;
    if (!id) return;
    setHidden((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (!active || !payload?.length) return null;
    const p = payload[0];
    const title = p?.payload?.title ?? p?.name ?? "";
    const val = p?.payload?.value;
    return (
      <div style={{ background: "rgba(0,0,0,0.75)", color: "#fff", padding: 8, borderRadius: 6, fontSize: 12 }}>
        <div style={{ fontWeight: 700, marginBottom: 4 }}>{title}</div>
        <div>{label}</div>
        <div><b>{fmt(val, 3)}</b></div>
      </div>
    );
  };

  const yTickFormatter = (v: any) => {
    const n = Number(v);
    return Number.isFinite(n) ? n.toFixed(2) : v;
  };

  return (
    <div style={{ width: "100%", height: 360, marginBottom: 16 }}>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart margin={{ top: 12, right: 24, bottom: 8, left: 18 }}>
          <XAxis
            dataKey="term"
            type="category"
            allowDuplicatedCategory={false}
            ticks={terms}
            tick={{ fontSize: 11 }}
            interval={0}
          />
          <YAxis
            domain={yDomain as any}
            tick={{ fontSize: 11 }}
            tickFormatter={yTickFormatter}
            allowDecimals
            tickCount={6}
          />
          <Tooltip content={<CustomTooltip />} />
          {showLegend && (
            <Legend
              verticalAlign="top"
              align="right"
              payload={legendPayload as any}
              onClick={onLegendClick}
              wrapperStyle={{ cursor: "pointer" }}
              iconSize={14}
            />
          )}
          {visible.map((s, idx) => {
            const color = PALETTE[idx % PALETTE.length];
            return (
              <React.Fragment key={`series-${s.key}`}>
                <Line
                  name={s.title}
                  data={s.actual}
                  dataKey="value"
                  stroke={color}
                  strokeWidth={2}
                  dot={false}
                  isAnimationActive={false}
                  connectNulls
                />
                {s.pred?.length ? (
                  <Line
                    name={s.title}
                    data={s.pred}
                    dataKey="value"
                    stroke={color}
                    strokeDasharray="6 6"
                    strokeWidth={2}
                    dot={{ r: 2 }}
                    isAnimationActive={false}
                  />
                ) : null}
              </React.Fragment>
            );
          })}
        </LineChart>
      </ResponsiveContainer>
      {meta && (
        <div style={{ textAlign: "right", fontSize: 12, color: "#666" }}>
          Units: <b>{meta.units}</b> &nbsp;•&nbsp; Next Term: <b>{meta.next_term}</b>
        </div>
      )}
    </div>
  );
};

// -------- Main component: overlay chart + table --------
export const ForecastData: React.FC = () => {
  const [loading, setLoading] = React.useState(false);
  const [rows, setRows] = React.useState<SeriesItem[]>([]);
  const [meta, setMeta] = React.useState<MetaBlock | null>(null);

  // Endpoint id options -> directly passed as the id
  const FILTERS = [
    { label: "By Department", value: "Z" },
    { label: "Comp Sci Courses", value: "C" },
    { label: "Biology Courses", value: "B" },
  ] as const;
  const [idValue, setIdValue] = React.useState<(typeof FILTERS)[number]["value"]>("Z");

  // NEW: hide legend toggle
  const [showLegend, setShowLegend] = React.useState(true);

  React.useEffect(() => {
    setLoading(true);
    fetchForecasts(idValue)
      .then((res: any) => {
        const data: ForecastResponse = typeof res === "string" ? JSON.parse(res) : res;
        setMeta(data?.meta ?? null);
        setRows(data?.series ?? []);
      })
      .catch(() => {
        setMeta(null);
        setRows([]);
      })
      .finally(() => setLoading(false));
  }, [idValue]);

  const getLastActual = (s: SeriesItem) => {
    const hist = s.history || [];
    for (let i = hist.length - 1; i >= 0; i--) {
      if (!hist[i].isPred && hist[i].value != null) return hist[i].value!;
    }
    return Number.NEGATIVE_INFINITY;
  };
  const getPredicted = (s: SeriesItem) => s.next_point?.value ?? Number.NEGATIVE_INFINITY;

  const columns = [
    {
      title: <span style={{ fontSize: 16 }}>Title</span>,
      dataIndex: "title",
      key: "title",
      render: (_: any, record: SeriesItem) => (
        <Space direction="vertical" size={0}>
          <Typography.Text style={{ fontSize: 16 }}>{record.title}</Typography.Text>
          {record.department_letter && (
            <Typography.Text type="secondary" style={{ fontSize: 12 }}>
              Dept: {record.department_letter}
            </Typography.Text>
          )}
        </Space>
      ),
      width: 220,
      fixed: "left" as const,
    },
    {
      title: <span style={{ fontSize: 16 }}>Kind</span>,
      dataIndex: "kind",
      key: "kind",
      render: (k: string) => <Tag color={kindColor(k)} style={{ fontSize: 12 }}>{k}</Tag>,
      filters: [
        { text: "Department", value: "department" },
        { text: "Overall", value: "overall" },
      ],
      onFilter: (value: any, record: SeriesItem) => record.kind === value,
      width: 140,
    },
    {
      title: (
        <span style={{ fontSize: 16 }}>
          Last Actual{meta?.terms?.length ? ` (${meta.terms[meta.terms.length - 1]})` : ""}
        </span>
      ),
      key: "last",
      sorter: (a: SeriesItem, b: SeriesItem) => getLastActual(a) - getLastActual(b),
      render: (_: any, record: SeriesItem) => {
        const v = getLastActual(record);
        return <span style={{ fontSize: 15 }}>{isFinite(v) ? fmt(v, 3) : "-"}</span>;
      },
      width: 140,
    },
    {
      title: (
        <span style={{ fontSize: 16 }}>
          Predicted {meta?.next_term ? `(${meta.next_term})` : ""}
        </span>
      ),
      key: "pred",
      defaultSortOrder: "descend" as const,
      sorter: (a: SeriesItem, b: SeriesItem) => getPredicted(a) - getPredicted(b),
      render: (_: any, record: SeriesItem) => {
        const v = getPredicted(record);
        const outOfRange = isFinite(v) && (v < 0 || v > 5);
        return (
          <Typography.Text strong style={{ fontSize: 16 }}>
            <Tag color={outOfRange ? "volcano" : "green"} style={{ fontSize: 14, padding: "2px 8px" }}>
              {isFinite(v) ? fmt(v, 3) : "-"}
            </Tag>
          </Typography.Text>
        );
      },
      width: 160,
    },
  ];

  return (
    <div style={{ maxWidth: 1200, margin: "0 auto" }}>
      <div style={{ marginBottom: 8, display: "flex", justifyContent: "space-between", alignItems: "center", gap: 12 }}>
        <div>
          <Typography.Title level={4} style={{ marginBottom: 0 }}>
            Forecasts (Overlay)
          </Typography.Title>
          {meta && (
            <Typography.Text type="secondary">
              Metric: <b>{meta.metric}</b> &nbsp;•&nbsp; Units: <b>{meta.units}</b>
              {meta.agg ? <> &nbsp;•&nbsp; Aggregation: <b>{meta.agg}</b></> : null}
              {meta.next_term ? <> &nbsp;•&nbsp; Next Term: <b>{meta.next_term}</b></> : null}
            </Typography.Text>
          )}
        </div>

        {/* Controls */}
        <Space align="center">
          <Select
            size="small"
            value={idValue}
            onChange={setIdValue}
            options={[
              { label: "By Department", value: "Z" },
              { label: "Comp Sci Courses", value: "C" },
              { label: "Biology Courses", value: "B" },
            ]}
            style={{ width: 200 }}
          />
          <Space size={6} align="center">
            <Typography.Text style={{ fontSize: 12 }}>Show legend</Typography.Text>
            <Switch size="small" checked={showLegend} onChange={setShowLegend} />
          </Space>
        </Space>
      </div>

      {/* Overlay chart across all series */}
      <OverlayChart meta={meta} series={rows} showLegend={showLegend} />

      <Divider />

      {/* Table for sorting & details */}
      <Table<SeriesItem>
        size="large"
        columns={columns}
        dataSource={rows}
        rowKey={(r) => r.key}
        loading={loading}
        pagination={{ pageSize: 8 }}
        scroll={{ x: 1000 }}
      />
    </div>
  );
};

export default ForecastData;
