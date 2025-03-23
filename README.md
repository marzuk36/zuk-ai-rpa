# 🤖 AI + RPA Prototype Apps

**This repository contains two lightweight AI + RPA demo apps built with Streamlit,**  
showcasing how artificial intelligence and automation can streamline **Legal** and **Client Servicing** operations.

---

## 📄 Legal Contract Review – NER + Compliance

### 🎯 **Purpose**  
Assist legal and compliance teams in reviewing contracts by detecting missing clauses and extracting key information automatically.

### ⚙️ **How It Works**
- Uses the pretrained BERT-based NER model [`dslim/bert-base-NER`](https://huggingface.co/dslim/bert-base-NER) to extract:
  - **Persons**, **Organizations**, **Locations**, and **Dates**
- Performs rule-based clause detection using regex to find:
  - **Governing Law**, **Confidentiality**, **Termination**, **Payment Terms**, **Indemnity**
- Flags missing clauses as potential risks
- Displays a compliance checklist and calculates a risk score
- Includes **mock RPA buttons** (e.g., “Send for Legal Review”, “Auto-File”) to simulate downstream automation

> 💼 **LegalOps teams can use this tool as a first-pass triage**  
> to prioritize contracts for deeper review, ensuring key clauses are present.

---

## 📧 Email Prioritization Assistant

### 🎯 **Purpose**  
Help client servicing teams triage emails more efficiently based on intent, urgency, and sentiment.

### ⚙️ **How It Works**
- Performs intent classification using simple NLP logic
- Detects urgency using keywords like **"urgent"**, **"ASAP"**, etc.
- Runs sentiment analysis using **TextBlob**
- Labels each email with:
  - **Intent** (e.g., Complaint, Request)
  - **Urgency** (High / Normal)
  - **Sentiment** (Positive / Neutral / Negative)
- Generates a **priority tag** to assist fast decision-making

> 📨 **Support teams can auto-prioritize high-risk or time-sensitive emails,**  
> improving response times and SLA compliance.

---

## 🧠 Tech Stack

- **Python 3.10**
- **Streamlit**
- **Transformers**: [`dslim/bert-base-NER`](https://huggingface.co/dslim/bert-base-NER)
- **TextBlob**
- Regex
- GitHub + Streamlit Cloud (for deployment)

---

## 🌐 Live Demo

> 🚀 [Launch App on Streamlit Cloud](https://marzuk.streamlit.app)

---

## ✨ Features

- ✅ Named Entity Recognition (NER) using BERT
- ✅ Rule-based clause detection and risk flagging
- ✅ Compliance scoring system
- ✅ Email triage using intent, urgency, and sentiment
- ✅ RPA action simulation buttons
  
---

<sub>Created by [Marzuk](https://github.com/marzuk36) · Powered by Streamlit + Hugging Face Transformers</sub>
