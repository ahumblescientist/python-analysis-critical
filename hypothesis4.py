import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

df = pd.read_csv("responses_english.csv")

sns.set_theme(style="whitegrid")
likert_map = {
    "Strongly disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly agree": 5
}

df["local_products_suitable_alternative_code"] = (
    df["local_products_suitable_alternative"].map(likert_map)
)

df["continue_buying_local_after_boycott_decreases_code"] = (
    df["continue_buying_local_after_boycott_decreases"].map(likert_map)
)

likert_order = [
    "Strongly disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly agree"
]

h4_table = pd.crosstab(
    df["local_products_suitable_alternative"],
    df["continue_buying_local_after_boycott_decreases"]
)

h4_table = h4_table.reindex(
    index=likert_order,
    columns=likert_order
)

plt.figure(figsize=(8, 6))

sns.heatmap(
    h4_table,
    annot=True,
    fmt=".0f",
    linewidths=0.5,
    cmap="Blues"
)

plt.title("H4: Local Alternatives vs Continued Local Buying")
plt.xlabel("Intention to Continue Buying Local Products")
plt.ylabel("Local Products Are Suitable Alternatives")
plt.xticks(rotation=35, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()

plt.show()

h4_temp = df[
    [
        "local_products_suitable_alternative_code",
        "continue_buying_local_after_boycott_decreases_code"
    ]
].dropna()

rho, p_value = spearmanr(
    h4_temp["local_products_suitable_alternative_code"],
    h4_temp["continue_buying_local_after_boycott_decreases_code"]
)

h4_result = pd.DataFrame({
    "Hypothesis": ["H4: Belief in local alternatives is associated with continued local buying intention"],
    "Test": ["Spearman correlation"],
    "Spearman rho": [round(rho, 4)],
    "P-value": [f"{p_value:.4e}" if p_value < 0.0001 else round(p_value, 4)],
    "Decision": ["Reject H0" if p_value < 0.05 else "Fail to reject H0"]
})

print("\nH4 Cross-tabulation Table:")
print(h4_table.to_string())

print("\nH4 Test Result:")
print(h4_result.to_string(index=False))
