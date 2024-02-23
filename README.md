
> **Note**
> <br>→ [Kazuhito00/hand-keypoint-classification-model-zoo](https://github.com/Kazuhito00/hand-keypoint-classification-model-zoo)

# hand-gesture-recognition-using-mediapipe
![mqlrf-s6x16](https://user-images.githubusercontent.com/37477845/102222442-c452cd00-3f26-11eb-93ec-c387c98231be.gif)



# Requirements
* mediapipe 0.8.4
* OpenCV 4.6.0.66 or Later
* Tensorflow 2.9.0 or Later
* protobuf <3.20,>=3.9.2
* scikit-learn 1.0.2 or Later 
* matplotlib 3.5.1 or Later

# Demo
sudo docker build -t hand_gesture .

sudo xhost +local: && \
sudo docker run --rm -it \
--device /dev/video0:/dev/video0 \
-v `pwd`:/home/user/workdir \
-v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
--network=host \
-e DISPLAY=$DISPLAY \
hand_gesture:latest

python app.py --device 0

### --privileged

# Directory
<pre>
│  app.py
│  keypoint_classification.ipynb
│  point_history_classification.ipynb
│
├─model
│  ├─keypoint_classifier
│  │  │  keypoint.csv
│  │  │  keypoint_classifier.hdf5
│  │  │  keypoint_classifier.py
│  │  │  keypoint_classifier.tflite
│  │  └─ keypoint_classifier_label.csv
│  │
│  └─point_history_classifier
│      │  point_history.csv
│      │  point_history_classifier.hdf5
│      │  point_history_classifier.py
│      │  point_history_classifier.tflite
│      └─ point_history_classifier_label.csv
│
└─utils
    └─cvfpscalc.py
</pre>


# License
hand-gesture-recognition-using-mediapipe is under [Apache v2 license](LICENSE).
