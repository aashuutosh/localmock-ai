import streamlit as st
import json
import re
from openai import OpenAI

# Connect to local Ollama engine
client = OpenAI(base_url="http://localhost:11434/v1", api_key="hackathon")

st.set_page_config(page_title="LocalMock AI", page_icon="🧬", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    model = st.selectbox("🤖 Local Model", ["tinyllama", "phi4", "llama3.2", "mistral"])
    st.markdown("---")
    st.success("🔒 100% Local Processing")
    st.info("No internet required.\nZero data leaves your machine.")
    st.markdown("---")
    st.markdown("### 📋 Example Prompts")
    examples = [
        "5 fake hospital patients with id, name, age, diagnosis, insurance_balance",
        "10 fake bank transactions with sender, receiver, amount, date",
        "3 fake e-commerce orders with product, quantity, price, customer_name",
        "5 fake students with roll_no, name, subject, marks, grade",
        "4 fake employees with emp_id, name, department, salary, joining_date"
    ]
    for ex in examples:
        if st.button(f"📌 {ex[:40]}...", key=ex):
            st.session_state["prompt"] = ex

# --- MAIN UI ---
st.title("🧬 LocalMock AI")
st.subheader("Privacy-Safe Mock Data Generator")
st.write("Generate realistic test data **(JSON / CSV / SQL)** 100% offline using open-weight AI. Your schema **never** leaves your laptop.")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    default_prompt = st.session_state.get("prompt", "Generate 5 fake hospital patients with id, name, age, diagnosis, and insurance_balance.")
    data_request = st.text_area(
        "📝 Describe your dataset:",
        value=default_prompt,
        height=150
    )

with col2:
    output_format = st.selectbox("📦 Output Format:", ["JSON", "CSV", "SQL INSERT Statements"])
    num_rows = st.slider("Number of rows", min_value=3, max_value=20, value=5)

# --- GENERATE BUTTON ---
if st.button("🪄 Generate Data Locally", use_container_width=True):
    if data_request:
        with st.spinner(f"Generating {output_format} locally using {model}..."):
            try:
                if output_format == "JSON":
                    format_instruction = "Output ONLY a valid JSON array. No markdown, no code blocks, no explanation. Start directly with [ and end with ]."
                elif output_format == "CSV":
                    format_instruction = "Output ONLY valid CSV with a header row. No markdown. Just raw CSV text."
                else:
                    format_instruction = "Output ONLY valid SQL INSERT statements. No markdown. Just the SQL."

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": f"You are a data synthesis engine. {format_instruction} Generate exactly {num_rows} rows of realistic fake data."},
                        {"role": "user", "content": data_request}
                    ],
                    temperature=0.7
                )

                raw_result = response.choices[0].message.content
                cleaned = raw_result.strip()
                # Auto-remove markdown code blocks
                cleaned = re.sub(r"```[\w]*\n?", "", cleaned)
                cleaned = cleaned.replace("```", "").strip()
                st.session_state["result"] = cleaned
                st.session_state["format"] = output_format

            except Exception as e:
                st.error(f"❌ Is Ollama running? Error: {e}")
    else:
        st.warning("Please describe your dataset first.")

# --- SHOW RESULTS ---
if "result" in st.session_state and st.session_state["result"]:
    st.markdown("---")
    st.success("✅ Data Generated Locally — Zero bytes sent to cloud!")
    result = st.session_state["result"]
    fmt = st.session_state["format"]

    # Pretty-print JSON
    if fmt == "JSON":
        try:
            result = json.dumps(json.loads(result), indent=2)
            st.session_state["result"] = result
        except:
            st.warning("⚠️ Minor formatting issue in output. Showing raw result.")

    lang_map = {"JSON": "json", "CSV": "csv", "SQL INSERT Statements": "sql"}
    st.code(result, language=lang_map.get(fmt, "text"))

    ext_map = {"JSON": "json", "CSV": "csv", "SQL INSERT Statements": "sql"}
    st.download_button(
        label=f"💾 Download {fmt} File",
        data=result,
        file_name=f"mock_data.{ext_map.get(fmt, 'txt')}",
        mime="text/plain",
        use_container_width=True
    )

    # Table preview for JSON
    if fmt == "JSON":
        try:
            import pandas as pd
            parsed = json.loads(result)
            if isinstance(parsed, list):
                st.markdown("### 📊 Preview as Table")
                st.dataframe(pd.DataFrame(parsed), use_container_width=True)
        except:
            pass

st.markdown("---")
st.caption("🧬 LocalMock AI | Built with Streamlit + Ollama + TinyLlama | MIT License | Hacktoberfest 2026")
