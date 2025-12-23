# TMMLU+ Leaderboard 🇹🇼

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 About TMMLU+
**TMMLU+** (Traditional Chinese Massive Multitask Language Understanding) is an advanced benchmark designed to evaluate Large Language Models (LLMs) within the linguistic and cultural context of **Taiwan**.

The benchmark covers **66 subjects** including STEM, Social Sciences, Humanities, and local professional certifications, providing a rigorous standard for Traditional Chinese NLP evaluation.

## 📊 Live Leaderboard Features
- **Overall Rankings:** Automated sorting by mean accuracy.
- **Dynamic Visualizations:** Discipline-specific Radar and Bar charts.
- **Hierarchical Drill-down:** Expand models to see Major Disciplines, and expand those to see individual subject scores.
- **Search Functionality:** Real-time filtering to find specific models.
- **Integrated General Tasks:** Scores for DRCD, TW-RAG, GSM8K, and more.

👉 **[Access the Leaderboard](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)**

## 📂 Repository Structure
```text
├── .github/ISSUE_TEMPLATE/  # Model submission form configuration
├── docs/
│   └── index.html           # Interactive Frontend (Plotly, PapaParse, Bootstrap)
├── results/
│   └── benchmark.csv        # Central Data Source
└── README.md                # Documentation

🚀 How to Submit Results
We welcome submissions from the research community!

1. Prepare your data: Ensure your results are in the same format as results/benchmark.csv.

2. Submit an Issue: Click the "Submit Your Model Results" button on the leaderboard website.

3. Open a PR: Alternatively, fork this repo, add your model's column to the CSV, and submit a Pull Request.

📄 Citation
If you utilize this benchmark or leaderboard in your research, please cite:
@misc{aslam2025tmmluplus,
  author = {Aslam, Muhammad Saqlain},
  title = {TMMLU+ Leaderboard: Traditional Chinese Massive Multitask Language Understanding Benchmark},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{[https://github.com/MuhammadSaqlainAslam/tmmlu-leaderboard](https://github.com/MuhammadSaqlainAslam/tmmlu-leaderboard)}}
}
