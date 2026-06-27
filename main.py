import cv2
import HandTrackingModule as htm
from pycaw.pycaw import AudioUtilities
import numpy as np 



# Getting the system volume access(current active output device)
devices = AudioUtilities.GetSpeakers()

volume = devices.EndpointVolume



vol_range = volume.GetVolumeRange()

min_vol = vol_range[0]
max_vol = vol_range[1]
vol = 0


# Accessing the default webcam ( 0 = primary webcam )
cap = cv2.VideoCapture(0)


# Create a hand detector object to access the methods of HandTrackingModule
detector = htm.HandDetector(
    maxHands=1,
    detectionCon=0.5
)



while True:

    success, img = cap.read()


    # Updating the current output device
    devices = AudioUtilities.GetSpeakers()

    volume = devices.EndpointVolume



    img = detector.findHands(img)

    landmark_list = detector.findPosition(
        img,
        handNo=0
    )


    if landmark_list:

        # Get the thumb and index finger tip coordinates  ----> (x1, y1) and (x2, y2) are the coordinates of the thumb and index finger respectively
        x1, y1 = landmark_list[4][1], landmark_list[4][2]
        x2, y2 = landmark_list[8][1], landmark_list[8][2]


        # Calculating the distance between the thumb and index finger, the main tool of this project, it will later help us controlling the sound
        distance = detector.findDistance(
            4,
            8,
            img
        )


        # Mapping the distance value to its equivalent volumen using NumPy methods
        target_vol = np.interp(
            distance,
            [20,100],
            [min_vol, max_vol]
        )


        # Smoothly adjust the volume to avoid sudden changes caused my small hand movements or detection noises
        vol = vol * 0.8 + target_vol * 0.2



        volume.SetMasterVolumeLevel(
            vol,
            None
        )



        vol_percent = np.interp(
            vol, 
            [min_vol, max_vol],
            [0, 100]
        )



        cv2.putText(
            img,
            f"Volume: {int(vol_percent)}%",
            (40, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255, 0, 0),
            3
        )
        

        cv2.rectangle(
            img,
            (50, 100),
            (85, 400),
            (0, 255, 0),
            3
        )



        cv2.rectangle(
            img, 
            (50, int(400-(vol_percent * 3))),
            (85, 400),
            (0, 255, 0),
            cv2.FILLED
        )



        # Drawing the line between the fingers
        cv2.line(
            img,
            (x1, y1),
            (x2, y2),
            (255, 0, 255),
            3
        )



        # Drawing circle on the fingertips specified
        cv2.circle(
            img, 
            (x1, y1),
            10,
            (255, 0, 255),
            cv2.FILLED
        )



        cv2.circle(
            img, 
            (x2, y2),
            10,
            (255, 0, 255),
            cv2.FILLED
        )



        print(distance)



    cv2.imshow(
        "Gesture Volume Control",
        img
    )



    # '0xFF' is used to bring the focus onto the camera window
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break



cap.release()

cv2.destroyAllWindows()
