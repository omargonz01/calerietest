

@app.route('/food-snap', methods=['GET'])
def food_snap():
   
    img_url = request.args.get('img_url')

    if img_url:
        
        response = requests.get(img_url)

        
        if response.status_code == 200:
          
            image = Image.open(BytesIO(response.content))

           
            model = genai.GenerativeModel('gemini-pro-vision')

            response = model.generate_content(["Analyse the food and give output in this manner in a json format eg {status:'unhealthy',description:'the food contains paneer and gravy'. est calories:'400-500 cal', XP:'the value ranges from 1-10 depending on the food health', diet: 'suggest a good diet for the person to stay fit and healthy'} pls do not halucinate and give unique recommendations and output for new food images", image], stream=True)
            response.resolve()

           
            return jsonify({"result": response.text})
        else:
            return jsonify({"error": "Failed to retrieve the image"}), 400
    else:
        return jsonify({"error": "img_url parameter is required"}), 400

@app.route ('/calories', methods=['GET'])
def calc_calories():
    food = request.args.get('food')
    if food:
        response = requests.get('https://api.edamam.com/api/food-database/parser?ingr='+food+'&app_id=1b3c5f0b&app_key=5f2b1a7c2a7e7f5e9e0e4c6f5f5b7d2e')
        if response.status_code == 200:
            data = response.json()
            calories = data['parsed'][0]['food']['nutrients']['ENERC_KCAL']
            return jsonify({"calories": calories})
        else:
            return jsonify({"error": "Failed to retrieve the food"}), 400
    else:
        return jsonify({"error": "food parameter is required"}), 400


@app.route('/food-recipe', methods=['GET'])
def food_recipe():
    food = request.args.get('food')
    if food:
        response = requests.get('https://api.edamam.com/search?q='+food+'&app_id=1b3c5f0b&app_key=5f2b1a7c2a7e7f5e9e0e4c6f5f5b7d2e')
        if response.status_code == 200:
            data = response.json()
            recipe = data['hits'][0]['recipe']['ingredientLines']
            return jsonify({"recipe": recipe})
        else:
            return jsonify({"error": "Failed to retrieve the food"}), 400
    else:
        return jsonify({"error": "food parameter is required"}), 400
