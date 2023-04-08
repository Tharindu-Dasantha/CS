const form = document.querySelector('#myForm');

form.addEventListener('submit', function(event) {
  event.preventDefault(); // prevent the default form submission

  const selectedColor = document.querySelector('input[name="color"]:checked');
  if (!selectedColor) {
    alert('Please select a color');
    return;
  }

  // continue with the form submission
  form.submit();
});
