from ultralytics import YOLO # type: ignore


def replace_backslashes(string):
    return string.replace('\\', '/')


model_path = r"D:\Programação\CV\football_analysis\training\runs\detect\2.lfdb1e201280\weights\best.pt"
model_path_good = replace_backslashes(model_path)

model = YOLO(model_path_good) 
model.track('input_videos/08fd33_4.mp4', save=True, conf=0.1)



# print(results[0])
# print('===========================================')
# for box in results[0].boxes:
#     print(box)