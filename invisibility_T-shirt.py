import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0) # Make an instance of the camera
codec = cv2.VideoWriter_fourcc(*'XVID') # Video Codec
out = cv2.VideoWriter('Output.avi',codec,20.0,(640,480)) # out is the video file
_, bag = cap.read() # Capture the background without the person
# Below code is running indefinitely until 'q' is pressed to quit
while True:
    _, frame = cap.read() # Capture the frames
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert them to hsv format
    lower = np.array([155,160,0]) # Lower limit
    upper = np.array([255,255,255]) # Upper limit
    mask = cv2.inRange(frame, lower, upper) # Anything that is within this range, this is the mask for background
    mask_inv = cv2.bitwise_not(mask) # Make an inverse mask for foreground
    fg = cv2.bitwise_and(frame, frame, mask = mask_inv) # In the frame where there is something in frame and mask is true
    bg = cv2.bitwise_and(bag, bag, mask = mask) # In bag where there is something in bag and mask is true
    final = cv2.add(bg, fg) # Adding the foreground and background to create the final image
    cv2.imshow("final", final) # Showing the final image
    out.write(final) # saving the frames

    if cv2.waitKey(1) & 0xFF == ord('q'): # quit if pressed q
        break
cap.release() # Releasing the camera
out.release() # Finishing the video formation
cv2.destroyAllWindows() # Closing all the windows
