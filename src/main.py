import  google.generativeai as genai
import  os
from    dotenv import load_dotenv
import  PIL.Image
import  requests
import  json

load_dotenv()

gemini_api_key = os.environ["GEMINI_API_KEY"]
if not gemini_api_key:
    raise ValueError("No GEMINI_API_KEY set for generativeai")
genai.configure(api_key=gemini_api_key)

spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
if not spoonacular_api_key:
    raise ValueError("No SPOONACULAR_API_KEY set for spoonacular")

# Placeholders
agent_1 = None
agent_2 = None
agent_3 = None
agent_4 = None
agent_5 = None

def agent_init_1():
    global agent_1, agent_2

    agent_1_job_description = """
        You are trying to understand the user's food preparation habits.
        You should ask the user about these topics: Time Investment, Dietary Restrictions, Health Focus, Ingredient Preference, and Cooking Equipment.
        You can ask one question at a time and each question should be on a different topic.
    """

    agent_1 = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=agent_1_job_description
    )

    agent_2_job_description = """
        You are reading a conversation between a user and an AI agent about the user's food preparation habits.
        Your job is to summarize the user's food preparation habits.
    """

    agent_2 = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=agent_2_job_description
    )

def agent_init_2(user_profile):
    global agent_3, agent_4, agent_5

    agent_3 = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
    )

    agent_4_job_description = f"""
        You read a json string about a recipe. 
        You read the user profile: {user_profile}.
        In the first line of your answer, you give me a number between 1 and 10 based on how much you think the user would like the recipe. 
        In the next line and after, you give me your reason for coming up with the number. 
    """

    agent_4 = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=agent_4_job_description
    )

    agent_5_job_description = f"""
        You read a string that includes different recipe's names, their grades, and the reasons for grades.
        You read the user profile: {user_profile}.
        Your job is to tell me the name of the recipe you think is best for the user.
        You can do this based on the grade; the highest grade is the best. 
        But sometimes, there are multiples with the highest grades. It is up to you to choose which is best among the highest-grade recipes.
        In the first line of your answer, you give me the name of the recipe that you think is the best word for word.
        In the following line and after, you give me your reason for coming up with the recipe chosen. 
    """

    agent_5 = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=agent_5_job_description
    )

def detect_ingredients(image_path):
    image   = PIL.Image.open(image_path)
    prompt      = 'Give me only list of ingredients currently in the provided image in comma seperated and plain text format with only specific ingredients'
    response    = agent_3.generate_content([prompt, image])
    list_of_ingredients = response.text.replace(" ","")
    return list_of_ingredients

def find_recipe_ID(list_of_ingredients):
    global recipe_info
    response    = requests.get(
        url="https://api.spoonacular.com/recipes/findByIngredients",
        params={
            "apiKey": spoonacular_api_key,
            "ingredients": list_of_ingredients,
            "number": 6
        }
    )
    if response.status_code == 200:
        recipes         = response.json()
        for i in recipes:
            value_list = []
            value_list.append(i["id"])
            recipe_info[i["title"]] = value_list

def find_best_recipe():
    global recipe_info, round_winner

    items = list(recipe_info.items())
    chunk_size = 2

    for i in range(0, len(items), chunk_size):
        grading_str = ''
        chunk = items[i:i + chunk_size]

        for key, value in chunk:
            response = requests.get(
                url=f"https://api.spoonacular.com/recipes/{value[0]}/information",
                params={"apiKey": spoonacular_api_key}
            )
            if response.status_code == 200:
                recipe_instr        = response.json()
                json_string         = json.dumps(recipe_instr, indent=4)
                agent_4_response    = agent_4.generate_content(json_string)
                instructions        = recipe_instr.get("instructions", "No instructions available") or "No instructions available"

                parts  = agent_4_response.text.split('\n\n')
                grade  = parts[0]
                reason = parts[1]

                # Appending to the recipe_info table
                value.append(grade)
                value.append(reason)
                value.append(instructions)

                grading_str += f"Name of the Recipe: {key}, Recipe Grade: {grade}, and Reason for the Grade: {reason}."

        # Saving round winner
        agent_5_response = agent_5.generate_content(grading_str)
        print(f"Round winner: {agent_5_response.text}")
        parts2  = agent_5_response.text.split('\n\n')
        round_winner[parts2[0]] = parts2[1]


state               = 'Create user profile'

# Part 1 setup
agent_init_1()
user_profile        = ''
chat_log            = []
chat                = agent_1.start_chat()

# Part 2 setup
recipe_info         = {}
round_winner        = {}


while True:
    match state:
        case 'Create user profile':
            if not chat_log:
                agent_1_response_2 = chat.send_message("Start the conversation about food")
                print("AI:", agent_1_response_2.text)
                chat_log.append({"role": "AI", "content": agent_1_response_2.text.strip()})

            user_input = input()
            # print("User:", user_input)
            chat_log.append({"role": "User", "content": user_input.strip()})

            # About 5 questions in
            if len(chat.history) >= 12:
                # Send chat log to Agent 2 for analysis
                context             = ". ".join([f"{entry['role']}: {entry['content']}" for entry in chat_log])
                agent_2_response    = agent_2.generate_content(context)
                user_profile        = agent_2_response.text
                print(f"User Profile: {user_profile}")

                # Let the user know we are proceeding to the next step
                agent_1_response_2  = chat.send_message("Tell the user that we are done with gathering their information. We a moving on to the next part")
                print("AI:", agent_1_response_2.text)

                #
                state = 'Find recipe recommendation from the input picture'
            else:
                agent_1_response_2 = chat.send_message(user_input)
                print("AI:", agent_1_response_2.text)
                chat_log.append({"role": "AI", "content": agent_1_response_2.text.strip()})

        case 'Find recipe recommendation from the input picture':
            agent_init_2(user_profile)
            image_path = input("Enter the path of the image: ")
            list_of_ingredients = detect_ingredients(image_path)
            print(f"Here are the ingredients spotted in the picture: {list_of_ingredients}")
            print("Looking up recipes")
            find_recipe_ID(list_of_ingredients)
            print("Finding the best recipe")
            find_best_recipe()

            #
            state = 'Give recipe recommendation'

        case 'Give recipe recommendation':

            for key, val in round_winner.items():
                print(f"Here is the recommendated recipe based on you profile: {key}")
                print()
                print(f"Reasoning: {val}")
                print()
                user_input = input(f"Do you want to proceed with making {key}? (y/n) ")
                print()
                if user_input.lower() == 'y':
                    print("Here is the instructions:")
                    print(recipe_info[key][3])
                    state = 'Last state'
                    break

            if state != 'Last state':
                print("We have maxed out the options")
                user_input = input(f"Do you want to look at the options one more? (y/n) ")
                if user_input.lower() == 'y':
                    state = 'Give recipe recommendation'
                else:
                    state = 'Last state'

        case 'Last state':

            user_input = input(f"Do you want to look at another picture? (y/n) ")
            if user_input.lower() == 'y':
                recipe_info     = {}
                round_winner    = {}
                state = 'Find recipe recommendation from the input picture'
            else:
                user_input = input(f"Do you want to create another profile? (y/n) ")
                if user_input.lower() == 'y':
                    user_profile    = ''
                    recipe_info     = {}
                    round_winner    = {}
                    chat_log        = []
                    chat            = None
                    chat            = agent_1.start_chat()
                    state           = 'Create user profile'