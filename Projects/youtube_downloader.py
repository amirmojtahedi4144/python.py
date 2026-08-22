###########  WELCOME TO YOUTUBE DOWNLOADER ############
import yt_dlp

url = input("Youtube URL: ")

options = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": 
    "/Users/mohammadpishbin/%(title)s.%(ext)s",
    "merge_output_format": "mp4"
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])


print("================================================")
print("Download completed successfully!")