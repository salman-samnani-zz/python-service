
import face_recognition
import cv2
import numpy as np
import time
import os
#videoPath = 0#['rtsp://EVA:eva123@74.67.193.24:85/cam/realmonitor?channel=3&subtype=0' , 'rtsp://admin:Epagingadmin@10.194.2.51:554/' ]

def make_dataset(folder,no_of_data,videoPath):
    count = 0
    #print(len(folder))
    print('In make_dataset')
    print(no_of_data)

    path_0 = os.path.join(os.getcwd(),'dataset',folder)
    if not os.path.exists(path_0):
        os.makedirs(path_0)
    print(path_0)
    # Get a reference to webcam #0 (the default one)
    video_capture_0 = cv2.VideoCapture(videoPath)

    print("ok")
    process_this_frame =True
    
    
    while True:
        try:
            # Grab a single frame of video
            ret, frame_0 = video_capture_0.read()
        
            #sky_0 = cv2.resize(frame_0,(400, 400))
            sky_0 = cv2.resize(frame_0,(0, 0),fx=0.60,fy=0.60)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame_0 = sky_0[:, :, ::-1]
            if process_this_frame:
                # Find all the faces and face enqcodings in the frame of video
                face_locations = face_recognition.face_locations(rgb_frame_0,model="hog")
                for face_location in face_locations:

                    # Print the location of each face in this image
                    top, right, bottom, left = face_location
                    #gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                
                    crop_img = sky_0[top-60:bottom+60, left-60:right+60]
                    name_time = int(time.time())
                    path_0 = os.path.join(os.getcwd(), 'dataset' ,folder, str(name_time) +'.jpg')
                    try:
                        cv2.imwrite(path_0, crop_img)
                        print('Image is saved')
                        count = count + 1
                        print(count)
                        time.sleep(1)
                        
                    except:
                        print('in except of image saved')
                        pass            
                    
                    # Draw a box around the face
                    cv2.rectangle(sky_0, (left, top), (right, bottom), (0, 0, 255), 2)
            process_this_frame = not process_this_frame
        except:
            pass


        # Display the resulting image
        cv2.imshow('Video_0', sky_0)
        if count >= no_of_data:
            break

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('exit system')
            break
    
    # Release handle to the webcam
    video_capture_0.release()
    cv2.destroyAllWindows()


mydir = 'add-person-file.txt'
file_to_read = os.path.join(os.getcwd(),mydir)



def read_file():
    f= open("e:\salman.txt","w+")
    for i in range(10):
        f.write("This is line sas %d\r\n" % (i+1))
    no_of_pics = 30
    with open(file_to_read, 'r') as file:
        plist = file.read()
        if len(plist) > 0:
            slist = plist.split(',')

            uId = slist[0]
            #no_of_pics = slist[1]
            videoPath = slist[2] # last
            state = slist[3]
            print(uId)
            print(no_of_pics)
            print(videoPath)
            if int(state) == 2:
                make_dataset(uId,no_of_pics,videoPath)
                open(file_to_read,"w")
                file.close()

if __name__ == '__main__':
    while True:
        read_file()
        print('No fill to read')
        time.sleep(10)

        
        
    '''
    with open('D:/david/DemoApp/add-person.txt', 'r') as file:
        plist = file.read()
    slist = plist.split(',')

    uId = slist[0]
    no_of_pics = slist[1]
    videoPath = slist[2] # last
    print(uId)
    print(no_of_pics)
    print(videoPath)
    '''
    #make_dataset(uId,no_of_pics,videoPath)
    '''
    except:
        print("There is an error in system")
    '''
    