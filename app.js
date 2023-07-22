const express = require('express');
const app = express();
const stripeAPIKey = process.env.STRIPE_API_KEY || 'your_stripe_api_key';
const dotenv = require('dotenv');
dotenv.config();
const stripe = require('stripe')(stripeAPIKey);
const PORT = process.env.PORT || 3000;

// Set up static file serving
app.use('/static', express.static('static'));
// Middleware for JSON request handling
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Set up view engine
app.set('views', './templates');
app.set('view engine', 'html');
app.engine('html', require('ejs').renderFile);
// Routes placeholder
// Handler for root path
app.get('/', (req, res) => {
  res.render('index', { title: 'Card Checker Web Application' });
});
// Handler for card validation
app.post('/validate_card', async (req, res) => {
  try {
    const card = req.body;
    if (!card.number || !card.exp_month || !card.exp_year || !card.cvc) {
      throw new Error('Missing card information.');
    }
    const cardResult = await stripe.tokens.create({
      card: {
        number: card.number,
        exp_month: card.exp_month,
        exp_year: card.exp_year,
        cvc: card.cvc
      }
    });
    res.json({ success: true, token: cardResult.id });
  } catch (error) {
    res.status(400).json({ success: false, error: error.message });
  }
});
  res.render('index');
  res.send('Card Checker Web Application');
});

// Listen to PORT
app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);





