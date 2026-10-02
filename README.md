# 🧬 LocalMock AI — Privacy-Safe Mock Data Generator

> Built at Hacktoberfest Hack Day Bhopal x BuilderBase | Major League Hacking
> Best Open-Source AI Project Challenge

---

## 🔥 The Problem

Every developer needs fake/mock data to test their applications.

But using ChatGPT means uploading your private database schema to a cloud server — violating NDAs and data privacy policies.

**LocalMock AI fixes this.**

---

## ✅ The Solution

Describe your dataset in plain English → Get realistic JSON, CSV, or SQL data generated 100% offline using an open-weight AI model running on YOUR machine.

🔒 Your schema never leaves your laptop. Ever.

---

## 🚀 Features

- 🧬 Natural language input — describe data in plain English
- 📦 3 output formats — JSON, CSV, SQL INSERT Statements
- 🎛️ Row count slider — generate 3 to 20 rows
- 📊 Live table preview — see JSON as a formatted table instantly
- 💾 One-click download — correct file extension automatically
- 📋 Example prompts — Hospital, Finance, E-commerce, Student, Employee
- 🔒 100% offline — no internet required after model download
- ⚡ Auto-clean output — strips markdown, validates and pretty-prints JSON

---

## 🛡️ Cloud AI vs LocalMock AI

| Feature | ChatGPT / Cloud AI | LocalMock AI |
|---|---|---|
| Schema Privacy | ❌ Sent to cloud | ✅ Stays on device |
| Works Offline | ❌ No | ✅ Yes |
| API Cost | ❌ Paid per request | ✅ Free forever |
| Data Compliance | ❌ NDA Risk | ✅ Safe |
| Rate Limits | ❌ Limited | ✅ Unlimited |

---

## 💡 Real-World Use Cases

| Industry | Use Case |
|---|---|
| 🏥 Healthcare | Fake patient records without touching real PHI data |
| 🏦 Fintech | Fake transactions without exposing financial schemas |
| 🛒 E-commerce | Fake product catalogs for load testing |
| 🎓 Education | Realistic datasets for students to practice SQL |
| 🏢 Enterprise | Test internal tools without violating NDA |

---

## 🧱 Tech Stack

| Layer | Technology | License |
|---|---|---|
| UI | Streamlit (Python) | Apache 2.0 |
| AI Engine | Ollama (Local API) | MIT |
| Model | TinyLlama 1.1B | Apache 2.0 |
| Project License | MIT | ✅ Open Source |

---

## ⚙️ How to Run

### 1 — Pull the open-weight model
ollama run tinyllama

### 2 — Install dependencies
pip install streamlit openai pandas

### 3 — Run the app
python -m streamlit run app.py

### 4 — Open browser
http://localhost:8501

---

## 🔮 Future Roadmap

- [ ] XML, YAML, Excel output formats
- [ ] Upload your existing table schema file
- [ ] Relationship-aware data with foreign keys
- [ ] Docker one-command setup

---

## 🏆 Hackathon

| Field | Value |
|---|---|
| Event | Hacktoberfest Hack Day Bhopal x BuilderBase |
| Organizer | Major League Hacking (MLH) |
| Challenge | Best Open-Source AI Project |
| Model | TinyLlama (Apache 2.0) |
| License | MIT ✅ |

---

"The best privacy tool is one that never sends your data anywhere in the first place."
