# import the opencv library 
import cv2 

  
  
# define a video capture object 
cap = cv2.VideoCapture(0) 
# Create the MOSSE tracker
tracker = cv2.legacy.TrackerMOSSE_create()
ret, frame = cap.read() 
bbox = cv2.selectROI("Tracking",frame,False)
tracker.init(frame,bbox)

def drawBox(frame,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(frame,"Tracking",(75,75), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
   



  
while True: 
    timer = cv2.getTickCount()
      
    # Capture the video frame 
    # by frame 
    ret, frame = cap.read() 

    ret,bbox = tracker.update(frame)
    print(type(bbox))

    if ret:
        drawBox(frame,bbox)
    else:
        cv2.putText(frame,"Lost",(75,75), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)




    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(frame,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
  
    # Display the resulting frame 
    cv2.imshow('Tracking', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

       

        
  
