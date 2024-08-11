+ Using Python 3.8.10 for installing mediapipe (if u don't want to use mediapipe as 2D pose estimation) u can install python, opencv-python and numpy with latest version. Make sure with multiple python versions let's use virtualenv
+ With pose detection can apply:
    - Mediapipe (GG)
    - OpenPose using CMake
    - PoseNet (via TensorFlow.js)
Some Framework to easily apply for object detection:
1. TensorFlow Object Detection API: This provides several pre-trained models such as SSD (Single Shot MultiBox Detector) and Faster R-CNN. It's quite flexible and can be used with TensorFlow 2.x.
2. Detectron2: Developed by Facebook AI Research, Detectron2 is a powerful library for object detection, segmentation, and other computer vision tasks. It offers models like Faster R-CNN, Mask R-CNN, and RetinaNet.
3. OpenCV with DNN Module: OpenCV's Deep Neural Network (DNN) module supports various pre-trained models for object detection, including SSD and Faster R-CNN. It’s useful if you want to leverage pre-trained models without installing a lot of additional libraries.
4. Haar Cascades: If you’re working on simpler tasks or don't need the performance of more advanced models, Haar cascades can be used for object detection. They are less accurate but easier to set up.
5. YOLO Alternatives: If you're open to alternatives similar to YOLO, you might explore models like EfficientDet, which is designed to be both efficient and accurate.
