import matplotlib.pyplot as plt
import numpy as np

histogram = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42, 108: 32, 109: 16,
    110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40, 145: 65, 146: 43, 147: 32, 148: 20,
    149: 10, 150: 4
}

total = sum(histogram.values())
sum_all = sum(t * histData for t, histData in histogram.items())
sumB = 0
wB = 0
varMax = 0
threshold = 0

thresholds = list(range(100, 151))
results = []

for t in thresholds:
    if t in histogram:
        wB += histogram[t]
        if wB == 0:
            continue

        wF = total - wB
        if wF == 0:
            break

        sumB += t * histogram[t]

        mB = sumB / wB
        mF = (sum_all - sumB) / wF

        varBetween = wB * wF * (mB - mF) ** 2

        vB = varBetween / total
        vF = varBetween / total
        wC = varBetween

        if varBetween > varMax:
            varMax = varBetween
            threshold = t

        results.append((t, wB / total, mB, vB, wF / total, mF, vF, wC))
        print("wB:", wB, "wF:", wF, "sumB:", sumB, "mB:", mB, "mF:", mF, "varBetween:", varBetween, "Threshold:", t,
              "Variance:", varBetween)

print("Optimal Threshold:", threshold)


def plot_histogram(ax, histogram, t):
    keys = list(histogram.keys())
    values = list(histogram.values())
    ax.bar(keys, values, color=['black' if k < t else 'white' for k in keys], edgecolor='black')
    ax.set_title(f'Threshold = {t}', fontsize=10)
    ax.set_xticks(range(min(keys), max(keys) + 1, 5))
    ax.set_yticks(range(0, max(values) + 1, 10))
    ax.set_xlim(min(keys) - 1, max(keys) + 1)
    ax.set_ylim(0, max(values) + 1)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', alpha=0.6)


def create_combined_figure(results_subset, start_index):
    fig, axes = plt.subplots(7, len(results_subset), figsize=(20, 15), constrained_layout=True)

    for i, (t, wB, mB, vB, wF, mF, vF, wC) in enumerate(results_subset):
        # Plot histograms
        plot_histogram(axes[0, i], histogram, t)

        # Plot weights
        axes[1, i].text(0.5, 0.5, f'wB = {wB:.3f}', ha='center', va='center', fontsize=10,
                        bbox=dict(facecolor='white', alpha=0.5))
        axes[1, i].axis('off')

        # Plot means
        axes[2, i].text(0.5, 0.5, f'mB = {mB:.3f}', ha='center', va='center', fontsize=10,
                        bbox=dict(facecolor='white', alpha=0.5))
        axes[2, i].axis('off')

        # Plot variances
        axes[3, i].text(0.5, 0.5, f'vB = {vB:.3f}', ha='center', va='center', fontsize=10,
                        bbox=dict(facecolor='white', alpha=0.5))
        axes[3, i].axis('off')

        # Plot weights foreground
        axes[4, i].text(0.5, 0.5, f'wF = {wF:.3f}', ha='center', va='center', fontsize=10,
                        bbox=dict(facecolor='white', alpha=0.5))
        axes[4, i].axis('off')

        # Plot means foreground
        axes[5, i].text(0.5, 0.5, f'mF = {mF:.3f}', ha='center', va='center', fontsize=10,
                        bbox=dict(facecolor='white', alpha=0.5))
        axes[5, i].axis('off')

        # Plot variances foreground
        axes[6, i].text(0.5, 0.5, f'vF = {vF:.3f}', ha='center', va='center', fontsize=10,
                        bbox=dict(facecolor='white', alpha=0.5))
        axes[6, i].axis('off')

    plt.suptitle('Otsu Thresholding Visualization', fontsize=16)
    plt.show()


for i in range(0, len(results), 6):
    create_combined_figure(results[i:i + 6], i)
