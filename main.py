import streamlit as st

# Set page config
st.set_page_config(page_title="AI + RPA Demo Projects", layout="centered")

# Title
st.title("AI + RPA Demo Projects")

st.markdown("Select a demo project to explore. Each prototype demonstrates how AI and automation can be used to streamline key processes in Legal and Client Servicing domains.")

# Demo menu
menu = ["📄 Legal NER Demo", "📧 Email Prioritization"]
choice = st.radio("Choose a Demo", menu)

# ---------- Legal NER Demo ----------
if choice == "📄 Legal NER Demo":
    st.subheader("📄 Legal Contract Review – NER + Compliance")
    st.markdown("""
    **Purpose:** Assist legal teams in reviewing contracts by extracting key entities and flagging missing or risky clauses.  
    **Tech Used:** `dslim/bert-base-NER` (Hugging Face), regex clause detection, Streamlit.  
    **Features:** Named Entity Recognition (ORG, PER, DATE, LOC), rule-based clause detection, compliance score, mock RPA actions.
    """)
    st.markdown("[🔗 Click here to go to Legal NER Demo](legal_ner_app)")

# ---------- Email Prioritization Demo ----------
elif choice == "📧 Email Prioritization":
    st.subheader("📧 Email Intent & Urgency Classifier")
    st.markdown("""
    **Purpose:** Help client servicing teams triage emails by identifying intent, urgency, and sentiment for faster response handling.  
    **Tech Used:** Fine-tuned classification model, basic sentiment analysis, Streamlit UI.  
    **Features:** Email classification by type (e.g. request, complaint), urgency scoring, auto-priority labels.
    """)
    st.markdown("[🔗 Click here to go to Email Prioritization Demo](email_app)")
