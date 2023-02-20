function GetCartProducts(): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/getcartproducts",
        data:{},
        success: function( data ) {
            let counter = document.getElementById('cart-count');
            counter.innerHTML = data.data;
        }
     })
}

