from PIL import Image, ImageChops, ImageFont, ImageDraw, ImageFilter

SOURCE_DIR = 'images/'

"""pict1 = Image.open(SOURCE_DIR + '1.jpeg')
ava = pict1.crop((0, 0, pict1.width, pict1.width)).resize((700, 700)).transpose(Image.FLIP_LEFT_RIGHT)
ava.save(SOURCE_DIR + 'ava.jpeg')
ava.show()"""

"""first = Image.open(SOURCE_DIR + '2.jpeg')
back = Image.open(SOURCE_DIR + '3.jpg')
r, g, b = first.split()"""
"""r.show()
g.show()
b.show()
"""
"""mask_temp = g.point(lambda x: (70 < x < 140) and 255)
mask = ImageChops.invert(mask_temp)
new_first = Image.composite(first, back, mask)
new_first.show()"""

ava = Image.open(SOURCE_DIR + 'ava.jpeg')
leo = Image.open(SOURCE_DIR + 'leo.jpg')
leo = leo.resize((300, 300))

"""result = ImageChops.add(ava, leo, scale=1.5, offset=5)
result.show()
result = ImageChops.darker(ava, leo)
result.show()
result = ImageChops.difference(ava, leo)
result.show()
result = ImageChops.lighter(ava, leo)
result.show()
result = ImageChops.multiply(ava, leo)
result.show()
result = ImageChops.soft_light(ava, leo)
result.show()
result = ImageChops.hard_light(ava, leo)
result.show()
result = ImageChops.overlay(ava, leo)
result.show()
result = ImageChops.screen(ava, leo)
result.show()"""
"""
result = ImageChops.subtract(ava, leo, 1.5, 5)
result.show()
result = result.convert("RGBA")
txt = Image.new("RGBA", result.size, (255, 255, 255, 0))
fnt = ImageFont.truetype(SOURCE_DIR + 'Mainstay.ttf', 10)
d = ImageDraw.Draw(txt)
for i in range(0, result.height + 90, 30):
    for j in range(0, result.height + 90, 30):
        d.text((i - 10, j - 10), 'I\'m programmer', font=fnt, fill=(200, 200, 200, 120))
txt = txt.rotate(10)
result = Image.alpha_composite(result, txt)
result.show()
"""

r, g, b = leo.split()
img1 = Image.merge('RGB', (r, g, b))
img2 = Image.merge('RGB', (r, g.filter(ImageFilter.GaussianBlur(25)), b))
leo.show()
img1.show()
img2.show()
