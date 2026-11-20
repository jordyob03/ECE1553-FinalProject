import torch
import numpy as np
import scipy
import pandas as pd
import matplotlib
import mne

print("Environment verification")
print("------------------------")

print(f"PyTorch: {torch.__version__}")
print(f"NumPy: {np.__version__}")
print(f"SciPy: {scipy.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"MNE: {mne.__version__}")

print(f"CUDA available: {torch.cuda.is_available()}")

# Test a basic PyTorch operation
x = torch.randn(1, 1, 2048)
conv = torch.nn.Conv1d(1, 16, kernel_size=5, padding=2)

output = conv(x)

print(f"\nInput shape: {x.shape}")
print(f"Output shape: {output.shape}")

print("\nEnvironment setup successful!")

