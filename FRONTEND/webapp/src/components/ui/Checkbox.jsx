export default function Checkbox({ label, name, checked, onChange }) {
  return (
    <div className="form-group flex items-center gap-2">
      <input
        type="checkbox"
        id={name}
        name={name}
        checked={checked}
        onChange={onChange}
        className="w-4 h-4 cursor-pointer"
      />
      <label htmlFor={name} className="cursor-pointer select-none">
        {label}
      </label>
    </div>
  );
}
