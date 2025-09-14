"use client";
import { ClipLoader } from "react-spinners";

export default function ActionButton({
  buttonKey,
  loadingButton,
  setLoadingButton,
  onClick,
  children,
  className = "button button-primary",
}) {
  const handleClick = async (e) => {
    e.preventDefault();
    setLoadingButton(buttonKey);

    try {
      if (onClick) {
        await onClick();
      }
    } finally {
      // tu peux choisir de le remettre à null automatiquement
      // ou laisser le parent décider
      setLoadingButton(null);
    }
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
