

// Import the Tesseract.js library
const Tesseract = require('tesseract.js');

// Load an image
const image = 'lol.jpg';

Tesseract.recognize(image)
  .then(result => {
    console.log(result.text);
  })
  .catch(err => {
    console.error('Error:', err.message);
  });
