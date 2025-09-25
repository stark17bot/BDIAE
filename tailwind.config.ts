import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        muted: "var(--muted)",
        "muted-foreground": "var(--muted-foreground)",
        card: "var(--card)",
        "card-foreground": "var(--card-foreground)",
        gold: "var(--gold)",
        accent: "var(--accent)",
        danger: "var(--danger)",
        success: "var(--success)",
      },
      boxShadow: {
        gold: "0 0 0 1px rgba(255,215,0,0.4) inset, 0 0 24px rgba(255,215,0,0.2)",
      },
      borderRadius: {
        xl: "14px",
      },
    },
  },
  plugins: [],
};

export default config;


