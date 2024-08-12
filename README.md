# Calories Advisor App

**Calories Advisor App** uses Google's Gemini 1.5 Pro to analyze food images and estimate nutritional content. This app helps users understand the calorie content and nutritional value of their food based on uploaded images. It provides insights into ingredients, calorie estimates, and general dietary advice.

## Features

- **Image Analysis**: Upload food images to get insights on calorie content.
- **Nutritional Breakdown**: Receive details on calories, possible ingredients, and nutrient distribution (carbohydrates, fats, vitamins, etc.).
- **Portion Size Input**: Specify the portion size for more accurate estimates.
- **Dietary Advice**: Get tips on achieving a balanced diet and improving overall health.

## Technologies Used

- **Streamlit**: For building the user interface.
- **Google Gemini 1.5 Pro**: For analyzing and generating content from images.
- **Pillow (PIL)**: For image processing.
- **Python Libraries**: `dotenv`, `os`, `io`, `base64`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shruti23-ui/Calories-Advisor-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Calories-Advisor-App
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you have a `.env` file with your `GOOGLE_API_KEY` set.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided URL in your browser.
4. Upload a food image and enter the portion size to get nutritional insights.

## Contribution

Feel free to contribute by opening issues or submitting pull requests. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
