"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function DashboardPage() {
  const router = useRouter();
  useEffect(() => {
    router.replace("/");
  }, [router]);
  return (
    <div className="min-h-screen bg-[#0c0f14] flex items-center justify-center text-white">
      <p className="text-white/60">Redirecting to Environmental Station…</p>
    </div>
  );
}
