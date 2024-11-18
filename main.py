import google.generativeai as genai
import os
from dotenv import load_dotenv
import PIL.Image
import requests

load_dotenv()

gemini_api_key = os.environ["GEMINI_API_KEY"]
if not gemini_api_key:
    raise ValueError("No GEMINI_API_KEY set for generativeai")

spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
if not spoonacular_api_key:
    raise ValueError("No SPOONACULAR_API_KEY set for spoonacular")


recipe_endpoints = "https://api.spoonacular.com/recipes/findByIngredients"


genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel('models/gemini-1.5-flash')
# pick a image
img_path = input("Enter the path of the image: ")
fridge_img = PIL.Image.open(img_path)

prompt = 'Give me only list of ingredients currently in the provided image in comma seperated and plain text format with only specific ingredients'

print("Prompt: ", prompt)

# asking LLM ( Gemini ) to generate content based on the prompt and image
response = model.generate_content([prompt,fridge_img])

list_of_ingredients = response.text.replace(" ","")
print("Answer: ", list_of_ingredients)

print("Gathering recipes for the following ingredients: ", list_of_ingredients)

# get request to spoonacular api
response = requests.get(recipe_endpoints, params={"apiKey": spoonacular_api_key, "ingredients": list_of_ingredients, "number": 5})

if response.status_code == 200:
   list_recipes = response.json()
   for i in list_recipes:
       print(i["title"])