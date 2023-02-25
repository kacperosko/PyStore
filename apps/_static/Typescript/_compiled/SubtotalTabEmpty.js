var table = document.getElementById('subtotal-tab');
var table_header = document.getElementById('subtotal-tab-head');
var table_body = document.getElementById('subtotal-tab-body');
var message = document.getElementById('no-products-message');
var checkout_button = document.getElementById('checkout_button');
function ShowMessage() {
    table_header.classList.add("hidden");
    message.classList.remove("hidden");
    document.getElementById('checkout_button').disabled = true;
}
function HideMessage() {
    table_header.classList.remove("hidden");
    message.classList.add("hidden");
    document.getElementById('checkout_button').disabled = false;
}
function CheckTableRows() {
    console.log("TABLE EVENT");
    if (table_body.childElementCount === 1) {
        ShowMessage();
    }
    else {
        HideMessage();
    }
}
var observer = new MutationObserver(CheckTableRows);
observer.observe(table_body, { subtree: true, characterData: false, childList: true, attributes: false });
