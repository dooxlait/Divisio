import { useState, useEffect } from "react";

export default function useSplash(duration = 2000) {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), duration);
    return () => clearTimeout(timer);
  }, [duration]);

  return { loading };
}
