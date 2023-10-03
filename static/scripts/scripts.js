document.addEventListener("DOMContentLoaded", () => {
    $('a#test2').bind('click', function () {
        let request = new XMLHttpRequest();
        request.open('GET', '/background_process_test2', true);
        request.onload = function () {
            if (this.status >= 200 && this.status < 400) {
                let data = JSON.parse(this.response);
            }
        };
        request.send();
        return false;
    });
});
document.addEventListener("DOMContentLoaded", () => {
    $('a#test').bind('click', function () {
        let request = new XMLHttpRequest();
        request.open('GET', '/background_process_test', true);
        request.onload = function () {
            if (this.status >= 200 && this.status < 400) {
                let data = JSON.parse(this.response);
            }
        };
        request.send();
        return false;
    });
});