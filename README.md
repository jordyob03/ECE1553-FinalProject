
# EEG Motion Artifact Denoising

## Overview

This project investigates lightweight deep learning
architectures for removing motion artifacts from EEG
signals using movement information from inertial sensors.

The objective is to determine whether incorporating
movement information and adaptive feature fusion can
improve EEG denoising while maintaining computational
efficiency for potential wearable applications.

## Models

Three architectures will be investigated:

1. EEG-only CNN
2. EEG + IMU CNN
3. Motion-Adaptive CNN

## Dataset

The project initially uses the publicly available
Motion Artifact Contaminated fNIRS and EEG dataset
from PhysioNet.

Dataset:
https://physionet.org/content/motion-artifact/1.0.0/

## Technologies

- Python
- PyTorch
- NumPy
- SciPy
- Pandas
- MNE
- Matplotlib
- JupyterLab

## Setup

Clone the repository:

```bash
git clone <repository-url>
```

Create and activate the environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Register the Jupyter kernel:

```bash
python -m ipykernel install --user \
    --name eeg-denoising \
    --display-name "Python (EEG Denoising)"
```
