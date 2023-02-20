function AddProductToCart(product_id): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/addproducttocart",
        data:{
                 product_id: product_id
        },
        success: function( data ) {
            let counter = document.getElementById('cart-count');
            let val: number = isNaN(parseInt(counter.innerHTML)) ? 0 : parseInt(counter.innerHTML);
            counter.innerHTML = (String)(1 + val);
            // @ts-ignore
            Alert.success(
                data.product_name + ' added to cart!',
                'add_product',
                {displayDuration: 3000, pos: 'top'})
        },
        error: function (data){
            // @ts-ignore
            Alert.error(
                'Something went wrong, try again',
                'On merlin\'s beard!',
                {displayDuration: 3000, pos: 'top'})
        }
     })
}

