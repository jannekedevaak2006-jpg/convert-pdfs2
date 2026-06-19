from pathlib import Path
import fitz

input_dir = Path("input_pdfs")
output_dir = Path("output_text")

output_dir.mkdir(exist_ok=True)

for pdf_file in input_dir.glob("*.pdf"):
    doc = fitz.open(pdf_file)
    
    text = ""
    for page in doc:
        text += page.get_text()

    # cleaning
    text = "\n".join(line.strip() for line in text.split("\n") if line.strip())

    output_file = output_dir / (pdf_file.stem + ".txt")
    output_file.write_text(text, encoding="utf-8")

    print(f"Converted: {pdf_file} → {output_file}")
