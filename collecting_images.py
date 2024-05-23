import cv2
import os
import time

# Directory to save images
save_dir = r'C:\Users\ncai\Desktop\assignment_01_deep_learning\dataset\9'
os.makedirs(save_dir, exist_ok=True)

# Open the default camera
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the interval for capturing images (in seconds)
capture_interval = 0.2
last_capture_time = time.time()

try:
    count = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame
        cv2.imshow('Live Feed', frame)

        # Check if it's time to capture the next image
        current_time = time.time()
        if current_time - last_capture_time >= capture_interval:
            # Save the frame as an image file
            filename = os.path.join(save_dir, f'image_{count:04d}.jpg')
            cv2.imwrite(filename, frame)
            print(f'Saved {filename}')
            last_capture_time = current_time
            count += 1

        # Check for exit key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
