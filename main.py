import pytube
from moviepy.editor import VideoFileClip
import pywhisper
import os

def download_video(url):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

def AudiotoText(filename):
    model = pywhisper.load_model("base")
    result = model.transcribe(filename)
    print(result["text"])

def main():
    print('''
    This tool will convert Youtube videos to mp3 files and then transcribe them to text using Whisper.
    ''')

    print("Enter the link of the video you want to convert:")
    link = input()
    print("Downloading video... Please wait.")
    try:
        filename = download_video(link)
        print("Downloaded video as " + filename)
    except:
        print("Not a valid link..")
        return
    try:
        convert_to_mp3(filename)
        print("Converted video to mp3")
    except:
        print("Error converting video to mp3")
        return
    try:
        AudiotoText(filename[:-4] + ".mp3")
        print("Transcribed audio to text")
        os.remove(filename)
        os.remove(filename[:-4] + ".mp3")
        print("Removed video and audio files")
        print("Done!")
    except:
        print("Error transcribing audio to text")
        return

if __name__ == "__main__":
    main()
