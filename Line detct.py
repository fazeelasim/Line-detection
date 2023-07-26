import cv2
import numpy as np
from lanedet import LaneDet
def detect_lines_lanedet(video_path, output_path):
    # Create LaneDet object and load pre-trained weights
    model = LaneDet(weights_path='C:\Users\fazee\Desktop\lanedet-main\configs\condlane\resnet50_culane.py') 
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        lane_detected_frame = model.detect_lane(frame)
        cv2.imshow('Lane Detection', lane_detected_frame)
        out.write(lane_detected_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    input_video_path = "C:/Users/fazee/Desktop/Test.mp4"
    output_video_path = "C:/Users/fazee/Desktop/file"
    detect_lines_lanedet(input_video_path, output_video_path)
