function redirectToPayment() {
  window.location.href = "khaltipayment.html";
}

// Assuming you have a button with id "bookNowButton"
document.getElementById("bookNowButton").addEventListener("click", redirectToPayment);
