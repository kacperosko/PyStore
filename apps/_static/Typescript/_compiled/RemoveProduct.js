function RemoveProduct(product_id) {
    $.ajax({
        type: "GET",
        url: "/ajax/removeproduct",
        data: {
            product_id: product_id
        },
        success: function (data) {
            var counter = document.getElementById('cart-count');
            var total = document.getElementById('total-price');
            var product_row = document.getElementById('sub-product-' + product_id);
            product_row.remove();
            counter.innerHTML = data.counter;
            total.innerHTML = "$" + data.total;
        }
    });
}
