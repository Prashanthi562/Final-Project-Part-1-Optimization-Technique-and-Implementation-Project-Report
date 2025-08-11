## Description:The standardization of this operation is done by dividing every detail in the list or array by the highest absolute value. It makes all of the resulting values to be in the -1 to 1 range providing consistent scaling.

import numpy as np
import time
import matplotlib.pyplot as plt

# Data setup
# Setting the total number of data points
N = 2_000_000

# Creating arrays to store x, y, z values for each point
xs = np.empty(N, dtype=np.float64)
ys = np.empty(N, dtype=np.float64)
zs = np.empty(N, dtype=np.float64)

# Filling the arrays with calculated values
for i in range(N):
    xs[i] = i * 0.001
    ys[i] = i * 0.002
    zs[i] = i * 0.003

# Defining a process for adding values from all three arrays one by one
def aos_sum():
    s = 0.0
    for i in range(N):
        s += xs[i] + ys[i] + zs[i]
    return s

# Creating arrays for x, y, z values stored separately
x = np.arange(N, dtype=np.float64) * 0.001
y = np.arange(N, dtype=np.float64) * 0.002
z = np.arange(N, dtype=np.float64) * 0.003

# Defining a process for adding all x, y, z values together in bulk
def soa_sum():
    return np.sum(x + y + z)

# Timing the approaches
# Running both processes once for warming up
_ = aos_sum()
_ = soa_sum()

# Measuring time for the record-based process
t0 = time.perf_counter()
_ = aos_sum()
t1 = time.perf_counter()

# Measuring time for the separate-arrays process
_ = soa_sum()
t2 = time.perf_counter()

aos_time = t1 - t0
soa_time = t2 - t1

# Displaying time taken by both processes
print("Record-based time:", aos_time)
print("Separate-arrays time:", soa_time)

# Plotting the performance chart
methods = ['Array of Structures (AoS)', 'Structure of Arrays (SoA)']
times = [aos_time, soa_time]

plt.figure(figsize=(6,4))
bars = plt.bar(methods, times, color=['#FF6F61', '#6B8E23'])
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison: AoS vs SoA')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding text labels on bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f"{bar.get_height():.4f}s", ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("performance_comparison.png", dpi=300)
plt.show()

# Generating a simple AoS vs SoA layout diagram
fig, axes = plt.subplots(1, 2, figsize=(8, 3))

# AoS layout (grouped by entity)
aos_data = [["x1","y1","z1"], ["x2","y2","z2"], ["x3","y3","z3"]]
for row_idx, row in enumerate(aos_data):
    for col_idx, val in enumerate(row):
        axes[0].text(col_idx, -row_idx, val, ha='center', va='center',
                     bbox=dict(boxstyle='round', facecolor='#FFDDC1', edgecolor='black'))

axes[0].set_xlim(-0.5, 2.5)
axes[0].set_ylim(-2.5, 0.5)
axes[0].set_title('Array of Structures (AoS)')
axes[0].axis('off')

# SoA layout (grouped by attribute)
soa_data = [["x1","x2","x3"], ["y1","y2","y3"], ["z1","z2","z3"]]
for row_idx, row in enumerate(soa_data):
    for col_idx, val in enumerate(row):
        axes[1].text(col_idx, -row_idx, val, ha='center', va='center',
                     bbox=dict(boxstyle='round', facecolor='#C1E1FF', edgecolor='black'))

axes[1].set_xlim(-0.5, 2.5)
axes[1].set_ylim(-2.5, 0.5)
axes[1].set_title('Structure of Arrays (SoA)')
axes[1].axis('off')

plt.tight_layout()
plt.savefig("aos_vs_soa_layout.png", dpi=300)
plt.show()