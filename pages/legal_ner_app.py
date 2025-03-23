import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import pandas as pd
import re

st.set_page_config(page_title="Legal Contract Review AI", layout="centered")

# ---------- Load NER ----------
@st.cache_resource
def load_ner_pipeline():
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    return pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

ner_pipeline = load_ner_pipeline()

# ---------- Clause Patterns ----------
clause_patterns = {
    "Governing Law": r"(governing law.*?\.|this agreement.*?governed by.*?)",
    "Confidentiality": r"(confidentiality.*?\.|non-disclosure.*?\.|nda.*?)",
    "Termination": r"(termination.*?\.|this agreement may be terminated.*?)",
    "Payment Terms": r"(payment.*?terms.*?\.|fees.*?due.*?)",
    "Indemnity": r"(indemnif(y|ication).*?\.|liability.*?hold harmless.*?)",
}

# ---------- UI ----------
st.title("📑 Legal Contract Review – NER + Compliance")
st.markdown("""
This prototype uses a **pretrained BERT-based Named Entity Recognition (NER) model** from Hugging Face:  
🔗 `dslim/bert-base-NER`

It extracts key legal entities from a contract and combines it with rule-based clause detection and compliance checks.
This helps simulate how AI can assist legal teams in reviewing contracts and identifying missing or risky clauses.
""")


contract_text = st.text_area("📄 Paste your contract text:", """
This Agreement is made on March 23, 2025, between ABC Corporation and XYZ Consulting Services.
The governing law shall be the laws of the State of California. All services will be delivered in Q2 2025.
In the event of early termination, parties must give a 30-day notice.
""", height=300)

if st.button("🔍 Analyze Contract"):
    # ---------- NER ----------
    ents = ner_pipeline(contract_text)
    st.markdown("### 📌 Named Entities Found:")
    for ent in ents:
        st.markdown(f"**{ent['entity_group']}**: `{ent['word']}` (score: {ent['score']:.2f})")

    # ---------- Clause Detection ----------
    st.markdown("### 📚 Clause Detection & Risk Flags")
    clause_results = []
    found_count = 0

    for clause, pattern in clause_patterns.items():
        match = re.search(pattern, contract_text, re.IGNORECASE | re.DOTALL)
        if match:
            clause_results.append({"Clause": clause, "Found": "✅ Yes", "Excerpt": match.group(0).strip()})
            found_count += 1
        else:
            clause_results.append({"Clause": clause, "Found": "❌ No", "Excerpt": "⚠️ Missing – Potential risk"})

    clause_df = pd.DataFrame(clause_results)
    st.dataframe(clause_df, use_container_width=True)

    # ---------- Compliance Checklist ----------
    checklist = {
        "Governing Law Present": "governing law" in contract_text.lower(),
        "Organization Detected": any(ent['entity_group'] == "ORG" for ent in ents),
        "Person Detected": any(ent['entity_group'] == "PER" for ent in ents),
        "Location Detected": any(ent['entity_group'] == "LOC" for ent in ents),
        "Date Mentioned": any(ent['entity_group'] == "DATE" for ent in ents),
    }
    checklist_df = pd.DataFrame([
        {"Item": item, "Status": "✅ Passed" if passed else "❌ Missing"}
        for item, passed in checklist.items()
    ])
    st.markdown("### ✅ Compliance Checklist")
    st.dataframe(checklist_df, use_container_width=True)

    # ---------- Compliance Score Summary ----------
    total_passed = found_count + sum(checklist.values())
    total_items = len(clause_patterns) + len(checklist)
    score = round((total_passed / total_items) * 100)

    st.markdown(f"### 📊 Compliance Score: **{score}%**")
    if score >= 80:
        st.success("This contract appears ready for legal approval ✅")
    elif score >= 50:
        st.warning("Some risks found – needs legal review ⚠️")
    else:
        st.error("High risk – major clauses or info missing ❌")

    # ---------- Highlighted Contract Text ----------
    highlighted = contract_text
    offset = 0
    for ent in sorted(ents, key=lambda x: x['start']):
        start, end = ent['start'] + offset, ent['end'] + offset
        word = contract_text[ent['start']:ent['end']]
        label = ent['entity_group']
        tag = f"<span style='background-color: #ffff33; color: black; padding: 2px 4px; border-radius: 4px;' title='{label}'>{word}</span>"
        highlighted = highlighted[:start] + tag + highlighted[end:]
        offset += len(tag) - len(word)

    st.markdown("### 🖍️ Highlighted Entities in Contract:")
    st.markdown(highlighted, unsafe_allow_html=True)

    # ---------- Export & RPA Simulations ----------
    st.markdown("### ⚙️ RPA Actions (Prototype Only)")
    st.markdown("_These buttons simulate automated actions. They do not perform any real tasks — for POC/demo purposes only._")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.download_button("📤 Export Clause Summary", clause_df.to_csv(index=False), file_name="clauses.csv")

    with col2:
        if st.button("📨 Send for Legal Review (Mock)"):
            st.info("🔔 This button is a prototype and does not perform a real action.")

    with col3:
        if st.button("🗂️ Auto-File in Compliance Drive (Mock)"):
            st.info("📁 Prototype action — no file movement is triggered.")
