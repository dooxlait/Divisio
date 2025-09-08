// components/form/Select.jsx
export default function Select({
  label,
  name,
  options = [], // ✅ valeur par défaut
  value,
  onChange,
  required = false,
}) {
  return (
    <div className="form-group">
      <label htmlFor={name}>{label}</label>
      <select
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
        style={{ padding: "0.7rem", Width: "50%" }}
      >
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
}
