
let modal_window = $("#user-modal")

function ShowAddresses(user_id): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/showaddresses",
        data:{
            user_id: user_id,
        },
        success: function( data ) {
            // @ts-ignore
            ModalWindow.showWindow()
            modal_window.html(data)
        },
        error: function (data){
            // @ts-ignore
            Alert.error(
                'Try again',
                'Opss something went wrong :(',
                {displayDuration: 4000, pos: 'top'})
        }
     })
}

function ChooseAddress(address_id): void {
    $.ajax(
    {
        type:"GET",
        url: "/ajax/chooseaddress",
        data:{
            address_id: address_id,
        },
        success: function( data ) {
            // @ts-ignore
            ModalWindow.hideWindow()
            RefreshAddress(data.address);
            // @ts-ignore
            Alert.success(
                'Delivery is closer!',
                'Address updated successful',
                {displayDuration: 4000, pos: 'top'})
        },
        error: function (data){
            // @ts-ignore
            Alert.error(
                'Try again',
                'Opss something went wrong :(',
                {displayDuration: 4000, pos: 'top'})
        }
     })
}


function AddAddress() {
    $('#add_address').removeClass("hover:text-green-500 hover:bg-green-500");
    $('#add_address_msg').addClass("hidden")
    $('#address_form').removeClass("hidden")
}


function SaveAddress() {
    let name = $('#address_form_name')
    let address = $('#address_form_address')
    let postal_code = $('#address_form_postal_code')
    let city = $('#address_form_city')
    let country = $('#address_form_country')

    let postal_code_regex = /^[0-9]{2}-[0-9]{3}$/;

    if (!postal_code_regex.test(postal_code.val() + "")) {
           // @ts-ignore
            Alert.error(
                'Correct example: 12-345',
                'Wrong format of Postal Code ' + postal_code.val() + "" ,
               {displayDuration: 5000, pos: 'top'})
        return
        }



    $.ajax(
    {
        type:"GET",
        url: "/ajax/saveaddress",
        data:{
            name: name.val(),
            address: address.val(),
            postal_code: postal_code.val(),
            city: city.val(),
            country: country.val()
        },
        success: function( data ) {
            // @ts-ignore
            ModalWindow.hideWindow()
            RefreshAddress(data.address);
            // @ts-ignore
            Alert.success(
                'Delivery is closer!',
                'Address added successful',
                {displayDuration: 4000, pos: 'top'})
        },
        error: function (data){
            // @ts-ignore
            Alert.error(
                'Try again',
                'Opss something went wrong :(',
                {displayDuration: 4000, pos: 'top'})
        }
     })
}

function RefreshAddress(address){
    address = JSON.parse(address)[0].fields;
    $("#user-address").val(address.address);
    $("#user-postal_code").val(address.postal_code);
    $("#user-city").val(address.city);
    $("#user-country").val(address.country);
}

