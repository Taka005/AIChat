const fs = require("fs");
const message = require("./message.json");

const data = message[2].data
  .map(d=>d.content)
  .filter(text=>text.length > 5);

fs.appendFileSync("./data.json",JSON.stringify(data),"utf8");