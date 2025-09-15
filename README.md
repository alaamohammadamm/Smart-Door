# Smart Door: A STEM Education Project 🚪

This project, developed for the **NSF-funded iTest SmartCT program**, serves as a demonstration tool to teach **K-12 students** about the power and practical applications of **machine learning**. It's an automated access system that uses a computer vision model to open a door only for authorized users. 

***

## 🛠️ Hardware & Components

The system is built on a **4GB Raspberry Pi 4** and uses several key components to function:

* **NEMA 17 Stepper Motor:** Controls the precise movement of the door.
* **DRV8825 Stepper Motor Driver Chip:** An interface that allows the Raspberry Pi to control the motor.
* **Raspberry Pi V2 Camera:** Captures live video footage for the machine learning model.
* **3D-Printed Structural Components:** The frame and the **pinion and rack movement system** were all custom-designed and printed.

***

## 💻 How It Teaches Machine Learning

The core educational component is the machine learning model, created using **Google Teachable Machine**. This platform simplifies the process of training a model for students. The model is trained to classify images into three categories:

* **Authorized:** Allows access.
* **Unauthorized:** Denies access.
* **Background:** No person or animal is present.

For the classroom demonstration, the model is trained to identify and grant access to a specific plush toy, illustrating how an AI can be trained to recognize patterns and make decisions based on data.

***

## ⚙️ The System in Action

1.  The Raspberry Pi's camera continuously feeds images to the machine learning model.
2.  The model classifies the image.
3.  If an **"Authorized"** subject is detected, the Raspberry Pi signals the motor to open the door for **5 seconds**.
4.  The door then closes automatically, completing the cycle.

This hands-on project allows students to see the concepts of artificial intelligence and robotics come to life, from data collection and model training to physical automation.
