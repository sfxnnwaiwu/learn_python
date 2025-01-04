import qrcode
import random

def create_qr_code(web_url: str, file_name: str) -> None:
    qr = qrcode.QRCode(box_size = 10, border = 5)
    # qr_code = qrcode.make(url)
    qr.add_data(web_url)
    # qr_code.save(file_name)
    # qr.make(fit=True)
    qr.make_image(fill_color = "black", back_color = "white").save(file_name)
    print(f"QR code saved as {file_name}")


web_url: str = input("Enter the URL you want to create a QR code for: ").strip()
file_name: str = input("Enter the file name for the QR code: ").strip()

create_qr_code(web_url, file_name)

# random_number = random.randint(1, 100)
# print(f"Random number: {random_number}")