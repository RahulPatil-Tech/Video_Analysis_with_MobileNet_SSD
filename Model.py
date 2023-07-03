import cv2

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Define the classes
classes = ['background', 'weapons', 'cleaning', 'cooking', 'carrying flammable objects', 'fighting', 'theft',
           'fall', 'shouting', 'dancing', 'baby crying']

# Open the video file
video_file = 'Dataset.mp4'
cap = cv2.VideoCapture(video_file)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Define the output video file in AVI format
output_file = 'output_video.avi'

# Get the original frame dimensions
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a video writer in AVI format
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(output_file, fourcc, 30.0, (frame_width, frame_height))

# Read frames from the video
while True:
    # Read the next frame
    ret, frame = cap.read()

    # Break the loop if no more frames are available
    if not ret:
        break

    # Resize the frame to a fixed size
    frame = cv2.resize(frame, (640, 480))

    # Create a blob from the frame
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)

    # Set the input to the pre-trained model
    net.setInput(blob)

    # Run forward pass through the network
    detections = net.forward()

    # Process the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])

            # Check if the class is one of the specified classes
            if class_id < len(classes):
                class_name = classes[class_id]
                print(f"Detected class: {class_name}, Confidence: {confidence}")

                # Draw class label and confidence on the frame
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Write the annotated frame to the output video file
    out.write(frame)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and video writer, and close windows
cap.release()
out.release()
cv2.destroyAllWindows()
