#!/usr/bin/env python
import os
from flask import Flask, request
import stripe
# Execute unit tests, integration tests, and manual tests
import sys
import unittest

if __name__ == "__main__":
app = Flask(__name__)
app.config['STRIPE_PUBLIC_KEY'] = os.environ.get('STRIPE_PUBLIC_KEY', 'your_stripe_public_key')
app.config['STRIPE_SECRET_KEY'] = os.environ.get('STRIPE_SECRET_KEY', 'your_stripe_secret_key')
stripe.api_key = app.config['STRIPE_SECRET_KEY']
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cc_Genckr.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


@app.route('/charge', methods=['POST'])
def charge():
    amount = 500
    if not token:
        return 'Error: stripeToken missing', 400
    currency = 'usd'
    description = 'Card Checker Charge'
token = request.form.get('stripeToken')

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            description=description,
            source=token,
        )
        return 'Charge successful!'
    except stripe.error.CardError as e:
        return str(e)

if __name__ == '__main__':
    # Check 'test' argument to run tests
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        sys.argv.pop(1)
        unittest.main()
    else:
        app.run()


