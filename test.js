const isLegacy = true;
const d = { id: 1 };
const str = `${isLegacy ? "<button class='ban' style='background:#000' onclick='del(\"" + d.id + "\")'>Delete</button>" : ""}`;
