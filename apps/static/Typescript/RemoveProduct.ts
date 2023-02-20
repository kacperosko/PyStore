function RemoveProduct(product_id: string): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/removeproduct",
        data:{
            product_id: product_id,
        },
        success: function(data) {
            let counter = document.getElementById('cart-count');
            let total = document.getElementById('total-price');
            let product_row = document.getElementById('sub-product-' + product_id);

            product_row.remove();
            counter.innerHTML = data.counter;
            total.innerHTML = "$" + data.total;

        }
     })


}