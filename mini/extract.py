import cv2
import os

# Set your file paths
video_path = 'cosy-retreat-rain.mp4'
output_folder = 'cabin'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the video
vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()
count = 0

print("Extracting frames...")

while success:
    # Save frame as PNG file
    output_path = os.path.join(output_folder, f"frame_{count:04d}.png")
    cv2.imwrite(output_path, image)     
    
    # Read the next frame
    success, image = vidcap.read()
    count += 1

print(f"Done! Extracted {count} frames.")