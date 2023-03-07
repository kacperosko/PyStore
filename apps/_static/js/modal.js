
let ModalWindow = undefined;


(function (ModalWindow){

    let modal_popup = document.getElementById("user-modal")
    let bg_popup = document.getElementById("user-modal-bg")
    let is_hidden = true;
    let showWindow, hideWindow;


    showWindow = function(){
    if (is_hidden) {
        modal_popup.classList.toggle('hidden')
        bg_popup.classList.toggle('hidden')
        is_hidden = !is_hidden
    }
}

    hideWindow = function(){
        if (!is_hidden) {
            modal_popup.classList.toggle('hidden')
            bg_popup.classList.toggle('hidden')
            is_hidden = !is_hidden
        }
    }

    ModalWindow.showWindow = showWindow;
    ModalWindow.hideWindow = hideWindow;

})((ModalWindow = {}));

this.ModalWindow = ModalWindow;
