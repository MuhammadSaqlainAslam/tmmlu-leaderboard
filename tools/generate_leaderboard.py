import csv
import json
import os
import math
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(__file__))
CSV_PATH = os.path.join(ROOT, "benchmark.csv")
OUT_PATH = os.path.join(ROOT, "docs", "leaderboard.json")

def safe_avg(values):
    vals = [v for v in values if isinstance(v, (int, float)) and not math.isnan(v)]
    return round(sum(vals) / len(vals), 4) if vals else 0.0

models = []
tmmlu = defaultdict(lambda: defaultdict(dict))
general = defaultdict(dict)

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        task = row["task_name"]
        metric = row["metric"]

        if metric != "accuracy":
            continue

        for model, val in row.items():
            if model in ("task_name", "metric"):
                continue
            if model not in models:
                models.append(model)

            try:
                score = float(val)
            except:
                score = None

            if task.startswith("TCEval-v2/tmmluplus-"):
                sub = task.replace("TCEval-v2/tmmluplus-", "")
                tmmlu[sub][model] = score
            else:
                general[task][model] = score

# ---- GROUP TMMLU+ INTO CATEGORIES (SIMPLE & SAFE) ----
def infer_category(sub):
    key = sub.lower()
    if "law" in key or "politic" in key:
        return "law & politics"
    if "medicine" in key or "medical" in key or "pharma" in key:
        return "medicine"
    if "chemistry" in key or "physics" in key:
        return "science"
    if "math" in key or "statistics" in key:
        return "mathematics"
    if "engineering" in key or "mechanical" in key:
        return "engineering"
    if "economics" in key or "finance" in key or "accounting" in key:
        return "economics"
    if "education" in key:
        return "education"
    return "others"

categories = defaultdict(lambda: defaultdict(dict))
for sub, scores in tmmlu.items():
    cat = infer_category(sub)
    categories[cat][sub] = scores

# ---- BUILD FINAL JSON ----
leaderboard = {"models": []}

for model in models:
    cat_avgs = {}
    for cat, subs in categories.items():
        scores = []
        for s in subs.values():
            if model in s and s[model] is not None:
                scores.append(s[model])
        cat_avgs[cat] = safe_avg(scores)

    tmmlu_all = []
    for subs in categories.values():
        for s in subs.values():
            if model in s and s[model] is not None:
                tmmlu_all.append(s[model])

    gen_scores = [
        v for v in general.values()
        if model in v and v[model] is not None
        for v in [v]
    ]

    leaderboard["models"].append({
        "name": model,
        "tmmlu_avg": safe_avg(tmmlu_all),
        "general_avg": safe_avg(gen_scores),
        "tmmlu_categories": cat_avgs,
        "tmmlu_details": categories
    })

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(leaderboard, f, indent=2)

print("✅ leaderboard.json generated successfully")
