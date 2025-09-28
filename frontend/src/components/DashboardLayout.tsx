/* Dashboard Layout */
import React, { useState } from "react";
import { Layout, Menu, Button, Drawer, Grid, theme } from "antd";
import { getFeatures } from "../utils/getFeatures";
import { useUserInfo } from "../context/UserInfoProvider";
import { MenuFoldOutlined, MenuUnfoldOutlined } from "@ant-design/icons";

const { Content, Sider } = Layout;
const { useBreakpoint } = Grid;

export const DashboardLayout: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);
  const { userInfo } = useUserInfo();
  const items = getFeatures(userInfo.isAdmin || false);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const screens = useBreakpoint();
  const isMobile = !screens.lg;
  const { token } = theme.useToken();

  const RightPanelContent = (
    <div style={{ padding: 16 }}>
      <Menu
        mode="inline"
        items={items.map((it) => ({
          ...it,
          icon: React.cloneElement(it.icon as React.ReactElement, { style: { fontSize: 20 } }),
        }))}
        defaultSelectedKeys={["overview"]}
      />
      <div style={{ marginTop: 16 }}>
        <p style={{ marginBottom: 8, color: token.colorTextSecondary }}>Quick Filters</p>
        <Button block type="primary">Apply</Button>
      </div>
    </div>
  );

  return (
    <Layout>
      <Content style={{ padding: 16, minHeight: "calc(100vh - 64px)" }}>
        <Layout
          style={{
            borderRadius: token.borderRadiusLG,
            overflow: "hidden",
            background: token.colorBgContainer,
            minHeight: "100%",
            position: "relative",
          }}
        >
          <Content style={{ padding: 16 }}>
            <div
              style={{
                height: "100%",
                minHeight: 480,
                borderRadius: token.borderRadiusLG,
                boxShadow: token.boxShadowTertiary,
                background: token.colorFillTertiary,
                display: "grid",
                placeItems: "center",
              }}
            >
              <div style={{ opacity: 0.75 }}>Central Graphic Area</div>
            </div>
          </Content>

          {isMobile ? (
            <>
              <Button
                type="text"
                icon={<MenuUnfoldOutlined />}
                style={{ position: "absolute", top: 12, right: 12, zIndex: 2 }}
                onClick={() => setDrawerOpen(true)}
              />
              <Drawer
                title="Selections"
                placement="right"
                open={drawerOpen}
                onClose={() => setDrawerOpen(false)}
                width={320}
                bodyStyle={{ padding: 0 }}
              >
                {RightPanelContent}
              </Drawer>
            </>
          ) : (
            <Sider
              theme="light"
              width="20%"
              collapsible
              collapsed={collapsed}
              onCollapse={(val) => setCollapsed(val)}
              collapsedWidth={80}
              style={{
                borderInlineStart: `1px solid ${token.colorBorderSecondary}`,
                background: token.colorBgContainer,
              }}
            >
              <div style={{ padding: 16 }}>
                <Menu
                  mode="inline"
                  items={items.map((it) => ({
                    ...it,
                    label: collapsed ? undefined : it.label,
                    icon: React.cloneElement(it.icon as React.ReactElement, { style: { fontSize: 20 } }),
                  }))}
                  defaultSelectedKeys={["overview"]}
                />
              </div>

              {!collapsed && (
                <div style={{ padding: 16, borderTop: `1px solid ${token.colorBorderSecondary}` }}>
                  <p style={{ marginBottom: 8, color: token.colorTextSecondary }}>Quick Filters</p>
                  <Button block type="primary">Apply</Button>
                </div>
              )}

              <Button
                type="text"
                icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
                onClick={() => setCollapsed(!collapsed)}
                style={{ position: "absolute", top: 8, left: 8 }}
              />
            </Sider>
          )}
        </Layout>
      </Content>
    </Layout>
  );
};

export default DashboardLayout;
