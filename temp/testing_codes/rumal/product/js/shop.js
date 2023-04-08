//DOM Elements ==========================================================================================================================================

var cart = document.getElementById("cart");
var cartList = document.getElementById("cart-list");
var productButtons = document.getElementsByClassName("add-button");
var cartTotalDisplay = document.getElementById("cart-total");
var submitButton = document.getElementById("submitButton")

// Arrays ==============================================================================================================================================

var cartListArray = [];

// Functions ===========================================================================================================================================

// Updates the cart list when called---------------------------------------------------------------------------------------------------------
function updateCartList() {
  removeEventListeners();

  //   this is where it takes the data from cartListArray and updates the cart list
  cartList.innerHTML = cartListArray
    .map((item) => {
      return `
        <!-- cart-item -->
        <div data-name="${item.name}" class="cart-item">
          <div class="cart-item-details">
            <img src="${item.img}" alt="" />
            <section class="">
              <p class="product-name-cart">${item.name}</p>
              <p class="product-price-cart">$<span>${item.price}</span></p>
             <input  type="number" value="${item.quantity}" class="product-quantity-cart"  min="0"/>
            </section>
          </div>
        <button class="cart-item-dlt">X</button>
        </div>
        `;
    })
    .join("<br>");

  showForm();
  getCartTotal();
  addEventListners();
}

//remove the product from cart-------------------------------------------------------------------------------------------------------------------

function removeItem(event) {
  var cartItemEle = event.target.parentElement;

  var productInArrayIndex = cartListArray.findIndex(
    (productElement) =>
      productElement.name === cartItemEle.getAttribute("data-name")
  );
  cartListArray.splice(productInArrayIndex, 1);

  updateCartList();
}

// This function updates the input field values in the array--------------------------------------------------------------------------------------
function cartItemValueChanged(event) {
  var cartItemElement = event.target.parentElement.parentElement.parentElement;

  var productInArray = cartListArray.find(
    (productElement) =>
      productElement.name === cartItemElement.getAttribute("data-name")
  );

  productInArray.quantity = event.target.value;

  updateCartList();
}

// Add products to the cart List when chicked on the add to cart button of a perticular product--------------------------------------------------

function addToCartClicked(event) {
  // Getting the details from the DOM elements
  var product = event.target.parentElement;
  var productName = product.getElementsByClassName("product-name")[0].innerHTML;
  var productImg = product
    .getElementsByClassName("product-img")[0]
    .getAttribute("src");
  var productPrice =
    product.getElementsByClassName("product-price")[0].innerHTML;

  // Check whether the product is already in the cart array
  var productAlreadyInCart = cartListArray.find(
    (productElement) => productElement.name === productName
  );

  if (productAlreadyInCart) {
    // If it is already in the cart array; add 1 to the quantity
    productAlreadyInCart.quantity++;
  } else {
    // If it is not; then create an object containg the  product and adding it to thr cart array

    cartListArray.push({
      name: productName,
      quantity: 1,
      price: productPrice,
      img: productImg,
    });
  }

  updateCartList();
}

// Get the total price of the cart -------------------------------------------------------------------------------------------------------------------

function getCartTotal() {
  var cartTotal = 0.0;

  if (cartListArray.length > 0) {
    cartListArray.forEach((productItem) => {
      cartTotal += parseFloat(productItem.price) * productItem.quantity;
      let floatnumber = cartTotal.toFixed(2);

      cartTotalDisplay.textContent = floatnumber;
    });
  } else {
    cartTotalDisplay.textContent = 0.0;
  }
}

// Showing the form when there is at leat one item added to the cart ----------------------------------------------------------------------------------

function showForm() {
  if (cartListArray.length > 0) {
    document.getElementById("order-form").style.display = "block";
  } else {
    document.getElementById("order-form").style.display = "none";
  }
}

// EventListners =====================================================================================================================================
function autorunFunctions() {
  for (var productButton of productButtons) {
    productButton.addEventListener("click", addToCartClicked);
  }
  submitButton.addEventListener("click", errorMessageifemply);
}

autorunFunctions();

// Removing Event Listners (optional just for optimizations)-------------------------------------------------------------------------------------------------------------
function removeEventListeners() {
  // This part is optional. this is a event listner remover to improve the performance
  for (var element of document.getElementsByClassName(
    "product-quantity-cart"
  )) {
    var quantityInput = element;
    quantityInput.removeEventListener("input", cartItemValueChanged);
  }
  for (var ele of document.getElementsByClassName("cart-item-dlt")) {
    var dltButton = ele;
    dltButton.removeEventListener("click", removeItem);
  }
}

// Adding Event Listners------------------------------------------------------------------------------------------------------------------------------
function addEventListners() {
  // Adding event listern to cart input fields
  for (var element of document.getElementsByClassName(
    "product-quantity-cart"
  )) {
    element.addEventListener("input", cartItemValueChanged);
  }

  // Adding eventListner to watch for the removal button click
  for (var ele of document.getElementsByClassName("cart-item-dlt")) {
    ele.addEventListener("click", removeItem);
  }
}

// Printing out a error message if any field of the form is empty
function errorMessageifemply(event) {
  // Get the form element
  event.preventDefault();
  const myForm = document.getElementById("order-form");

  // Iterate over the input fields in the form
  for (let i = 0; i < myForm.elements.length; i++) {
    // Check if the element is an input field
    if (myForm.elements[i].nodeName === "INPUT") {
      // Get the value of the input field
      const inputVal = myForm.elements[i].value;

      // Check if the input field is empty
      if (inputVal === "") {
        // Do something, such as displaying an error message or preventing form submission
        window.alert("Invalid");
        return false;
      }
    }
  }
}

// Good luck mchn, If you don't understand anything don't hesitate to send the issue to me through this URL===>  shorturl.at/lxzGO