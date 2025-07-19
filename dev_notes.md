# CyberAI_IDS – Project Document (v1.0)

**Developer:** Kirtan Kumar Kori  
**Branch:** CSE (AI-ML), SOIT – RGPV  
**Status:** In Development  
**Disclaimer:** For educational and Testing use only.  

---

## 🔒 Project Summary

**CyberAI_IDS** is an AI-based Intrusion Detection System (IDS) that uses machine learning to classify network traffic as either:

- ✅ Normal  
- 🚨 Malicious (Attack)

The goal is to detect threats in structured `.csv` log files based on the NSL-KDD dataset.

---

## ⚠️ Targeted Attacks (Based on NSL-KDD)

### 1. **DoS – Denial of Service**
- Goal: Overwhelm system with traffic  
- Examples: `neptune`, `smurf`, `back`

### 2. **Probe Attacks**
- Goal: Scan for vulnerabilities  
- Examples: `nmap`, `portsweep`, `ipsweep`

### 3. **U2R – User to Root**
- Goal: Gain admin privileges from user access  
- Examples: `buffer_overflow`, `perl`, `loadmodule`

### 4. **R2L – Remote to Local**
- Goal: Unauthorized login from remote machine  
- Examples: `guess_passwd`, `ftp_write`, `imap`

---

## 🛠️ Tools & Technologies

| Tool        | Purpose                             |
|-------------|-------------------------------------|
| Python      | Core programming language           |
| Pandas      | Data preprocessing                  |
| Scikit-learn| ML modeling                         |
| Matplotlib  | Visual analysis                     |
| Google Colab| Cloud-based training                |
| GitHub      | Code versioning                     |
| Streamlit   | (Optional) GUI for predictions      |
| Jupyter     | Local development notebooks         |

---

## 🧠 How It Works (Simple Flow)

1. Load dataset (e.g. `KDDTrain+.csv`)  
2. Preprocess: clean, encode, normalize  
3. Train ML models (e.g., RandomForest, DecisionTree)  
4. Test on validation set  
5. Save model as `.pkl` file  
6. Predict on new logs  
7. Classify as "normal" or specific "attack"

---

## 🧪 Installation & Use

**During Development:**
- Run on Google Colab
- Experiment with data and models

**For Deployment (Prototype Phase):**
- Can be run on system admin's PC
- Accepts `.csv` logs as input
- Displays prediction: Normal / DoS / R2L etc.

**Future Possibilities:**
- Real-time intrusion detection via packet sniffing
- Integration into cloud servers
- API-based log analysis

---

## 🎯 Project Goals

- ✅ >90% model accuracy  
- ✅ Detect all 4 major attack types  
- ✅ GUI via Streamlit *(optional)*  
- ✅ Publish on GitHub with README  
- ✅ Keep system light and offline usable

