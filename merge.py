
from PIL import Image 
import os
import shutil

train_path = 'train_cropped'
test_path = 'test_cropped'


train = os.listdir(train_path)



for i in train:
    img_train_path = os.path.join(train_path, i)
    img_test_path = os.path.join(test_path, i)
    img_train = Image.open(img_train_path)
    img_test = Image.open(img_test_path)
    img_01_size = img_train.size 
    img_02_size = img_test.size 
    new_im = Image.new('RGB', (2*img_01_size[0],1*img_01_size[1])) 
    new_im.paste(img_train, (0,0)) 
    new_im.paste(img_test, (img_01_size[0],0))
    new_im.save(f'train_merged/{i}')
