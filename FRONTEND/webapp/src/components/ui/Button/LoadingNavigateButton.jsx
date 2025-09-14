"use client";
import { useRouter } from "next/navigation";
import { ClipLoader } from "react-spinners";

export default function LoadingButton({
  path,
  buttonKey,
  loadingButton,
  setLoadingButton,
  children,
  className = "button button-primary",
}) {
  const router = useRouter();

  const handleClick = () => {
    setLoadingButton(buttonKey);
    router.push(path);
  };

  return (
    <button
      className={className}
      onClick={handleClick}
      disabled={loadingButton !== null}
    >
      {children}
      {loadingButton === buttonKey && <ClipLoader color="#fff" size={20} />}
    </button>
  );
}
