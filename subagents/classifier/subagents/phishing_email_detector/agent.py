"""
Phishing Email Detector Agent
Uses pre-trained TF-IDF + Logistic Regression model to classify emails.
"""

import os
import joblib
from google.adk.agents import Agent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "/Users/abhishekp.v.s/Desktop/Email-Security-Agents/logistic_regression.joblib")
VECTORIZER_PATH = os.path.join(BASE_DIR, "/Users/abhishekp.v.s/Desktop/Email-Security-Agents/tfidf_vectorizer.joblib")

vectorizer = joblib.load(VECTORIZER_PATH)
model = joblib.load(MODEL_PATH)

def classify_email(email_text: str) -> dict:
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0].max()

    return {
        "prediction": "PHISHING" if prediction == 1 else "LEGITIMATE",
        "confidence": round(float(probability), 3)
    }
phishing_email_detector_agent = Agent(
    name="PhishingEmailDetectorAgent",
    model="gemini-2.0-flash",
    instruction=""" 
    Only respond if the user provides email text content.
    Ignore greetings (hi, hello, hey) and casual chat.
    If the input is a greeting (hi, hello, hey) or not a email text, stay completely silent and do not reply.
    When analyzing, return only one of: PHISHING or LEGITIMATE.
    you are a helpful agent that uses the following tool to predict:
      whether the email body is phising or legit.""",
    description="Classifies email text as PHISHING or LEGITIMATE using ML model.",
    tools=[classify_email],
    output_key="phishing_result"
)