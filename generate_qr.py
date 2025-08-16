import qrcode
import os

# Make sure folder exists
os.makedirs("qrcodes", exist_ok=True)

base_url = "https://zacharybloedow.github.io/animal_science_qrcodes/page.html?id={}"

for i in range(1, 26):  # Pages 1–25
    url = base_url.format(i)
    img = qrcode.make(url)
    img.save(f"qrcodes/qr_page{i}.png")
    print(f"Generated QR code for {url}")
