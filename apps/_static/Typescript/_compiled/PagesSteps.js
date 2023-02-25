function PagesSteps() {
    var current_url = window.location.pathname.split('/').filter(function (n) { return n; });
    if (current_url.length < 2)
        return;
    var pages_steps = document.getElementById('pages_steps');
    console.log(current_url);
    for (var i = 0; i < current_url.length; i++) {
        var key = current_url.at(i);
        pages_steps.innerHTML +=
            '<a href="/' + current_url.slice(0, i + 1).join('/') + '" class="hover:underline">'
                + CapitalizeEveryWord(key.replace('-', ' ')) +
                '</a>';
        if (i != current_url.length - 1) {
            pages_steps.innerHTML += '<span class="text-lime"> > </span>';
        }
    }
}
window.addEventListener('load', function () {
    console.log("WINDOW LOAD");
    var pages_steps = document.getElementById('pages_steps');
    if (typeof (pages_steps) != 'undefined' && pages_steps != null) {
        PagesSteps();
    }
});
function CapitalizeEveryWord(str) {
    var splitStr = str.toLowerCase().split(' ');
    for (var i = 0; i < splitStr.length; i++) {
        splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
    }
    return splitStr.join(' ');
}
