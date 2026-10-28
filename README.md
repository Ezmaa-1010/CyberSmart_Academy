🛡️ CyberSmart Academy
CyberSmart Academy is a beginner-friendly, interactive cybersecurity awareness app built with Python and Streamlit. It teaches safer digital habits through fictional phishing examples, a local password safety demo, quizzes, and real-life decision scenarios.
Features
- Dashboard: XP, level, completed scenarios, and safety reminders.
- Phishing Detective: Review simulated messages, inspect clues, and learn how to identify common warning signs.
- Password Safety Lab: Test a made-up sample password against basic local checks. The app processes the entered value on its server, but does not save it persistently or send it to an external API.
- Quiz Arena: Ten multiple-choice cybersecurity questions with explanations.
- Safety Scenarios: Practice safe responses to common online situations.
- XP and levels: Earn points for completing learning activities.
Important: This is an educational awareness demo, not a professional security audit. Do not enter a real password. Scoring/progress is held in Streamlit session state and may reset when the session ends or the app restarts. Persistent user accounts and database storage are not included in this first version.

Run locally
1. Install Python
Use Python 3.10 or newer.
2. Download or clone this repository
git clone https://github.com/YOUR-USERNAME/cybersmart-academy.git
cd cybersmart-academy
Or download the repository ZIP from GitHub and extract it.
3. Create and activate a virtual environment (recommended)
Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
4. Install dependencies
python -m pip install -r requirements.txt
5. Start the app
streamlit run app.py
Streamlit will print a local URL, usually http://localhost:8501.
Deploy on Streamlit Community Cloud
1. Create a GitHub repository named cybersmart-academy.
2. Upload app.py, requirements.txt, and README.md to the repository's root directory.
3. Visit Streamlit Community Cloud and sign in with GitHub.
4. Choose Create app (or Deploy an app).
5. Select your repository, branch (usually main), and main file path: app.py.
6. Click Deploy and wait for the build to finish.
7. Open the generated public app URL.
No API key or secret is required for this version.
Repository structure
cybersmart-academy/
├── app.py
├── requirements.txt
└── README.md
Safety and privacy notes
- All messages in Phishing Detective are fictional training examples using reserved .example domains.
- Do not use real credentials in the Password Safety Lab.
- The password demo processes the sample in the app server process. It is not saved persistently or sent to an external API by the app. As with any hosted web app, the input is transmitted to the server running the app, so only use fictional sample passwords.
- The password strength estimate is intentionally simple; it does not check breach databases or guarantee that a password is safe.
- The app is for defensive education only. Do not use security lessons to access accounts or systems without permission.
Troubleshooting
- streamlit command not found: run python -m pip install -r requirements.txt, then start with python -m streamlit run app.py.
- App fails during dependency install: confirm that requirements.txt contains streamlit>=1.40,<2.0, then redeploy.
- Changes do not appear: commit and push the updated files to GitHub, then use the app's Streamlit Community Cloud management page to reboot or redeploy.
- Progress disappeared: this starter version uses session state only. Persistent storage is a future enhancement.
License
Choose a license before publishing if you intend others to reuse or redistribute this project. For a simple open-source project, consider the MIT License after reviewing its terms.
