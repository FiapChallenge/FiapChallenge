import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        azul: {
          claro: "#00a7ef",
          escuro: "#334a73",
        },
        preto: "#333",
        branco: "#fff",
        cinza: {
          DEFAULT: "#7D7C7C",
          claro: "#26272b",
          escuro: "#1b1b1d",
        },
      },
    },
  },
  plugins: [],
};
export default config;
