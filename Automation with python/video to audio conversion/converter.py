from moviepy import VideoFileClip

# Load the video file
video = VideoFileClip("1128.mp4") 

# Extract the audio
audio = video.audio 

# Save the audio
audio.write_audiofile("1128_audio.mp3")