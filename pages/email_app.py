import streamlit as st
import pandas as pd
from textblob import TextBlob

# Set up page
st.set_page_config(page_title="Client Email Prioritization", layout="wide")
st.title("📧 Client Email Prioritization Dashboard")
st.info("📂 For this POC, we're using a demo CSV file instead of connecting to an email server (e.g., IMAP/Outlook).")
# Delay loading of CSV until button is clicked
load_data = st.button("🚀 Load Demo Email Data")

# Only proceed if button is clicked
if load_data:
    @st.cache_data
    def load_demo_emails():
        return pd.read_csv("test_emails.csv")

    email_data = load_demo_emails()



    # ----- Email Classification Logic -----
    def detect_intent(text):
        text = text.lower()
        if any(word in text for word in ["status", "information", "know", "details"]):
            return "Inquiry"
        elif any(word in text for word in ["delay", "issue", "problem", "not working", "frustrated"]):
            return "Complaint"
        elif any(word in text for word in ["please send", "can you provide", "request", "need", "require"]):
            return "Request"
        elif any(word in text for word in ["thank", "great", "feedback", "appreciate", "love"]):
            return "Feedback"
        else:
            return "General"

    def classify_email(text):
        if "urgent" in text.lower():
            urgency = "High"
        elif "please" in text.lower():
            urgency = "Medium"
        else:
            urgency = "Low"

        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            sentiment_label = "Positive"
        elif sentiment < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        intent = detect_intent(text)
        return urgency, sentiment_label, intent

    # Classify and sort
    email_data['Urgency'], email_data['Sentiment'], email_data['Intent'] = zip(*email_data['Body'].apply(classify_email))
    urgency_order = {"High": 1, "Medium": 2, "Low": 3}
    email_data['Urgency Rank'] = email_data['Urgency'].map(urgency_order)
    email_data = email_data.sort_values('Urgency Rank')

    # Color formatting
    def highlight_urgency(val):
        color = {
            "High": "background-color: red; color: white",
            "Medium": "background-color: yellow; color: black",
            "Low": "background-color: green; color: white"
        }.get(val, "")
        return color

    st.subheader("📋 Prioritized Emails")
    st.dataframe(
        email_data[["Subject", "Body", "Urgency", "Sentiment", "Intent"]]
        .style.applymap(highlight_urgency, subset=["Urgency"])
    )

    st.download_button(
        label="📥 Download Prioritized Emails",
        data=email_data.to_csv(index=False),
        file_name="prioritized_emails.csv",
        mime="text/csv"
    )

    # ---- Roadmap Card ----
    with st.container():
        st.markdown("### 💼 Project: Client Servicing – Email Communication Enhancement")
        st.markdown("""
        <div style='
            background-color: #1e1e1e;
            border: 1px solid #444;
            padding: 20px;
            border-radius: 10px;
            margin-top: 10px;
        '>
            <h4 style='color: #fff;'>🚀 Future Enhancements with AI & RPA</h4>
            <ul style='color: #ddd;'>
                <li>🤖 Intent detection using AI (e.g. BERT)</li>
                <li>😊 Sentiment analysis to detect tone</li>
                <li>🧠 Auto-reply recommendations</li>
                <li>📝 Email summarization</li>
                <li>🔍 Entity extraction (names, dates, IDs)</li>
                <li>⚙️ RPA to triage based on urgency/sentiment (e.g., escalate negative emails)</li>
                <li>🤝 RPA to create tickets, assign to teams, or trigger workflows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
