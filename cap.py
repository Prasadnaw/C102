import cv2
import dropbox
import time
import random

startTime = time.time()

def take_snapshot():
    number = random.randint(0, 100)

    videoCaptureObject = cv2.videoCaptureObject(0)

    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        startTime = time.time
        result = False

    return image_name
    print("Snapshot Taken")

    videoCaptureObject.release()

    cv2.destroyAllWindows()

take_snapshot() 

def upload_file(image_name):
    access_token = 'tDk1b7Q0FFUAAAAAAAAAAX_yltGRd4uWP0yGZRFgHrQprT0Fm-aPbX9Pxfu7P__p'
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMOde.overWrite)
        print("file Uploaded")

def main():
    while(True):
        if((time.time() - startTime) >= 3):
            name = take_snapshot()
            upload_file(name)

main()            
