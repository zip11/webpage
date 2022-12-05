import fetch from "node-fetch";
fetch("https://csdn.net")
  .then(res=>res.text())
  .then(json=>console.log(json));