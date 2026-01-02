import os
from barcode import Code128
from barcode.writer import ImageWriter
from products import products

OUTPUT_DIR = "barcodes/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_barcode(product):
    filename = f"{product['name'].replace(' ', '_')}_{product['weight']}_{product['price']}shs"

    writer_options = {
    "module_width": 0.6,     # Keep bars wide for easy scanning
    "module_height": 20.0,   # Reduced height to fit labels better
    "quiet_zone": 8.0,       # Keep good white space
    "font_size": 11,         # Slightly smaller text
    "text_distance": 5.0,
    "dpi": 300,
    "write_text": True
    }


    barcode = Code128(
        product["code"],
        writer=ImageWriter()
    )

    barcode.save(
        os.path.join(OUTPUT_DIR, filename),
        options=writer_options
    )

    print(f"✔ Generated barcode for {product['name']}")

def main():
    print("Generating Pearl Spices barcodes...\n")

    for product in products:
        generate_barcode(product)

    print("\n✅ All barcodes generated successfully!")

if __name__ == "__main__":
    main()
