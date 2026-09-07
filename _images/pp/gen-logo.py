from PIL import Image, ImageDraw, ImageFont

path = "/home/ilias/Desktop/DSK/Teaching/Courses/OS/2026-2027/website/it-intro-to-os/_images/pp/ilias-logo.png"

img = Image.new("RGB", (200, 200), (46, 64, 87))
draw = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
except:
    font = ImageFont.load_default()
bbox = draw.textbbox((0, 0), "IT", font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
x, y = (200 - tw) // 2, (200 - th) // 2 - 10
draw.text((x, y), "IT", fill="white", font=font)
img.save(path)
print("Done - replaced ilias-logo.png with IT placeholder")