import os
import shutil
from PIL import Image

train_path = 'train_resize'
test_path = 'test'

train = os.listdir(train_path)

# print(train)

# for i in train:
#     img_train_path = os.path.join(train_path, i)
#     img_test_path = os.path.join(test_path, i[:-4])
#     img_train = Image.open(img_train_path)
#     img_test = Image.open(img_test_path)
#     width, height = img_train.size
#     img_train = img_train.crop((width-512,150,width, 512+150))
#     img_test = img_test.crop((width-512,150,width, 512+150))
#     print(img_train.size, img_test.size)
#     i = i[:-4]
#     img_train.save(f'train_cropped/{i}')
#     img_test.save(f'test_cropped/{i}')


# image_path = r'train_resize\0.png.png'

# img = Image.open(image_path)
# size = img.size
# width, height = img.size
# new_image = img.crop((width-512,150,width, 512+150))
# print(new_image.size)
# new_image.show()
# new_image.save('test_0.png')

# print(img.size)

# new_image = img.resize((1920, 1088))

# new_image.save('5_test.png')

# print(new_image.size)


# 111

img_test = Image.open('test_test.jpeg')
new_image = img_test.resize((512, 512))
new_image.save('test_r_2.png')
print(new_image.size)