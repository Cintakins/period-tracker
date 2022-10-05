var stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);

var stripe = Stripe(stripePublicKey);

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

// var form = document.getElementById("form-payment");
// form.addEventListener("submit", function (event) {
//     event.preventDefault();
//     card.update({'disabled': true});
//     document.getElementById('submit-checkout').setAttribute('disabled', true);
//     stripe.confirmCardPayment(clientSecret, {
//         payment_method:{
//             card: card,
//         }
//     }).then(function(result){
//         if (result.error) {
//             let text = `
//             <span>${result.error.message}</span>`;
//             document.querySelector("#card-error").innerHTML = text;
//             card.update({'disabled': false});
//             document.getElementById('submit-checkout').setAttribute('disabled', false);
//         } else {
//             if (result.paymentIntent.status == 'succeeded'){
//                 form.submit();
//             }
//         }       
//     })
//     // Complete payment when the submit button is clicked
//     payWithCard(stripe, card, data.clientSecret);
// });




// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var formSubmit = document.getElementById('submit-checkout');
var form = document.getElementById('form-payment');

formSubmit.addEventListener('click', function(ev) {
    console.log('something happened2')
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-checkout').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-checkout').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});