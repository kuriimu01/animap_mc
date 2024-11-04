import configparser
from VideoConfigurator import GetTimeInput, SetFps, SetSize, TrimVideo
from GenerateFrames import GenerateFrames
from AssembleFrames import AssembleFrames
from GenerateCommands import GenerateCommands

# Load paths from paths.txt
config = configparser.ConfigParser()
config.read('paths.txt')

# Paths from the config file
input_path = config['DEFAULT']['video_input_path']
fps_output_path = config['DEFAULT']['fps_output_path']
timed_output_path = config['DEFAULT']['timed_output_path']
output_path = config['DEFAULT']['output_path']
image_path = config['DEFAULT']['image_path']
frames_path = config['DEFAULT']['frames_path']
tick_path = config['DEFAULT']['tick_path']

def main():
    
    # Get user input for timing
    start_time, end_time = GetTimeInput()

    print("Trimming the video...")
    TrimVideo(input_path, timed_output_path, start_time, end_time)
    
    # Set FPS to 40
    print("Setting the video FPS to 40...")
    SetFps(timed_output_path, fps_output_path)
    
    # Set the video to 128x128 size
    print("Resizing the video to 128x128...")
    SetSize(fps_output_path, output_path)

    # Extract frames from the video and saving frames count
    print("Extracting frames from the video...")
    total_frames = GenerateFrames(output_path, frames_path)

    # Assembling Frames
    print("Creating compound image from frames...")
    AssembleFrames(frames_path, image_path, total_frames)

    #Generate Minecraft commands
    print("Generating Minecraft commands for ...")
    GenerateCommands(tick_path, 3608)  

    print("All steps completed successfully!")

if __name__ == "__main__":
    main()
