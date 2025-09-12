import { useState, useEffect } from "react";
import { axiosInstance } from "../services/AxiosInstance";

export default function useApi({ endpoint }) {
  const [status, setStatus] = useState("loading");
  const [data, setData] = useState(null);

  useEffect(() => {
    let isMounted = true; // éviter maj d’état après un unmount

    const fetchData = async () => {
      try {
        const res = await axiosInstance.get(`/${endpoint}`);
        console.log("hook", res);

        if (res.status === 200) {
          if (isMounted) {
            setStatus("ok");
            setData(res.data);
          }
        } else {
          if (isMounted) setStatus("error");
        }
      } catch (err) {
        if (isMounted) setStatus("error");
      }
    };

    fetchData();

    return () => {
      isMounted = false;
    };
  }, [endpoint]);

  return { status, data };
}
