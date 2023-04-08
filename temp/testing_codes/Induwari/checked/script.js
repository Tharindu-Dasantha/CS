// This is just a example javascript code to do the job please make changes or customizations for your likings

const form = document.querySelector("#myform");
const radioInputChecking = document.querySelectorAll('input[name="delivery"]'); // this will select all the input fields that has the name attribute "delivery"

form.addEventListener("submit", function (event) {
  let isChecked = false;

  // loop through all the radio fields to check if any is unchecked
  radioInputChecking.forEach(function (input) {
    if (input.checked) {
      isChecked = true;
    }
  });

  if (!isChecked) {
    const myDiv = document.getElementById("error1");
    myDiv.innerHTML = "<p>This question is required.</p>";
  }

  event.preventDefault();
});
