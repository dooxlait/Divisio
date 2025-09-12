// FRONTEND\webapp\src\helpers\buildHierarchy.js
export function buildHierarchy(payload) {
  const map = {};
  payload.forEach((item) => {
    map[item.id] = { ...item, subdivisions: [] };
  });

  payload.forEach((item) => {
    item.subdivisions.forEach((sub) => {
      if (map[sub.id]) {
        map[item.id].subdivisions.push(map[sub.id]);
      }
    });
  });

  const allChildrenIds = new Set(
    payload.flatMap((item) => item.subdivisions.map((sub) => sub.id))
  );

  return payload
    .filter((item) => !allChildrenIds.has(item.id))
    .map((item) => map[item.id]);
}
