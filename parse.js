const fs = require("fs");
let data = require("message.json");

text = data[2].data
  .map(d=>d.content)
  .filter(text=>text.length > 5);

fs.appendFileSync("./data.json",JSON.stringify(data),"utf8");