# Development of an Intelligent Interactive Medical Device for Enhanced Respiratory Therapy Using AI and IoT

## Abstract

Incentive spirometers are commonly used for respiratory therapy to encourage deep breathing and lung expansion. However, traditional devices lack real-time feedback, performance tracking, and patient engagement features. This project proposes the development of an intelligent interactive medical system that integrates Artificial Intelligence (AI), Computer Vision, and Internet of Things (IoT) technologies to revolutionize respiratory therapy. The system provides real-time visual feedback, logs therapy sessions, and supports personalized interaction through an intuitive interface and RFID-based patient identification. This innovation aims to improve patient adherence, enable remote monitoring, and ultimately enhance therapy outcomes.

## 1. Introduction

Respiratory therapy plays a vital role in recovery from surgeries, pulmonary diseases, and sedentary lifestyles. Despite the effectiveness of incentive spirometers, their traditional form is limited by passive design and lack of interactivity. Our project introduces a modern alternative: a smart medical device that transforms the incentive spirometer experience using a combination of AI, computer vision, and IoT.

The system is designed around the Raspberry Pi platform and equipped with a camera, touchscreen interface, and RFID reader. It tracks colored balls representing breath strength, delivers instant feedback through a GUI, and records performance metrics for further analysis. Data is stored and visualized in Excel, enabling health professionals to monitor patient progress remotely.

## 2. Problem Statement

Traditional spirometers present several challenges:
- No real-time feedback or correction
- Manual data recording and analysis
- Lack of personalization or progress tracking
- Reduced motivation due to repetitive, non-interactive design

## 3. Objectives

- Develop a color-tracking AI system using computer vision to detect incentive spirometer ball movement
- Provide real-time visual feedback on therapy performance
- Enable RFID-based patient identification
- Log session data and generate automated performance reports
- Improve patient motivation and enable remote healthcare integration

## 4. Methodology

### 4.1 Hardware Components
- Raspberry Pi 4/5
- PiCamera 2
- RFID USB reader
- 7-inch Raspberry Pi touchscreen
- 3D printed case
- Power supply and accessories

### 4.2 Software Tools and Libraries
- Python 3.9+
- OpenCV (for image processing)
- NumPy and Pandas (for data handling)
- Tkinter and PIL (for GUI)
- OpenPyXL (for Excel logging and charting)
- Picamera2 (camera interface)

### 4.3 System Workflow
1. **Calibration**: HSV color ranges for Blue, Orange, and Green balls are set using an interactive calibration tool.
2. **Patient Login**: RFID scan identifies the patient and starts a session.
3. **Real-Time Tracking**: Live video feed detects ball color and position, updates a GUI with dynamic indicators.
4. **Data Logging**: After the session, performance is saved with timestamps and values into an Excel file.
5. **Visualization**: Excel automatically generates a bar chart showing session performance.

## 5. Results and Features

- Real-time tracking of colored balls with visual indicators
- Interactive GUI with patient-specific sessions
- Data saved in Excel format with performance charts
- Single-instance protection using lock file mechanism
- Easy-to-use HSV calibration tool for color detection tuning
- RFID-based session tracking and personalization

## 6. Applications and Impact

This system serves as a low-cost, scalable, and intelligent solution for:
- Home-based respiratory therapy
- Post-operative recovery monitoring
- Pediatric and elderly care where engagement is critical
- Integration with digital health records in hospitals and clinics

## 7. Files and Structure

```bash
respiratory-therapy-ai-iot/
├── 
│   └── respiratory_therapy.py          # Main therapy system
├── 
│   └── color_calibration.py            # HSV calibration interface
├── 
│   └── HSV.data                        # Saved color thresholds
├── 
│   ├── qstss.png                       # School logo
│   ├── moe.png                         # Ministry logo
│   └── example_output.xlsx             # Example data output
├── README.md                           # This document
├── requirements.txt                    # Python dependencies
└── LICENSE                             # License file
```

## 8. Installation

### 8.1 Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/respiratory-therapy-ai-iot.git
cd respiratory-therapy-ai-iot
```

### 8.2 Install Dependencies
```bash
pip install -r requirements.txt
```

### 8.3 Run Color Calibration Tool
```bash
python calibration/color_calibration.py
```

### 8.4 Start the Main Application
```bash
python main_app/respiratory_therapy.py
```

## 9. Limitations and Future Work

### Current Limitations:
- Requires calibration in different lighting conditions
- Limited to detecting predefined HSV color ranges
- No cloud integration yet

### Future Enhancements:
- Add AI model to classify performance automatically
- Integrate with cloud-based dashboards and APIs
- Add audio feedback for accessibility

## 10. References

1. NuvoAir Digital Spirometer – https://www.nuvoair.com  
2. Masimo SafetyNet – https://www.masimo.com/products/safetynet  
3. Raspberry Pi Documentation – https://www.raspberrypi.com/documentation  
4. OpenCV Library – https://opencv.org  

## 11. License

This project is licensed under the MIT License – see the `LICENSE` file for details.

## 12. Acknowledgments

- Qatar Science and Technology Secondary School for Boys (QSTSS)  
- Ministry of Education and Higher Education  
- Students: [Insert student names]  
- Supervisor: Dr. Mohammed Salameh  
