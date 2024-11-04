import os
import sys
import cv2
from PIL import Image

def GenerateFrames(input_path, frames_path):
    # Clear the frames directory
    for filename in os.listdir(frames_path):
        file_path = os.path.join(frames_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  # Remove the file
        except Exception as e:
            print(f"Error removing file {file_path}: {e}")

    # Initialize the video capture object
    cap = cv2.VideoCapture(input_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_id = 0

    # Extract frames from the video
    while frame_id < total_frames:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there are no more frames

        # Convert BGR (OpenCV format) to RGB (PIL format)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Create a PIL Image from the frame
        frame_image = Image.fromarray(frame_rgb)

        # Save the frame as a PNG file with its frame ID
        frame_file_path = os.path.join(frames_path, f"{frame_id}.png")
        frame_image.save(frame_file_path)

        # Update the frame counter and print the progress
        frame_id += 1
        if frame_id % 100 == 0 or frame_id == total_frames:
            # Print the current progress
            sys.stdout.write(f"Extracted {frame_id}/{total_frames} frames\r")
            sys.stdout.flush()

    # Release the video capture object
    cap.release()
    print(f"\nFrames extracted and saved in {frames_path}")
    return total_frames
