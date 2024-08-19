function listen_for_nfc(callback) {
    var source = new EventSource("/listen");
    source.addEventListener('message', function(event) {
        var data = JSON.parse(event.data);
        console.log("NFC data received", data);
        if ("nfc" in data) {
            callback(data.nfc);
        }
    }, false);
}

function init_global_logout(seconds) {
    setTimeout(() => {
        document.getElementById('logout').submit();
    }, seconds * 1000);
}
