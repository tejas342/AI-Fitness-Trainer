# AI-Fitness-Trainer
![image](https://user-images.githubusercontent.com/86593289/129444651-1d11134c-6caa-4259-85b1-2a44f6ff98a2.png)

It is an AI fitness Trainer which count your number of dumbbell-curls.
# Code
Firstly I made a Module "PoseModule.py", this file contains the code which detects our arm, in this file I have created functions for specific tasks in a class "poseDetector()".

Short description of functions are -

* findPose() - This function detect our pose and show landmarks of our body and it return image in RGB.
* findPosition() - This function finds the position of particular landmark of our body and it returns a list containing *id_of_that_bodyPart, x_position_of_that_bodyPart, y_position_of_that_bodyPart*.
* findAngle() - This function draw landmarks on three points, calculate and return the angle between three given points.

Then another file is "AITrainerProject.py", this file uses that PoseModule and contains the code which shows bar and count the number of curls.

This project is created in Python-3 language using OpenCV and Mediapipe library.
