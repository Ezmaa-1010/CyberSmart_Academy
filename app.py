import os
import random
import re
import streamlit as st

try:
    from groq import Groq
except ImportError:
    Groq = None

st.set_page_config(
    page_title="CyberSmart Academy",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------- Sample content -----------------------------
PHISHING_SCENARIOS = [
    {
        "sender": "security-alerts@paypaI.example",
        "subject": "URGENT: Your account will be closed in 10 minutes",
        "message": "We noticed unusual activity. Confirm your password immediately to avoid losing access.",
        "clues": [
            "The message uses pressure and urgency.",
            "The sender address uses a suspicious look-alike spelling.",
            "A legitimate service should not ask you to send your password in a message.",
        ],
        "answer": "Phishing",
        "explanation": "This message uses urgency, a look-alike sender address, and a request for a password. Don't click links or share credentials. Visit the service using its official app or a web address you type yourself.",
    },
    {
        "sender": "library@university.example",
        "subject": "Library opening hours this week",
        "message": "The library will close at 5 PM on Friday. You can check the notice board in the student portal.",
        "clues": [
            "The message gives routine information.",
            "It does not request a password, payment, or urgent action.",
            "You can verify the notice through a known university channel.",
        ],
        "answer": "Likely legitimate",
        "explanation": "This message has no obvious phishing indicators in the text shown. Still, verify unexpected messages through a known official channel; a message can look ordinary and still be fraudulent.",
    },
    {
        "sender": "prize-team@free-gift.example",
        "subject": "Congratulations! You won a new phone",
        "message": "You were selected randomly. Pay a small delivery fee today and send your one-time code to claim the prize.",
        "clues": [
            "An unexpected prize is used as bait.",
            "It asks for payment to claim the prize.",
            "It asks for a one-time code, which must remain private.",
        ],
        "answer": "Phishing",
        "explanation": "Unexpected prizes, payment demands, and requests for one-time codes are strong warning signs. Never share an OTP. Verify promotions independently using the organisation's official website or app.",
    },
    {
        "sender": "it-helpdesk@company.example",
        "subject": "Action required: review your account",
        "message": "Please review the account notice in the usual employee portal. If you are unsure, contact IT using the number in the company directory.",
        "clues": [
            "It points to a known portal instead of asking for a password by email.",
            "It suggests verifying through a known contact method.",
            "The text alone cannot prove who sent it.",
        ],
        "answer": "Not enough information",
        "explanation": "There isn't enough information to label this message safe. The safest choice is to open the portal using a saved bookmark or known address, and contact IT through the company directory.",
    },
    {
        "sender": "delivery-update@parcel.example",
        "subject": "Delivery problem — confirm details",
        "message": "Your parcel is delayed. Open the attached file and enable macros to see the delivery address.",
        "clues": [
            "It asks you to open an unexpected attachment.",
            "It asks you to enable macros, which can run risky code.",
            "You can check delivery status through the courier's official app or website.",
        ],
        "answer": "Phishing",
        "explanation": "Unexpected attachments and requests to enable macros are dangerous warning signs. Don't open the file. Check your delivery directly through the courier's official app or website.",
    },
]

QUIZ_QUESTIONS = [
    {
        "topic": "Phishing",
        "question": "You receive an unexpected email asking for your account password. What is the safest response?",
        "options": [
            "Reply with the password so support can help",
            "Do not reply; verify through the official app or website",
            "Forward it to all your friends",
            "Click every link to see where it goes",
        ],
        "answer": "Do not reply; verify through the official app or website",
        "explanation": "Never send passwords by email or message. Use a known official app, saved bookmark, or address you type yourself.",
    },
    {
        "topic": "Account security",
