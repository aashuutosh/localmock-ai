import streamlit as st
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="hackathon")
st.set_page_config(page_title="LocalMock AI", page_icon="🧬", layout="wide")
st.title("🧬 LocalMock AI — Privacy-Safe Mock Data Generator")
st.write("Generate realistic test data (JSON/CSV/SQL) 100% offline. Your schema never leaves your laptop.")
st.markdown("---")
data_request = st.text_area("Describe your dataset:", value="Generate 5 fake hospital patients with id, name, age, diagnosis, and insurance_balance.", height=150)
output_format = st.selectbox("Output Format:", ["JSON", "CSV", "SQL INSERT Statements"])
if st.button("🪄 Generate Locally"):
    if data_request:
        with st.spinner("Generating on your local machine..."):
            try:
                response = client.chat.completions.create(
                    model="tinyllama",
                    messages=[
                        {"role": "system", "content": f"You are a data synthesis engine. Output ONLY valid {output_format}. No explanations. Raw data only."},
                        {"role": "user", "content": data_request}
                    ]
                )
                result = response.choices[0].message.content
                st.success("✅ Done! Generated locally — zero data sent to cloud.")
                st.code(result, language="json")
                st.download_button("💾 Download File", data=result, file_name="mock_data.txt")
            except Exception as e:
                st.error(f"Is Ollama running? Error: {e}")