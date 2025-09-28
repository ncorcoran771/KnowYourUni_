/* Theme controller dropdown from the header toolbar thing */
import React, { useMemo } from "react";
import { Dropdown, Button, ColorPicker, Radio, Switch, Space } from "antd";
import { BgColorsOutlined } from "@ant-design/icons";
import type { Color } from "antd/es/color-picker";
import { useThemeConfig } from "../context/ThemeProvider";
import type { ThemeMode } from "../context/ThemeProvider";

/* Theme controller - dropdown to be used in the header toolbar */
const ThemeController: React.FC = () => {
  const { mode, setMode, primary, setPrimary, compact, setCompact, systemDark } = useThemeConfig();

  const systemBadge = useMemo(
    () => (mode === "system" ? (systemDark ? " (dark)" : " (light)") : ""),
    [mode, systemDark]
  );

  /* Menu Stuff */
  const menu = {
    items: [
      {
        key: "appearance",
        label: (
          <div style={{ padding: 8 }}>
            <div style={{ fontWeight: 600, marginBottom: 6 }}>Appearance</div>
            <Radio.Group
              value={mode}
              onChange={(e) => setMode(e.target.value as ThemeMode)}
              optionType="button"
              buttonStyle="solid"
            >
              <Radio.Button value="light">Light</Radio.Button>
              <Radio.Button value="dark">Dark</Radio.Button>
              <Radio.Button value="system">System{systemBadge}</Radio.Button>
            </Radio.Group>
          </div>
        ),
      },
      { type: "divider" as const },
      {
        key: "brand",
        label: (
          <div style={{ padding: 8 }}>
            <div style={{ fontWeight: 600, marginBottom: 6 }}>Brand Color</div>
            <Space align="center">
              <ColorPicker
                value={primary}
                onChangeComplete={(c: Color) => setPrimary(c.toHexString())}
                presets={[
                  {
                    label: "Presets",
                    colors: ["#1677ff", "#722ED1", "#13C2C2", "#52C41A", "#F5222D", "#FA8C16"],
                  },
                ]}
              />
              <span style={{ opacity: 0.7, fontSize: 12 }}>{primary}</span>
            </Space>
          </div>
        ),
      },
      { type: "divider" as const },
      {
        key: "compact",
        label: (
          <div style={{ padding: 8 }}>
            <Space align="center" style={{ width: "100%", justifyContent: "space-between" }}>
              <div>
                <div style={{ fontWeight: 600 }}>Compact Spacing</div>
                <div style={{ opacity: 0.7, fontSize: 12 }}>Denser layout for data-heavy screens</div>
              </div>
              <Switch checked={compact} onChange={setCompact} />
            </Space>
          </div>
        ),
      },
    ],
  };

  /* Returning the dropdown element */
  return (
    <Dropdown menu={menu} trigger={["click"]} placement="bottomRight" arrow>
      <Button type="text" icon={<BgColorsOutlined style={{ fontSize: 18 }} />}>
        Theme
      </Button>
    </Dropdown>
  );
};

export default ThemeController;
