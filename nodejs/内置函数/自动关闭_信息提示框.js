// ==UserScript==
// @name         自动关闭_信息提示框
// @namespace    https://bbs.tampermonkey.net.cn/
// @version      0.1.0
// @description  自动关闭_信息提示框
// @author       You
// @match        https://bbs.tampermonkey.net.cn/
// ==/UserScript==

(function() {
    'use strict';

    // 实现类似this.$message的效果（使用 class 封装）
    class Message {
    constructor() {
        this.container = document.createElement('div');
        this.container.id = 'messageContainer';
        this.container.style.position = 'fixed';
        this.container.style.top = '20px';
        this.container.style.left = '50%';
        this.container.style.transform = 'translateX(-50%)';
        this.container.style.display = 'flex';
        this.container.style.alignItems = 'center';
        this.container.style.justifyContent = 'center';
        this.container.style.zIndex = '9999';
        document.body.appendChild(this.container);
    }

    show(message, iconType) {
        const p = document.createElement('p');
        p.style.margin = '10px';
        p.style.padding = '10px';
        p.style.backgroundColor = '#f5f5f5';
        p.style.borderRadius = '4px';
        p.style.display = 'flex';
        p.style.alignItems = 'center';

        let icon;
        if (iconType === 'tick') {
        icon = document.createElement('span');
        icon.style.width = '16px';
        icon.style.height = '16px';
        icon.style.backgroundColor = 'green';
        icon.style.borderRadius = '50%';
        icon.style.marginRight = '10px';
        const checkmark = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        checkmark.setAttribute("viewBox", "0 0 24 24");
        checkmark.setAttribute("width", "16");
        checkmark.setAttribute("height", "16");
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", "M9 16.2l-3.6-3.6c-.8-.8-.8-2 0-2.8s2-.8 2.8 0L9 11.6l6.2-6.2c.8-.8 2-.8 2.8 0s.8 2 0 2.8L11.8 16.2c-.4.4-.8.6-1.3.6-.5 0-.9-.2-1.3-.6z");
        path.setAttribute("fill", "white");
        checkmark.appendChild(path);
        icon.appendChild(checkmark);
        } else {
        icon = document.createElement('span');
        icon.style.width = '16px';
        icon.style.height = '16px';
        icon.style.backgroundColor = 'green';
        icon.style.borderRadius = '50%';
        icon.style.marginRight = '10px';
        }

        p.appendChild(icon);
        const text = document.createTextNode(message);
        p.appendChild(text);
        this.container.appendChild(p);

        setTimeout(() => {
        this.container.removeChild(p);
        }, 3000);
    }
    }

    // 使用示例
    const message = new Message();
    // message.show('这是一条消息提示')
    message.show('这是一条消息提示', 'tick'); // 显示绿色圆形，带白色对号的消息提示

})();