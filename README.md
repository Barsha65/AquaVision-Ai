#  AquaVision AI

> **Intelligent Underwater Image Enhancement and Real-Time Marine Object Detection System**

AquaVision AI is a computer vision system that investigates whether **underwater image enhancement can improve downstream marine object detection**.

The system combines image preprocessing, underwater image enhancement, and YOLO-based object detection into an end-to-end pipeline.

```text
Underwater Image
       ↓
Preprocessing
       ↓
Image Enhancement
       ↓
Enhanced Image
       ↓
YOLO Object Detection
       ↓
Bounding Boxes + Classes + Confidence
       ↓
Visualization & Evaluation
```

---

## ✨ Features

* 🌊 Underwater image preprocessing
* 🎨 Color correction using Gray-World White Balance
* 🔆 Contrast enhancement using CLAHE
* 🎯 YOLO-based underwater object detection
* 🐟 Detection of multiple marine object categories
* 📊 Quantitative image enhancement evaluation
* 📈 Object detection evaluation using standard detection metrics
* ⚡ Inference latency and FPS measurement
* 🔬 Raw vs enhanced image detection comparison
* 🌐 Web-based inference interface *(in development)*

---

##  Research Focus

The primary objective is to determine whether image enhancement improves the performance of downstream object detection.

Two pipelines are evaluated under controlled conditions:

### Raw → YOLO

```text
Raw Image → YOLO → Detection
```

### Enhanced → YOLO

```text
Raw Image → Enhancement → YOLO → Detection
```

The comparison focuses on both **detection performance** and the **computational overhead introduced by enhancement**.

No experimental performance values are reported until they are obtained from actual experiments.

---

## 📊 Evaluation

### Image Enhancement

The enhancement stage is evaluated using:

* PSNR
* SSIM
* UIQM
* UCIQE

### Object Detection

The detection stage is evaluated using:

* Precision
* Recall
* F1-score
* mAP@0.5
* mAP@0.5:0.95
* Inference latency
* FPS

---

##  Datasets

### Enhancement

The project investigates:

* **UIEB** — Underwater Image Enhancement Benchmark
* **EUVP** — Enhancing Underwater Visual Perception

### Object Detection

The current detection experiments use **RUOD (Real-world Underwater Object Detection)**.

Prepared YOLO dataset:

| Split      |     Images |     Labels |
| ---------- | ---------: | ---------: |
| Train      |      9,800 |      9,800 |
| Validation |      4,200 |      4,200 |
| **Total**  | **14,000** | **14,000** |

### RUOD Classes

```text
holothurian
echinus
scallop
starfish
fish
corals
diver
cuttlefish
turtle
jellyfish
```

Dataset files are not included in this repository.

---

## 🤖 Object Detection

AquaVision currently uses the **YOLO family of object detectors**.

The current baseline uses a lightweight pretrained YOLO model fine-tuned on the prepared RUOD dataset.

The detection pipeline is being developed with an emphasis on balancing:

* Detection accuracy
* Inference speed
* Model size
* Deployment feasibility

---

## 🛠️ Technology Stack

### Machine Learning & Computer Vision

* Python
* PyTorch
* Ultralytics YOLO
* OpenCV
* NumPy

### Development

* Jupyter / Google Colab
* Git
* GitHub

### Application

* FastAPI *(backend in development)*
* Web frontend *(in development)*

---

## 📁 Project Structure

```text
AquaVision-Ai/
│
├── app/                    # Application layer
│
├── assets/
│   ├── architecture/      # Architecture diagrams
│   └── screenshots/       # Project screenshots
│
├── configs/               # Experiment configurations
│
├── data/                  # Dataset metadata and documentation
│
├── docs/                  # Project documentation
│
├── experiments/
│   └── results/            # Experimental results
│
├── models/                 # Model-related files and references
│
├── notebooks/              # Exploration and analysis notebooks
│
├── scripts/                # Dataset and experiment scripts
│
├── src/
│   └── aquavision/
│       ├── data/           # Dataset handling
│       ├── detection/      # Object detection
│       ├── enhancement/    # Image enhancement
│       ├── evaluation/    # Evaluation metrics
│       ├── preprocessing/  # Image preprocessing
│       └── utils/          # Utility functions
│
├── tests/                  # Tests
│
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Barsha65/AquaVision-Ai.git
cd AquaVision-Ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the project

```bash
pip install -e .
```

> Dataset setup and model-specific instructions are being documented alongside the corresponding experiments.

---

## 🧪 Current Development Status

| Component                        | Status |
| -------------------------------- | ------ |
| Project structure                | ✅      |
| Enhancement preprocessing        | ✅      |
| Gray-World + CLAHE baseline      | ✅      |
| RUOD dataset conversion          | ✅      |
| YOLO dataset preparation         | ✅      |
| YOLO baseline training           | 🔄     |
| Enhancement + detection pipeline | ⏳      |
| Raw vs enhanced evaluation       | ⏳      |
| FastAPI inference API            | ⏳      |
| Web interface                    | ⏳      |

---

## Trained Model Checkpoint

AquaVision uses a trained YOLO model for underwater marine-object detection. The model weights are distributed separately from the source code and are not committed to this repository.

### Download the Model

1. Download `best.pt` from the team's Google Drive: **[Download trained model](https://drive.google.com/file/d/1Dc5yFIdIWsbKuW_qDgmMveYGofvsKnqu/view?usp=drive_link)**.
2. Create the `models` directory in the repository if it does not already exist.
3. Place the downloaded checkpoint at:

   `models/best.pt`

### Important Notes

- The trained checkpoint is required to run object detection.
- Dataset files and trained model weights are maintained separately from the source repository.
- Do not commit model checkpoints, datasets, virtual environments, or generated training outputs.

## 📌 Project Principles

* **No fabricated results** — metrics are reported only from completed experiments.
* **Reproducible experiments** — configurations and processing steps are tracked.
* **Baseline first** — simple approaches are evaluated before adding complexity.
* **Downstream performance matters** — visually improved images are not automatically considered better if detection performance does not improve.
* **Large artifacts stay outside Git** — datasets, model weights, virtual environments, and generated outputs are excluded from version control.

---

