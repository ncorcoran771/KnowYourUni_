/* "Shell" wrapper around the dashboard layout */

import React from "react";
import { Layout, theme } from "antd";
import ThemeController from "../components/ThemeController";
import DashboardLayout from "../components/DashboardLayout";
import { SVGLogo } from "../utils/getSVGLogo";

const { Header, Content } = Layout;

export const Shell: React.FC = () => {
  const { token } = theme.useToken();

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Header
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          paddingInline: 16,
        }}
      >
        <SVGLogo />
        <div style={{ color: "#fff", fontWeight: 600 }}>Know Your Uni</div>
        <ThemeController />
      </Header>

      <Layout>
        <Content style={{ background: token.colorBgLayout }}>
          <DashboardLayout />
        </Content>
      </Layout>
    </Layout>
  );
};

export default Shell;
