const fetch = require('node-fetch');

const apiKey = 'API_KEY';

// The URL of the image you want to analyze
const imageUrl = 'https://www.pommietravels.com/wp-content/uploads/2012/04/Zurek-soup.jpg';

// The API endpoint
const apiEndpoint = `https://api.bite.ai/vision?image_url=${encodeURIComponent(imageUrl)}`;

// Make a request to the API
fetch(apiEndpoint, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${apiKey}`
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error:', error);
});
