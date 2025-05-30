# 🧠 AI-Powered Mental Health Chatbot

This project is an AI-based chatbot built to detect signs of mental stress and provide empathetic responses using natural language processing. It is powered by a fine-tuned **LLaMA 2 7B** model and aims to promote mental well-being through thoughtful and supportive conversations.

## 🌟 Project Overview

- **Objective:** Identify stress indicators in user input and respond supportively using an AI language model.
- **Model Used:** Fine-tuned LLaMA 2 (7B) for mental health dialogue.
- **Interface:** Streamlit-based frontend for real-time interaction.

---

## 🔧 Technologies Used

- **Python**
- **LLaMA 2 (7B)** – via Hugging Face Transformers
- **Streamlit** – for web deployment
- **Tokenizers, Datasets** – for data processing
- **PyTorch / CUDA** – for model fine-tuning
- **python-dotenv** – for secure API key management

---

## 🚀 Features

- Analyzes user input to detect mental stress
- Generates empathetic, context-aware responses
- Fine-tuned on mental health-specific datasets
- Lightweight and interactive Streamlit app

---

## 🔑 API Key Setup

This project uses an API key to access the LLaMA 2 model (or other services).

1. Create a `.env` file in the root directory.
2. Add your API key in the following format:

```bash
API_KEY=your_api_key_here

3. The key will be loaded using the python-dotenv package.
✅ Important: Do not push your .env file to GitHub. Add it to your .gitignore file like this:
bash
.env

📂 Project Structure
├── data/
│   └── mental_health_dataset.csv
├── model/
│   └── fine_tuned_llama_model/
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── chatbot.py
├── app/
│   └── streamlit_app.py
├── .env
├── README.md
└── requirements.txt


▶️ How to Run

Step 01 : Clone the Repository
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot

Step 02 : Install Dependencies

Step 03 : Set Up API Key
Create a .env file as shown above and add your key.


Step 04 : Launch the Chatbot App

Step 04 : bash
streamlit run app/streamlit_app.py


