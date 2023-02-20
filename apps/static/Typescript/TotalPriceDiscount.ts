
let total_price_discount = document.getElementById('total_price_discount');

function TotalPriceDiscount() {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/gettotaldiscount",
        success: function( data ) {
            let total_price = document.getElementById('total-price');
            if (data.total_discount === 0 || data.total_discount === null) {
                total_price_discount.innerHTML = "";
                total_price.classList.remove("line-through", "text-gray-500");

            }else {
                total_price_discount.innerHTML = "$" + data.total_discount;
                total_price.classList.add("line-through", "text-gray-500");
            }
        }
     })
}

const observer = new MutationObserver(TotalPriceDiscount);
observer.observe(document.getElementById('total-price'), {subtree: true, characterData: false, childList: true, attributes: false});
observer.observe(document.getElementById('discount_name'), {subtree: true, characterData: false, childList: true, attributes: false});