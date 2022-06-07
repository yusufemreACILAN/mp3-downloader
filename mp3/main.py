from ast import Return
from cProfile import label
from tkinter import *
from pytube import YouTube
from moviepy.editor import *

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Patalin's YouTube Downloader")
root.configure(bg="#f2eee3")

label(root,
    text='YouTube Video Downloader',
    font='arial 20 bold',
    bg="#f2eee3",
    fg="red").pack()


Link = StringVar()
label(root,
    text='Paste The YouTube Link Here:',
    font='arial 15 bold',
    bg="#f2eee3").place(x=40, y=60)


Link_enter=Entry(root,
            width=50,
            textvariable=Link).place(x=32, y=90)

def Downloader():
    url=YouTube(str(Link.get()))
    video=url.streams[1]
    video.Download()
    label(root,
        text='DOWNLOADED',
        font='arial 15',
        bg="#f2eee3",
        fg="red").place(x=185, y=185)
    return video.download()

   










def converter():

    mp3_file = f"/Users/Z112_17/mp3/Youtube-Downloader"\
         f"-and-MPE-Converter/Converted MP4.mp3"

MP4_file=Downloader()
videoclip = VideoFileClip(MP4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()

label(root,
        text='CONVERTED',
        font='arial 15',
        bg="#f2eee3",
        fg="red").place(x=185, y=185)
       


Download_mp4 = Button(root,
        text='DOWNLOAD',
        font='arial 15 bold',
        bg='pale violet red',
        padx=2,
        command=Downloader,
        fg="blue").place(x=180, y=150)



connvert_mp4 = Button(root,
        text='Convert to mp3',
        font='arial 15 bold',
        bg='pale violet red',
        padx=2,
        command=converter,
        fg="blue").place(x=180, y=210)

root.mainloop()
            

 


             



