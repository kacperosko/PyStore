
function ChangeProductQuantity(val: number, product_id: string): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/addproducttocart",
        data:{
            product_id: product_id,
            quantity: Math.abs(val),
            update: true,
        },
        success: function(data) {
            let counter = document.getElementById('cart-count');
            let total_price = document.getElementById('total-price');
            counter.innerHTML = data.counter;
            total_price.innerHTML = "$" + data.total;
            // input.value = Math.abs(val) as any as string;
        }
     })


}