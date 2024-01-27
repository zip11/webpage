// ==UserScript==
// @name         fsm_pt_dl
// @namespace    fsm-dl
// @version      0.1.0
// @description  try to take over the world!
// @author    
// @match           https://fsm.name/Torrents/mine?type=favorite
// @match           https://fsm.name/Forums
// @grant       GM_getValue
// @grant       GM_setValue
// @grant       GM_xmlhttpRequest 
// @connect     api.fsm.name
// ==/UserScript==

/* ==UserConfig==
group1:
  configA:                                # 键值为group.config,例如本键为:group1.configA
    title: passkey                   # 配置的标题
    description: passkey 是32位，数字和英文字符    # 配置的描述内容
    type: text                            # 选项类型,如果不填写会根据数据自动识别
    default:                        # 配置的默认值
    min: 2                               # 文本最短2个字符
    max: 88                               # 文本最长18个字符
    password: true                        # 设置为密码

 ==/UserConfig== */
    // 在此处键入代码……

( function() {
    'use strict';

    // xhr 读取网页
    async function readWebpageContent(url) {

        GM_xmlhttpRequest({

            method: 'GET',
            url: url,
            onload: function(response) {

                if (response.status === 200) {

                    var content = response.responseText;
                    // console.log("read webpage :",content);

                    // save page
                    save_page(content);
                    return content
                }
            },
            onerror: function() {
                console.log('请求失败');
                return "error"
            }
        });
    }

    // 保存rss网页
    function save_page(rss_con){

        // 保存 rss 网页 内容
        GM_setValue("rss_con",rss_con);

        // 读取 rss 内容
        let rss_wy =  GM_getValue("rss_con");
        console.log("save_browser: ",rss_wy);
    }

    // rss内容，提取
    function rss_nr(xmlString) {

        // 假设 xmlString 是你的 XML 字符串
        // const xmlString = '<root><item>Value 1</item><item>Value 2</item></root>';

        console.log("rss nr: " ,xmlString);

        // 使用 DOMParser 解析 XML 字符串
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(xmlString, 'text/xml');

        // 现在 xmlDoc 是一个包含 XML 数据的 DOM 对象，你可以使用 DOM 操作方法来处理它
        const items = xmlDoc.getElementsByTagName('item');

        // 遍历 下载 任务
        for (let i = 0; i < items.length; i++) {

            // 多个文件,全部信息
            // console.log(items[i].textContent);

            // 帖子 标题
            const title = items[i].querySelector('title').textContent;
            
            // 帖子 链接
            const link = items[i].querySelector('link').textContent;

            console.log(i+'-Item Title:', title);
            console.log(i+'-Item Link:', link);


        }
    }

    // 获取 文件 下载链接
   function extractEnclosureUrl(xmlContent) {

        // 创建一个DOMParser对象，用于解析xmlContent
        const parser = new DOMParser();
    
        // 使用DOMParser对象解析xmlContent，并将其转换为xml文档
        const xmlDoc = parser.parseFromString(xmlContent, "application/xml");

        // 使用XPath表达式，查找xml文档中的enclosure节点
        const enclosureNodes = xmlDoc.evaluate('//enclosure', xmlDoc, null, XPathResult.ANY_TYPE, null);

        // 创建一个变量node，用于遍历enclosure节点
        let node = enclosureNodes.iterateNext();

        // 创建一个变量urls，用于存储enclosure节点的url属性
        let urls = [];

        // 使用while循环，遍历enclosure节点，并将其url属性存入urls数组中
        while (node) {
            urls.push(node.getAttribute('url'));
            node = enclosureNodes.iterateNext();
        }

        // 返回urls数组
        return urls;
    }

    // st ~~~~~~~~~~~~~

    // 读取 passkey
    let pk = GM_getValue("group1.configA");
    // console.log(pk);

    // rss 网址
    pk = "https://api.fsm.name/Rss/me?passkey=" + pk

    // 读取website ，保存网页
    // let rss_con = readWebpageContent(pk);
    
    // 读取 rss 内容
    let rss_nr2 =  GM_getValue("rss_con");
    
    // rss内容 ,提取
    // rss_nr(rss_nr2);

    // 获取 rss 下载链接
    let xzwz2 = extractEnclosureUrl(rss_nr2);
    console.log("下载网址-数组",xzwz2);


})();

