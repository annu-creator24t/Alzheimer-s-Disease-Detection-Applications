# Alzheimer’s Disease Detection Platform

A modern, multi-page Streamlit healthcare application designed as a clinical screening and patient support prototype for Alzheimer's disease management. The platform combines interactive cognitive screening, longitudinal tracking dashboards, caregiver alerts, and clinical workflow interfaces with custom healthcare-themed UI styling.

---

## 📌 Project Overview

This repository hosts the **frontend and application layer prototype** of an Alzheimer's Disease Detection and Care Management System. The application provides dedicated interfaces for patients, clinicians, and caregivers to explore diagnostic screening workflows, monitor cognitive health indicators, and manage daily care routines.

### Key Application Modules:
- **Landing Portal ([`App.py`](App.py))**: Platform overview featuring key diagnostic benchmarks and navigation shortcuts.
- **Login Portal ([`pages/1_Login.py`](pages/1_Login.py))**: Role-based access selection for Patients, Doctors, and Caregivers.
- **Cognitive Assessment ([`pages/2_Cognitive_Test.py`](pages/2_Cognitive_Test.py))**: An interactive 6-stage clinical screening tool evaluating Orientation, Word Encoding, Attention (Serial 7s), Word Recall, Language/Reasoning, and Visuospatial abilities.
- **AI Detection Interface ([`pages/3_AI_Detecton.py`](pages/3_AI_Detecton.py))**: An upload interface for neuroimaging scans (MRI/PET) with simulated risk scoring and downloadable clinical summaries.
- **Patient Dashboard ([`pages/4_Dashboard.py`](pages/4_Dashboard.py))**: Longitudinal risk tracking and appointment history visualization.
- **Caregiver Panel ([`pages/5_Caregiver_Panel.py`](pages/5_Caregiver_Panel.py))**: Remote patient monitoring, alert dispatching to physicians, and status tracking.
- **Medication Reminder ([`pages/6_Medication_Reminder.py`](pages/6_Medication_Reminder.py))**: Daily prescription scheduler and adherence checklist.
- **Emergency Support ([`pages/7_Emergency.py`](pages/7_Emergency.py))**: Rapid SOS contact directory and emergency response triggers.
- **About ([`pages/8_About.py`](pages/8_About.py))**: System background and feature summary.

---

## 🔬 Associated Research Work

This application is conceptualized alongside research on deep learning-based Alzheimer's disease classification using structural brain MRI scans.

### Research Summary (Reported in Associated Study):
* **Task**: 4-class stage classification of Alzheimer's Disease (Non-Demented, Very Mild Demented, Mild Demented, Moderate Demented).
* **Dataset**: Approximately 44,000 brain MRI slices evaluated across preprocessed structural neuroimaging datasets.
* **Architecture Comparison**: Evaluation of transfer learning architectures including **ResNet50**, **EfficientNetB4**, **InceptionV3**, and **MobileNetV2**.
* **Methodology**: Two-stage transfer learning pipeline involving initial feature extraction followed by selective fine-tuning on a stratified 70/30 train/test split.
* **Reported Research Results**:
  * **ResNet50 Test Accuracy**: **89.96%**
  * **ResNet50 Macro F1-Score**: **0.90**

> [!NOTE]
> **Important Distinction**: The metrics and transfer-learning models described above represent the **experimental findings of the associated research paper**. The current repository contains the **Streamlit web application interface and cognitive assessment prototype**; it does not host the raw 44,000 image dataset or deep-learning training scripts.

---

## 🚀 Current Application Features

| Module | Implementation Status | Description |
| :--- | :--- | :--- |
| **Cognitive Screening** | Functional Logic | 6-stage interactive test calculating domain scores (max 22 points) and risk categorization. |
| **Scan Upload UI** | Prototype Interface | Accepts MRI/PET scan files and patient demographics for diagnostic intake. |
| **Risk Prediction** | Demo / Mock Engine | Generates risk percentage and stage categorization (`Normal`, `Mild`, `Severe`) via simulation utility. |
| **Explainability Heatmap** | UI Placeholder | Demonstrates UI placement for future Grad-CAM visual attention maps. |
| **Report Generation** | Functional Utility | Generates base64-encoded downloadable clinical text reports. |
| **Patient Dashboard** | Dynamic Prototype | Plots risk progression trends and appointment timelines using Pandas & NumPy. |
| **Caregiver & SOS** | UI Workflow | Provides alert notifications, physician contact directory, and medication schedules. |
| **Design System** | Custom Styling | Dedicated [style.css](style.css) theme with responsive cards, progress tracks, and clean typography. |

---

## 🛠️ Technology Stack

The codebase relies strictly on the following technologies:

- **Python 3.10+**: Core programming language.
- **Streamlit**: Multi-page web application framework.
- **Pandas**: Data handling and tabular time-series structures.
- **NumPy**: Numerical arrays and random series generation for dashboard visualization.
- **Vanilla CSS3**: Custom styles for cards, hero banners, badges, and layout enhancements.
- **TOML**: Streamlit configuration settings (`.streamlit/config.toml`).

---

## 📁 Repository Structure

```
Alzheimer-Detection/
│
├── .streamlit/
│   └── config.toml               # Streamlit light theme styling
│
├── pages/
│   ├── 1_Login.py                # Role-based login portal
│   ├── 2_Cognitive_Test.py       # 6-stage clinical cognitive assessment
│   ├── 3_AI_Detecton.py          # Scan upload & AI detection interface
│   ├── 4_Dashboard.py            # Longitudinal risk visualizer
│   ├── 5_Caregiver_Panel.py      # Caregiver monitoring & doctor alerts
│   ├── 6_Medication_Reminder.py  # Daily medication schedule tracker
│   ├── 7_Emergency.py            # Emergency contacts and SOS trigger
│   └── 8_About.py                # Application background & features
│
├── App.py                        # Application homepage & navigation hub
├── style.css                     # Custom CSS design system
├── utils.py                      # Helper utilities, styling loader & demo logic
├── requirements.txt              # Core Python dependencies
├── .gitignore                    # Git ignore specifications
└── README.md                     # Project documentation
```

---

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Anviksha797/Alzheimer-Detection.git
cd Alzheimer-Detection
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Or manually install: `pip install streamlit pandas numpy`)*

### 4. Run the Streamlit Application
```bash
streamlit run App.py
```

The application will open in your default browser at `http://localhost:8501`.

---

## ⚠️ Limitations

- **Prototype Scope**: This repository serves as a front-end application layer and clinical workflow prototype.
- **Simulated Inference**: The neuroimaging detection page currently uses demo scoring logic and placeholder heatmap graphics.
- **Model Weights**: Deep-learning model weights (`.h5`, `.keras`, `.pt`) and large-scale training pipelines are not bundled in this web repository.
- **Non-Diagnostic Notice**: This application is built for academic demonstration and screening workflow prototyping; it is **not** a certified medical diagnostic device.

---

## 🔮 Future Work

- [ ] **Model Weight Integration**: Deploying the pre-trained ResNet50 / EfficientNetB4 inference models for direct neuroimaging classification.
- [ ] **Dynamic Grad-CAM**: Integrating real-time convolutional activation map generation for visual scan explainability.
- [ ] **Secure Database Backend**: Connecting user authentication and longitudinal records to a secure HIPAA/GDPR-compliant database.
- [ ] **Independent Dataset Validation**: Validating end-to-end inference across diverse clinical cohorts.
