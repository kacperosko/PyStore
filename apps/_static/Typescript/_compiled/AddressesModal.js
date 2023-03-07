var modal_window = $("#user-modal");
function ShowAddresses(user_id) {
    $.ajax({
        type: "GET",
        url: "/ajax/showaddresses",
        data: {
            user_id: user_id
        },
        success: function (data) {
            // modal.removeClass("hidden")
            // @ts-ignore
            ModalWindow.showWindow();
            modal_window.html(data);
        },
        error: function (data) {
            // @ts-ignore
            Alert.error('Try again', 'Opss something went wrong :(', { displayDuration: 4000, pos: 'top' });
        }
    });
}
function ChooseAddress(address_id) {
    $.ajax({
        type: "GET",
        url: "/ajax/chooseaddress",
        data: {
            address_id: address_id
        },
        success: function (data) {
            // @ts-ignore
            ModalWindow.hideWindow();
            RefreshAddress(data.address);
            // @ts-ignore
            Alert.success('Delivery is closer!', 'Address updated successful', { displayDuration: 4000, pos: 'top' });
        },
        error: function (data) {
            // @ts-ignore
            Alert.error('Try again', 'Opss something went wrong :(', { displayDuration: 4000, pos: 'top' });
        }
    });
}
function RefreshAddress(address) {
    address = JSON.parse(address)[0].fields;
    $("#user-address").val(address.address);
    $("#user-postal_code").val(address.postal_code);
    $("#user-city").val(address.city);
    $("#user-country").val(address.country);
}
