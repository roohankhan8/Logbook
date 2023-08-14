const passwordField = document.getElementById("password-field");
const showPasswordIcon = document.getElementById("show-password");

// if (passwordField.value == "") {
//   showPasswordIcon.style.display = "none";
// }else{
//     showPasswordIcon.style.display = "block";
// }

showPasswordIcon.addEventListener("click", function () {
  if (passwordField.type === "password") {
    passwordField.type = "text";
  } else {
    passwordField.type = "password";
  }
});
