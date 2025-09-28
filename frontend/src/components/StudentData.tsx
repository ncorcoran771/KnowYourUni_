/* StudentData.tsx — Simple table of students (dynamic columns) */
import React from "react";
import { Table, Typography, Alert } from "antd";
import { fetchStudents } from "../api";

/** Try to pull an array of rows out of a few common server shapes. */
function normalizeStudentResponse(payload: any): any[] {
  if (Array.isArray(payload)) return payload;
  if (!payload || typeof payload !== "object") return [];
  return (
    payload.students ??
    payload.results ??
    payload.buddies ?? // matches the current api.ts return type
    []
  );
}

/** Pretty-print a key like "student_id" or "firstName" to a column title. */
function titleize(key: string): string {
  if (!key) return key;
  // split camelCase → spaced
  const spaced = key.replace(/([a-z0-9])([A-Z])/g, "$1 $2").replace(/_/g, " ");
  return spaced
    .split(" ")
    .map(w => (w ? w[0].toUpperCase() + w.slice(1) : w))
    .join(" ");
}

const pickRowKey = (row: Record<string, any>, idx: number) =>
  String(
    row.id ??
    row.student_id ??
    row.studentId ??
    row.uuid ??
    row.email ??
    row.user_id ??
    idx
  );

export const StudentData: React.FC = () => {
  const [loading, setLoading] = React.useState(false);
  const [rows, setRows] = React.useState<Record<string, any>[]>([]);
  const [error, setError] = React.useState<string | null>(null);

  React.useEffect(() => {
    setLoading(true);
    setError(null);
    fetchStudents()
      .then((res: any) => {
        const data = typeof res === "string" ? JSON.parse(res) : res;
        const arr = normalizeStudentResponse(data);
        setRows(Array.isArray(arr) ? arr : []);
      })
      .catch((e: any) => setError(e?.message || "Failed to load students"))
      .finally(() => setLoading(false));
  }, []);

  // Build columns from the first row’s keys
  const columns = React.useMemo(() => {
    const first = rows[0] || {};
    const keys = Object.keys(first);
    if (keys.length === 0) {
      // Provide a placeholder column if empty so the Table renders nicely
      return [
        {
          title: <span style={{ fontSize: 16 }}>No Data</span>,
          dataIndex: "__nodata__",
          key: "__nodata__",
          render: () => <span style={{ color: "#999" }}>No student records yet.</span>,
        },
      ];
    }
    return keys.map((k) => ({
      title: <span style={{ fontSize: 16 }}>{titleize(k)}</span>,
      dataIndex: k,
      key: k,
      render: (val: any) => {
        if (val == null) return <span style={{ color: "#999" }}>—</span>;
        if (typeof val === "number") {
          // Light formatting for numbers; keep raw to avoid surprises
          return <span style={{ fontVariantNumeric: "tabular-nums" }}>{val}</span>;
        }
        return <Typography.Text>{String(val)}</Typography.Text>;
      },
    }));
  }, [rows]);

  return (
    <div style={{ maxWidth: 1100, margin: "0 auto" }}>
      <Typography.Title level={4} style={{ marginBottom: 12 }}>
        Students
      </Typography.Title>

      {error && (
        <Alert
          type="error"
          message="Error loading students"
          description={error}
          style={{ marginBottom: 12 }}
          showIcon
        />
      )}

      <Table<Record<string, any>>
        size="large"
        columns={columns as any}
        dataSource={rows}
        rowKey={pickRowKey}
        loading={loading}
        pagination={{ pageSize: 10 }}
      />
    </div>
  );
};

export default StudentData;
