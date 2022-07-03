import os
from pytube import YouTube

def file_location():
    try:
        root=os.chdir('/Users/alcole')
        folders=os.listdir()
        path_check=os.path.isdir("/Users/alcole/downloaded_vids")
        for i in folders:
            if path_check:
                os.chdir("/Users/alcole/downloaded_vids")
                return "path has been found and path has been changed"

            else:
                os.mkdir("downloaded_vids")
                os.chdir("/Users/alcole/downloaded_vids")
                return "path wasnt found but has been created"
    except PermissionError as e:
        return "No permission to modify"
        
def tuber(url):
    try:
        yt=YouTube(url)
        streamer=yt.streams.get_by_itag(22)
        return streamer.download()
    except Exception as e:
        return e



if __name__=="__main__":
    file_location()
    url=input("Please submit a url: ")
    print(tuber(url))
    
