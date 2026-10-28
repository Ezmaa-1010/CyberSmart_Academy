CyberSmart Academy
An interactive cybersecurity education app built with Python and Streamlit. It helps learners practice identifying phishing messages, understand password safety, and answer everyday cybersecurity scenarios. The app also supports optional explanations from the xAI Grok API.
Features
- Phishing identification game with fictional training emails and explanations.
- Password safety checker using simple rule-based checks that run locally in the app.
- Cybersecurity scenarios and quizzes with feedback.
- Personal safety score based on correct answers in completed activities.
- Optional Grok assistant for beginner-friendly cybersecurity questions.
Privacy note: Do not enter a real password into the checker. Password text is not sent to Grok. The score is an educational indicator, not a guarantee of security. Activity progress is stored in Streamlit session state and is not a permanent account profile.

Project files
cybersmart_academy/
├── app.py
├── requirements.txt
└── README.md
Run locally
1. Install Python 3.10 or newer.
2. Download or clone this project.
3. Open a terminal in the project folder.
4. Install dependencies:
   pip install -r requirements.txt
5. Start the app:
   streamlit run app.py
6. Open the local URL shown in the terminal, usually http://localhost:8501.
The learning games and rule-based password checker work without an API key.
Configure the Grok API key
1. Create or copy an API key from your xAI account.
2. Never paste the key directly into app.py or commit it to GitHub.
3. For local use, you can set an environment variable before starting Streamlit.
   Windows PowerShell
   $env:GROK_API_KEY="your-xai-api-key"
   streamlit run app.py
   macOS / Linux
   export GROK_API_KEY="your-xai-api-key"
   streamlit run app.py
The app calls the OpenAI-compatible xAI endpoint at https://api.x.ai/v1/chat/completions and uses the grok-3-mini model. If your xAI account does not have access to that model, change the model value in app.py to a model available to your account.
Deploy on Streamlit Community Cloud
1. Create a GitHub repository and upload app.py, requirements.txt, and README.md.
2. Open Streamlit Community Cloud and deploy the repository.
3. In your deployed app's Settings → Secrets, add:
   GROK_API_KEY = "your-xai-api-key"
4. Save the secrets and restart/reboot the app if required.
Keep the API key in Streamlit Secrets. Do not commit a .streamlit/secrets.toml file containing a real key to a public repository.
How the score works
The personal safety score is the percentage of correct answers among the phishing and scenario questions answered in the current session. Each correct answer is worth 10 points. It is a learning progress indicator, not a professional security rating.
Troubleshooting
- ModuleNotFoundError: run pip install -r requirements.txt or confirm Streamlit Cloud installed the dependencies.
- Grok is not configured: add GROK_API_KEY to your environment or Streamlit Secrets.
- Grok API error: check that the key is valid, billing/access is configured, and the model name is available to your xAI account.
- App syntax or startup error: ensure the full app.py file was uploaded and that you did not accidentally omit part of the code.
Disclaimer
This project is for general cybersecurity awareness and education. It is not a substitute for professional incident response, and its rule-based checks may produce inaccurate or incomplete assessments.
