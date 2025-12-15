import os
import re
import json
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "results", "benchmark.csv")
OUT_JSON = os.path.join(BASE_DIR, "docs", "leaderboard.json")

SUBJECT_CATEGORIES = {
    "fire_science": "Science",
    "secondary_physics": "Science",
    "advance_chemistry": "Science",
    "organic_chemistry": "Science",
    "physics": "Science",
    "junior_science_exam": "Science",
    "junior_chemistry": "Science",
    "engineering_math": "Science",
    "statistics_and_machine_learning": "Science",
    "tve_mathematics": "Science",
    "tve_natural_sciences": "Science",

    "auditing": "Business",
    "financial_analysis": "Business",
    "insurance_studies": "Business",
    "business_management": "Business",
    "marketing_management": "Business",
    "management_accounting": "Business",
    "finance_banking": "Business",
    "taxation": "Business",
    "real_estate": "Business",
    "anti_money_laundering": "Business",
    "trust_practice": "Business",
    "official_document_management": "Business",

    "clinical_psychology": "Health & Medicine",
    "pharmacy": "Health & Medicine",
    "veterinary_pathology": "Health & Medicine",
    "dentistry": "Health & Medicine",
    "pharmacology": "Health & Medicine",
    "veterinary_pharmacology": "Health & Medicine",
    "basic_medical_science": "Health & Medicine",
    "occupational_therapy_for_psychological_disorders": "Health & Medicine",
    "optometry": "Health & Medicine",
    "traditional_chinese_medicine_clinical_medicine": "Health & Medicine",

    "logic_reasoning": "Humanities & Social Science",
    "education": "Humanities & Social Science",
    "educational_psychology": "Humanities & Social Science",
    "human_behavior": "Humanities & Social Science",
    "geography_of_taiwan": "Humanities & Social Science",
    "jce_humanities": "Humanities & Social Science",
    "chinese_language_and_literature": "Humanities & Social Science",
    "junior_chinese_exam": "Humanities & Social Science",
    "politic_science": "Humanities & Social Science",
    "three_principles_of_people": "Humanities & Social Science",
    "national_protection": "Humanities & Social Science",
    "general_principles_of_law": "Humanities & Social Science",
    "administrative_law": "Humanities & Social Science",
    "introduction_to_law": "Humanities & Social Science",
    "taiwanese_hokkien": "Humanities & Social Science",
    "music": "Humanities & Social Science",
    "education_(profession_level)": "Humanities & Social Science",

    "computer_science": "Tech & Engineering",
    "mechanical": "Tech & Engineering",
    "nautical_science": "Tech & Engineering",
    "technical": "Tech & Engineering",
    "agriculture": "Tech & Engineering",
    "culinary_skills": "Tech & Engineering",
    "tve_design": "Tech & Engineering",

    "drcd": "General",
    "penguin_table": "General",
    "TW-RAG": "General",
    "GSM8K": "General",
    "GPQA": "General",
    "AIEC": "General",
    "AITEST": "General",
}

GENERAL_TASKS = ["drcd", "penguin_table", "TW-RAG", "GSM8K", "GPQA", "AIEC", "AITEST"]
DISCIPLINES = sorted(set(v for v in SUBJECT_CATEGORIES.values() if v != "General"))


def choose_metric(df):
    if df["metric"].str.contains("accuracy", case=False).any():
        return df[df["metric"].str.contains("accuracy", case=False)].iloc[0]
    if df["metric"].str.contains("exact_match", case=False).any():
        return df[df["metric"].str.contains("exact_match", case=False)].iloc[0]
    return df.iloc[0]


def match_subject(df, subject):
    pats = [rf"/{subject}$", rf"^{subject}$"]
    mask = False
    for p in pats:
        mask |= df["task_name"].str.contains(p, regex=True)
    return df[mask]


def main():
    df = pd.read_csv(CSV_PATH).fillna(0)
    models = [c for c in df.columns if c not in ["task_name", "metric"]]

    selected = (
        df.groupby("task_name")
          .apply(choose_metric)
          .reset_index(drop=True)
    )

    leaderboard = []
    details = {}

    for model in models:
        overall = round(selected[model].mean(), 4)

        tmmlu = {}
        for d in DISCIPLINES:
            subs = [s for s, v in SUBJECT_CATEGORIES.items() if v == d]
            scores = {}
            for s in subs:
                m = match_subject(selected, s)
                if not m.empty:
                    scores[s] = round(m[model].mean(), 4)
            if scores:
                tmmlu[d] = scores

        general = {}
        for g in GENERAL_TASKS:
            m = match_subject(selected, g)
            general[g] = round(m[model].mean(), 4) if not m.empty else None

        flat = [v for d in tmmlu.values() for v in d.values()]
        tmmlu_overall = round(sum(flat) / len(flat), 4) if flat else None

        leaderboard.append({
            "model": model,
            "overall": overall,
            "tmmlu_overall": tmmlu_overall
        })

        details[model] = {"tmmlu": tmmlu, "general": general}

    leaderboard.sort(key=lambda x: x["overall"], reverse=True)

    with open(OUT_JSON, "w") as f:
        json.dump({"leaderboard": leaderboard, "details": details}, f, indent=2)

    print("✅ leaderboard.json generated")


if __name__ == "__main__":
    main()
