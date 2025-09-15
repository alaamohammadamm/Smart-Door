# Smart Door: An Automated Access System 🚪

This project, developed for the NSF-funded iTest SmartCT program, details a **smart door** that uses a **machine learning model** to grant access only to authorized users. The system identifies authorized individuals or pets in real-time and automatically opens the door for them. 

---

## 🛠️ Hardware & Components

The core of the system is a **4GB Raspberry Pi 4**, which processes the camera's input and controls the door's movement. The mechanical components include:

* **NEMA 17 Stepper Motor:** Provides precise and controlled movement for the door.
* **DRV8825 Stepper Motor Driver Chip:** Manages the stepper motor, allowing the Raspberry Pi to control its speed and direction.
* **Raspberry Pi V2 Camera:** Captures the live video feed for the machine learning model.
* **3D-Printed Structural Components:** All the physical parts, including the **pinion and rack movement system**, were designed and printed in-house.

---

## 💻 Machine Learning Model

The machine learning model was developed using **Google Teachable Machine**, a user-friendly web-based tool for creating custom machine learning models. The model is trained to classify live images from the camera into one of three categories:

1.  **Authorized:** The model recognizes a person or pet with access.
2.  **Unauthorized:** The model identifies a person or pet without access.
3.  **Background:** The model detects no person or pet in front of the door.

For our demonstration, we trained the model to differentiate between different plush toys, with one "pet" being designated as authorized to show the system's functionality.

---

## ⚙️ How It Works

1.  The Raspberry Pi continuously receives a live image feed from the camera.
2.  This image is fed into the machine learning model.
3.  If the model classifies the image as **"Authorized,"** it sends a signal to the DRV8825 driver chip.
4.  The driver chip activates the NEMA 17 stepper motor, which, through the pinion and rack system, opens the door.
5.  After **5 seconds**, the system automatically commands the stepper motor to close the door.
6.  If the model detects an "Unauthorized" person or "Background," no action is taken.

---

## Prototype Diagram

<img width="1920" height="1080" alt="Coral AI Accel" src="https://github.com/user-attachments/assets/b453dbe2-a9a8-4f50-b0a9-51ec7053539e" />


This project showcases an efficient and accessible way to integrate machine learning with robotics, creating a practical and secure automated access system.
