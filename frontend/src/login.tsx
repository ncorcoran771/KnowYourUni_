/* Login component logic */

import React, { useState } from 'react';
import { Layout, Button, Form, Input, Typography, Card, message } from 'antd';
import { useNavigate } from 'react-router-dom';
import { isAdmin } from './context/verify-admin';
import { fetchKGDataById, fetchFullKGData } from './api';
import { useUserInfo } from './context/UserInfoProvider';
import { useKGInfo } from './context/KGInfoProvider';
import GraphSelector from './components/graphSelector';

const { Header, Content, Footer } = Layout;
const { Title, Text } = Typography;

/* Functional component for the login page */
export const Login: React.FC = () => {
  // add in a graph selector here for admin to view different relationship types
  const navigate = useNavigate();
  const { setUserInfo } = useUserInfo();
  const { setKGInfo } = useKGInfo();

  const [submitting, setSubmitting] = useState(false);

  const onFinish = async (values: { id: string }) => {
    const id = values.id?.trim();
    if (!id) return;

    setSubmitting(true);
    try {
      if (isAdmin(id)) {
        // Admin login
        setUserInfo({ id, isAdmin: true });
        setKGInfo(prev => ({ ...prev, loading: true, error: null }));

        const data = await fetchFullKGData().catch();
        setKGInfo({
          nodes: data.nodes ?? [],
          relationships: data.relationships ?? [],
          loading: false,
          error: null,
        });

        navigate('/admin');
      } else {
        // Student login
        setUserInfo({ id, isAdmin: false });
        setKGInfo(prev => ({ ...prev, loading: true, error: null }));

        const data = await fetchKGDataById(id);
        if ('error' in data) {
          setKGInfo({ nodes: [], relationships: [], loading: false, error: data.error });
          message.error(data.error || 'Failed to fetch knowledge graph data.');
          return;
        }
        setKGInfo({
          nodes: data.nodes ?? [],
          relationships: data.relationships ?? [],
          loading: false,
          error: null,
        });

        navigate('/student');
      }
    } catch (err: unknown) {
      console.error(err);
      if (err instanceof Error) {
        message.error(err.message || 'Unexpected error. Please try again.');
      } else {
        message.error('Unexpected error. Please try again.');
      }
      // ensure loading false on error as well
      setKGInfo(prev => ({ ...prev, loading: false }));
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ display: 'flex', alignItems: 'center', backgroundColor: '#001529' }}>
        <h1 style={{ color: 'white', margin: 0 }}>KnowYourUni</h1>
      </Header>
      <Content
        style={{
          margin: '16px',
          padding: '16px',
          backgroundColor: 'white',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Card style={{ width: 420, maxWidth: '95%', boxShadow: '0 6px 18px rgba(0,0,0,0.08)' }}>
          <Title level={3} style={{ marginBottom: 8 }}>
            Sign in
          </Title>
          <Text type="secondary" style={{ display: 'block', marginBottom: 16 }}>
            Enter your ID to continue.
          </Text>
          <GraphSelector />;

          <Form layout="vertical" onFinish={onFinish} autoComplete="off" requiredMark={false}>
            <Form.Item
              label="ID"
              name="id"
              rules={[{ required: true, message: 'Please enter your ID' }]}
            >
              <Input
                size="large"
                placeholder="e.g., A12345678"
                onPressEnter={() => { /* Form handles submission via onFinish */ }}
              />
            </Form.Item>

            <Form.Item>
              <Button
                type="primary"
                htmlType="submit"
                size="large"
                block
                loading={submitting}
                disabled={submitting}
              >
                Continue
              </Button>
            </Form.Item>
          </Form>

          <Text type="secondary">
            Admins can sign in with their admin ID to access administrative tools.
          </Text>
        </Card>
      </Content>
      

      <Footer style={{ textAlign: 'center' }}>© 2025 KnowYourUni</Footer>
    </Layout>
  );
};

export default Login;