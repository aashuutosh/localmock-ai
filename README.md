# 🧬 LocalMock AI — Privacy-Safe Mock Data Generator

> **Built at Hacktoberfest Hack Day Bhopal x BuilderBase | MLH**  
> *Best Open-Source AI Project Challenge*

---

## 🔥 The Problem

Every developer needs **fake/mock data** to test their applications — fake user profiles, fake medical records, fake financial transactions.

But today, developers do one of two things:

- ❌ **Use ChatGPT or cloud AI** — which means sending your **private database schema** to a third-party server. This violates NDAs and company data policies.
- ❌ **Write fake data by hand** — which is slow, tedious, and inconsistent.

**Both options are broken.**

---

## ✅ The Solution

**LocalMock AI** generates realistic, structured mock data (JSON, CSV, SQL) using an **open-weight AI model that runs 100% on your local machine.**

Your schema never leaves your laptop. Ever.

---

## 🎯 How It Works

```
Developer describes their dataset
        ↓
LocalMock AI sends it to TinyLlama (running locally via Ollama)
        ↓
Open-weight model generates realistic fake data
        ↓
Output is shown as JSON / CSV / SQL — ready to download
        ↓
Zero bytes sent to any cloud server ✅
```

---

## 🚀 Demo

| Input | Output |
|---|---|
| *"5 fake hospital patients with name, age, diagnosis, insurance_balance"* | Clean JSON with realistic names, ages, diagnoses |
| *"10 fake bank transactions with sender, receiver, amount, timestamp"* | CSV ready to import into any database |
| *"Create a users table with 3 rows"* | Valid SQL INSERT statements |

---

## 🛡️ Why Open-Weight AI?

| Feature | Cloud AI (ChatGPT) | LocalMock AI |
|---|---|---|
| Schema Privacy | ❌ Sent to cloud | ✅ Stays on device |
| Works Offline | ❌ No | ✅ Yes |
| API Cost | ❌ Paid per request | ✅ Free forever |
| Data Compliance | ❌ Risk | ✅ Safe |

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| **UI** | Streamlit (Python) |
| **AI Engine** | Ollama (Local API Server) |
| **Model** | TinyLlama (Open-weight, Apache 2.0 License) |
| **Output** | JSON / CSV / SQL |
| **License** | MIT |

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed

### Step 1 — Pull the model
```bash
ollama run tinyllama
```

### Step 2 — Install dependencies
```bash
pip install streamlit openai
```

### Step 3 — Run the app
```bash
python -m streamlit run app.py
```

### Step 4 — Open your browser
```
http://localhost:8501
```

---

## 💡 Use Cases

- 🏥 **Healthcare apps** — Generate fake patient records for testing without touching real PHI data
- 🏦 **Fintech apps** — Generate fake transactions without exposing real financial schemas
- 🛒 **E-commerce** — Generate fake product catalogs and orders for load testing
- 🎓 **Students & Educators** — Generate realistic datasets for learning without needing real data

---

## 📁 Project Structure

```
localmock-ai/
├── app.py          # Main Streamlit application
├── README.md       # This file
└── LICENSE         # MIT License
```

---

## 🏆 Hackathon Submission

- **Event:** Hacktoberfest Hack Day Bhopal x BuilderBase
- **Challenge:** Best Open-Source AI Project
- **Model Used:** TinyLlama (open-weight, runs via Ollama)
- **License:** MIT

---

## 👤 Author

Built with ❤️ at Hacktoberfest Hack Day 2026

---

*"The best privacy tool is one that never sends your data anywhere in the first place."*
