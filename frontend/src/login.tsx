/* Login component logic */

import React, { useState } from 'react';
import { Layout, Button, Form, Input, Typography, message, theme } from 'antd';
import { useNavigate } from 'react-router-dom';
import { isAdmin } from './utils/verifyAdmin';
import { fetchKGDataById, fetchFullKGData } from './api';
import { useUserInfo } from './context/UserInfoProvider';
import { useKGInfo } from './context/KGInfoProvider';
import { SVGLogo } from './utils/getSVGLogo';
import ThemeController from './components/ThemeController';
import GraphCanvas from './components/graphSelector'; // <-- full-bleed graph component

const { Header, Content, Footer } = Layout;
const { Title, Text } = Typography;

/* Functional component for the login page */
export const Login: React.FC = () => {
  const navigate = useNavigate();
  const { setUserInfo } = useUserInfo();
  const { setKGInfo } = useKGInfo();
  const [submitting, setSubmitting] = useState(false);

  const { token } = theme.useToken(); // use AntD theme tokens for colors

  const onFinish = async (values: { id: string }) => {
    const id = values.id?.trim();
    if (!id) return;

    setSubmitting(true);
    try {
      if (isAdmin(id)) {
        // Admin login
        setUserInfo({ id, isAdmin: true });
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
      message.error(err instanceof Error ? err.message : 'Unexpected error. Please try again.');
      setKGInfo(prev => ({ ...prev, loading: false }));
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          paddingInline: 16,
          background: token.colorPrimary,
        }}
      >
        <SVGLogo />
        <div style={{ fontWeight: 800, color: token.colorTextLightSolid }}>Know Your Uni</div>
        <ThemeController />
      </Header>

      {/* FULL-WIDTH CONTENT: two-column split */}
      <Content style={{ margin: 0, padding: 0, background: token.colorBgLayout }}>
        <div
          style={{
            display: 'flex',
            minHeight: 'calc(100vh - 64px - 70px)', // Header 64px, Footer ~70px
            background: token.colorBgLayout,
          }}
        >
          {/* LEFT: Graph fills entire left side (no Card/box) */}
          <div style={{ flex: 1, position: 'relative' }}>
            <GraphCanvas />
          </div>

          {/* RIGHT: Login panel (fixed width) */}
          <div
            style={{
              width: 420,
              padding: 24,
              background: token.colorBgContainer,
              borderLeft: `1px solid ${token.colorSplit}`,
              display: 'flex',
              flexDirection: 'column',
              gap: 12,
            }}
          >
            <Title level={3} style={{ marginBottom: 4 }}>
              Sign in
            </Title>
            <Text type="secondary" style={{ marginBottom: 12 }}>
              Enter your Student ID to continue.
            </Text>

            <Form layout="vertical" onFinish={onFinish} autoComplete="off" requiredMark={false}>
              <Form.Item
                label="Student ID"
                name="id"
                rules={[{ required: true, message: 'Please enter your ID' }]}
              >
                <Input size="large" placeholder="e.g., A12345" />
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
          </div>
        </div>
      </Content>

      <Footer style={{ textAlign: 'center', background: token.colorBgLayout }}>
        HackUMBC '25 - KnowYourUni
      </Footer>
    </Layout>
  );
};

export default Login;
