from flask import Flask, request, jsonify
import PyPDF2

app = Flask(__name__)

def read_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except:
        return ""

@app.route('/chat', methods=['POST'])
def chat():
    pdf_file = request.files['pdf']
    question = request.form['question']
    pdf_text = read_pdf(pdf_file)
    
    # Minimal response: just search for keywords
    answer = "Sorry, I don't have an answer."
    if question.lower() in pdf_text.lower():
        answer = f"I found your query in the PDF: '{question}'"
    
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)