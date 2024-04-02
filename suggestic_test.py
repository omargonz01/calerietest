import requests
import json


base_url = 'https://api.suggestic.com'


api_key = 'Api-key'
user_id = 'User-id'

# Define headers 
headers = {
    'x-api-key': api_key,
    'x-user-id': user_id,
    'Content-Type': 'application/json'
}

# Define the GraphQL query for recipe search
query = """
query {
  searchRecipes(query: "chicken") {
    edges {
      node {
        id
        title
        image
        ingredients {
          name
          quantity
          unit
        }
        instructions
      }
    }
  }
}
"""

# Make the API request
response = requests.post(base_url, headers=headers, data=json.dumps({'query': query}))

# Print the response
print(response.json())
