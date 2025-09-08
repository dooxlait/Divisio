// components/form/InputText.jsx
export default function InputText({
  label,
  name,
  value,
  onChange,
  required = false,
  type = "text",
  placeholder = "",
  ...restProps
}) {
  return (
    <div className="form-group">
      <label htmlFor={name}>{label}</label>
      <input
        type={type}
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
        placeholder={placeholder}
        style={{ padding: "0.7rem" }}
        {...restProps}
      />
    </div>
  );
}
