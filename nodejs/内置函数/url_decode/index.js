// url decode
function urlDecode(encodedUrl) {
    return decodeURIComponent(encodedUrl);
}

// 测试

// url encode
function urlEncode(url) {
    return encodeURIComponent(url);
}


// 测试


let wz1 = urlEncode('测试');
console.log("url encode:",wz1);

let wz2 = urlDecode(wz1);
console.log("url decode:",wz2);

