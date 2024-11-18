import google.generativeai as genai

def list_all_models():
    try:
        models = genai.list_models()
        for model in models:
            print(f"Name: {model.name}, Display Name: {model.display_name}")
    except Exception as exception:
        print("Error listing models:", exception)
list_all_models()