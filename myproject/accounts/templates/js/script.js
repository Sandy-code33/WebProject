/* function buyProduct(productName, price) {
    let quan=document.getElementById("input_quan").value;
    const modalBody = document.getElementById("buyModalBody");
    modalBody.innerHTML = `
      <p><strong>Thank you for purchasing!</strong></p>
      <p>Product: ${productName}</p>
      <p>Price: Rs.${price.toLocaleString()}</p>
      <p>Total Price: Rs.${price.toString() * quan}</p>
    `;
    //const buyModal = new bootstrap.Modal(document.getElementById('buyModal'));buyModal.show();
  };
*/
  /*
  document.body.addEventListener("click", function (e) {
      if (e.target.classList.contains("plus") || e.target.classList.contains("minus")) {
        const productDiv = e.target.closest(".product");
        const quantitySpan = productDiv.querySelector(".quantity_count");
        let quantity = parseInt(quantitySpan.textContent);

        if (e.target.classList.contains("plus")) {
          quantity++;
        } else if (e.target.classList.contains("minus") && quantity > 1) {
          quantity--;
        }

        quantitySpan.textContent = quantity;
      }
    })
    */

    function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

function addToCart(event,form) {
  event.preventDefault(); 
    const formData = new FormData(form);

    fetch("{% url 'cart_product' %}", {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || "Item added to cart!");
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong.");
    });
}