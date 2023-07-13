var password_input = document.getElementById("register_password_input");
var length_msg = document.getElementById("register_password_length");
var specialcharacter_number_msg = document.getElementById("register_password_specialnumber");
var submit_button = document.getElementById("register_password_submit");
submit_button.disabled = true;
var upperCaseLetters = /(?=.*[a-z])(?=.*[A-Z])/g;
var special_character_reg = /[!@#%&()^~{}]/;
var numbers_reg = /\d/;
function check_submit() {
    submit_button.disabled = !(password_input.value.match(numbers_reg) && password_input.value.match(special_character_reg) && password_input.value.length >= 9);
}
// When the user starts to type something inside the password field
password_input.addEventListener("keyup", function (event) {
    // password_input.onkeyup = function() {
    console.log("PASS " + password_input.value);
    // Validate numbers
    if (password_input.value.match(numbers_reg) && password_input.value.match(special_character_reg)) {
        specialcharacter_number_msg.classList.add("success");
    }
    else {
        specialcharacter_number_msg.classList.remove("success");
    }
    // Validate length
    if (password_input.value.length >= 9) {
        length_msg.classList.add("success");
    }
    else {
        length_msg.classList.remove("success");
    }
    check_submit();
});
