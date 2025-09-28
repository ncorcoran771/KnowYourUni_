import React, { useState } from "react";
import { Input, Button, List, Typography } from "antd";

/** Component for LLM Interface 
* Sends POST requests to backend and displays responses in a chat-like interface
* Spolier Unibud is actualy just Mr. Gemini with context
*/

const { TextArea } = Input;

/** Functional Component that returns the interface guy */
const UnibudChat: React.FC = () => {
    const [messages, setMessages] = useState<{ sender: string; text: string }[]>([]);
    const [input, setInput] = useState("");

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMessage = { sender: "User", text: input };
        setMessages((prev) => [...prev, userMessage]);
        setInput("");

        // Attempting to send and receive response from backend
        try {
            const response = await fetch("/api/ask-unibud", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: input }),
            });
            const data = await response.json();

            const botMessage = { sender: "Unibud", text: data.reply || "No response" };
            setMessages((prev) => [...prev, botMessage]);
        } catch {
            const errorMessage = { sender: "Unibud", text: "Error: Unable to fetch response" };
            setMessages((prev) => [...prev, errorMessage]);
        }
    };

    // Rendering the chat interface
    return (
        <div style={{ maxWidth: 600, margin: "0 auto", padding: "20px" }}>
            <List
                bordered
                dataSource={messages}
                renderItem={(item) => (
                    <List.Item>
                        <Typography.Text strong>{item.sender}:</Typography.Text> {item.text}
                    </List.Item>
                )}
                style={{ marginBottom: "20px" }}
            />
            <TextArea
                rows={4}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your message here..."
                style={{ marginBottom: "10px" }}
            />
            <Button type="primary" onClick={handleSend} block>
                Send
            </Button>
        </div>
    );
};

export default UnibudChat;