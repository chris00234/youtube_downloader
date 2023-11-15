from pytube import YouTube

def download_youtube_video(video_url, res, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        

        # Get the highest resolution stream
        video_stream = yt.streams.filter(file_extension="mp4", res=res).first()

        # Download the video to the specified output path
        video_stream.download(output_path)

        print(f"Video downloaded successfully to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Replace 'https://www.youtube.com/watch?v=VIDEO_ID' with the YouTube video URL you want to download
youtube_video_url = ''

# Replace 'output_directory' with the path where you want to save the downloaded video
output_directory = ''

# Download the YouTube video
youtube_video_url = input('put your youtube url')
output_directory = input('Where do you want to store it to?')
res = input('choose resolution (360, 480, 720, 1080)')

download_youtube_video(youtube_video_url, res, output_directory)
