# TMMLU+ Leaderboard 🇹🇼

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 About TMMLU+
**TMMLU+** is a comprehensive benchmark designed to evaluate the multitask language understanding capabilities of Large Language Models (LLMs) in **Traditional Chinese**. 

Unlike standard benchmarks, TMMLU+ focus specifically on the cultural, linguistic, and academic context of **Taiwan**, covering 66 subjects ranging from elementary school level to professional certifications. It includes specialized disciplines such as:
- **STEM:** Physics, Engineering Math, Chemistry, Agriculture.
- **Social Sciences:** Geography of Taiwan, Administrative Law, Logic Reasoning.
- **Professional:** Auditing, Clinical Psychology, Real Estate Practice.
- **Local Language:** Taiwanese Hokkien.

## 📊 Live Leaderboard
We host an interactive leaderboard that provides:
- **Overall Rankings:** Based on mean accuracy across all subjects.
- **Discipline Breakdown:** Comparative analysis via Radar and Bar charts.
- **Granular Subject Scores:** Drill-down views for 60+ individual sub-tasks.
- **General Benchmarks:** Integration of external tasks like DRCD, TW-RAG, and GSM8K.

👉 **[View the Live Leaderboard here](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)**

## 📂 Repository Structure
```text
├── docs/
│   └── index.html         # Interactive frontend (Bootstrap, Plotly, PapaParse)
├── results/
│   └── benchmark.csv      # Source data containing model scores and metrics
└── README.md              # Project documentation
