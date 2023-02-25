function GetCartProducts() {
    $.ajax({
        type: "GET",
        url: "/ajax/getcartproducts",
        data: {},
        success: function (data) {
            var counter = document.getElementById('cart-count');
            counter.innerHTML = data.data;
        }
    });
}
