import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

df = pd.read_csv("responses_english.csv")
sns.set_theme(style="whitegrid")

h2_percent_table = pd.crosstab(
    df["origin_check_frequency"],
    df["boycott_status"],
    normalize="index"
) * 100

freq_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
boycott_order = ["No", "Maybe", "Yes"]

h2_percent_table = h2_percent_table.reindex(index=freq_order, columns=boycott_order)

plt.figure(figsize=(8, 5))

h2_percent_table.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

plt.title("H2: Boycott Status by Product-Origin Checking Frequency")
plt.xlabel("Product-Origin Checking Frequency")
plt.ylabel("Percentage of respondents")
plt.xticks(rotation=25, ha="right")
plt.legend(title="Boycott Status", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

h2_observed = pd.crosstab(
    df["origin_check_frequency"],
    df["boycott_status"]
)

chi2, p_value, dof, expected = chi2_contingency(h2_observed)

h2_expected = pd.DataFrame(
    expected,
    index=h2_observed.index,
    columns=h2_observed.columns
)
h2_result = pd.DataFrame({
    "Hypothesis": ["H2: Product-origin checking is associated with boycott status"],
    "Test": ["Chi-square test of independence"],
    "Chi-square statistic": [round(chi2, 4)],
    "Degrees of freedom": [dof],
    "P-value": [f"{p_value:.4e}" if p_value < 0.0001 else round(p_value, 4)],
    "Decision": ["Reject H0" if p_value < 0.05 else "Fail to reject H0"]
})

print("\nObserved Table:")
print(h2_observed.to_string())

print("\nExpected Table:")
print(h2_expected.round(2).to_string())

print("\nH2 Test Result:")
print(h2_result.to_string(index=False))
