# Industrial Pork Packaging Tray Inspection System

An automated real-time defect detection pipeline using YOLOv8 to inspect pork packaging trays prior to thermal heat-sealing in high-throughput food processing facilities.

---

## Project Overview
In industrial meat processing, raw meat rashers crossing the tray boundary compromise the heat seal, leading to product spoilage, leakage, and costly recalls. This project implements a lightweight deep learning framework (**YOLOv8 Nano**) to inspect $540 \times 540$ RGB camera feeds from conveyor lines, identifying packaging defects and signaling pneumatic actuators for automated rejection.

---

## Key Performance & Dataset Metrics
* **Dataset Size:** ~3,500 annotated packaging tray images
* **Defect Classes:** `loose-meat`, `packaging-error`, `twisted-meat`, `unsealed`, and `wrinkle`
* **Test Accuracy:** **83.75%** overall accuracy achieved
* **Architecture:** YOLOv8 Nano (`yolov8n.pt`) with anchor-free decoupled head
* **Training Setup:** 15 epochs, SGD optimizer ($\eta = 0.01$, momentum $= 0.937$), CIoU + BCE loss

---

## Repository Structure
```text
├── figures/                   # Exported report figures (confusion matrix, predictions, loss curves)
├── runs/                      # Ultralytics YOLOv8 training/validation run outputs
├── datasets/                  # Dataset configuration and directory structure
├── 01_eda.ipynb               # Exploratory Data Analysis and batch generation notebook
├── train.py                   # Model training and hyperparameter configuration script
├── export_figures.py          # Automated figure export script for reporting
├── requirements.txt           # Python dependencies and environment configuration
└── README.md                  # Project documentation