import yt_dlp

url = input("write url: ")
ydl_opts = {
    'cookiefile': '/storage/emulated/0/Youtube video/cookies.txt',
    'format': 'best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
