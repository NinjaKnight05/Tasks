const fname = document.getElementById('fname');
const lname = document.getElementById("lname");
const email = document.getElementById('email');
const phone = document.getElementById("phone");
const submitbtn = document.getElementById('button');
const gender = document.getElementById('gender')

function check(){
    submitbtn.disabled = !(fname.value.trim() &&
    lname.value.trim() &&
    email.value.trim() &&
    phone.value.trim() &&
    gender.value.trim());
}
fname.addEventListener('input',check);
lname.addEventListener("input", check);
phone.addEventListener("input", check);
email.addEventListener("input", check);
gender.addEventListener("change", check);
document.getElementById("registerForm").addEventListener("submit", function (e) {
    e.preventDefault(); 
    alert("Submitted!");
  });