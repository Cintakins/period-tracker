var stripe_public_key = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var client_secret = document.getElementById('id_client_secret').textContent.slice(1, -1);
console.log(stripe_public_key)
var stripe = Stripe(stripe_public_key);

var elements = stripe.elements();

var style = {
    base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#32325d"
        }
    },
    invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#fa755a",
        iconColor: "#fa755a"
    }
};
let card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// card.on("change", function (event) {
//     // Disable the Pay button if there are no card details in the Element
//     document.querySelector("#submit-checkout").disabled = event.empty;
//     document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
//     if (event.error) {
//         document.querySelector("#card-error").innerHTML = `<span>${event.error.message}</span>`;
//     } else {
//         document.querySelector("#card-error").innerHTML = ''
//     }
// });

var form = document.getElementById("payment-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    // Complete payment when the submit button is clicked
    payWithCard(stripe, card, data.clientSecret);
});