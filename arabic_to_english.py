import pandas as pd
import numpy as np

df = pd.read_csv("responses.csv") # read the data into a pandas data frame

df.columns = [
    "timestamp",
    "gender",
    "age_group",
    "student_status",
    "boycott_status",
    "origin_check_frequency",
    "main_boycott_reason",
    "buys_local_instead",

    "boycott_increased_local_reliance",
    "local_products_suitable_alternative",
    "local_quality_affects_purchase",
    "local_price_affects_purchase",
    "local_availability_encourages_purchase",
    "local_products_need_more_support",
    "continue_buying_local_after_boycott_decreases",

    "quality_food",
    "quality_medicine",
    "quality_detergents",
    "quality_cosmetics",
    "quality_electrical_devices",

    "replace_food",
    "replace_medicine",
    "replace_clothes",
    "replace_cosmetics",
    "replace_electrical_devices",
] # rename columns in english

df.drop("timestamp", axis=1, inplace=True) # drop the time of answering column -- no need for it 

df = df[df["gender"] != "أفضل عدم التصريح"].copy() # remove prefer not to say responses


translation_map = {
    # Gender
    "ذكر": "Male",
    "أنثى": "Female",

    # Yes / No / Maybe
    "نعم": "Yes",
    "لا": "No",
    "ربما": "Maybe",

    # Age groups
    "أقل من 18 سنة": "Under 18",
    "18 – 25 سنة": "18–25",
    "18 - 25 سنة": "18–25",
    "26 – 35 سنة": "26–35",
    "26 - 35 سنة": "26–35",
    "أكثر من 35 سنة": "Over 35",

    # Frequency
    "أبداً": "Never",
    "أبدًا": "Never",
    "نادرًا": "Rarely",
    "نادراً": "Rarely",
    "أحيانًا": "Sometimes",
    "أحياناً": "Sometimes",
    "غالبًا": "Often",
    "غالباً": "Often",
    "دائمًا": "Always",
    "دائماً": "Always",

    # Likert scale
    "لا أوافق بشدة": "Strongly disagree",
    "لا أوافق": "Disagree",
    "محايد": "Neutral",
    "أوافق": "Agree",
    "أوافق بشدة": "Strongly agree",

    # Quality scale
    "ضعيفة جدًا": "Very poor",
    "ضعيفة جدا": "Very poor",
    "ضعيفة": "Poor",
    "متوسطة": "Average",
    "جيدة": "Good",
    "ممتازة": "Excellent",

    # Boycott reasons
    "سبب وطني أو سياسي": "National or political reason",
    "دعم المنتجات المحلية": "Supporting local products",
    "التأثر بحملات المقاطعة": "Influenced by boycott campaigns",
    "سبب اقتصادي": "Economic reason",
    "توفر بدائل محلية مناسبة": "Availability of local alternatives",
    "أسباب تتعلق بالجودة أو الثقة بالمنتج": "Quality or trust concerns",
    "سبب آخر": "Other reason",
}

df = df.replace(translation_map)

df.to_csv("responses_english.csv", index=False, encoding="utf-8-sig")
