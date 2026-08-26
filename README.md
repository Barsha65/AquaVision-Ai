# AquaVision AI

## Intelligent Underwater Image Enhancement and Real-Time Marine Object Detection System

AquaVision AI is a project that investigates whether underwater image enhancement can improve downstream marine object detection.

The system is designed as an end-to-end computer vision pipeline:

```text
Underwater Image / Frame
        ↓
   Preprocessing
        ↓
  Image Enhancement
        ↓
   Enhanced Image
        ↓
 YOLO Object Detection
        ↓
Bounding Boxes + Classes
        ↓
  Confidence Scores
        ↓
Visualization & Evaluation
```

---

## Research Question

> **Does underwater image enhancement improve downstream marine object detection, and what is the trade-off between detection performance and computational latency?**

The project will compare object detection performance on raw underwater images against enhanced underwater images using controlled experiments.

---

## Project Status

🚧 **Under active development**

The final enhancement model, object detection dataset, model configuration, and experimental results will be determined through systematic evaluation.

No performance results are reported until they are obtained from actual experiments.

---

## Objectives

The project aims to:

- Enhance degraded underwater images.
- Detect and classify marine objects using a YOLO-based detector.
- Evaluate image enhancement quantitatively.
- Evaluate object detection quantitatively.
- Compare detection on raw and enhanced images.
- Measure the computational overhead introduced by enhancement.
- Develop a reproducible inference pipeline.
- Provide a web-based demonstration application.

---

## Research Question

Does underwater image enhancement improve downstream marine object detection?

We will investigate this through two controlled pipelines.

### Experiment A — Raw Images

```text
Raw Underwater Image
        ↓
      YOLO
        ↓
Detection Results
```

### Experiment B — Enhanced Images

```text
Raw Underwater Image
        ↓
   Enhancement
        ↓
Enhanced Image
        ↓
      YOLO
        ↓
Detection Results
```

The two pipelines will be compared using detection accuracy and computational performance.

---

## Evaluation

### Image Enhancement

The enhancement stage will be evaluated using:

- PSNR
- SSIM
- UIQM
- UCIQE

### Object Detection

The detection stage will be evaluated using:

- Precision
- Recall
- F1-score
- mAP@0.5
- mAP@0.5:0.95
- Inference latency
- FPS

### Downstream Comparison

The primary experiment will compare:

| Metric | Raw → YOLO | Enhanced → YOLO |
|---|---:|---:|
| Precision | TBD | TBD |
| Recall | TBD | TBD |
| F1-score | TBD | TBD |
| mAP@0.5 | TBD | TBD |
| mAP@0.5:0.95 | TBD | TBD |
| FPS | TBD | TBD |
| Latency | TBD | TBD |

**TBD values will only be replaced after actual experiments are performed.**

---

## Datasets

### Image Enhancement

The project currently investigates:

- UIEB — Underwater Image Enhancement Benchmark
- EUVP — Enhancing Underwater Visual Perception

Dataset setup instructions will be documented separately.

### Object Detection

The project is currently evaluating underwater object detection datasets including:

- URPC
- RUOD

The final detection dataset will be selected after examining:

- Dataset size
- Image quality
- Object classes
- Annotation quality
- Annotation format
- Class distribution
- Train/validation/test splits
- Licensing and usage conditions
- Suitability for the research question

---

## Enhancement Models

The project will investigate a combination of traditional and deep-learning approaches.

### Traditional Baselines

- White Balance
- CLAHE

### Deep Learning

Water-Net is currently a primary candidate for evaluation.

Additional enhancement models may be considered if they provide a meaningful experimental comparison and remain feasible within the project deadline.

The final model will be selected based on:

- Dataset compatibility
- Reproducibility
- Availability of implementation and pretrained weights
- Enhancement quality
- Computational requirements
- Downstream detection performance
- Development time

---

## Object Detection

The project will use a YOLO-family object detector.

A lightweight pretrained model will be preferred where appropriate to balance:

- Detection accuracy
- Inference speed
- Model size
- GPU requirements
- Deployment feasibility

The detector will be fine-tuned on the selected underwater object detection dataset.

---

## Project Structure

```text
AquaVision-Ai/
│
├── app/                    # Web application
│
├── assets/
│   ├── architecture/      # Architecture diagrams
│   └── screenshots/       # Application/project screenshots
│
├── configs/               # Experiment and model configurations
│
├── data/                  # Dataset documentation and metadata
│
├── docs/                  # Project documentation
│
├── experiments/
│   └── results/           # Experimental results
│
├── models/                # Model documentation/references
│
├── notebooks/             # Exploration and analysis notebooks
│
├── scripts/               # Command-line training/evaluation scripts
│
├── src/
│   └── aquavision/
│       ├── data/          # Dataset handling
│       ├── detection/     # Object detection
│       ├── enhancement/   # Image enhancement
│       ├── evaluation/    # Evaluation metrics
│       ├── preprocessing/ # Image preprocessing
│       └── utils/         # Shared utilities
│
└── tests/                 # Automated tests
```

---

## Technology Stack

The project is expected to use technologies including:

- Python
- PyTorch
- OpenCV
- YOLO
- NumPy
- Jupyter
- Git
- GitHub

The final application framework will be selected during the application-development phase.

---

## Installation

Installation instructions will be added after the project environment and dependencies are finalized.

---

## Dataset Setup

Datasets are **not stored inside this Git repository**.

Users will be provided with instructions for obtaining the required datasets from their respective public sources.

Large datasets, model checkpoints, generated outputs, and other large files will not be committed to the repository unnecessarily.

---

## Experiments

Experiments will be tracked using reproducible configurations and result records.

Each experiment should record information such as:

- Experiment ID
- Dataset
- Dataset split
- Model
- Preprocessing
- Hyperparameters
- Training configuration
- Hardware
- Evaluation metrics
- Inference latency
- Observations

---

## Results

Results will be added only after running the corresponding experiments.

No experimental performance values are fabricated or estimated.

---

## Limitations

Known limitations and constraints will be documented as the project develops.

These may include:

- Dataset limitations
- Generalization to unseen underwater environments
- Computational requirements
- Enhancement artifacts
- Detection failures
- Real-time performance limitations

---

## Future Work

Potential future improvements will be documented separately from currently implemented functionality.

Possible directions may include additional enhancement models, detector architectures, deployment optimization, and broader underwater datasets.

---

## Team

**AquaVision AI Team**

- Barsha Gupta
- Pruthviraj
- Soham
- Manasi

### Guide

**Prof. Ashwini Chavan**

---

## Academic Project

This project is being developed as a B.Tech Computer Science and Engineering capstone project.


---

## Acknowledgements

Dataset and model acknowledgements, citations, and source references will be added as the corresponding components are finalized.

---

## License

License information will be finalized after reviewing the licensing conditions of the datasets, models, and dependencies used in the project.