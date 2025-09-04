import { useState, useEffect } from "react";
import { axiosInstance } from "../services/AxiosInstance";

export default function useApiCheck() {
  const [status, setStatus] = useState("loading"); // loading | ok | error

  useEffect(() => {
    const check = async () => {
      try {
        const res = await axiosInstance.get("/API/health"); // endpoint "ping"
        if (res.status === 200) setStatus("ok");
        else setStatus("error");
      } catch (err) {
        setStatus("error");
      }
    };
    check();
  }, []);

  return { status };
}
