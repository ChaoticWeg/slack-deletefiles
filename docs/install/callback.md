---
layout: page
permalink: /install/callback
---

<style type="text/css">
    .spacer {
        margin: 3em;
    }
</style>

<script type="text/javascript" src="//code.jquery.com/jquery-3.3.1.min.js"></script>

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

    function toggleVisibility() {
        var thisVal = $("#token").attr("type");
        $("#token").attr("type", (thisVal === "password") ? "text" : "password");
    };

    function onError(message) {
        $("#loading").hide();
        $("#error p").html(message);
        $("#error").show();
        console.error(message);
    };

    function onSuccess(token) {
        $("#loading").hide();
        $("#token").val(token);
        $("#token-form").show();
        console.log("received token: " + token);
    };

    function onAjaxDone(data) {
        console.log(data);

        if (!data['ok']) {
            return onError("Error while fetching OAuth token: " + data['error']);
        }

        if (!data['access_token']) {
            return onError("Error while fetching OAuth token: no token received from server.");
        }

        var token = data['access_token'];
        return onSuccess(token);
    };

    function translateError(error) {
        while (error.indexOf('_') > -1) {
            error = error.replace('_', ' ');
        }
        return error;
    };

    function onAjaxError(err) { 
        console.error(err);
        var msg = 
        onError("<strong>Error while fetching OAuth token:</strong> " + translateError(err['responseJSON']['error']));
    };

    $(function () {
        $("#token-form").hide();
        $("#error").hide();
        $("#loading").show();

        var code = getParam("code");
        if (!code) {
            return alert("Unable to fetch OAuth token: no code given");
        }

        var data = { code: code };
        $.post("//api.chaoticweg.cc/slack-deletefiles/token", data, onAjaxDone).fail(onAjaxError);
    });
</script>

## Installed!

<div id="token-form">
<form>
    Code: <input id="token" type="password" /> <input type="button" onclick="toggleVisibility()" value="Show" />
</form>
<div class="spacer"></div>
<p>
    <strong>This is your OAuth 2.0 token. Keep it safe! Do not share it with anyone, publish it in a code repository, or allow anyone to see it!</strong> 
</p>
</div>

<div id="loading"><p>Fetching OAuth token from Slack...</p></div>
<div id="error"><p>Error while fetching OAuth token.</p></div>

<div class="spacer"></div>

Copy this token into your `.env` file - don't lose it, and don't share it with _anyone_! If you do lose this token, you can just [re-install][install] the app to your workspace and get a new token, but the old one _will_ be invalidated!

[install]: /slack-deletefiles/install
