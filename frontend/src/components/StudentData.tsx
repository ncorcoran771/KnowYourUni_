import React, { useState, useMemo, useEffect } from 'react';
import { Table, Button, Modal, Input, Card, Typography, Space, Alert } from 'antd';
import type { TableProps } from 'antd';

// --- TYPE DEFINITION ---
// Defines the structure for a single student object
interface Student {
  id: number;
  name: string;
  financialAid: boolean;
  gradYear: number;
}

// --- MOCK DATA ---
// A sample array of student data. In a real application, this would likely come from an API.
const studentData: Student[] = [
  { id: 101, name: 'Alice Johnson', financialAid: true, gradYear: 2025 },
  { id: 102, name: 'Bob Smith', financialAid: false, gradYear: 2026 },
  { id: 103, name: 'Charlie Brown', financialAid: true, gradYear: 2025 },
  { id: 104, name: 'Diana Prince', financialAid: false, gradYear: 2027 },
  { id: 105, name: 'Ethan Hunt', financialAid: true, gradYear: 2026 },
  { id: 106, name: 'Fiona Glenanne', financialAid: false, gradYear: 2025 },
  { id: 107, name: 'George Costanza', financialAid: true, gradYear: 2027 },
  { id: 108, name: 'Hannah Montana', financialAid: true, gradYear: 2026 },
];

const { Title, Text, Paragraph } = Typography;
const { Search } = Input;


// --- MAIN APP COMPONENT ---
const App: React.FC = () => {
  // State for the API Key
  const [apiKey, setApiKey] = useState<string>('');
  
  // State for the search query
  const [searchTerm, setSearchTerm] = useState('');
  // State for modal visibility
  const [isModalVisible, setIsModalVisible] = useState(false);
  // State to manage which student is being viewed in the modal
  const [selectedStudent, setSelectedStudent] = useState<Student | null>(null);
  
  // State for Gemini API functionality
  const [summary, setSummary] = useState<string | null>(null);
  const [isLoadingSummary, setIsLoadingSummary] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  // Load API key from local storage on initial render
  useEffect(() => {
    const savedApiKey = localStorage.getItem('geminiApiKey');
    if (savedApiKey) {
      setApiKey(savedApiKey);
    }
  }, []);

  // Save API key to local storage whenever it changes
  useEffect(() => {
    if (apiKey) {
      localStorage.setItem('geminiApiKey', apiKey);
    } else {
      // Allows user to clear the key
      localStorage.removeItem('geminiApiKey');
    }
  }, [apiKey]);


  // Filter students based on the search term.
  const filteredStudents = useMemo(() => {
    if (!searchTerm) {
      return studentData;
    }
    return studentData.filter(student =>
      student.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [searchTerm, studentData]);

  // Handler to open the modal
  const handleViewClick = (student: Student) => {
    setSelectedStudent(student);
    setIsModalVisible(true);
    // Reset Gemini-related state when opening a new modal
    setSummary(null);
    setError(null);
  };

  // Handler to close the modal
  const handleCloseModal = () => {
    setIsModalVisible(false);
    setSelectedStudent(null);
  };

  // --- GEMINI API INTEGRATION ---
  const getPerformanceSummary = async () => {
    if (!selectedStudent) return;
    
    // Check for API key before making a request
    if (!apiKey) {
      setError("Please enter your Gemini API Key to use this feature.");
      return;
    }

    setIsLoadingSummary(true);
    setError(null);
    setSummary(null);
    
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=${apiKey}`;

    const systemPrompt = "You are an academic advisor. Generate a brief, encouraging, and positive performance summary for a student. Focus on their strengths and potential for future success. Keep the summary to 2-3 concise sentences.";
    const userQuery = `Student Name: ${selectedStudent.name}\nFinancial Aid Status: ${selectedStudent.financialAid ? 'Receiving' : 'Not Receiving'}\nGraduation Year: ${selectedStudent.gradYear}`;

    const payload = {
      contents: [{ parts: [{ text: userQuery }] }],
      systemInstruction: { parts: [{ text: systemPrompt }] },
    };

    try {
      let response;
      for (let i = 0; i < 4; i++) {
        response = await fetch(apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (response.ok) break;
        if (response.status === 400) {
            throw new Error("Invalid API Key provided. Please check your key and try again.");
        }
        if (response.status === 429) {
           await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000));
        } else {
            throw new Error(`API request failed with status ${response.status}`);
        }
      }

      if (!response || !response.ok) {
        throw new Error('API request failed after multiple retries.');
      }
      
      const result = await response.json();
      const generatedText = result.candidates?.[0]?.content?.parts?.[0]?.text;

      if (generatedText) {
        setSummary(generatedText);
      } else {
        throw new Error('Failed to generate a summary. The API returned an unexpected response.');
      }
    } catch (err) {
      console.error("Gemini API Error:", err);
      setError(err instanceof Error ? err.message : 'An unknown error occurred.');
    } finally {
      setIsLoadingSummary(false);
    }
  };

  // Define columns for the antd Table
  const columns: TableProps<Student>['columns'] = [
    { title: 'Name', dataIndex: 'name', key: 'name', sorter: (a, b) => a.name.localeCompare(b.name) },
    { title: 'ID', dataIndex: 'id', key: 'id', sorter: (a, b) => a.id - b.id },
    { 
      title: 'Financial Aid', 
      dataIndex: 'financialAid', 
      key: 'financialAid', 
      sorter: (a, b) => (a.financialAid === b.financialAid ? 0 : a.financialAid ? -1 : 1),
      render: (hasFinancialAid: boolean) => (hasFinancialAid ? 'Yes' : 'No'),
    },
    { title: 'Grad Year', dataIndex: 'gradYear', key: 'gradYear', sorter: (a, b) => a.gradYear - b.gradYear },
    {
      title: 'Action',
      key: 'action',
      render: (_, record) => (
        <Button type="primary" onClick={() => handleViewClick(record)}>
          View
        </Button>
      ),
    },
  ];

  return (
    <>
      <style>{`
        body { background-color: #f0f2f5; }
      `}</style>
      
      <div style={{ padding: '24px' }}>
        <Card>
          <Title level={2}>Student Directory</Title>
          <Text type="secondary">Search and view student information.</Text>
          <Input.Password
            placeholder="Enter your Gemini API Key to enable AI features"
            value={apiKey}
            onChange={e => setApiKey(e.target.value)}
            style={{ margin: '16px 0' }}
            addonBefore="API Key"
          />
          <Search
            placeholder="Search by name..."
            onSearch={value => setSearchTerm(value)}
            onChange={e => setSearchTerm(e.target.value)}
            style={{ marginBottom: 16, width: '100%' }}
            enterButton
          />
          <Table columns={columns} dataSource={filteredStudents} rowKey="id" />
        </Card>
      </div>

      <Modal
        title={<Title level={4}>Student Details</Title>}
        open={isModalVisible}
        onCancel={handleCloseModal}
        footer={[
          <Button key="back" onClick={handleCloseModal}>
            Close
          </Button>,
        ]}
      >
        {selectedStudent && (
          <Space direction="vertical" style={{ width: '100%' }}>
            <p><Text strong>ID:</Text> {selectedStudent.id}</p>
            <p><Text strong>Name:</Text> {selectedStudent.name}</p>
            <p><Text strong>Financial Aid:</Text> {selectedStudent.financialAid ? 'Yes' : 'No'}</p>
            <p><Text strong>Graduation Year:</Text> {selectedStudent.gradYear}</p>
            
            <Card size="small" title="AI-Powered Summary" style={{ marginTop: 16 }}>
              <Button
                  type="default"
                  onClick={getPerformanceSummary}
                  loading={isLoadingSummary}
                  style={{ width: '100%' }}
                  disabled={!apiKey}
              >
                  🔒 Get Performance Summary
              </Button>
              {summary && (
                  <div style={{ marginTop: 16 }}>
                      <Paragraph>{summary}</Paragraph>
                  </div>
              )}
              {error && <Alert message={error} type="error" showIcon style={{ marginTop: 16 }} />}
            </Card>
          </Space>
        )}
      </Modal>
    </>
  );
};

export default App;

