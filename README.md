# 🛡️ AI-Powered Phishing & Malicious URL Detection System

An end-to-end Machine Learning web application designed to detect and flag fraudulent, deceptive, and malicious website URLs in real time. Built using Python, Scikit-learn, and Streamlit, the system extracts structural heuristic markers from URLs to deliver high-accuracy classification.

---

## 📌 Project Overview
Phishing attacks are one of the most common cybersecurity threats, where fraudulent domains mimic legitimate websites to steal credentials and sensitive data. Traditional security engines rely heavily on static blacklists, which fail against newly registered domains (zero-day phishing).

This project solves that limitation by utilizing **Heuristic Feature Engineering** combined with a **Machine Learning Classifier** (Random Forest). Rather than searching a static database, the AI model inspects the structural patterns, lexical signatures, and redirection behaviors of any given URL.

---

## 🚀 Live Demo & Repository
- **Deployed Web App:** [Live Streamlit App](https://ai-phishing-url-detector-kjvuta5nzi32nfbyaxuguo.streamlit.app)
- **Source Code:** [GitHub Repository](https://github.com/abhinavtiwari002/ai-phishing-url-detector)

---

## 🧠 Key Extracted Features (Heuristic Analysis)
The system analyzes 8 distinct technical markers from each URL:
1. **URL Length:** Malicious URLs often contain extensive query parameters to conceal true targets.
2. **'@' Symbol Presence:** Browsers ignore all characters preceding the `@` symbol, a common phishing spoofing trick.
3. **Hyphen ('-') Check:** Fraudulent links commonly use dashes to imitate established brands (e.g., `secure-login-portal.com`).
4. **Redirection '//' Check:** Detecting multiple double slashes appearing after the protocol string indicating redirection loops.
5. **Security Protocol (HTTPS):** Validating whether the transport protocol enforces TLS/SSL encryption.
6. **Digit Count:** Excessive numeric characters typically correlate with auto-generated domain hashes.
7. **IP Address Detection:** Identifying direct IP addresses (IPv4) used in place of standard Domain Name System (DNS) hostnames.
8. **Suspicious Keyword Matching:** Scanning for targeted bait triggers (e.g., `verify`, `login`, `secure`, `bank`, `bonus`, `update`).

---

## ⚙️ Technology Stack
- **Language:** Python
- **Machine Learning:** Scikit-learn (Random Forest Classifier)
- **Data Engineering:** NumPy, Pandas, Regular Expressions (`re`)
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib
- **Deployment Platform:** Streamlit Community Cloud & GitHub

---

## 🏗️ System Architecture & Workflow
