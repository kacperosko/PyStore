var password_input1 = document.getElementById("register_password_input1");
var password_input2 = document.getElementById("register_password_input2");
var length_msg = document.getElementById("register_password_length");
var specialcharacter_number_msg = document.getElementById("register_password_specialnumber");
var confirmation = document.getElementById("register_password_confirmation");
var submit_button = document.getElementById("register_password_submit");
submit_button.disabled = true;
var upperCaseLetters = /(?=.*[a-z])(?=.*[A-Z])/g;
var special_character_reg = /[!@#%&()^~{}]/;
var numbers_reg = /\d/;
function check_submit() {
    submit_button.disabled = !(password_input1.value.match(numbers_reg)
        // && password_input1.value.match(special_character_reg)
        && password_input1.value.length >= 9
        && password_input1.value == password_input2.value);
}
// When the user starts to type something inside the password field
password_input1.addEventListener("keyup", function (event) {
    // password_input.onkeyup = function() {
    console.log("PASS " + password_input1.value);
    // Validate numbers
    if (password_input1.value.match(numbers_reg)
    // && password_input1.value.match(special_character_reg)
    ) {
        specialcharacter_number_msg.classList.add("success");
    }
    else {
        specialcharacter_number_msg.classList.remove("success");
    }
    // Validate length
    if (password_input1.value.length >= 9) {
        length_msg.classList.add("success");
    }
    else {
        length_msg.classList.remove("success");
    }
    if (password_input1.value == password_input2.value) {
        confirmation.classList.add("success");
    }
    else {
        confirmation.classList.remove("success");
    }
    check_submit();
});
password_input2.addEventListener("keyup", function (event) {
    if (password_input1.value == password_input2.value) {
        confirmation.classList.add("success");
    }
    else {
        confirmation.classList.remove("success");
    }
    check_submit();
});
