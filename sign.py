import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF is not installed. Run:  pip install pymupdf")

# --- Config ---
INPUT_PDF   = "Beschwerde-Netto-Detmolder.pdf"
SIGNATURE   = "Unterschrift.png"
OUTPUT_PDF  = "Beschwerde-Netto-Detmolder-sign.pdf"

SIGNATURE_WIDTH  = 90
SIGNATURE_HEIGHT = 80
MARGIN_LEFT      = 40  # points from left edge
MARGIN_BOTTOM    = 170 # points from bottom edge
# --------------

doc = fitz.open(INPUT_PDF)
sig_bytes = Path(SIGNATURE).read_bytes()

page = doc[-1]  # last page
page_height = page.rect.height

x = MARGIN_LEFT
y = page_height - MARGIN_BOTTOM - SIGNATURE_HEIGHT

rect = fitz.Rect(x, y, x + SIGNATURE_WIDTH, y + SIGNATURE_HEIGHT)
page.insert_image(rect, stream=sig_bytes, keep_proportion=True, overlay=True)

doc.save(OUTPUT_PDF, deflate=True)
doc.close()
print(f"✓ Signed PDF saved as: {OUTPUT_PDF}")
