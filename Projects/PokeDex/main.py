from PIL import Image, ImageFilter

img = Image.open('./testImages/cake.jpg')

img.thumbnail((1024, 1024))

img.show()

print(img.size)