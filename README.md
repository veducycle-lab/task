Описание:

100to70-30_train-val.py - файл для нарезки датасета из source/images, source/labels  ------> dataset/train/(images, labels), dataset/val/(images, labels). Размерность датасета была поделена 70/30.

trainer.py - файл для обучения модели. Была выбрана 8x модель, как самая лучшая, для точного распознавания цифр. imgsz картинок не изменялся и был взять напрямую, размерность 200 на 40. Выбрано 5 эпох, так как мой комп не может работать с драйверами CUDA и пришлость ждать пока модель обучится на процессоре.

map_evaluator.py - файл в котором производилась оценка по метрике mAP. Делалось это очень просто, так как сам YOLO производит вычисление этой метрики, а нам остается лишь только забрать метрики и записать в файл в виде логов.

Папка data - внутри папки содержатся просто ради примера то как выглядел датасет в момент его обучения.
