from moviepy.editor import VideoFileClip

def GetTimeInput():
    print("Choose timing option:")
    print("1. Custom time set")
    print("2. Default time (full video)")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        start_time = input("Enter start time (format: mm:ss): ")
        end_time = input("Enter end time (format: mm:ss): ")
        return start_time, end_time
    elif choice == '2':
        return None, None
    else:
        print("Invalid choice, using default (full video).")
        return None, None
    
def SetFps(input_path, output_path, fps=40):
    clip = VideoFileClip(input_path)
    clip_upscaled = clip.set_fps(fps)
    clip_upscaled.write_videofile(output_path, codec='libx264', fps=fps, bitrate="20000k")
    print(f"Video successfully upscaled to {fps} FPS and saved to {output_path}")

def SetSize(input_path, output_path, width=128, height=128):
    clip = VideoFileClip(input_path)
    resized_clip = clip.resize(newsize=(width, height))    
    resized_clip.write_videofile(output_path, codec='libx264', bitrate="20000k")
    print(f"Video resized to {width}x{height} and saved to {output_path}")

def TrimVideo(input_path, output_path, start_time=None, end_time=None):
    clip = VideoFileClip(input_path)
    
    if start_time is not None and end_time is not None:
        trimmed_clip = clip.subclip(start_time, end_time)
    else:
        trimmed_clip = clip  # Use the full video if no trim times are specified

    trimmed_clip.write_videofile(output_path, codec='libx264', bitrate="2000k", audio=False)
    print(f"Video trimmed and saved to {output_path}")
