"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function PagesHome() {
  const router = useRouter();
  useEffect(() => {
    router.replace("/");
  }, [router]);
  return (
    <div className="min-h-screen bg-[#0c0f14] flex items-center justify-center text-white/60">
      Redirecting…
    </div>
  );
}
