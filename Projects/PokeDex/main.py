from PIL import Image

img = Image.open('./testImages/pikachu.jpg')

for i in dir(img):
    print(i)
#print(dir(img))

print()