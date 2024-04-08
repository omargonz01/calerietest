

// Import the Tesseract.js library
const Tesseract = require('tesseract.js');

// Load an image
const image = 'lol.jpg';

// Recognize text in the image
Tesseract.recognize(image)
  .then(result => {
    // Print the recognized text
    console.log(result.text);
  })
  .catch(err => {
    console.error('Error:', err);
  });


//   tested with couple images - returns undefined - will come back later to fix