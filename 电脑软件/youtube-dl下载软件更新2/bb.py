import requests
import os

response = requests.get("https://api.github.com/repos/yt-dlp/yt-dlp/releases/latest")

zxbb = response.json()["tag_name"]

print(zxbb,type(zxbb))



os.system("pause")