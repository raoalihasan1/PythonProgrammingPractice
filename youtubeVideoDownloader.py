# This Program Works On Linux And MacOS

# Import All Modules Needed For The App
from pytube import YouTube
from tkinter import *
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
from pathlib import Path
from yt_dlp import YoutubeDL
from tkinter.messagebox import askyesno
import os


# Class Containing Attributes And Methods To Download The Video/Audio
class YouTubeVideo:

    # Constructor Which Takes The YouTube URL
    def __init__(self, videoURL):
        self.__URL = videoURL

    # Method That Returns The Video Details And Thumbnail Of The Video If A Valid URL Was Inputted By The User
    def getVideoDetails(self):
        try:
            self.__getVideo = YouTube(self.getURL())
            urlData = urlopen(self.__getVideo.thumbnail_url)
            rawData = urlData.read()
            urlData.close()
            return [True, "{}".format(self.__getVideo.title), "Total Views:  {}".format(self.__getVideo.views), rawData]
        except:
            return [False]

    # Method That Downloads The Video/Audio Based On What The User Chose Hence Using The Imported Library Based On Users' Choice
    def downloadVideo(self, Format):
        downloadFolder = str(os.path.join(Path.home(), "Downloads"))
        if (Format == "Audio"):
            ydlOpts = {
                'outtmpl': '{}/%(title)s.%(ext)s'.format(downloadFolder),
                'format': 'm4a/bestaudio/best',
                'quiet': True,
                "external_downloader_args": ['-loglevel', 'panic'],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            with YoutubeDL(ydlOpts) as YDL:
                YDL.download([self.getURL()])
                return True
        else:
            self.__bestResolution = self.__getVideo.streams.get_highest_resolution()
            if (self.__bestResolution.download(downloadFolder)):
                return True
        return False

    # Method That Returns The Video URL
    def getURL(self):
        return self.__URL


# Method Called When User Clicks Download And Displays A Message If It Was Downlaoded Or Not
def downloadVideoOrAudio(Obj, Type):
    global downloadFrame, mainFrame, videoURL, resultMessage
    resultMessage = Label(downloadFrame, text="Successfully Downloaded {}!".format(formatType.get()),
                          font=("Lucida Console", 17, "bold"), foreground="#65BD0D")
    if (Obj != None):
        if (not Obj.downloadVideo(Type)):
            resultMessage.config(
                text="Failed To Download The {}!".format(formatType.get()), foreground="#FF0033")
    resultMessage.place(x=(WIDTH/2)-217.5, y=(HEIGHT/2)+57.5)
    downloadFrame.after(5000, afterDownload())


# Method That Displays A Prompt After Attempting To Download And Takes Action Based On Users' Response
def afterDownload():
    global youTubeDownloader
    downloadAgain = askyesno(title='YouTube Downloader  ·  By Ali Hasan',
                             message='Download Another? ')
    if (downloadAgain):
        returnToMainFrame(True)
    else:
        youTubeDownloader.destroy()


# Method That Gets URL From User And Changes To The Next Frame If The URL Is Valid
def getInput():
    global videoURL, WIDTH, HEIGHT, downloadFrame, mainFrame, formatType
    URL = videoURL.get("1.0", END)
    if (URL != ""):
        downloadFromYouTube = YouTubeVideo(URL)
    if (downloadFromYouTube.getVideoDetails()[0]):
        mainFrame.forget()
        downloadFrame.pack(fill="both", expand=1, pady=30)
        # Get The Thumbnail Image And Place It In The Label
        getImage = Image.open(
            BytesIO(downloadFromYouTube.getVideoDetails()[3]))
        getImage = getImage.resize((175, 100), Image.ANTIALIAS)
        thePhoto = ImageTk.PhotoImage(getImage)
        thumbnailLabel = Label(downloadFrame, image=thePhoto)
        thumbnailLabel.image = thePhoto
        # Create And Place The Widgets In The Main Frame
        videoTitle = Label(downloadFrame, text="{}".format(downloadFromYouTube.getVideoDetails()[1]),
                           font=("Lucida Console", 14, "bold"), foreground="#020408", wraplength=525, justify=LEFT)
        videoViews = Label(downloadFrame, text="{}".format(downloadFromYouTube.getVideoDetails()[2]),
                           font=("Lucida Console", 13), foreground="#020408")
        selectFormat = OptionMenu(
            downloadFrame, formatType, "Video", "Audio", command=changeFormatType())
        returnBtn = Button(downloadFrame, text="Return",
                           font=("Consolas 18 bold"),
                           width=15, borderwidth=2,
                           cursor="plus", bg="#ED4D4D",
                           activebackground="#fd3a2d",
                           activeforeground="#FFF",
                           highlightthickness=3,
                           highlightbackground="#2B2B2B",
                           fg="#C5C5C5", command=lambda: returnToMainFrame(False))
        donwloadLink = Button(downloadFrame, text="Download",
                              font=("Consolas 18 bold"),
                              width=15, borderwidth=2,
                              bg="#63C5DA", activebackground="#0492C2",
                              activeforeground="#FFF",
                              highlightbackground="#2B2B2B",
                              fg="#DCD9CD",
                              highlightthickness=3, cursor="plus",
                              command=lambda: downloadVideoOrAudio(downloadFromYouTube, formatType.get()))
        thumbnailLabel.place(x=(WIDTH/2)-340, y=(HEIGHT/2)-135)
        videoTitle.place(x=(WIDTH/2)-150, y=(HEIGHT/2)-135)
        videoViews.place(x=(WIDTH/2)-150, y=(HEIGHT/2)-70)
        returnBtn.place(x=(WIDTH/2)-340, y=(HEIGHT/2)-20, height=45)
        donwloadLink.place(x=(WIDTH/2)-80, y=(HEIGHT/2)-20, height=45)
        selectFormat.config(width=8, height=1, borderwidth=2, cursor="plus", bg="#03C04A",
                            activebackground="#03AC13", activeforeground="#FFF",
                            highlightthickness=3, highlightbackground="#2B2B2B",
                            fg="#C5C5C5", font=("Consolas 18 bold"))
        selectFormat.place(x=(WIDTH/2)+180, y=(HEIGHT/2)-20)


# Method That Returns The App To The Main Frame
def returnToMainFrame(completedDownload):
    global downloadFrame, mainFrame, videoURL, resultMessage
    downloadFrame.forget()
    if (completedDownload):
        resultMessage.destroy()
    videoURL.delete('1.0', END)
    mainFrame.pack(fill="both", expand=1, pady=(30, 0))


# Method That Changes The Value of The OptionMenu When The User Changes Between Audio And Video Option
def changeFormatType():
    global formatType
    if (formatType.get() == "Audio"):
        formatType.set("Video")
    else:
        formatType.set("Audio")


# Set Width And Height Of The Window To Constants
WIDTH, HEIGHT = 775, 300

# Create The Window, Set Values And Create Frames
youTubeDownloader = Tk()
youTubeDownloader.title("YouTube Downloader  ·  By Ali Hasan")
youTubeDownloader.geometry(f"{WIDTH}x{HEIGHT}")
mainFrame = Frame(youTubeDownloader)
mainFrame.pack(fill="both", expand=1, pady=(30, 0))
downloadFrame = Frame(youTubeDownloader)

# Get And Display The YouTube Logo At The Bottom Of The Main Frame
urlData = urlopen(
    "https://upload.wikimedia.org/wikipedia/commons/3/34/YouTube_logo_%282017%29.png")
rawData = urlData.read()
urlData.close()
getImage = Image.open(BytesIO(rawData))
getImage = getImage.resize((85, 22), Image.ANTIALIAS)
thePhoto = ImageTk.PhotoImage(getImage)
thumbnailLabel = Label(mainFrame, image=thePhoto)
thumbnailLabel.image = thePhoto

# Create And Place The Widgets In The Main Frame
downloaderTitle = Label(mainFrame, text="YouTube Downloader",
                        font=("Lucida Console", 24, "bold"), foreground="#020408")
downloaderPrompt = Label(mainFrame, text="Enter URL:",
                         font=("Lucida Console", 18, "bold"), foreground="#020408")
videoURL = Text(mainFrame, bd=2, font=("Lucida Console", 13),
                foreground="#020408", width=41, height=1, spacing1=2, spacing3=2)
getVideoBtn = Button(mainFrame, text="Get Video",
                     font=("Consolas 18 bold"),
                     width=19, borderwidth=2,
                     bg="#63C5DA", activebackground="#0492C2",
                     activeforeground="#FFF",
                     highlightbackground="#2B2B2B",
                     fg="#DCD9CD",
                     highlightthickness=3, cursor="plus", command=getInput)
exitBtn = Button(mainFrame, text="Exit",
                 font=("Consolas 18 bold"),
                 width=19, borderwidth=2,
                 cursor="plus", bg="#ED4D4D",
                 activebackground="#fd3a2d",
                 activeforeground="#FFF",
                 highlightthickness=3,
                 highlightbackground="#2B2B2B",
                 fg="#C5C5C5", command=youTubeDownloader.destroy)
downloaderTitle.place(x=(WIDTH/2)-180, y=(HEIGHT/2)-150)
downloaderPrompt.place(x=(WIDTH/2)-316, y=(HEIGHT/2)-70)
videoURL.place(x=(WIDTH/2)-156, y=(HEIGHT/2)-70)
getVideoBtn.place(x=(WIDTH/2)-316, y=(HEIGHT/2)-20, height=50)
exitBtn.place(x=(WIDTH/2)+2.25, y=(HEIGHT/2)-20, height=50)
thumbnailLabel.place(x=(WIDTH/2)-38.5, y=(HEIGHT/2)+85)

formatType, resultMessage = StringVar(downloadFrame), None
formatType.set("Audio")
youTubeDownloader.mainloop()
