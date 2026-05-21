import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

sns.set_theme(style="whitegrid")

df = pd.read_csv("responses_english.csv")
h3_percent_table = pd.crosstab(
    df["gender"],
    df["boycott_status"],
    normalize="index"
) * 100

gender_order = ["Male", "Female"]
boycott_order = ["No", "Maybe", "Yes"]

h3_percent_table = h3_percent_table.reindex(index=gender_order, columns=boycott_order)

plt.figure(figsize=(7, 5))

h3_percent_table.plot(
    kind="bar",
    stacked=True,
    figsize=(7, 5)
)

plt.title("H3: Boycott Status by Gender")
plt.xlabel("Gender")
plt.ylabel("Percentage of respondents")
plt.xticks(rotation=0)
plt.legend(title="Boycott Status", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.show()


h3_observed = pd.crosstab(
    df["gender"],
    df["boycott_status"]
)

chi2, p_value, dof, expected = chi2_contingency(h3_observed)

h3_expected = pd.DataFrame(
    expected,
    index=h3_observed.index,
    columns=h3_observed.columns
)

h3_result = pd.DataFrame({
    "Hypothesis": ["H3: Gender is associated with boycott status"],
    "Test": ["Chi-square test of independence"],
    "Chi-square statistic": [round(chi2, 4)],
    "Degrees of freedom": [dof],
    "P-value": [f"{p_value:.4e}" if p_value < 0.0001 else round(p_value, 4)],
    "Decision": ["Reject H0" if p_value < 0.05 else "Fail to reject H0"]
})

print("\nObserved Table:")
print(h3_observed.to_string())

print("\nExpected Table:")
print(h3_expected.round(2).to_string())

print("\nH3 Test Result:")
print(h3_result.to_string(index=False))
