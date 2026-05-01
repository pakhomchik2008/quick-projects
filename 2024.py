import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, ttest_rel

# load

data = pd.read_csv("../irs/202409_mobile_coverage_pcon_r01.csv", encoding="latin1", low_memory=False)

# clean column names
data.columns = data.columns.str.strip()

# find numeric columns automatically
numeric_cols = data.select_dtypes(include=['float64','int64']).columns

# assign them as -105 and -95 for comparison
cov_105 = data[numeric_cols[0]]
cov_95 = data[numeric_cols[1]]

print("Using columns:")
print("105 dBm proxy:", numeric_cols[0])
print("95 dBm proxy:", numeric_cols[1])

# -----------------------
# HISTOGRAM
# -----------------------

plt.hist(cov_105, bins=20, alpha=0.6, label="-105 dBm")
plt.hist(cov_95, bins=20, alpha=0.6, label="-95 dBm")

plt.title("Distribution of Mobile Coverage by Signal Threshold")
plt.xlabel("Coverage (%)")
plt.ylabel("Frequency")
plt.legend()

plt.show()

# -----------------------
# BOXPLOT
# -----------------------

plt.boxplot([cov_105, cov_95], labels=["-105 dBm", "-95 dBm"])

plt.title("Comparison of Mobile Coverage Thresholds")
plt.ylabel("Coverage (%)")

plt.show()

# -----------------------
# CORRELATION
# -----------------------

r_value, p_corr = pearsonr(cov_105, cov_95)

print("\nCorrelation Test")
print("r value:", round(r_value,3))
print("p-value:", p_corr)

# -----------------------
# T TEST
# -----------------------

t_stat, p_val = ttest_rel(cov_105, cov_95)

print("\nT-test")
print("t statistic:", round(t_stat,3))
print("p-value:", p_val)

if p_val < 0.05:
    print("Result: The difference between -105 dBm and -95 dBm coverage is statistically significant.")
else:
    print("Result: No statistically significant difference detected.")