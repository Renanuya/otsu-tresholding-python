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

for t in range(256):
    if t in histogram:
        wB += histogram[t]  # Weight Background
        if wB == 0:
            continue

        wF = total - wB  # Weight Foreground
        if wF == 0:
            break

        sumB += t * histogram[t]

        mB = sumB / wB  # Mean Background
        mF = (sum_all - sumB) / wF  # Mean Foreground

        # Calculate Between Class Variance
        varBetween = wB * wF * (mB - mF) ** 2

        # Check if new maximum found
        if varBetween > varMax:
            varMax = varBetween
            threshold = t
        print("wB:", wB, "wF:", wF, "sumB:", sumB, "mB:", mB, "mF:", mF, "varBetween:", varBetween,"Threshold:", t, "Variance:", varBetween)

print("Optimal Threshold:", threshold)
