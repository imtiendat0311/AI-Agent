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