import re
import joblib
import numpy as np
import streamlit as st


# Feature extraction logic (Same as training)
def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if "-" in url else 0)
    features.append(1 if "//" in url[7:] else 0)
    features.append(1 if url.startswith("https://") else 0)
    features.append(sum(c.isdigit() for c in url))

    ip_pattern = r"(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])"
    features.append(1 if re.search(ip_pattern, url) else 0)

    suspicious_words = [
        "login",
        "verify",
        "bank",
        "free",
        "update",
        "bonus",
        "account",
        "secure",
        "claim",
    ]
    features.append(
        1 if any(word in url.lower() for word in suspicious_words) else 0
    )

    return np.array(features).reshape(1, -1)


# UI Layout Settings
st.set_page_config(
    page_title="CyberShield AI - URL Scanner", page_icon="🛡️", layout="centered"
)

st.title("🛡️ CyberShield AI: Malicious & Phishing URL Detector")
st.markdown(
    "Analyze website URLs in real time using Machine Learning heuristic classification."
)
st.write("---")

# User Input Box
url_input = st.text_input(
    "🔗 Enter URL to inspect:",
    placeholder="https://example.com or suspicious link...",
)

col1, col2 = st.columns([1, 4])
with col1:
    scan_button = st.button("🚀 Analyze Link")

if scan_button:
    if not url_input.strip():
        st.warning("⚠️ Please provide a URL first.")
    else:
        try:
            # Model load aur prediction
            model = joblib.load("model.pkl")
            features = extract_features(url_input)
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0]

            st.write("### 🔍 Security Analysis Result")

            if prediction == 1:
                st.error("🚨 **Danger: Potential Phishing / Malicious URL!**")
                confidence = probability[1] * 100
                st.metric("Malicious Risk Score", f"{confidence:.2f}%")
                st.progress(int(confidence))
            else:
                st.success("✅ **Safe: Legitimate Website Signature Detected.**")
                confidence = probability[0] * 100
                st.metric("Legitimate Safety Score", f"{confidence:.2f}%")
                st.progress(int(confidence))

            # Technical Feature Inspection
            st.markdown("#### 🔬 Heuristic Indicator Breakdown")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("URL Length", len(url_input))
            c2.metric(
                "Protocol", "HTTPS" if url_input.startswith("https://") else "HTTP"
            )
            c3.metric(
                "IP Address Check",
                (
                    "Detected"
                    if re.search(
                        r"(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])",
                        url_input,
                    )
                    else "None"
                ),
            )
            c4.metric(
                "Suspicious Symbols",
                "Found" if ("@" in url_input or "-" in url_input) else "Clean",
            )

        except Exception as err:
            st.error(f"Error executing prediction: {err}")