
from pytube import YouTube

def dowload(link):
    youtubeobject= YouTube(link)
    youtubeobject=youtubeobject.streams.get_highest_resolution()
    try:
        youtubeobject.download()
    except:
        print("There is a download error, please try again later")
    print("dowload successfull")
    
link = input("Put your youtube link here!! URL: ")
dowload(link)
    