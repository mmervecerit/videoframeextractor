import os
import cv2
import uuid
import argparse
#example call: python videoframe.py -sp "C:/Users/username/foldername" -dp "C:/Users/username/foldername"
#reqs: python3, opencv-python, uuid, argparsei you can download via pip
def extractFrames(pathIn,dirnameout, pathOut):
    if not os.path.isdir(dirnameout):
        os.mkdir(dirnameout)
    os.mkdir(pathOut)
 
    cap = cv2.VideoCapture(pathIn)
    count = 0
 
    while (cap.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
def main(dirnamein,dirnameout):
    for video in os.listdir(dirnamein):
        print(video)
        extractFrames(dirnamein+'/'+video, dirnameout,(dirnameout+'/'+video.split('.')[0]+str(uuid.uuid4())))
 
if __name__=="__main__":
    parser = argparse.ArgumentParser(description = 'Give the path of the directory including video and the destination path for jpegs')
    parser.add_argument('-sp','--sourcepath', help='enter the full directory path has the videos')
    parser.add_argument('-dp','--destpath', help='enter the full destination directory path')
    args = parser.parse_args()
    videodirpath = args.sourcepath
    destpath=args.destpath
    main(videodirpath,destpath)