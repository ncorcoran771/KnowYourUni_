/* Theme Provider */

import React, { createContext, useContext, useEffect, useMemo, useState } from "react";
import { ConfigProvider, theme } from "antd";  // Controlling themes for antd components

// Different native themes
export type ThemeMode = "light" | "dark" | "system";

// Theme context
type ThemeContextValue = {
  mode: ThemeMode;
  setMode: (m: ThemeMode) => void;
  primary: string;
  setPrimary: (c: string) => void;
  compact: boolean;
  setCompact: (v: boolean) => void;
  systemDark: boolean;
};

const ThemeContext = createContext<ThemeContextValue | null>(null);

export const useThemeConfig = (): ThemeContextValue => {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useThemeConfig must be used within ThemeConfigProvider");
  return ctx;
};

export const ThemeConfigProvider: React.FC<React.PropsWithChildren> = ({ children }) => {
  const [mode, setMode] = useState<ThemeMode>(() => (localStorage.getItem("themeMode") as ThemeMode) || "system");
  const [primary, setPrimary] = useState<string>(() => localStorage.getItem("primaryHex") || "#1677ff");
  const [compact, setCompact] = useState<boolean>(() => localStorage.getItem("compact") === "true");

  // Track system dark mode for "system" option
  const [systemDark, setSystemDark] = useState<boolean>(() =>
    typeof window !== "undefined" ? window.matchMedia?.("(prefers-color-scheme: dark)").matches : false
  );

  // Listen to system theme changes
  useEffect(() => {
    const mq = window.matchMedia?.("(prefers-color-scheme: dark)");
    const apply = () => setSystemDark(!!mq?.matches);
    apply();
    mq?.addEventListener?.("change", apply);
    return () => mq?.removeEventListener?.("change", apply);
  }, []);

  // Determine which algorithms to use based on mode and compact settings
  const effectiveDark = mode === "system" ? systemDark : mode === "dark";
  const algorithms = useMemo(() => {
    const base = effectiveDark ? theme.darkAlgorithm : theme.defaultAlgorithm;
    return compact ? [base, theme.compactAlgorithm] : [base];
  }, [effectiveDark, compact]);

  // Making the theme stuff persist
  useEffect(() => localStorage.setItem("themeMode", mode), [mode]);
  useEffect(() => localStorage.setItem("primaryHex", primary), [primary]);
  useEffect(() => localStorage.setItem("compact", String(compact)), [compact]);

  // Memoize context value to avoid unnecessary re-renders
  const contextValue = useMemo<ThemeContextValue>(
    () => ({ mode, setMode, primary, setPrimary, compact, setCompact, systemDark }),
    [mode, primary, compact, systemDark]
  );

  // Provide theme context and configure antd theme
  return (
    <ThemeContext.Provider value={contextValue}>
      <ConfigProvider
        theme={{
          cssVar: true,
          algorithm: algorithms,
          token: {
            colorPrimary: primary,
            borderRadius: 8,
          },
        }}
      >
        {children}
      </ConfigProvider>
    </ThemeContext.Provider>
  );
};


