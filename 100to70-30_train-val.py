import os
import shutil
import random

source_images_dir = 'up+low/images'
source_labels_dir = 'up+low/labels'

train_images_dir = 'data/train/images'
train_labels_dir = 'data/train/labels'
val_images_dir = 'data/val/images'
val_labels_dir = 'data/val/labels'

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

all_images = [f for f in os.listdir(source_images_dir) if f.endswith('.png')]
all_labels = [f for f in os.listdir(source_labels_dir) if f.endswith('.txt')]

matched_files = [f[:-4] for f in all_images if f[:-4] + '.txt' in all_labels]

random.shuffle(matched_files)

split_index = int(len(matched_files) * 0.7)
train_files = matched_files[:split_index]
val_files = matched_files[split_index:]

def move_files(files, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
    for file in files:
        img_src = os.path.join(src_img_dir, file + '.png')
        lbl_src = os.path.join(src_lbl_dir, file + '.txt')
        
        shutil.move(img_src, os.path.join(dest_img_dir, file + '.png'))
        shutil.move(lbl_src, os.path.join(dest_lbl_dir, file + '.txt'))

move_files(train_files, source_images_dir, source_labels_dir, train_images_dir, train_labels_dir)
move_files(val_files, source_images_dir, source_labels_dir, val_images_dir, val_labels_dir)

print("Done")
