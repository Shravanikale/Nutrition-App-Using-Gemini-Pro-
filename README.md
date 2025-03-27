# Gemini Pro AI Health Management App

## Overview
The **Gemini Pro AI Health Management App** is an AI-powered nutritionist application that helps users analyze food images and provides calorie estimations. It is built using **Streamlit** and integrates with **Google Gemini Pro** for AI-based analysis.

## Features
- 📷 **Image-based Food Analysis**: Upload a food image to get calorie details.
- 💬 **AI-powered Insights**: Uses Gemini Pro AI to provide nutrition information.
- ⚡ **User-friendly UI**: Simple drag-and-drop functionality for food image uploads.
- 🌐 **Deployable on Streamlit Cloud, Render, or AWS**.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Streamlit
- OpenAI/Google Gemini API (if applicable)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gemini-pro-nutritionist.git
   cd gemini-pro-nutritionist
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and add your API key:
     ```
     API_KEY=your_api_key_here
     ```
   - Or, if deploying on **Streamlit Cloud**, add secrets via `secrets.toml`.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Deployment
### Deploy on Streamlit Cloud
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and create a new app.
3. Add API secrets in `Secrets` settings.
4. Deploy your app!

## Screenshots

### Home Page
![Home Page](assets/Screenshot%20(207).png)

### Upload Image Section
![Upload Image](assets/Screenshot%20(208).png)

### Analysis Result
![Analysis Result](assets/Screenshot%20(209).png)


## Technologies Used
- **Python**
- **Streamlit**
- **Google Gemini Pro API**
- **PIL for Image Processing**


## Contact
For queries, feel free to reach out!

📧 Email: kaleshravani84@gmail.com 

