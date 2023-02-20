
function AddDiscount(): void {
    let discount_input = document.getElementById('discount_input') as HTMLInputElement;
    $.ajax(
    {
        type:"GET",
        url: "/ajax/adddiscount",
        data:{
            discount_name: discount_input.value,
        },
        success: function(data) {
            console.log("DISC SUCCESS", data.total_discount)
            let discount_name = document.getElementById('discount_name');
            let discount_percentage = document.getElementById('discount_percentage');

            discount_name.innerHTML = data.discount_name;
            discount_percentage.innerHTML = "-" + data.discount_percentage + "%";
        },
        error: function (data){
            console.log("ERROR", data)
        }
     })


}

$("#discount_input").on('keyup', function (e) {
    if (e.key === 'Enter' || e.keyCode === 13) {
        AddDiscount();
    }
});