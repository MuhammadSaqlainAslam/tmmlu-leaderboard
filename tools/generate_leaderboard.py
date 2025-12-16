import pandas as pd
import json
import os

CSV_PATH = "benchmark.csv"
OUT_PATH = "docs/leaderboard.json"

TMMLU_CATEGORY_MAP = {
    "physics": "Science",
    "secondary_physics": "Science",
    "engineering_math": "Science",
    "statistics_and_machine_learning": "Science",
    "advance_chemistry": "Science",
    "organic_chemistry": "Science",
    "fire_science": "Science",
    "junior_science_exam": "Science",
    "junior_chemistry": "Science",

    "auditing": "Business",
    "business_management": "Business",
    "finance_banking": "Business",
    "financial_analysis": "Business",
    "insurance_studies": "Business",
    "management_accounting": "Business",
    "marketing_management": "Business",
    "taxation": "Business",
    "economics": "Business",
    "accounting": "Business",
    "trade": "Business",
    "real_estate": "Business",

    "basic_medical_science": "Health & Medicine",
    "clinical_psychology": "Health & Medicine",
    "dentistry": "Health & Medicine",
    "pharmacology": "Health & Medicine",
    "pharmacy": "Health & Medicine",
    "veterinary_pharmacology": "Health & Medicine",

    "computer_science": "Tech & Engineering",
    "mechanical": "Tech & Engineering",
    "technical": "Tech & Engineering",
}

df = pd.read_csv(CSV_PATH)
models = [c for c in df.columns if c not in ["task_name", "metric"]]

result = {"leaderboard": [], "details": {}}

for model in models:
    details = {
        "tmmlu": {},
        "general": {}
    }

    # ---------- TMMLU+ ----------
    tmmlu_rows = df[
        df.task_name.str.contains("tmmluplus") &
        (df.metric == "accuracy")
    ]

    for _, r in tmmlu_rows.iterrows():
        task = r.task_name.split("tmmluplus-")[-1]
        category = TMMLU_CATEGORY_MAP.get(task, "Other")

        details["tmmlu"].setdefault(category, {})
        details["tmmlu"][category].setdefault(task, {})
        details["tmmlu"][category][task][task] = float(r[model])

    # ---------- GENERAL ----------
    gen_rows = df[
        ~df.task_name.str.contains("tmmluplus") &
        (df.metric == "accuracy")
    ]

    for _, r in gen_rows.iterrows():
        details["general"][r.task_name] = float(r[model])

    # ---------- AVERAGES ----------
    tmmlu_scores = []
    for cat in details["tmmlu"].values():
        for sub in cat.values():
            tmmlu_scores.extend(sub.values())

    tmmlu_avg = sum(tmmlu_scores) / len(tmmlu_scores) if tmmlu_scores else 0
    gen_avg = sum(details["general"].values()) / len(details["general"]) if details["general"] else 0

    result["leaderboard"].append({
        "model": model,
        "overall": round(gen_avg, 4),
        "tmmlu_overall": round(tmmlu_avg, 4)
    })

    result["details"][model] = details

result["leaderboard"].sort(key=lambda x: x["overall"], reverse=True)

os.makedirs("docs", exist_ok=True)
with open(OUT_PATH, "w") as f:
    json.dump(result, f, indent=2)

print("✅ leaderboard.json generated successfully")
