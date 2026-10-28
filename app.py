import os
import random
import re
import requests
import streamlit as st

st.set_page_config(
    page_title="CyberSmart Academy",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# App content and rule-based checks
# ----------------------------
PHISHING_EMAILS = [
    {
        "sender": "security-alert@paypaI-support.example",
        "subject": "URGENT: Your account will be closed",
        "body": "We detected unusual activity. Verify your account immediately using this link or your account will be permanently suspended.",
        "answer": "Phishing",
        "clues": [
            "Urgent pressure and a threat of account closure",
            "A suspicious sender address that imitates a trusted brand",
            "A request to click a link to verify an account",
        ],
    },
    {
        "sender": "updates@library.example",
        "subject": "Your library book is due Friday",
        "body": "This is a reminder that your borrowed book is due Friday. You can check the due date by opening the library app or typing the library website address into your browser.",
        "answer": "Likely legitimate",
        "clues": [
            "The message does not demand passwords or payment",
            "It suggests opening the official app or typing the address yourself",
            "Still verify unexpected messages through a known official channel",
        ],
    },
    {
        "sender": "prize-team@claim-now.example",
        "subject": "Congratulations! Claim your free phone",
        "body": "You have won a new phone! Pay a small delivery fee today and enter your card details to receive your prize.",
        "answer": "Phishing",
        "clues": [
            "An unexpected prize is used to attract attention",
            "It asks for card details and a fee",
            "A deadline creates pressure to act quickly",
        ],
    },
    {
        "sender": "hr@company.example",
        "subject": "Please review the updated staff policy",
        "body": "Please review the policy during your next work session. If you are unsure whether this message is genuine, visit the company portal using your saved bookmark or contact HR through the usual channel.",
        "answer": "Likely legitimate",
        "clues": [
            "It does not ask you to share a password or payment details",
            "It recommends using a known company portal",
            "Sender addresses can be spoofed, so verify unexpected attachments or links",
        ],
    },
    {
        "sender": "support@micros0ft-account.example",
        "subject": "Password expired — sign in now",
        "body": "Your password expires in 10 minutes. Use the link below and enter your password and one-time code to prevent account deletion.",
        "answer": "Phishing",
        "clues": [
            "It creates extreme urgency",
            "The sender uses a look-alike brand spelling",
            "It asks for a password and one-time code through a message link",
        ],
    },
]

SCENARIOS = [
    {
        "question": "A stranger messages you a link and says you must log in to see a surprise package. What should you do?",
        "options": [
            "Open the link and sign in quickly",
            "Ignore the link and verify the claim through the official delivery service",
            "Forward the link to friends to ask if it works",
        ],
        "answer": "Ignore the link and verify the claim through the official delivery service",
        "explanation": "Unexpected links can lead to fake sign-in pages. Use the official app or a website address you already trust.",
        "points": 10,
    },
    {
        "question": "You receive a login approval request that you did not initiate. What is the safest response?",
        "options": [
            "Approve it so the notifications stop",
            "Deny it, change your password if needed, and review account security",
            "Share the code with the person who says they are IT support",
        ],
        "answer": "Deny it, change your password if needed, and review account security",
        "explanation": "An unexpected approval request may mean someone knows your password. Never share verification codes.",
        "points": 10,
