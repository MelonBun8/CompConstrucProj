from pypdf import PdfReader

reader = PdfReader("CompilerProject.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)
