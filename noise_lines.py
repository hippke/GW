import numpy as np

spacings, offsets, n_min, n_max = np.loadtxt(
    'noise_lines_O2_L1.txt', usecols=[0, 1, 2, 3], unpack=True)
all_lines = []
for idx in range(len(offsets)):
    ns = np.arange(int(n_min[idx]), int(n_max[idx]) + 1, 1)
    all_lines.append(offsets[idx] + ns * spacings[idx])

all_lines = np.sort(np.concatenate(all_lines).ravel())
for line in all_lines:
    print(line)
