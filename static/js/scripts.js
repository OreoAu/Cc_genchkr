
document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('card-details-form');
  const submitBtn = document.getElementById('submit-card-details');
const stripe = Stripe('REPLACE_WITH_API_KEY');
  const elements = stripe.elements();
  const card = elements.create('card');

  card.mount('#card-element');

  card.on('change', function (event) {
    const displayError = document.getElementById('card-errors');
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = '';
    }
  });

  form.addEventListener('submit', async function (event) {
    event.preventDefault();

    // Call backend API to create a PaymentIntent
    const response = await fetch('/api/create_payment_intent', {
      // Add authentication headers for secure API communication
      'Authorization': 'Bearer REPLACED_WITH_API_SECRET_KEY',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    const paymentIntent = await response.json();

    const result = await stripe.confirmCardPayment(paymentIntent.client_secret, {
      payment_method: {
        card: card,
      }
    });

    if (result.error) {
      // Show user an error message
      const errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      // Payment succeeded, show success message
      const successElement = document.getElementById('payment-success');
      successElement.textContent = 'Payment successful!';
    }
  });
});

