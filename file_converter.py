import os
import json
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image

# Author: Jeba Seelan
# Topic: File Converter Tool
# Created on: 2024-10-24
# Description: A script to convert between MP4, MP3, JPG, PNG, TXT, and JSON formats.

def mp4_to_mp3(input_file: str, output_file: str):
    """Convert MP4 file to MP3."""
    try:
        audio = AudioFileClip(input_file)
        audio.write_audiofile(output_file)
        audio.close()
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def mp3_to_mp4(input_file: str, output_file: str, placeholder_video: str):
    """Convert MP3 file to MP4 using a placeholder video."""
    try:
        audio = AudioFileClip(input_file)
        video = VideoFileClip(placeholder_video)
        final_video = video.set_audio(audio)
        final_video.write_videofile(output_file)
        audio.close()
        video.close()
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def jpg_to_png(input_file: str, output_file: str):
    """Convert JPG image to PNG."""
    try:
        with Image.open(input_file) as img:
            img.save(output_file, "PNG")
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def png_to_jpg(input_file: str, output_file: str):
    """Convert PNG image to JPG."""
    try:
        with Image.open(input_file) as img:
            rgb_img = img.convert("RGB")
            rgb_img.save(output_file, "JPEG")
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def text_to_json(input_file: str, output_file: str):
    """Convert text file to JSON."""
    try:
        with open(input_file, 'r') as txt_file:
            content = txt_file.read()
        with open(output_file, 'w') as json_file:
            json.dump({"content": content}, json_file, indent=4)
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def json_to_text(input_file: str, output_file: str):
    """Convert JSON file back to text."""
    try:
        with open(input_file, 'r') as json_file:
            data = json.load(json_file)
        with open(output_file, 'w') as txt_file:
            txt_file.write(data["content"])
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def convert_file(input_file: str, output_file: str, placeholder_video: str):
    """Determine the conversion type based on file extensions."""
    _, ext = os.path.splitext(input_file)
    _, out_ext = os.path.splitext(output_file)

    conversion_map = {
        ('.mp4', '.mp3'): mp4_to_mp3,
        ('.mp3', '.mp4'): lambda i, o: mp3_to_mp4(i, o, placeholder_video),
        ('.jpg', '.png'): jpg_to_png,
        ('.png', '.jpg'): png_to_jpg,
        ('.txt', '.json'): text_to_json,
        ('.json', '.txt'): json_to_text,
    }

    converter = conversion_map.get((ext, out_ext))
    if converter:
        converter(input_file, output_file)
    else:
        print("Unsupported conversion or file extension mismatch.")

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the desired output file path (with extension): ")
    placeholder_video = "path/to/placeholder.mp4"  # Change this to your actual placeholder video path

    convert_file(input_file, output_file, placeholder_video)  # Start the conversion process
