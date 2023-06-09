function AddProduct(product_id, quantity: number = 1, update:boolean = false): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/addproducttocart",
        data:{
            quantity: Math.abs(quantity),
            update: update,
            product_id: product_id
        },
        success: function( data ) {
            document.getElementById('cart-count').innerHTML = (String)(data.counter);
            // @ts-ignore
            Alert.success(
                data.product_name + ' added to cart!',
                'add_product',
                {displayDuration: 3000, pos: 'top'})
        },
        error: function ($xhr,textStatus,errorThrown){

            switch ($xhr.status) {
                case 401:
                     // @ts-ignore
                    Alert.error(
                        'This product is not active',
                        'On a jungle mess!',
                        {displayDuration: 4000, pos: 'top'})
                    break;
                default:
                     // @ts-ignore
                    Alert.error(
                        'Try again',
                        'Opss our plants are feeling a bit shy',
                        {displayDuration: 4000, pos: 'top'})
                    break;

            }

        }
     })
}

