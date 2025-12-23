# TMMLU+ Leaderboard 🇹🇼

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 About TMMLU+
**TMMLU+** (Traditional Chinese Massive Multitask Language Understanding) is an advanced benchmark designed to evaluate Large Language Models (LLMs) within the linguistic and cultural context of **Taiwan**.

The benchmark covers **66 subjects** including STEM, Social Sciences, Humanities, and local professional certifications (e.g., Real Estate, Clinical Psychology, and Law), providing a rigorous standard for Traditional Chinese NLP evaluation.

## 📊 Live Interactive Leaderboard
We provide an interactive dashboard that offers more than just raw scores:
- **Search & Filter:** Find specific models instantly by name.
- **Visual Analytics:** Compare performance via Discipline Radar Maps and Category Bar Charts.
- **Hierarchical Drill-down:** Click on a model to see Major Disciplines, and expand those to see scores for all 66+ individual subjects.
- **General Benchmarks:** Integration of external evaluations such as DRCD, TW-RAG, and GSM8K.

👉 **[Access the Interactive Leaderboard Here](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)**

## 📂 Repository Structure
```text
├── .github/ISSUE_TEMPLATE/  # Submission form configuration
├── docs/
│   └── index.html           # Website Frontend (Plotly, PapaParse, Bootstrap)
├── results/
│   └── benchmark.csv        # Central Data Source
└── README.md                # Project Documentation

---

## 🚀 How to Submit Results
We welcome contributions from the research community! To add your model to the leaderboard:

1. **Prepare Data:** Ensure your results are calculated using the TMMLU+ methodology and formatted to match `results/benchmark.csv`.
2. **Submit an Issue:** Click the **"Submit Your Model Results"** button on the live leaderboard website to fill out a pre-formatted request.
3. **Pull Request:** Alternatively, fork this repo, add your model's column to the CSV, and submit a Pull Request.

---
**Maintained by:** [Muhammad Saqlain Aslam](https://github.com/MuhammadSaqlainAslam)  
*Dedicated to the Traditional Chinese NLP Community.*
