import cv2
import os

video_path = 'cropped_video.MOV'
frames_dir = 'video_frames'
os.makedirs(frames_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

start_frame = 2000  # Frame to start saving from
end_frame = 3000    # Frame to stop saving at
frame_skip = 5   # Number of frames to skip between saves

total_frame_count = 0  # Total frames processed
saved_frame_count = 0  # Total frames saved

# Set the video position to the start_frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret or total_frame_count + start_frame >= end_frame:
        break

    # Save only every Nth frame after start_frame until end_frame
    if total_frame_count % frame_skip == 0:
        frame_filename = f"{frames_dir}/frame_{total_frame_count + start_frame:04d}.png"
        cv2.imwrite(frame_filename, frame)
        saved_frame_count += 1

    total_frame_count += 1

cap.release()

# Print the total number of frames processed and saved
print(f"Total frames processed: {total_frame_count}")
print(f"Total frames saved: {saved_frame_count}")
