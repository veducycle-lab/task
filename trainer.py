from ultralytics import YOLO
import torch
################################################ 
import os                                         # DEBUG MY OS
os.environ['KMP_DUPLICATE_LIB_OK']='True'         # DEBUG MY OS
################################################

# DRIVERS CUDA ON WIN10 NOT WORKING
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# print(f'Using device: {device}')

# model = YOLO('yolov8x.pt').to(device)
# torch.cuda.set_device(0)


model = YOLO('yolov8x.pt')

model.train(data='data/set.yaml', epochs=5, imgsz=(200, 40), save_dir='saved', name='test')
