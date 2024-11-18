import google.generativeai as genai
import os
from dotenv import load_dotenv
import PIL.Image

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('models/gemini-1.5-flash')

burger_img = PIL.Image.open("burger.jpg")

prompt = 'Write me a description of this provided image'
response = model.generate_content([prompt,burger_img])

print(response.text)