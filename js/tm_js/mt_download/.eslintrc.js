module.exports = {
    "env": {
        "es6": true,
        "browser": true
    },
    "parserOptions": {
        "ecmaVersion": 2022,
        "sourceType": "script",
        "ecmaFeatures": {
            "globalReturn": true
        },
        "allowAwaitOutsideFunction": true
    },
    "rules": {
        "userscripts/no-invalid-grant": 1,
        "userscripts/no-invalid-headers": 1,
        "userscripts/no-invalid-metadata": [
            2,
            {
                "top": "optional"
            }
        ],
        "userscripts/require-name": [
            2,
            "required"
        ],
        "userscripts/require-description": [
            1,
            "required"
        ],
        "userscripts/require-version": [
            1,
            "required"
        ],
        "userscripts/require-attribute-space-prefix": 1,
        "userscripts/use-homepage-and-url": 0,
        "userscripts/use-download-and-update-url": 1,
        "userscripts/better-use-match": 1,
        "curly": [
            1,
            "multi-line"
        ],
        "dot-location": 0,
        "dot-notation": [
            1,
            {
                "allowKeywords": true
            }
        ],
        "no-caller": 1,
        "no-case-declarations": 2,
        "no-div-regex": 0,
        "no-empty-pattern": 2,
        "no-eq-null": 0,
        "no-eval": 1,
        "no-extra-bind": 1,
        "no-fallthrough": 1,
        "no-implicit-globals": 2,
        "no-implied-eval": 1,
        "no-lone-blocks": 1,
        "no-loop-func": 1,
        "no-multi-spaces": 1,
        "no-multi-str": 1,
        "no-native-reassign": 1,
        "no-octal-escape": 2,
        "no-octal": 2,
        "no-proto": 1,
        "no-redeclare": 2,
        "no-return-assign": 1,
        "no-sequences": 1,
        "no-undef": 1,
        "no-useless-call": 1,
        "no-useless-concat": 1,
        "no-with": 1
    },
    "globals": {
        "uneval": "writeable",
        "unsafeWindow": "writeable",
        "GM_info": "writeable",
        "GM": "writeable",
        "GM_addStyle": "writeable",
        "GM_addElement": "writeable",
        "GM_cookie": "writeable",
        "GM_deleteValue": "writeable",
        "GM_listValues": "writeable",
        "GM_getValue": "writeable",
        "GM_download": "writeable",
        "GM_log": "writeable",
        "GM_registerMenuCommand": "writeable",
        "GM_unregisterMenuCommand": "writeable",
        "GM_openInTab": "writeable",
        "GM_setValue": "writeable",
        "GM_addValueChangeListener": "writeable",
        "GM_removeValueChangeListener": "writeable",
        "GM_xmlhttpRequest": "writeable",
        "GM_webRequest": "writeable",
        "GM_getTab": "writeable",
        "GM_saveTab": "writeable",
        "GM_getTabs": "writeable",
        "GM_setClipboard": "writeable",
        "GM_notification": "writeable",
        "GM_getResourceText": "writeable",
        "GM_getResourceURL": "writeable"
    }
}
