from pytube import YouTube
import asyncio
from time import sleep
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import webbrowser


def callback(url):
    webbrowser.open_new(url)


def DisplayDetails(yt):
    global root

    # Title
    Label(root, text="Title", font=segoe_bold, background="#1a1a1a", foreground="#fff").place(
        x=50, y=180, width=73, height=30)
    Label(root, font='"Segoe UI" 15', text=yt.title, background="#1a1a1a", foreground="#fff").place(
        x=125, y=180, width=500, height=30)
    # Title END

    # Views
    Label(root, text="Views", font=segoe_bold, background="#1a1a1a", foreground="#fff").place(
        x=50, y=220, width=73, height=30)
    Label(root, font='"Segoe UI" 15', text=yt.views, background="#1a1a1a", foreground="#fff").place(
        x=125, y=220, width=500, height=30)
    # Views END

    # Rating
    Label(root, text="Rating", font=segoe_bold, background="#1a1a1a", foreground="#fff").place(
        x=50, y=260, width=73, height=30)
    Label(root, font='"Segoe UI" 15', text=yt.rating, background="#1a1a1a", foreground="#fff").place(
        x=125, y=260, width=500, height=30)
    # Rating END

    # Length
    Label(root, text="Length", font=segoe_bold, background="#1a1a1a", foreground="#fff").place(
        x=50, y=300, width=73, height=30)
    Label(root, font='"Segoe UI" 15', text=yt.length, background="#1a1a1a", foreground="#fff").place(
        x=125, y=300, width=500, height=30)
    # Length END

    Label(root, text="Downloading Complete", font=segoe_bold, background="#1a1a1a", foreground="#fff").place(
        x=50, y=340, width=500, height=30)


def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)


async def Download():
    Youtube_link = ytURL.get()
    download_Folder = download_Path.get()

    print(Youtube_link)
    print(download_Folder)
    getVideo = YouTube(Youtube_link)
    DisplayDetails(getVideo)
    sleep(3)
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(output_path=download_Folder, filename=getVideo.title)


def DownloadAsync():
    Label(root, text="Download Started", font=segoe_bold, background="#1a1a1a", foreground="#fff").place(
        x=50, y=180, height=30)
    loop = asyncio.new_event_loop()
    ss = loop.run_until_complete(Download())
    loop.close()


root = tk.Tk()
segoe_bold = '"Segoe UI" 15 bold'
ft = tkFont.Font(family='Segoe UI', size=10)


root.title("YouTube Downloader")
root.resizable(False, False)
root.geometry('600x500')
root.config(background="#1a1a1a")


video_Link = StringVar()
download_Path = StringVar()


destinationBtn = tk.Button(root, command=Browse, font=ft, justify="center",
                           bg="#6264a7", fg="#fff", text="Browse")
destinationLabel = Label(root, text="Save Location",
                         font='"Segoe UI" 10', background="#1a1a1a", foreground="#fff")
destination = tk.Entry(root, textvariable=download_Path,
                       font=ft, justify="left")

ytURLLabel = Label(root, text="Video URL",
                   font='"Segoe UI" 10', background="#1a1a1a", foreground="#fff")
ytURL = tk.Entry(root, textvariable=video_Link,
                 font=ft, justify="left")
downloadBtn = tk.Button(root, command=DownloadAsync, font=ft, justify="center",
                        bg="#6264a7", fg="#fff", text="Download")

destinationLabel.place(x=50, y=10, width=500, height=30)
destinationBtn.place(x=352, y=40, width=70, height=30)
destination.place(x=50, y=40, width=300, height=30)

ytURLLabel.place(x=50, y=70, width=500, height=30)
ytURL.place(x=50, y=100, width=372, height=30)
downloadBtn.place(x=50, y=135, width=70, height=30)


footer = Label(root, text="© Mahmudul Hasan | mahmudX.com", font='"Segoe UI" 10',
               background="#1a1a1a", foreground="#fff")
footer.place(x=50, y=470)
footer.bind("<Button-1>", lambda e: callback("http://www.mahmudx.com"))
# Label(root, text="Video URL",
#       font='"Segoe UI" 10', background="#1a1a1a", foreground="#fff")
root.mainloop()
