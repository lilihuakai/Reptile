import tesserocr
from PIL import Image

# 简单
# result = tesserocr.file_to_text('code2.jpg')
# result = tesserocr.file_to_text('code.jpg')

# 识别效率好
image = Image.open('code2.jpg')
# image = Image.open('code.jpg')
image = image.convert('1')
# image = image.convert('L')
image.show()
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)
