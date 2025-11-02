from flask import Flask, render_template, request
import subprocess
import os
import re

app = Flask(__name__, template_folder='.')

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store scan results
scan_results = []  # [{filename: str, score: int}]


@app.route("/")
def home():
    # Show all previous results (latest first)
    return render_template('index.html', results=reversed(scan_results))
    
@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/scan", methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template("index.html", error="No file selected", results=reversed(scan_results))
    
    file = request.files['file']
    if not file.filename.endswith('.pdf'):
        return render_template("index.html", error="Only PDF files allowed", results=reversed(scan_results))

    # Save the uploaded file
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)
    print(f"File saved: {save_path}")

    # Run pdfid command
    result = subprocess.run(["pdfid", save_path], capture_output=True, text=True)
    output = result.stdout
    print(output)
    
    # Compute a simple risk score
    score = 0
    for i in output.splitlines():
        if re.search(r'\bobj\b', i):
            parts = i.split()
            if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) > 0:
                score += 0
        if re.search(r'\bJavaScript\b', i):   
            parts = i.split()
            if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) > 0:
                score += 60
        if re.search(r'\bEmbeddedFile\b', i):   
            parts = i.split()
            if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) > 0:
                score += 25
        if re.search(r'\bLaunch\b', i):   
            parts = i.split()
            if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) > 0:
                score += 25
        if re.search(r'\bOpenAction\b', i):   
            parts = i.split()
            if len(parts) > 1 and parts[1].isdigit() and int(parts[1]) > 0:
                score += 50

    # Cap score at 100
    if score > 100:
        score = 100

    # Save result
    scan_results.append({
        "filename": file.filename,
        "score": score
    })

    return render_template("index.html", 
                           file_name=file.filename, 
                           score=score,
                           results=reversed(scan_results))


if __name__ == '__main__':
    app.run(debug=True)
