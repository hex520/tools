const license_server = "https://hackbar.site/ping";
let license_ok = true;

let urlField = $('#url_field');
let postDataField = $('#post_data_field');
let refererField = $('#referer_field');
let userAgentField = $('#user_agent_field');
let cookieField = $('#cookie_field');

let loadUrlBtn = $('#load_url');
let splitUrlBtn = $('#split_url');
let executeBtn = $('#execute');

let enablePostBtn = $('#enable_post_btn');
let enableRefererBtn = $('#enable_referer_btn');
let enableUserAgentBtn = $('#enable_user_agent_btn');
let enableCookieBtn = $('#enable_cookie_btn');
let clearAllBtn = $('#clear_all');

function disable_hackbar(message=null) {
    $('#alert-license').removeClass('hidden');
    if(message){
        $('#alert-license span').text(message);
    }
    license_ok = false;
}

/* chrome.storage.local.get(['license'], function (result) {
        const license = result.license;
        if (license) {
            //check internet
            fetch("https://google.com")
                .then(function (response) {
                    // check licese
                    fetch(license_server + "/" + license)
                        .then(function (response) {
                            return response.json();
                        })
                        .then(function (data) {
                            const pong = data.pong;
                            if (pong === false) {
                                disable_hackbar(data.message);
                            }
                        }).catch(error => {
                            disable_hackbar();
                        });
                })
                .then(function (data) {
                }).catch(error => {
                });
        } else {
            disable_hackbar();
        }
    }); */

$('#licence-save').bind('click', () => {
    const license = $('#licence-input').val();
    chrome.storage.local.set({license: license});
    $('#alert-license').addClass('hidden');
});

const menu_btn_array = ['md5', 'sha1', 'sha256', 'rot13',
    'base64_encode', 'base64_decode', 'url_encode', 'url_decode', 'hex_encode', 'hex_decode',
    'sql_mysql_char', 'sql_basic_info_column', 'sql_convert_utf8', 'sql_convert_latin1', 'sql_mssql_char', 'sql_oracle_char', 'sql_union_statement', 'sql_spaces_to_inline_comments',
    'xss_string_from_charcode', 'xss_html_characters', 'xss_alert',
    'jsonify', 'uppercase', 'lowercase',];

let currentTabId = chrome.devtools.inspectedWindow.tabId;
let currentFocusField = urlField;

function onFocusListener() {
    currentFocusField = $(this);
}

/* Other function */
function jsonValid(text) {
    try {
        return JSON.parse(text);
    } catch (e) {
        return false;
    }
}

function getFieldFormData(dataString) {
    let fields = Array();
    let f_split = dataString.trim().split('&');
    for (let i in f_split) {
        let f = f_split[i].match(/(^.*?)=(.*)/);
        if (f.length === 3) {
            let item = {};
            item['name'] = f[1];
            item['value'] = unescape(f[2]);
            fields.push(item);
        }
    }
    return fields;
}

function urlEncode(inputStr) {
    return encodeURIComponent(inputStr).toLowerCase();
}

function jsonBeautify(inputStr) {
    let jsonString = jsonValid(inputStr);
    if (jsonString) {
        return JSON.stringify(jsonString, null, 4);
    }
    return false;
}

function upperCaseString(inputStr) {
    return inputStr.toUpperCase();
}

function lowerCaseString(inputStr) {
    return inputStr.toLowerCase();
}

// toggle element
function toggleElement(elementBtn, elementBlock) {
    if (elementBtn.prop('checked')) {
        elementBlock.show();
    } else {
        elementBlock.hide();
    }
}

function sendToBackground(action, data, response) {
    chrome.runtime.sendMessage({
        tabId: currentTabId,
        action: action,
        data: data
    }, function (message) {
        response(message)
    });
}

function loadUrl() {
    sendToBackground('load_url', null, function (message) {
        if ('url' in message && message.url) {
            urlField.val(message.url);
        }
        if ('data' in message && message.data && postDataField.val() === "") {
            postDataField.val(message.data);
        }
    });
}

function splitUrl() {
    let uri = currentFocusField.val();
    uri = uri.replace(new RegExp(/&/g), "\n&");
    uri = uri.replace(new RegExp(/\?/g), "\n?");
    currentFocusField.val(uri);
    return true;
}

function execute() {
    let referer = null;
    let user_agent = null;
    let cookie = null;
    let post_data = null;
    let method = 'GET';

    if (enableRefererBtn.prop('checked')) {
        referer = refererField.val();
    }
    if (enablePostBtn.prop('checked')) {
        method = 'POST';
        post_data = getFieldFormData(postDataField.val());
    }
    if (enableUserAgentBtn.prop('checked')) {
        user_agent = userAgentField.val();
    }
    if (enableCookieBtn.prop('checked')) {
        cookie = cookieField.val();
    }

    let url = urlField.val();
    url = url.replace(new RegExp(/\n|\r/g), '').trim();
    if (!(new RegExp(/^(http:\/\/|https:\/\/|view-source:)/gi)).test(url)) {
        url = 'http://' + url;
    }
    if (!url) {
        return;
    }
    chrome.runtime.sendMessage({
        tabId: currentTabId,
        action: 'send_requests',
        data: {url: url, method: method, post_data: post_data, referer: referer, user_agent: user_agent, cookie: cookie}
    });

}

function getSelectedText(callbackFunction) {
    const selectionStart = currentFocusField.prop('selectionStart');
    const selectionEnd = currentFocusField.prop('selectionEnd');
    if (selectionEnd - selectionStart < 1) {
        $('#myModal').modal();
        $('#myModal input').val("");
        $('#myModal button').bind('click', () => {
            const selected_text = $('#myModal input').val();
            callbackFunction(selected_text);
            $('#myModal').modal('hide');
        });
    } else {
        callbackFunction(currentFocusField.val().substr(selectionStart, selectionEnd - selectionStart));
    }
}

function setSelectedText(str) {
    let selectionStart = currentFocusField.prop('selectionStart');
    let selectionEnd = currentFocusField.prop('selectionEnd');
    let pre = currentFocusField.val().substr(0, selectionStart);
    let post = currentFocusField.val().substr(selectionEnd, currentFocusField.val().length);
    currentFocusField.val(pre + str + post);
    currentFocusField[0].setSelectionRange(selectionStart, selectionEnd + str.length)
}
 // listenener function
function check_license(){
    if(!license_ok){
        throw new Error('Please input valid license!');
    }
}
function onclickMenu(action, val) {
    switch (action) {
        case 'md5':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.md5(txt));
                }
            });
            break;
        case 'sha1':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.sha1(txt));
                }
            });
            break;
        case 'sha256':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.sha2(txt));
                }
            });
            break;
        case 'rot13':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.rot13(txt));
                }
            });
            break;
        case 'base64_encode':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.base64Encode(txt));
                }
            });
            break;
        case 'base64_decode':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.base64Decode(txt));
                }
            });
            break;
        case 'url_encode':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(urlEncode(txt));
                }
            });
            break;
        case 'url_decode':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(unescape(txt));
                }
            });
            break;
        case 'hex_encode':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.strToHex(txt));
                }
            });
            break;
        case 'hex_decode':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(Encrypt.hexToStr(txt));
                }
            });
            break;
        case 'jsonify':
            getSelectedText(function (txt) {
                if (txt && jsonBeautify(txt)) {
                    setSelectedText(jsonBeautify(txt));
                }
            });
            break;
        case 'uppercase':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(upperCaseString(txt));
                }
            });
            break;
        case 'lowercase':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(lowerCaseString(txt));
                }
            });
            break;
        case 'sql_mysql_char':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText(SQL.selectionToSQLChar("mysql", txt));
                }
            });
            break;

        case 'sql_basic_info_column':
            let sqlBasicStr = 'CONCAT_WS(CHAR(32,58,32),user(),database(),version())';
            this.setSelectedText(sqlBasicStr);
            break;

        case 'sql_convert_utf8':
            getSelectedText(function (txt) {
                if (txt) {
                    setSelectedText("CONVERT(" + txt + " USING utf8)");
                }
            });
            break;
        case 'sql_convert_latin1':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = "CONVERT(" + txt + " USING latin1)";
                    setSelectedText(newString);
                }
            });
            break;

        case 'sql_mssql_char':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = SQL.selectionToSQLChar("mssql", txt);
                    setSelectedText(newString);
                }
            });
            break;

        case 'sql_oracle_char':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = SQL.selectionToSQLChar("oracle", txt);
                    setSelectedText(newString);
                }
            });
            break;

        case 'sql_union_statement':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = SQL.selectionToUnionSelect(txt);
                    setSelectedText(newString);
                }
            });
            break;

        case 'sql_spaces_to_inline_comments':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = SQL.selectionToInlineComments(txt);
                    setSelectedText(newString);
                }
            });
            break;

        case 'xss_string_from_charcode':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = XSS.selectionToChar('stringFromCharCode', txt);
                    setSelectedText(newString);
                }
            });
            break;

        case 'xss_html_characters':
            getSelectedText(function (txt) {
                if (txt) {
                    const newString = XSS.selectionToChar('htmlChar', txt);
                    setSelectedText(newString);
                }
            });
            break;

        case 'xss_alert':
            const alertStr = "<script>alert(1)</script>";
            this.setSelectedText(alertStr);
            break;

        case 'LFI':
            this.setSelectedText(val);
            break;
    }
    currentFocusField.focus();
}

//on focus listener field
urlField.bind('click', onFocusListener, false);
postDataField.bind('click', onFocusListener, false);
refererField.bind('click', onFocusListener, false);
userAgentField.bind('click', onFocusListener, false);
cookieField.bind('click', onFocusListener, false);

//Events
loadUrlBtn.bind('click', function(){
    check_license();
    console.log('load url');
    loadUrl();
});
splitUrlBtn.bind('click', function(){
    check_license();
    splitUrl();
});
executeBtn.bind('click', function(){
    check_license();
    execute();
});
clearAllBtn.bind('click', function () {
    refererField.val('');
    userAgentField.val('');
    cookieField.val('');
});

enablePostBtn.click(function () {
    toggleElement($(this), postDataField.closest('.block'))
});
enableRefererBtn.click(function () {
    toggleElement($(this), refererField.closest('.block'))
});
enableUserAgentBtn.click(function () {
    toggleElement($(this), userAgentField.closest('.block'))
});
enableCookieBtn.click(function () {
    toggleElement($(this), cookieField.closest('.block'))
});

//Add event listener
menu_btn_array.forEach(function (elementID) {
    $('#' + elementID).bind('click', function(){
        check_license();
        onclickMenu(elementID)
    });
});

 $('#lfi .lfi_data').bind('click', function(e){
        check_license();
        onclickMenu('LFI', this.text);
    });

// Keyboard listener
$(document).on('keypress', function (event) {
    check_license();
    if ('key' in event && event.ctrlKey && event.charCode === 13) {
        execute();
    }
});