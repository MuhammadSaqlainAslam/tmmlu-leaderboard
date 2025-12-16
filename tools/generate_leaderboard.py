import pandas as pd
import json

CSV_PATH = "benchmark.csv"
OUT_PATH = "docs/leaderboard.json"

df = pd.read_csv(CSV_PATH)

models = [c for c in df.columns if c not in ["task_name", "metric"]]

def parse_tmmlu(task):
    x = task.split("tmmluplus-")[1]
    cat, disc = x.split("_", 1)
    return cat.capitalize(), disc.capitalize()

result = {"leaderboard": [], "details": {}}

for model in models:
    d = {
        "tmmlu_subjects": {},
        "tmmlu_categories": {},
        "tmmlu_disciplines": {},
        "general": {}
    }

    tmmlu = df[df.task_name.str.contains("tmmluplus") & (df.metric=="accuracy")]

    for _, r in tmmlu.iterrows():
        cat, disc = parse_tmmlu(r.task_name)
        d["tmmlu_subjects"][f"{disc}/{cat}"] = float(r[model])

    for k, v in d["tmmlu_subjects"].items():
        disc, cat = k.split("/")
        d["tmmlu_categories"].setdefault(cat, []).append(v)
        d["tmmlu_disciplines"].setdefault(disc, []).append(v)

    d["tmmlu_categories"] = {k: sum(v)/len(v) for k,v in d["tmmlu_categories"].items()}
    d["tmmlu_disciplines"] = {k: sum(v)/len(v) for k,v in d["tmmlu_disciplines"].items()}

    gen = df[~df.task_name.str.contains("tmmluplus")]
    for _, r in gen.iterrows():
        if r.metric == "accuracy":
            d["general"][r.task_name.split("/")[-1]] = float(r[model])

    tmmlu_overall = sum(d["tmmlu_categories"].values()) / len(d["tmmlu_categories"])
    overall = sum(d["general"].values()) / len(d["general"])

    result["leaderboard"].append({
        "model": model,
        "overall": round(overall, 4),
        "tmmlu_overall": round(tmmlu_overall, 4)
    })

    result["details"][model] = d

result["leaderboard"].sort(key=lambda x: x["overall"], reverse=True)

with open(OUT_PATH, "w") as f:
    json.dump(result, f, indent=2)

print("✅ leaderboard.json generated")
