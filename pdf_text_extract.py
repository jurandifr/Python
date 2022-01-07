# Tutorial
# https://realpython.com/creating-modifying-pdf/#extracting-text-from-a-pdf

from PyPDF4 import PdfFileReader
import re

pdf = PdfFileReader("ddexemplo2.pdf")
test_str=pdf.getPage(0).extractText().replace("\n", "").replace("  ", " ").strip()
print(f"Número de páginas: {pdf.getNumPages()}")

def getInfo(regex, test_str):
    matches = re.finditer(regex, test_str, re.IGNORECASE | re.DOTALL)
    return [match.group(matchNum).strip() for matchNum, match in enumerate(matches, start=1)]
  
regex = r"(?:.*Razão social:\W*)(.*)(?:\W*1\.2.*)"
getInfo(regex, test_str)[0]
