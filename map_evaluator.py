from ultralytics import YOLO
import datetime

model = YOLO('best.pt')

results = model.val(data='data/set.yaml', imgsz=(200, 40))

metrics = results.results_dict

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('evaluation_log.txt', 'a') as log_file:
    log_file.write(f"Дата лога: {current_time}\n")
    log_file.write(f"mAP_0.5: {metrics['metrics/mAP50(B)']:.4f}\n")
    log_file.write(f"mAP_0.5:0.95: {metrics['metrics/mAP50-95(B)']:.4f}\n")
    log_file.write("\n")

print("logged_done")
