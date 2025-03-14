import sys
import yt_dlp

link = sys.argv[1]

# Function to fetch and download video information
def download_video(url):
    with yt_dlp.YoutubeDL() as ydl:
        # Extract info without downloading the video
        info = ydl.extract_info(url, download=False)
        
        # Print video details
        print("Title:", info['title'])
        print("Views:", info['view_count'])

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download best video and audio
            'outtmpl': '%(title)s.%(ext)s',  # Save the video with the title as the filename
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

       
        print("Download complete.")

# Fetch and download the video for the provided link
download_video(link)


