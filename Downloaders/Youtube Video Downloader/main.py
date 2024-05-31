from pytube import YouTube
from os import system, remove
from bs4 import BeautifulSoup
from requests import get
import validators
import ffmpeg

def getPlaylistLinks(url: str):
    """Function to get all the videos from a playlist link

    Args:
        url (str): Playlist URL
    """
    urlList = list()
    sourceCode = get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        print(link)
        print(href)
        if href.startswith('/watch?'):
            print(link.string.strip())
            print(domain + href + '\n')
            urlList.append(domain + href)
    print(urlList)

def downloadPlaylist(URLlist: list):
    print(URLlist)

def menu(msg: str):
    msgLength = len(msg) + 10
    print("\/"*(msgLength//2))
    print(msg.center(msgLength))
    print("\/"*(msgLength//2))

path = "media"
system('cls')

def downloadFile(fileType = "video"):
    """Function who downloads an video or/and audio from the YouTube URL

    Parameters:
        fileType (str, optional):
        "video" to download just the video,
        "audio" to download just the audio.
        Defaults to "video".
    """

    connectionError = False
    while True:
        menu(f'Youtube {fileType.capitalize()} Downloader')
        print("OBS: Don't forget the 'http://' or 'https://' in the link.")
        try:
            link = str(input("Type or paste the link here: "))
            if validators.url(link) is True:
                break
            else:
                raise ValueError
        except (ValueError, TypeError):
            print("Error! Invalid link! Please try again.")
            input("Press ENTER to continue...")
            system('cls')
    try:
        yt = YouTube(link)
    except:
        print("Connection Error! Check if you are connected to the internet.")
        connectionError = True
    
    if connectionError is False:
        print(f"Downloading video...")
        if fileType == "video":
            path = "media/videos"
            video = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution')[-1]
            video.download(path)
        elif fileType == "audio":
            path = "media/audios"
            # Download video file
            audio = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution')[-1]
            audio.download(path)
            # Convert video file to audio file
            fileName = yt.streams.first().default_filename
            videoPath = path + "/" + fileName
            video = ffmpeg.input(videoPath)
            audio = video.audio
            stream = ffmpeg.output(audio, f"{fileName}.mp3")
            ffmpeg.run(stream)
            remove(videoPath)
        print("Video downloaded!")
        input("Press ENTER to continue...")
        system('cls')

while True:
    system('cls')
    while True:
        try:
            menu("YOUTUBE VIDEO DOWNLOADER")
            print("""[ 1 ] Download a video
[ 2 ] Download just the audio
[ 3 ] Download a whole playlist (doesn't work in the moment)
[ 4 ] Quit program""")
            option = int(input("Select an option: "))
            if 0 < option < 5:
                break
            else:
                raise ValueError
        except (ValueError, TypeError, SyntaxError):
            print("Invalid option! Please select an option between 1 and 4.")

    if option == 1:
        downloadFile("video")
    elif option == 2:
        downloadFile("audio")
    elif option == 3:
        getPlaylistLinks("https://www.youtube.com/playlist?")
        # downloadPlaylist()
    else:
        print("GoodBye!")
        exit()
