# Recipe Recommendation Agent

This project is a conversational AI agent that recommends recipes based on user preferences and ingredients detected in images. The agent leverages **Google Generative AI (Gemini)** for dialogue and reasoning tasks and **Spoonacular API** for recipe data.

---

## Features

1. **Interactive User Profile Creation**: The agent gathers information about the user's dietary habits, time investment, cooking equipment, and preferences through a conversation.
2. **Ingredient Detection**: Detects ingredients from an uploaded image using the Gemini API.
3. **Recipe Search**: Fetches recipes from the Spoonacular API based on detected ingredients.
4. **Recipe Evaluation**: Grades recipes based on their alignment with the user profile.
5. **Recommendation**: Selects and recommends the best recipe to the user, providing a detailed explanation for the choice.

---

## Demo

### **How It Works**

1. **User Profile Creation**:
   - The agent interacts with the user, asking 5-6 questions about their food preparation habits.
   - It summarizes these preferences into a "user profile."

2. **Ingredient Detection**:
   - The user uploads an image of ingredients, and the agent detects specific ingredients.

3. **Recipe Search and Grading**:
   - The agent fetches recipes using the Spoonacular API and evaluates them against the user profile.

4. **Recommendation**:
   - The agent suggests the best recipe with reasons and instructions for preparation.

5. **Repeatable Actions**:
   - Users can upload new images or restart the profiling process.

---

## Installation and Setup

### **Prerequisites**

1. Python 3.8 or higher.
2. API Keys for:
   - [Google Generative AI (Gemini)](https://developers.generativeai.google/)
   - [Spoonacular](https://spoonacular.com/food-api).

### **Setup**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/recipe-recommendation-agent.git
   cd recipe-recommendation-agent
2. **Set Up Environment**:
* Copy .env.example to .env:
   ```bash
   cp .env.example .env
* Add your API keys to .env:
   ```plaintext
   GEMINI_API_KEY=your_gemini_api_key
   SPOONACULAR_API_KEY=your_spoonacular_api_key
3. **Install Dependencies:**:
   ```bash
   pip install -r requirements.txt
4. **Run the Program**:
   ```bash
   python src/main.py   
## File Structure
   ```bash
    recipe-agent/
    ├── README.md               # Detailed project documentation
    ├── requirements.txt        # Python dependencies
    ├── src/
    │   ├── main.py             # Entry point of the application
    variables
    ├── LICENSE                 # License information
```
## How to Use

### Start the Program:
```bash
python src/main.py
```
### Follow the Prompts:
<ol>
  <li>Answer questions about your cooking preferences.</li>
  <li>Upload an image of ingredients when prompted.</li>
  <li>Review the recipes suggested and their reasoning.</li>
</ol>

### Interact with the Agent:
<ol>
  <li>Confirm if you want to proceed with a recipe or explore other options.</li>
  <li>Restart the process if needed.</li>
</ol>

## Example Usage
### Step 1: Create User Profile

    AI: What is your typical time investment for cooking?
    User: Around 30 minutes per meal.
    ...
    AI: Thank you! We've created a user profile based on your preferences.

### Step 2: Detect Ingredients

    Enter the path of the image: /path/to/ingredients.jpg
    AI: Detected ingredients: tomatoes, onions, garlic.

### Step 2: Detect Ingredients

    Enter the path of the image: /path/to/ingredients.jpg
    AI: Detected ingredients: tomatoes, onions, garlic.

### Step 3: Recipe Recommendation

    AI: Based on your profile and the detected ingredients, we recommend:
    - Recipe: Spaghetti Marinara
    - Grade: 9/10
    - Reason: It fits your time constraints, uses your ingredients, and matches your dietary preferences.
## Design Details

### Agent Structure
<ul>
  <li>Agent 1: Asks questions to build the user profile.</li>
  <li>Agent 2: Summarizes the user profile from the conversation.</li>
  <li>Agent 3: Detects ingredients from uploaded images.</li>
  <li>Agent 4: Grades recipes based on the user profile.</li>
  <li>Agent 5: Selects the best recipe among graded options.</li>
</ul>

### State Machine
Manages the flow of the program:
<ol>
  <li>Create user profile: Builds user profile.</li>
  <li>Find recipe recommendation from the input picture: Detects ingredients and searches for recipes.</li>
  <li>Give recipe recommendation: Recommends a recipe based on grading.</li>
  <li>Last state: Restarts or exits.</li>
</ol>

### Self-Propagation Mechanism
The agent autonomously:
<ol>
  <li>Create user profile: Builds user profile.</li>
  <li>Fetches recipes.</li>
  <li>Grades and recommends recipes without manual intervention.</li>

## Future Improvements

<ul>
  <li>Better Ingredient Detection: Incorporate advanced vision models for accuracy.</li>
  <li>Multilingual Support: Expand the agent's language capabilities.</li>
  <li>Enhanced Recipe Filtering: Use nutrition data for more tailored recommendations.</li>
</ul>

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributors
Hoan Lam, Dat Nguyen, Khoi Tran

For questions or suggestions, feel free to open an issue.