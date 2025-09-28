import React, { useState } from "react";
import { Input, Button, List, Typography, Alert } from "antd";

const { TextArea } = Input;

const UnibudChat: React.FC = () => {
  const [messages, setMessages] = useState<{ sender: string; text: string }[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);

  // Allow base URL override for dev/prod
  const API_BASE = import.meta?.env?.VITE_API_BASE_URL || "";
  const endpoint = `${API_BASE}/api/unibud`;

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    setErr(null);
    const userText = input;
    setMessages(prev => [...prev, { sender: "User", text: userText }]);
    setInput("");
    setLoading(true);

    const ctrl = new AbortController();
    const timeout = setTimeout(() => ctrl.abort(), 20000); // 20s timeout

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userText }), // ensure backend expects "message"
        signal: ctrl.signal,
      });

      // Non-200 → read text for debugging
      if (!res.ok) {
        const txt = await res.text().catch(() => "");
        console.error("HTTP error:", res.status, txt);
        setMessages(prev => [...prev, { sender: "Unibud", text: `Error ${res.status}: ${txt || "Request failed"}` }]);
        return;
      }

      // Try JSON first, then fall back to text
      let data: unknown = null;
      try {
        data = await res.json();
      } catch {
        const txt = await res.text();
        console.warn("Non-JSON reply:", txt);
        setMessages(prev => [...prev, { sender: "Unibud", text: txt || "Empty response" }]);
        return;
      }

      // Accept common field names: reply / answer / content / message
      const botText =
        data.reply ?? data.answer ?? data.content ?? data.message ?? "";

      if (!botText) {
        console.warn("No expected field in response:", data);
        setMessages(prev => [...prev, { sender: "Unibud", text: "No response (unexpected payload shape)" }]);
      } else {
        setMessages(prev => [...prev, { sender: "Unibud", text: botText }]);
      }
    } catch (e: any) {
      console.error("Fetch error:", e);
      setMessages(prev => [...prev, { sender: "Unibud", text: "Error: Unable to fetch response" }]);
      setErr(e?.name === "AbortError" ? "Request timed out" : (e?.message || "Network error"));
    } finally {
      clearTimeout(timeout);
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", padding: 20 }}>
      {err && <Alert type="error" showIcon message={err} style={{ marginBottom: 12 }} />}
      <List
        bordered
        dataSource={messages}
        renderItem={(item) => (
          <List.Item>
            <Typography.Text strong>{item.sender}:</Typography.Text>&nbsp;{item.text}
          </List.Item>
        )}
        style={{ marginBottom: 12 }}
      />
      <TextArea
        rows={4}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message here..."
        style={{ marginBottom: 8 }}
        onPressEnter={(e) => {
          if (!e.shiftKey) {
            e.preventDefault();
            handleSend();
          }
        }}
      />
      <Button type="primary" onClick={handleSend} block loading={loading}>
        {loading ? "Sending…" : "Send"}
      </Button>
    </div>
  );
};

export default UnibudChat;
