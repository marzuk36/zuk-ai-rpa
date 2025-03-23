📂 Project Overview
This repository contains two lightweight AI + RPA prototype apps built with Streamlit, showcasing how artificial intelligence and automation can streamline Legal and Client Servicing operations.

📄 1. Legal Contract Review – NER + Compliance
🎯 Purpose
Assist legal and compliance teams in reviewing contracts by detecting missing clauses and extracting key information automatically.

⚙️ How It Works
Uses the pretrained BERT-based NER model dslim/bert-base-NER to extract:

Persons, Organizations, Locations, and Dates

Performs rule-based clause detection using regex to find:

Governing Law, Confidentiality, Termination, Payment Terms, Indemnity

Flags missing clauses as potential risks

Displays a compliance checklist and calculates a risk score

Includes mock RPA buttons to simulate actions like "Send for Legal Review"

✅ Example Use Case
LegalOps teams can use this tool as a first-pass triage to prioritize contracts for deeper review, ensuring key clauses are present.

📧 2. Email Prioritization Assistant
🎯 Purpose
Help client servicing teams triage emails more efficiently based on intent, urgency, and sentiment.

⚙️ How It Works
Performs intent classification using simple NLP keyword logic

Detects urgency using keywords like "urgent", "ASAP", etc.

Runs sentiment analysis using TextBlob

Labels each email with:

Intent (e.g., Complaint, Request)

Urgency (High / Normal)

Sentiment (Positive / Neutral / Negative)

Generates a priority tag based on all three factors

✅ Example Use Case
Support teams can use this to auto-prioritize high-risk or time-sensitive emails, improving SLA response time.

🧠 Tech Stack
Python 3.10

Streamlit

Transformers: dslim/bert-base-NER

TextBlob

Regex

GitHub + Streamlit Cloud (Deployment)

## 🌐 Live Demo  
> [🔗 Launch the app](https://marzuk.streamlit.app)
