function AddDiscount() {
    var discount_input = document.getElementById('discount_input');
    $.ajax({
        type: "GET",
        url: "/ajax/adddiscount",
        data: {
            discount_name: discount_input.value
        },
        success: function (data) {
            console.log("DISCOUNT SUCCESS", data.total_discount);
            var discount_name = document.getElementById('discount_name');
            var discount_percentage = document.getElementById('discount_percentage');
            // @ts-ignore
            Alert.success('', 'Discount added sucessfully! :D', { displayDuration: 3000, pos: 'top' });
            discount_name.innerHTML = data.discount_name;
            discount_percentage.innerHTML = "-" + data.discount_percentage + "%";
            discount_input.value = '';
        },
        error: function ($xhr, textStatus, errorThrown) {
            console.log("ERROR : ", errorThrown);
            console.log("ERROR : ", $xhr);
            console.log("ERROR : ", textStatus);
            switch ($xhr.status) {
                case 401:
                    // @ts-ignore
                    Alert.warning(JSON.parse($xhr.responseText).message, 'What a green mess :(', { displayDuration: 3000, pos: 'top' });
                    break;
                case 402:
                    // @ts-ignore
                    Alert.error(JSON.parse($xhr.responseText).message, 'On the Monstera Leaf!', { displayDuration: 3000, pos: 'top' });
                    break;
                default:
                    // @ts-ignore
                    Alert.error('Try again and green luck!', 'Something went wrong :(', { displayDuration: 3000, pos: 'top' });
                    break;
            }
            discount_input.value = '';
        }
    });
}
$("#discount_input").on('keyup', function (e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
        AddDiscount();
    }
});
