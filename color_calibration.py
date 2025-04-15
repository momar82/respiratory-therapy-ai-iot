import cv2
import numpy as np
from picamera2 import Picamera2

def nothing(x):
    pass

# Initialize camera
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(
    main={"size": (640, 480), "format": "RGB888"}
)
picam2.configure(preview_config)
picam2.start()

# Create windows for each color
cv2.namedWindow('Original')
cv2.namedWindow('Blue Ball')
cv2.namedWindow('Orange Ball')
cv2.namedWindow('Green Ball')

# Create trackbars for Blue ball
cv2.createTrackbar('H min', 'Blue Ball', 94, 179, nothing)
cv2.createTrackbar('H max', 'Blue Ball', 126, 179, nothing)
cv2.createTrackbar('S min', 'Blue Ball', 80, 255, nothing)
cv2.createTrackbar('S max', 'Blue Ball', 255, 255, nothing)
cv2.createTrackbar('V min', 'Blue Ball', 2, 255, nothing)
cv2.createTrackbar('V max', 'Blue Ball', 255, 255, nothing)

# Create trackbars for Orange ball
cv2.createTrackbar('H min', 'Orange Ball', 4, 179, nothing)
cv2.createTrackbar('H max', 'Orange Ball', 25, 179, nothing)
cv2.createTrackbar('S min', 'Orange Ball', 100, 255, nothing)
cv2.createTrackbar('S max', 'Orange Ball', 255, 255, nothing)
cv2.createTrackbar('V min', 'Orange Ball', 20, 255, nothing)
cv2.createTrackbar('V max', 'Orange Ball', 255, 255, nothing)

# Create trackbars for Green ball
cv2.createTrackbar('H min', 'Green Ball', 23, 179, nothing)
cv2.createTrackbar('H max', 'Green Ball', 100, 179, nothing)
cv2.createTrackbar('S min', 'Green Ball', 42, 255, nothing)
cv2.createTrackbar('S max', 'Green Ball', 255, 255, nothing)
cv2.createTrackbar('V min', 'Green Ball', 0, 255, nothing)
cv2.createTrackbar('V max', 'Green Ball', 255, 255, nothing)

print("Instructions:")
print("1. Adjust the trackbars to get the best detection for each ball")
print("2. Show one ball at a time and adjust its values")
print("3. Press 's' to save the values")
print("4. Press 'q' to quit")
print("\nCurrent values will be displayed in the terminal")

try:
    while True:
        # Capture frame
        frame = picam2.capture_array()
        frame = cv2.flip(frame, 1)  # Mirror effect
        
        # Crop frame to match the main application
        cropped_frame = frame[0:352, 116:430]
        
        # Convert to HSV
        blurred = cv2.GaussianBlur(cropped_frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        # Get trackbar positions for each color
        # Blue
        blue_hmin = cv2.getTrackbarPos('H min', 'Blue Ball')
        blue_hmax = cv2.getTrackbarPos('H max', 'Blue Ball')
        blue_smin = cv2.getTrackbarPos('S min', 'Blue Ball')
        blue_smax = cv2.getTrackbarPos('S max', 'Blue Ball')
        blue_vmin = cv2.getTrackbarPos('V min', 'Blue Ball')
        blue_vmax = cv2.getTrackbarPos('V max', 'Blue Ball')
        
        # Orange
        orange_hmin = cv2.getTrackbarPos('H min', 'Orange Ball')
        orange_hmax = cv2.getTrackbarPos('H max', 'Orange Ball')
        orange_smin = cv2.getTrackbarPos('S min', 'Orange Ball')
        orange_smax = cv2.getTrackbarPos('S max', 'Orange Ball')
        orange_vmin = cv2.getTrackbarPos('V min', 'Orange Ball')
        orange_vmax = cv2.getTrackbarPos('V max', 'Orange Ball')
        
        # Green
        green_hmin = cv2.getTrackbarPos('H min', 'Green Ball')
        green_hmax = cv2.getTrackbarPos('H max', 'Green Ball')
        green_smin = cv2.getTrackbarPos('S min', 'Green Ball')
        green_smax = cv2.getTrackbarPos('S max', 'Green Ball')
        green_vmin = cv2.getTrackbarPos('V min', 'Green Ball')
        green_vmax = cv2.getTrackbarPos('V max', 'Green Ball')
        
        # Create masks for each color
        blue_mask = cv2.inRange(hsv, np.array([blue_hmin, blue_smin, blue_vmin]),
                               np.array([blue_hmax, blue_smax, blue_vmax]))
        orange_mask = cv2.inRange(hsv, np.array([orange_hmin, orange_smin, orange_vmin]),
                                 np.array([orange_hmax, orange_smax, orange_vmax]))
        green_mask = cv2.inRange(hsv, np.array([green_hmin, green_smin, green_vmin]),
                                np.array([green_hmax, green_smax, green_vmax]))
        
        # Apply morphological operations
        kernel = np.ones((5, 5), np.uint8)
        blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        orange_mask = cv2.morphologyEx(orange_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        orange_mask = cv2.morphologyEx(orange_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        
        # Show the original and masked images
        cv2.imshow('Original', cropped_frame)
        cv2.imshow('Blue Ball', blue_mask)
        cv2.imshow('Orange Ball', orange_mask)
        cv2.imshow('Green Ball', green_mask)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            # Save the values
            print("\nCurrent HSV Values:")
            print("Blue Ball:")
            print(f"    'lower': np.array([{blue_hmin}, {blue_smin}, {blue_vmin}]),")
            print(f"    'upper': np.array([{blue_hmax}, {blue_smax}, {blue_vmax}])")
            print("\nOrange Ball:")
            print(f"    'lower': np.array([{orange_hmin}, {orange_smin}, {orange_vmin}]),")
            print(f"    'upper': np.array([{orange_hmax}, {orange_smax}, {orange_vmax}])")
            print("\nGreen Ball:")
            print(f"    'lower': np.array([{green_hmin}, {green_smin}, {green_vmin}]),")
            print(f"    'upper': np.array([{green_hmax}, {green_smax}, {green_vmax}])")

            # Save to HSV.data using numpy savez
            np.savez('HSV.data',
                blue_lower=np.array([blue_hmin, blue_smin, blue_vmin]),
                blue_upper=np.array([blue_hmax, blue_smax, blue_vmax]),
                orange_lower=np.array([orange_hmin, orange_smin, orange_vmin]),
                orange_upper=np.array([orange_hmax, orange_smax, orange_vmax]),
                green_lower=np.array([green_hmin, green_smin, green_vmin]),
                green_upper=np.array([green_hmax, green_smax, green_vmax])
            )
            print("\nHSV values saved to HSV.data!")
            
finally:
    # Cleanup
    picam2.stop()
    cv2.destroyAllWindows() 
