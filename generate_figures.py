import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("responses_english.csv")


# ============ GENDER PLOT dist =================
gender_table = df["gender"].value_counts()
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="gender", order=["Male", "Female"])
plt.title("Figure 1: Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of respondents")
plt.tight_layout()
plt.show()


# =========== age group distribution =============
age_order = ["Under 18", "18–25", "26–35", "Over 35"]

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="age_group", order=age_order)
plt.title("Figure 2: Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of respondents")
plt.tight_layout()
plt.show()


# =================== boycot status ===== 
boycott_order = ["No", "Maybe", "Yes"]

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="boycott_status", order=boycott_order)
plt.title("Figure 3: Boycott Status Distribution")
plt.xlabel("Boycott Status")
plt.ylabel("Number of respondents")
plt.tight_layout()
plt.show()


# ========= checking product frequency =====
freq_order = ["Never", "Rarely", "Sometimes", "Often", "Always"]
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="origin_check_frequency", order=freq_order)
plt.title("Figure 4: Frequency of Checking Product Origin")
plt.xlabel("Checking Frequency")
plt.ylabel("Number of respondents")
plt.tight_layout()

# -====---- local product buying ====
local_order = ["No", "Sometimes", "Yes"]
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="buys_local_instead", order=local_order)
plt.title("Figure 5: Buying Local Products Instead")
plt.xlabel("Response")
plt.ylabel("Number of respondents")
plt.tight_layout()
plt.show()
plt.show()

# ==== reason for boycotting ===
plt.figure(figsize=(11, 5))
sns.countplot(
    data=df,
    x="main_boycott_reason",
    order=df["main_boycott_reason"].value_counts().index
)
plt.title("Figure 6: Main Reason for Boycotting")
plt.xlabel("Reason")
plt.ylabel("Number of respondents")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()



# =========== agreement on reliance ====

likert_order = [
    "Strongly disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly agree"
]

plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="boycott_increased_local_reliance",
    order=likert_order
)
plt.title("Figure 7: Boycott Increased Reliance on Local Products")
plt.xlabel("Agreement Level")
plt.ylabel("Number of respondents")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.show()

# ==== local products are a suitable alternative ====
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="local_products_suitable_alternative",
    order=likert_order
)
plt.title("Figure 8: Local Products Are Suitable Alternatives")
plt.xlabel("Agreement Level")
plt.ylabel("Number of respondents")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.show()

