# TMMLU+ Leaderboard 🇹🇼

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 About TMMLU+

**TMMLU+** (Traditional Chinese Massive Multitask Language Understanding) is a benchmark designed to evaluate Large Language Models (LLMs) within the linguistic and cultural context of **Taiwan**.

The benchmark covers **66 subjects** across five major disciplines:

| Discipline | Example Subjects |
| :--- | :--- |
| **Science** | Physics, Chemistry, Engineering Math, Statistics & ML |
| **Business** | Auditing, Financial Analysis, Taxation, Real Estate |
| **Health & Medicine** | Clinical Psychology, Dentistry, Pharmacology, Optometry |
| **Humanities** | Logic Reasoning, Education, Law, Geography of Taiwan |
| **Tech & Engineering** | Computer Science, Mechanical, Nautical Science, Agriculture |

In addition to TMMLU+ subjects, the leaderboard tracks performance on a wide range of **general benchmarks** including AIEC, AIME2025, BigBenchHard, DRCD, TW-RAG, GSM8K, GPQA, HumanEval, MuSR, SimpleQA, and more.

## 📊 Live Interactive Leaderboard

👉 **[Access the Interactive Leaderboard Here](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)**

The dashboard offers two views:

### Visual Leaderboard
- **Rank badges** — 🥇🥈🥉 medals for top 3 models, numbered badge for the rest
- **Score bars** — visual progress bars under each accuracy score for quick comparison
- **Sortable columns** — click **Overall Acc** or **TMMLU+ Avg** to sort ascending or descending
- **Sticky header** — column labels stay visible as you scroll
- **Search** — filter models by name in real time
- **Drill-down** — expand any model card to see per-discipline and per-subject scores, color-coded green (≥80%), amber (60–80%), and red (<60%)
- **Radar & Bar charts** — discipline-level performance for the top 5 models

### Side-by-Side Comparison
- Select any combination of models to compare
- All benchmark tasks are shown; a `—` indicates a model was not evaluated on that task
- Best score per row is highlighted in green
- Filter by discipline category (Science, Business, Health & Med, Humanities, Tech & Eng, General Benchmarks)
- **Select All / Clear All** buttons for quick model selection

## 📂 Repository Structure

```text
├── .github/
│   └── ISSUE_TEMPLATE/
│       └── model_submission.md   # GitHub issue template for model submissions
├── docs/
│   └── index.html                # Full frontend (Bootstrap, Plotly, PapaParse)
├── results/
│   └── benchmark.csv             # Central data source — one column per model
└── README.md
```

## 🚀 How to Submit Results

We welcome contributions from the research community!

1. **Prepare your data** — ensure your results follow the format in `results/benchmark.csv` (rows are `task_name` + `metric`, columns are model names, values are accuracy decimals 0–1).
2. **Submit an Issue** — open a [Model Submission issue](https://github.com/MuhammadSaqlainAslam/tmmlu-leaderboard/issues/new/choose) and select the **Model Submission** template.
3. **Pull Request** — fork this repo, add your model's column to `benchmark.csv`, and submit a PR.

## 📄 Citation

If you use this leaderboard in your research, please cite:

```bibtex
@misc{aslam2025tmmluplus,
  author    = {Aslam, Muhammad Saqlain},
  title     = {TMMLU+ Leaderboard: Traditional Chinese Massive Multitask Language Understanding Benchmark},
  year      = {2025},
  publisher = {GitHub},
  journal   = {GitHub Repository},
  howpublished = {\url{https://github.com/MuhammadSaqlainAslam/tmmlu-leaderboard}}
}
```

---

**Maintained by:** [Muhammad Saqlain Aslam](https://github.com/MuhammadSaqlainAslam)

*Dedicated to the Traditional Chinese NLP Community.*
