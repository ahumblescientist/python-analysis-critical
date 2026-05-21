import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, spearmanr

df = pd.read_csv("responses_english.csv")

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
    df["continue_buying_local_after_boycott_decreases"].map(likert_map))


### HYPOTHESIS TESTING

ALPHA = 0.05 # threshold

def decision(p): # reject or accept
    if p < ALPHA:
        return "Reject H0"
    return "Fail to reject H0"

def interpretation(p): # print results 
    if p < ALPHA:
        return "The result is statistically significant. The alternative hypothesis is supported."
    return "The result is not statistically significant. There is not enough evidence to reject the null hypothesis."

def chi_square_test(data, row_col, col_col, hypothesis_name): # chi square test
    observed = pd.crosstab(data[row_col], data[col_col])

    chi2, p, dof, expected = chi2_contingency(observed)

    expected_table = pd.DataFrame(
        expected,
        index=observed.index,
        columns=observed.columns
    )

    result = pd.DataFrame({
        "Hypothesis": [hypothesis_name],
        "Test": ["Chi-square test of independence"],
        "Chi-square statistic": [round(chi2, 4)],
        "Degrees of freedom": [dof],
        "P-value": [round(p, 4)],
        "Decision": [decision(p)],
        "Interpretation": [interpretation(p)]
    })

    return observed, expected_table.round(2), result

def spearman_test(data, x_col, y_col, hypothesis_name): # spearman test
    temp = data[[x_col, y_col]].dropna()

    rho, p = spearmanr(temp[x_col], temp[y_col])

    result = pd.DataFrame({
        "Hypothesis": [hypothesis_name],
        "Test": ["Spearman correlation"],
        "Spearman rho": [round(rho, 4)],
        "P-value": [round(p, 4)],
        "Decision": [decision(p)],
        "Interpretation": [interpretation(p)]
    })

    return result

h1_observed, h1_expected, h1_result = chi_square_test(
    df,
    "boycott_status",
    "buys_local_instead",
    "H1: Boycott status is associated with buying local products instead"
)

print(h1_observed.to_string());
print(h1_expected.round(2).to_string());
print(h1_result.to_string(index=False));
sns.set_theme(style="whitegrid")

def stacked_percentage_bar(data, x_col, hue_col, title, xlabel, ylabel="Percentage of respondents"):
    table = pd.crosstab(data[x_col], data[hue_col], normalize="index") * 100

    table.plot(
        kind="bar",
        stacked=True,
        figsize=(8, 5)
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=0)
    plt.legend(title=hue_col, bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


stacked_percentage_bar(
    df,
    x_col="boycott_status",
    hue_col="buys_local_instead",
    title="H1: Buying Local Products by Boycott Status",
    xlabel="Boycott Status"
)


