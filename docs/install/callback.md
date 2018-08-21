---
layout: page
permalink: /install/callback
---

<style type="text/css">
    .spacer {
        margin: 3em;
    }
</style>

<script type="text/javascript">

    function getParam(name, url) {
        url  = url ? url : window.location.href;

        var result = null;
        var tmp   = [];

        location.search.substr(1).split('&').forEach(function (item) { 
            tmp = item.split('=');
            result = (tmp[0] === name) ? decodeURIComponent(tmp[1]) : result;
        });

        return result;
    };

    function setToken(token) {
        var elem = document.getElementById("token");
        if (elem) {
            elem.value = token;
        }
    };

    function toggleVisibility() {
        var elem = document.getElementById("token");
        if (elem) {
            elem.type = (elem.type === "password") ? "text" : "password";
        }
    };

    function showTokenForm() {
        var form = document.getElementById("token-form");
        form.style = "";

        var placeholder = document.getElementById("loading");
        placeholder.style = "visibility:hidden;"
    };

    function handleResponse(xhttp) {
        console.log(xhttp);
    };

    function onReady() {
        var token = getParam("code");
        setToken(token);
        showTokenForm();
    };

    document.addEventListener("DOMContentLoaded", onReady);
</script>

## Installed!

<div id="token-form" style="visibility:hidden;">
<form>
    Code: <input id="token" type="password" /> <input type="button" onclick="toggleVisibility()" value="Show" />
</form>
<div class="spacer"></div>
<p>
    <strong>This is not your OAuth token.</strong> 
    You will need to use this verification code to get your OAuth token. 
    See <a href="/slack-deletefiles/install">here</a> for more.
</p>
</div>

<div id="loading"><p>Fetching code...</p></div>

<div class="spacer"></div>

~~Copy this token into your `.env` file - don't lose it, and don't share it with _anyone_! You may need a refresher on [how to install][install].~~

^ Don't do this yet.

[install]: /slack-deletefiles/install
