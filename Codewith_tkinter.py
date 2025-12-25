import tkinter as tk
import yt_dlp

root = tk.Tk()
root.title("test app")
root.geometry("350x180")

label_bar = tk.Label(root, text="paste any link from social media")
label_bar.pack(pady=20)

link = tk.Entry(root)
link.pack(pady=20)

def start():
	label_bar.config(text="starting download")
	text_link = link.get()
	ydl_opts = {
	 'cookiefile': '/storage/emulated/0/Youtube video/cookies.txt',
	 'format': 'best'
	 
} 
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download(text_link)
	label_bar.config(text="video complete download")


button = tk.Button(root, text="download", command=start)
button.pack(pady=20)


root.mainloop()
