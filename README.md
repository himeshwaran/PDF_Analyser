# 🧠PDF Analyzer

A lightweight malware analysis and document scanning web app built using **Flask**.  
The project helps identify **suspicious indicators, embedded scripts, and metadata anomalies** within document files such as **PDFs and DOCX**.

---

## 🔍 Purpose
This project was developed to explore **document-based threat detection** and **digital forensics** concepts.  
It demonstrates how files can be analyzed to detect malicious patterns, hidden payloads, and suspicious metadata in a simplified and educational way.

---

## ⚙️ Features
- 🧩 **PDF and Document Analysis** — Scans uploaded files for malicious indicators  
- 🧮 **Score Meter** — Displays a risk percentage (Safe / Suspicious / Malicious)  
- 🕵️ **Threat Hunting View** — Shows suspicious keywords and structural details   
- 💾 **Flask-Powered Web Interface** — Simple and fast upload/scan workflow  

---

## 🧰 Tech Stack
- **Backend:** Flask (Python)  
- **Frontend:** HTML, Bootstrap 5  
- **Tools:** PDFiD, PyPDF2  
- **Hosting:** (Local / any cloud platform supporting Linux-based environments)

---

## ⚡ Installation

bash
git clone https://github.com/<your-username>/PDF_Analyzer.git
cd PDF_Analyzer
pip install -r requirements.txt
python app.py


Then open your browser and visit:
\`\`\`
http://127.0.0.1:5000/
\`\`\`

---

## 🧑‍💻 Developer
**Himeshwaran E**  
Cybersecurity Enthusiast | Threat Hunter | Malware Analyst | Digital Forensics Learner  
📫 [LinkedIn]https://www.linkedin.com/in/himeshwaran-e-7ba18a281/

---

## 🧩 Future Enhancements
- Integration with **VirusTotal API** for comparison  
- Automatic **IOC extraction**  
- Add **AI-based document classification**  
- Multi-file scanning support
