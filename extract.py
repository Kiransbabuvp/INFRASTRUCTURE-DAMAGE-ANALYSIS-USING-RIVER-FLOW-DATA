'''
This is the embedded part of the project. This software will run on pi device
and is based on python. This program uses open cv to acquire images and substract them
and store it in predefined directories as detailed below



'''
# Import opencv
import cv2

#Import OS utilities
import os
from os import listdir
from os.path import isfile, join


# Directory of the project
BASE_DIR = 'E:/flow/project/'

# Directory where video is kept
INPUT_DIR = BASE_DIR + ''

#Directory where images are stored
IMAGE_DIR = BASE_DIR + 'images/'

#Directory where substracted images are stored
SUB_DIR = BASE_DIR + 'subs/'


# Base function to capture images from a source.
def capture(cap):
    os.chdir(IMAGE_DIR)
    i=0
    while(cap.isOpened() and i <=100 ):
        ret, frame = cap.read()
        if ret:
            print("Successfully captured frame #", i, "as", 'frame_'+str(f"{i:003}")+ '.jpg')
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            h, w = gray_image.shape
            # Tweak the below parameters to mark the ROI
            y = int(h * 2 / 5)
            x = int(w * 2 / 5)
            y_offset = int(h / 5)
            x_offset = int(w / 5)
            # End Tweaking
            
            roi_gray = gray_image[y:y + y_offset, x:x + x_offset]  # Extract bottom face
            
            
            cv2.imwrite('frame_'+str(f"{i:003}")+'.jpg',roi_gray)
            i+=1
        else :
            break

# The following function extract images from a video file
def extract():
    cap = cv2.VideoCapture(BASE_DIR + 'config/input_data.mp4')
    capture(cap)
    cap.release()
    cv2.destroyAllWindows()        

# This functionrecords the first 100 frames the first camera
def record():
    cap = cv2.VideoCapture(0)
    capture(cap)
    cap.release()
    cv2.destroyAllWindows()        

# THis function substract an image from a subsequent image and stores it.
def substract():
    os.chdir(SUB_DIR)
    file_list = [f for f in listdir(IMAGE_DIR) if isfile(join(IMAGE_DIR, f))]
    for index in range(0,len(file_list)-1):
        print("Substracting..", file_list[index],"from", file_list[index+1], " =>",'sub_'+str(f"{index:003}")+'.jpg' )
        first_file = cv2.imread(IMAGE_DIR + file_list[index])
        second_file = cv2.imread(IMAGE_DIR + file_list[index+1])
        
        sub_image = cv2.subtract(first_file,second_file)
        cv2.imwrite('sub_'+str(f"{index:003}")+'.jpg',sub_image)



# Main program is shown below

#Extract image from the video
extract()

#Extract image from the video
#record()

#Substract subsequent images
substract()

# Main program end
