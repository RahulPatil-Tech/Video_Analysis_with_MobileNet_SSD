# Video Analysis with MobileNet SSD

This project demonstrates video analysis using the MobileNet SSD (Single Shot MultiBox Detector) model. The model is used to detect and classify objects in a video stream.

## Prerequisites

- Python 3.6 or higher
- OpenCV (cv2) library
- Pre-trained MobileNet SSD model (`MobileNetSSD_deploy.prototxt` and `MobileNetSSD_deploy.caffemodel`)
- Video file for analysis

## Installation

1. Clone the repository:

```shell
git clone https://github.com/RahulPatil-Tech/Video_Analysis_with_MobileNet_SSD.git
```

2. Install the required dependencies:

```shell
pip install opencv-python
```

3. Download the pre-trained MobileNet SSD model files (MobileNetSSD_deploy.prototxt and MobileNetSSD_deploy.caffemodel) and place them in the project directory.

# Usage
1. Run the script:

```shell
python video_analysis.py
```

2. The script will process the video frame by frame, detect objects using the MobileNet SSD model, and display the detected class and confidence on each frame.

3. Press the 'q' key to stop the analysis and close the window.

4. The annotated video will be saved as output_video.avi in the project directory.

# Customization
1. To modify the list of classes, update the classes list in the code (['background', 'dancing', 'cleaning', 'cooking', ...]) to match your specific use case.

2. You can adjust the confidence threshold for detection by modifying the value 0.5 in the code (if confidence > 0.5).

3. To resize the output frame, change the dimensions in the code (frame = cv2.resize(frame, (640, 480))) to your desired size.

# License
This project is licensed under the MIT License.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Acknowledgements
1. The MobileNet SSD model is based on the work by Howard, A.G. et al., "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications", arXiv:1704.04861 (2017).

2. This project utilizes the OpenCV library for video analysis.

# Contact
If you have any questions, suggestions, or issues, feel free to contact the project maintainer at rp3252154@gmail.com.
