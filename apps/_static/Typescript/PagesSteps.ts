
function PagesSteps(): void {

    let current_url: string[] = window.location.pathname.split('/').filter(n => n);
    let pages_steps = document.getElementById('pages_steps');
    console.log(current_url)
    for (let i = 0; i < current_url.length; i++) {
        let key = current_url.at(i);
        pages_steps.innerHTML +=
            '<a href="/' + current_url.slice(0, i+1).join('/') + '" class="hover:underline">'
            + CapitalizeEveryWord(key.replace('-', ' ')) +
            '</a>';
        if (i != current_url.length - 1){
            pages_steps.innerHTML += '<span class="text-lime"> > </span>';
        }
    }

}

window.addEventListener('load', function(){
    console.log("WINDOW LOAD")
    let pages_steps =  document.getElementById('pages_steps');
    if (typeof(pages_steps) != 'undefined' && pages_steps != null) {
        PagesSteps();
    }
});

function CapitalizeEveryWord(str) {
    const splitStr = str.toLowerCase().split(' ');
    for (let i = 0; i < splitStr.length; i++) {
       splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
   }
   return splitStr.join(' ');
}