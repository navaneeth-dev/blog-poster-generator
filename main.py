from PIL import Image, ImageOps, ImageDraw, ImageFont

text = "SvelteKit From\nA NextJS Perspective"

# Load the generated image
img = Image.open("street.jpg")

# Get the size of the final image
width, height = img.size

new_width = 1024
new_height = 576

left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2

# Add text caption to the image
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Poppins-Bold.ttf", 32)
blog_font = ImageFont.truetype("Poppins-Regular.ttf", 24)
_, _, w, h = draw.textbbox((0, 0), text, font=font)
draw.text(((left + 30), (height-h) / 2), text, font=font, fill=(255, 255, 255))

_, _, w, h = draw.textbbox((0, 0), text, font=font)
draw.text(((left + 30), bottom-h), "rizexor.com/blog",
          font=blog_font, fill=(255, 255, 255))

img = img.crop((left, top, right, bottom))
img.show()
# img.save("final_image.jpg")
