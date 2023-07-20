let password_input1 :HTMLInputElement = <HTMLInputElement>document.getElementById("register_password_input1");
let password_input2 :HTMLInputElement = <HTMLInputElement>document.getElementById("register_password_input2");

let length_msg: HTMLElement = document.getElementById("register_password_length");
let specialcharacter_number_msg: HTMLElement = document.getElementById("register_password_specialnumber");
let confirmation: HTMLElement = document.getElementById("register_password_confirmation");

let submit_button :HTMLButtonElement = <HTMLButtonElement>document.getElementById("register_password_submit");


submit_button.disabled = true

let upperCaseLetters = /(?=.*[a-z])(?=.*[A-Z])/g;
let special_character_reg = /[!@#%&()^~{}]/;
let numbers_reg = /\d/;


function check_submit(){
 submit_button.disabled = !(
     password_input1.value.match(numbers_reg)
     // && password_input1.value.match(special_character_reg)
     && password_input1.value.length >= 9
     && password_input1.value == password_input2.value);
}

// When the user starts to type something inside the password field
password_input1.addEventListener("keyup", (event) => {
// password_input.onkeyup = function() {

  console.log("PASS " + password_input1.value);

  // Validate numbers
  if(
      password_input1.value.match(numbers_reg)
      // && password_input1.value.match(special_character_reg)
      ) {
    specialcharacter_number_msg.classList.add("success");
  } else {
    specialcharacter_number_msg.classList.remove("success");
  }

  // Validate length
  if(password_input1.value.length >= 9) {
    length_msg.classList.add("success");
  } else {
    length_msg.classList.remove("success");
  }

  if(password_input1.value == password_input2.value) {
    confirmation.classList.add("success");
  } else {
    confirmation.classList.remove("success");
  }

  check_submit();
});

password_input2.addEventListener("keyup", (event) => {
  if(password_input1.value == password_input2.value) {
    confirmation.classList.add("success");
  } else {
    confirmation.classList.remove("success");
  }
  check_submit();
});