import qrcode

# Your GitHub Pages URL (replace with your username!)
base_url = "https://yourusername.github.io/animal_science_qrcodes/page.html?id={}"

for i in range(1, 26):  # Pages 1–25
    url = base_url.format(i)
    img = qrcode.make(url)
    img.save(f"qr_page{i}.png")
    print(f"Generated QR code for {url}")
