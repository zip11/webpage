//import fetch from 'node-fetch';
const fetch = require('node-fetch')

async function getAll(){

    const res = await fetch('https://cn.bing.com/');
    const result = await res.text();

    return result;
}

getAll().then(function(res) {
  console.log("web: "+res.substring(1,100));
});

// module.exports = getAll;

console.log(getAll());