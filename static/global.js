function init_global_logout(seconds) {
    setTimeout(() => {
        document.getElementById('logout').submit();
    }, seconds * 1000);
}
