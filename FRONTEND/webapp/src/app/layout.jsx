// FRONTEND\webapp\src\app\layout.jsx

"use client";
import "./globals.css";
import { Toaster } from "react-hot-toast";
import SplashScreen from "@/components/feedback/splashscreen/SplashScreen";
import useSplash from "@/hooks/useSplash";

export default function RootLayout({ children }) {
  const { loading } = useSplash(1000);

  return (
    <html lang="fr">
      <body style={{ margin: 0, fontFamily: "sans-serif" }}>
        {loading ? <SplashScreen /> : children}
        <Toaster position="top-right" />
      </body>
    </html>
  );
}
