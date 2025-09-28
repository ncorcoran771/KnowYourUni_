import React from "react";
import { Table, Typography, Tooltip } from "antd";
import { useUserInfo } from "../context/UserInfoProvider";
import { suggestCourses } from "../api";

/* ---------- Types ---------- */
type Suggestion = {
  course_code: string;
  professor: string;
  confidence: number; // 0..5 (can be fractional like 3.25)
};

type SuggestionResponse = {
  student_id: string;
  suggestions: Suggestion[];
};

/* ---------- StarRating (fills smoothly to any decimal) ---------- */
const StarRating: React.FC<{ value: number; max?: number; size?: number }> = ({
  value,
  max = 5,
  size = 18,
}) => {
  const pct = Math.max(0, Math.min(100, (value / max) * 100));

  const starStyle: React.CSSProperties = {
    fontSize: size,
    lineHeight: 1,
    letterSpacing: 2,
    display: "inline-block",
    userSelect: "none",
  };

  // Two layers of identical stars; top layer is clipped by width to create partial fill
  return (
    <span style={{ position: "relative", display: "inline-block" }} aria-label={`${value.toFixed(2)} out of ${max}`}>
      <span style={{ ...starStyle, color: "#d9d9d9" }}>★★★★★</span>
      <span
        style={{
          ...starStyle,
          color: "#faad14",
          position: "absolute",
          top: 0,
          left: 0,
          width: `${pct}%`,
          overflow: "hidden",
          whiteSpace: "nowrap",
        }}
      >
        ★★★★★
      </span>
    </span>
  );
};

/* ---------- Main Component ---------- */
export const CourseSuggestion: React.FC = () => {
  const { userInfo } = useUserInfo();
  const [loading, setLoading] = React.useState(false);
  const [rows, setRows] = React.useState<Suggestion[]>([]);

  React.useEffect(() => {
    const id = userInfo?.id ?? "FS65039";
    if (!id) return;
    setLoading(true);
    suggestCourses(id)
      .then((res: SuggestionResponse | string) => {
        const data: SuggestionResponse = typeof res === "string" ? JSON.parse(res) : res;
        setRows(data?.suggestions ?? []);
      })
      .catch(() => setRows([]))
      .finally(() => setLoading(false));
  }, [userInfo?.id]);

  const columns = [
    {
      title: <span style={{ fontSize: 16 }}>Course</span>,
      dataIndex: "course_code",
      key: "course_code",
      render: (text: string) => (
        <Typography.Text style={{ fontSize: 16 }}>{text}</Typography.Text>
      ),
      sorter: (a: Suggestion, b: Suggestion) => a.course_code.localeCompare(b.course_code),
      width: 180,
    },
    {
      title: <span style={{ fontSize: 16 }}>Professor</span>,
      dataIndex: "professor",
      key: "professor",
      render: (text: string) => <span style={{ fontSize: 15 }}>{text}</span>,
      sorter: (a: Suggestion, b: Suggestion) => a.professor.localeCompare(b.professor),
      width: 260,
    },
    {
      title: <span style={{ fontSize: 16 }}>Confidence</span>,
      dataIndex: "confidence",
      key: "confidence",
      defaultSortOrder: "descend" as const,
      sorter: (a: Suggestion, b: Suggestion) => (a.confidence ?? 0) - (b.confidence ?? 0),
      render: (v: number) => (
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <Tooltip title={`${v.toFixed(2)} / 5.00`}>
            <StarRating value={v} />
          </Tooltip>
          <span style={{ fontSize: 14, color: "#888" }}>{v.toFixed(2)}</span>
        </div>
      ),
      width: 220,
    },
  ];

  return (
    <div style={{ maxWidth: 900, margin: "0 auto" }}>
      <Table<Suggestion>
        size="large"
        columns={columns}
        dataSource={rows}
        rowKey={(r) => `${r.course_code}__${r.professor}`}
        loading={loading}
        pagination={{ pageSize: 10 }}
        style={{ fontSize: 16 }}
      />
    </div>
  );
};

export default CourseSuggestion;
