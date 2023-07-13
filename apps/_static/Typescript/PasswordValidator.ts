let password_input :HTMLInputElement = <HTMLInputElement>document.getElementById("register_password_input");

let length_msg: HTMLElement = document.getElementById("register_password_length");
let specialcharacter_number_msg: HTMLElement = document.getElementById("register_password_specialnumber");

let submit_button :HTMLButtonElement = <HTMLButtonElement>document.getElementById("register_password_submit");


submit_button.disabled = true

let upperCaseLetters = /(?=.*[a-z])(?=.*[A-Z])/g;
let special_character_reg = /[!@#%&()^~{}]/;
let numbers_reg = /\d/;


function check_submit(){
 submit_button.disabled = !(password_input.value.match(numbers_reg) && password_input.value.match(special_character_reg) && password_input.value.length >= 9);
}

// When the user starts to type something inside the password field
password_input.addEventListener("keyup", (event) => {
// password_input.onkeyup = function() {

  console.log("PASS " + password_input.value);

  // Validate numbers
  if(password_input.value.match(numbers_reg) && password_input.value.match(special_character_reg)) {
    specialcharacter_number_msg.classList.add("success");
  } else {
    specialcharacter_number_msg.classList.remove("success");
  }

  // Validate length
  if(password_input.value.length >= 9) {
    length_msg.classList.add("success");
  } else {
    length_msg.classList.remove("success");
  }

  check_submit();
});