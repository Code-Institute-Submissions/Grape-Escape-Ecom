let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
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
let bankcard = elements.create('bankcard', { style: style });
bankcard.mount('#card-information');

bankcard.addEventListener('change', function (e) {
    let errorDiv = document.getElementbyId('card-errors');
    if (e.error) {
        let html = <span class="error-message">${e.error.message}</span>;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});