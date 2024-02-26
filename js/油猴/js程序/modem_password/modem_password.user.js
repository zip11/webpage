// ==UserScript==
// @name         光猫超级密码解密
// @namespace    modem_password
// @version      1.0
// @description  读取光猫加密密码，解密并显示密码
// @author       24-02-06
// @match        http://192.168.3.1:8080/cgi-bin/baseinfoSet.cgi
// @match        http://192.168.1.1:8080/cgi-bin/baseinfoSet.cgi
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {

    'use strict';

    // 目标网页的URL
    // var targetUrl  = GM_info.script.match
    // console.log(targetUrl);
    
    var targetUrl = 'http://192.168.3.1:8080/cgi-bin/baseinfoSet.cgi';
    // var targetUrl = 'http://192.168.1.1:8080/cgi-bin/baseinfoSet.cgi';  
    // 替换为实际的URL

    // 发送请求获取文本内容
    GM_xmlhttpRequest({

        method: 'GET',
        url: targetUrl,
        onload: function(response) {

            // 解析返回的文本内容
            var textContent = response.responseText;

            // 查找并解密baseinfoSet_TELECOMPASSWORD字段
            var regex = /"baseinfoSet_TELECOMPASSWORD":"(.*?)"/;
            var match = textContent.match(regex);

            if (match) {
                
                var encryptedStr = match[1];

                // 分割字符串，转整数，转ASCII码 字符
                var decryptedStr = decryptString(encryptedStr);
                
                // 凯撒解密 -4
                decryptedStr = caesarDecrypt(decryptedStr);

                decryptedStr = '超级用户telecomadmin解密后的密码:' + decryptedStr

                // 显示解密 字符串
                displayDecryptedString(decryptedStr);

            } else {
                console.error('无法找到baseinfoSet_TELECOMPASSWORD字段');
            }

            // useradmin password
            useradmin_caesarDecrypt(textContent);

            // 光猫序列号 最后五位
            serial_number(textContent);
            
        },
        onerror: function() {
            console.error('请求失败');
        }
    });

    // 用户密码 解密
    function useradmin_caesarDecrypt(str) {

        // 查找并解密baseinfoSet_TELECOMPASSWORD字段
        var regex = /"baseinfoSet_USERPASSWORD":"(.*?)"/;
        var match = str.match(regex);

        if (match) {
                
            var encryptedStr = match[1];

            // 分割字符串，转整数，转ASCII码 字符
            var decryptedStr = decryptString(encryptedStr);
            
            // 凯撒解密 -4
            decryptedStr = caesarDecrypt(decryptedStr);

            decryptedStr = 'useradmin解密后的密码:' + decryptedStr

            // 显示解密 字符串
            displayDecryptedString(decryptedStr);

            console.log('useradmin解密后的字符串:', decryptedStr);
            return decryptedStr;

        } else {
            console.error('无法找到baseinfoSet_TELECOMPASSWORD字段');
            return null;
        }
        
    }

    // 获取光猫 序列号 最后五位
    function serial_number(str) {

        const ser_num = '光猫序列号最后五位: ';

        // 查找 baseinfoSet_DEVICESERIALNUMBER 字段
        var regex = /"baseinfoSet_DEVICESERIALNUMBER":"(.*?)"/;
        var match = str.match(regex);

        if (match) {
                
            var encryptedStr = match[1];
            
            // encryptedStr 获取最后5位字符
            var decryptedStr = encryptedStr.substr(-5);
            
            decryptedStr = ser_num  + decryptedStr
            
            // 网页 显示 字符串
            displayDecryptedString(decryptedStr);

            console.log(ser_num, decryptedStr);
            return decryptedStr;

        } else {
            console.error('无法找到' + ser_num + '字段');
            return null;
        }

    }

    // 解密字符串的函数 ，分割字符串，转整数，转ASCII码 字符
    function decryptString(encryptedStr) {

        var decrypted = '';
        
        // 分割字符串
        var parts = encryptedStr.split('&');
        // 删除 数组 最后一个 元素
        parts.pop();
        
        for (var i = 0; i < parts.length; i++) {
        
            // 字符串 转 整数 10进制
            var code = parseInt(parts[i], 10);

            // 转 ASCII 码
            decrypted += String.fromCharCode(code);

            
        }
        return decrypted;
    }

    // 凯撒解密函数 -4
    function caesarDecrypt(text) {
        
        var decryptedText = '';
        var alphabet = 'abcdefghijklmnopqrstuvwxyz';
        var alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

        for (var i = 0; i < text.length; i++) {
            var char = text[i];
            var isUpper = char === char.toUpperCase();

            // 获取字符在字母表中的位置
            var charIndex = alphabet.indexOf(char.toLowerCase());
            if (charIndex === -1) {
                // 如果字符不是字母，直接添加到解密文本
                decryptedText += char;
                continue;
            }

            // 凯撒解密：向后移动4位
            var shift = 4;
            var decryptedCharCode = ((charIndex - shift + alphabet.length) % alphabet.length);

            // 根据字符是否大写，选择相应的字母表
            var decryptedChar = isUpper ? alphabetUpper[decryptedCharCode] : alphabet[decryptedCharCode];

            decryptedText += decryptedChar;
        }

        return decryptedText;
    }

    // 在页面上显示解密后的字符串
    function displayDecryptedString(decryptedStr) {

        var 解密后的字符串 = document.createElement('div');
        解密后的字符串.id = 'decrypted-password';

        解密后的字符串.textContent =  decryptedStr;
        document.body.appendChild(解密后的字符串);
    }

})();