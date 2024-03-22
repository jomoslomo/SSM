import cv2
import sys
import tkinter as tk
from tkinter import filedialog

def select_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    return file_path

# Get the input video path using the file dialog
input_video_path = select_video_file()
if not input_video_path:
    print("No video file selected.")
    exit()

# Define the path to the output video
output_video_path = 'cropped_video.mp4'

# Open the input video
cap = cv2.VideoCapture(input_video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Define the codec and create a VideoWriter object to write the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Read the first frame to get the ROI (Region of Interest)
ret, frame = cap.read()
if not ret:
    print("Error reading the video file.")
    cap.release()
    exit()

# Select the ROI (Region of Interest) manually
roi = cv2.selectROI("Select ROI", frame, fromCenter=False)
crop_x, crop_y, crop_width, crop_height = roi

# Create a clone of the frame to draw the selection rectangle
roi_frame = frame.copy()

# Draw the selection rectangle on the cloned frame
cv2.rectangle(roi_frame, (crop_x, crop_y), (crop_x + crop_width, crop_y + crop_height), (0, 255, 0), 2)

# Display the cloned frame with the selection rectangle
cv2.imshow("Selected ROI", roi_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Check if the user wants to exit or continue
key = cv2.waitKey(0) & 0xFF
if key == ord('q'):
    print("User exited without cropping.")
    cap.release()
    exit()

# Create the VideoWriter object with the selected ROI dimensions
out = cv2.VideoWriter(output_video_path, fourcc, fps, (crop_width, crop_height))

# Reset the video capture to the beginning
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Initialize the progress bar
progress = 0
print("Cropping video...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Crop the frame
    cropped_frame = frame[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]

    # Write the cropped frame to the output video
    out.write(cropped_frame)

    # Update the progress bar
    progress += 1
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %d%%" % ('=' * int(progress * 50 / total_frames), int(progress * 100 / total_frames)))
    sys.stdout.flush()

# Release everything when the job is finished
cap.release()
out.release()
print("\nCropping completed. The cropped video is saved as:", output_video_path)