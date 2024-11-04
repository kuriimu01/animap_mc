from PIL import Image
import os
from math import ceil,sqrt

def AssembleFrames(frames_path, output_image_path, frames_count):
    # Setting the dimensions for each frame and the final grid
    frame_size = (128, 128)
    columns = ceil(sqrt(frames_count))
    rows = ceil(frames_count/columns)
    print(f"Recommended map size: {columns} x {rows}")
    output_width = columns * frame_size[0]
    output_height = rows * frame_size[1]

    # Create a new blank image with the final output dimensions
    output_image = Image.new("RGB", (output_width, output_height))

    # Get and sort the list of frame filenames
    frame_files = sorted(
        [f for f in os.listdir(frames_path) if f.endswith(".png")], 
        key=lambda x: int(os.path.splitext(x)[0])  # Sort by numeric ID in filename
    )
    # Place each frame in the grid
    for index, frame_file in enumerate(frame_files):
        if index >= columns * rows:
            break  # Stop if we have placed the maximum number of frames
        
        # Open the frame image
        frame_path = os.path.join(frames_path, frame_file)
        frame = Image.open(frame_path)
        
        # Resize the frame if necessary, using LANCZOS instead of ANTIALIAS
        frame = frame.resize(frame_size, Image.LANCZOS)

        # Calculate position in the grid
        x = (index % columns) * frame_size[0]
        y = (index // columns) * frame_size[1]
        
        # Paste the frame into the output image
        output_image.paste(frame, (x, y))

    # Save the final combined image (ensure file extension is specified)
    output_image.save(output_image_path)
    print(f"Output image saved as {output_image_path}. \nNow you can upload it on https://rebane2001.com/mapartcraft/ and don't forget about map size ({columns}x{rows})")

