# TMMLU+ Leaderboard 🇹🇼

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 About TMMLU+
**TMMLU+** (Traditional Chinese Massive Multitask Language Understanding) is a state-of-the-art benchmark designed to evaluate Large Language Models (LLMs) specifically within the linguistic and cultural context of **Taiwan**.

The benchmark covers **66 subjects** including STEM, Social Sciences, Humanities, and professional certifications, providing a rigorous standard for Traditional Chinese NLP evaluation.

## 📊 Live Interactive Leaderboard
Our interactive dashboard allows you to explore model performance in detail:
- **Search & Filter:** Find specific models instantly.
- **Visual Analytics:** Compare performance via Discipline Radar Maps and Category Bar Charts.
- **Nested Drill-down:** Expand models to see Major Disciplines and individual subject scores.
- **General Benchmarks:** Includes evaluations for DRCD, TW-RAG, GSM8K, and more.

👉 **[Access the Interactive Leaderboard Here](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)**

## 📂 Repository Structure
```text
├── .github/ISSUE_TEMPLATE/  # Model submission form configuration
├── docs/
│   └── index.html           # Website Frontend (Plotly, PapaParse, Bootstrap)
├── results/
│   └── benchmark.csv        # Central Data Source
└── README.md                # Project Documentation

```

## 🚀 How to Submit Results

We welcome contributions from the research community! To add your model:

1. **Prepare Data:** Ensure results match the format in `results/benchmark.csv`.
2. **Submit an Issue:** Click the **"Submit Your Model Results"** button on the live website.
3. **Pull Request:** Fork this repo, add your model's column to the CSV, and submit a PR.

## 📄 Citation

If you utilize this benchmark or leaderboard in your research, please cite:

```bibtex
@misc{aslam2025tmmluplus,
  author = {Aslam, Muhammad Saqlain},
  title = {TMMLU+ Leaderboard: Traditional Chinese Massive Multitask Language Understanding Benchmark},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{[https://github.com/MuhammadSaqlainAslam/tmmlu-leaderboard](https://github.com/MuhammadSaqlainAslam/tmmlu-leaderboard)}}
}

```

---

**Maintained by:** [Muhammad Saqlain Aslam](https://github.com/MuhammadSaqlainAslam)

*Dedicated to the Traditional Chinese NLP Community.*

```
