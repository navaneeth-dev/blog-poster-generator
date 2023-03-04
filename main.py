from PIL import Image, ImageOps, ImageDraw, ImageFont

text = "SRM Vadapalani CTF"

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
font = ImageFont.truetype("Poppins-Bold.ttf", 36)
blog_font = ImageFont.truetype("Poppins-Regular.ttf", 24)
_, _, w, h = draw.textbbox((0, 0), text, font=font)
shadowcolor = (0, 0, 0)
draw.text((((width-w)/2)-1, ((height-h) / 2) - 1),
          text, font=font, fill=shadowcolor)
draw.text((((width-w)/2)+1, ((height-h) / 2) - 1),
          text, font=font, fill=shadowcolor)
draw.text((((width-w)/2)-1, ((height-h) / 2) + 1),
          text, font=font, fill=shadowcolor)
draw.text((((width-w)/2)+1, ((height-h) / 2) + 1),
          text, font=font, fill=shadowcolor)

draw.text(((width-w)/2, (height-h) / 2), text, font=font, fill=(255, 255, 255))

blog_text = "rizexor.com/blog"

_, _, w, h = draw.textbbox((0, 0), blog_text, font=blog_font)

draw.text((((width-w) / 2) - 1, ((bottom-h) - 20) - 1),
          blog_text, font=blog_font, fill=shadowcolor)
draw.text((((width-w) / 2) + 1, ((bottom-h) - 20) - 1),
          blog_text, font=blog_font, fill=(0, 0, 0))
draw.text((((width-w) / 2) - 1, ((bottom-h) - 20) + 1),
          blog_text, font=blog_font, fill=(0, 0, 0))
draw.text((((width-w) / 2) + 1, ((bottom-h) - 20) + 1),
          blog_text, font=blog_font, fill=(0, 0, 0))

# final text
draw.text(((width-w) / 2, (bottom-h) - 20), blog_text,
          font=blog_font, fill=(255, 255, 255))

img = img.crop((left, top, right, bottom))
# img.show()
img.save("final_image.jpg")
