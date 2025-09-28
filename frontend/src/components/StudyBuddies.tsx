/* Study buddy suggestions table */
import React from "react";
import { Table, Typography, Tag } from "antd";
import { fetchStudyBuddies } from "../api";
import { useUserInfo } from "../context/UserInfoProvider";

interface BuddyRow {
  coll_id: string;
  coll_name: string;
  perf_similarity: number;   // 0..1
  learn_similarity: number;  // 0..1
  overall: number;           // 0..1
}
interface ApiResponse {
  results: BuddyRow[];
}

const pct = (v?: number) =>
  v == null ? "-" : `${(v * 100).toFixed(1)}%`;

// simple color scale for overall similarity
const overallColor = (v?: number) => {
  if (v == null) return "default";
  if (v >= 0.92) return "green";
  if (v >= 0.86) return "gold";
  return "volcano";
};

export const StudyBuddies: React.FC = () => {
  const { userInfo } = useUserInfo();
  const [loading, setLoading] = React.useState(false);
  const [rows, setRows] = React.useState<BuddyRow[]>([]);

  React.useEffect(() => {
    const id = userInfo?.id ?? "FS65039";
    if (!id) return;
    setLoading(true);
    fetchStudyBuddies(id)
      .then((res: any) => {
        const data: ApiResponse = typeof res === "string" ? JSON.parse(res) : res;
        setRows(data?.results ?? []);
      })
      .catch(() => setRows([]))
      .finally(() => setLoading(false));
  }, [userInfo?.id]);

  const columns = [
    {
      title: <span style={{ fontSize: 16 }}>Name</span>,
      dataIndex: "coll_name",
      key: "coll_name",
      render: (text: string) => (
        <Typography.Text style={{ fontSize: 16 }}>{text}</Typography.Text>
      ),
    },
    {
      title: <span style={{ fontSize: 16 }}>Total Similarity</span>,
      dataIndex: "overall",
      key: "overall",
      defaultSortOrder: "descend" as const,
      sorter: (a: BuddyRow, b: BuddyRow) => (a.overall ?? 0) - (b.overall ?? 0),
      render: (v: number) => (
        <Typography.Text strong style={{ fontSize: 16 }}>
          <Tag color={overallColor(v)} style={{ fontSize: 14, padding: "2px 8px" }}>
            {pct(v)}
          </Tag>
        </Typography.Text>
      ),
    },
    {
      title: <span style={{ fontSize: 16 }}>Learning Type Similarity</span>,
      dataIndex: "learn_similarity",
      key: "learn_similarity",
      sorter: (a: BuddyRow, b: BuddyRow) =>
        (a.learn_similarity ?? 0) - (b.learn_similarity ?? 0),
      render: (v: number) => (
        <span style={{ fontSize: 15, opacity: 0.9 }}>{pct(v)}</span>
      ),
    },
    {
      title: <span style={{ fontSize: 16 }}>Performance Similarity</span>,
      dataIndex: "perf_similarity",
      key: "perf_similarity",
      sorter: (a: BuddyRow, b: BuddyRow) =>
        (a.perf_similarity ?? 0) - (b.perf_similarity ?? 0),
      render: (v: number) => (
        <span style={{ fontSize: 15, opacity: 0.9 }}>{pct(v)}</span>
      ),
    },
  ];

  return (
    <div style={{ maxWidth: 900, margin: "0 auto" }}>
      <Table<BuddyRow>
        size="large"
        columns={columns}
        dataSource={rows}
        rowKey="coll_id"
        loading={loading}
        pagination={{ pageSize: 10 }}
        style={{ fontSize: 16 }}
      />
    </div>
  );
};

export default StudyBuddies;
