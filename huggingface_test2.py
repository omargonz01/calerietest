from PIL import Image

# testing how i can quickly test a model from huggingface's image to text options

from transformers import AutoModelForImageClassification, PreTrainedTokenizerFast
import requests

# Load the pre-trained model
model = AutoModelForImageClassification.from_pretrained("hugginglearners/Ethiopian-Food-Classifier")

# Load the tokenizer
tokenizer = PreTrainedTokenizerFast.from_pretrained("hugginglearners/Ethiopian-Food-Classifier")

# replace this with user input image.jpg
image = open("your_image.jpg", "rb").read()

# Prepare your image for the model
inputs = tokenizer(image, return_tensors="pt")

response = requests.get('https://api.edamam.com/api/food-database/parser?ingr='+food+'&app_id=1b3c5f0b&app_key=5f2b1a7c2a7e7f5e9e0e4c6f5f5b7d2e')
image = Image.open("user-uploaded-image.jpg")
processed_image = tokenizer(image, return_tensors="pt")

# Make a prediction
outputs = model2(**processed_image)

# Print the estimated nutritional value
print(outputs.logits)
