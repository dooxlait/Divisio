// FRONTEND\webapp\src\app\layout.jsx

"use client";
import "../app/globals.css";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { toast, Toaster } from "react-hot-toast";
import SplashScreen from "@/components/splashscreen/SplashScreen";
import useSplash from "@/hooks/useSplash";

export default function RootLayout({ children }) {
  const { loading } = useSplash(1500);
  const router = useRouter();

  useEffect(() => {
    if (!loading) {
      router.push("/identification");
    }
  }, [loading, router]);

  return (
    <html lang="fr">
      <body style={{ margin: 0, fontFamily: "sans-serif" }}>
        {loading ? <SplashScreen /> : null}
        {/* quand loading est terminé, redirection automatique */}
        <main>{children}</main>
        <Toaster position="top-right" />
      </body>
    </html>
  );
}
