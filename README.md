# TMMLU+ Leaderboard 🇹🇼

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
**TMMLU+** (Traditional Chinese Massive Multitask Language Understanding) is a state-of-the-art benchmark designed to evaluate Large Language Models (LLMs) specifically within the linguistic and cultural context of **Taiwan**.

The benchmark includes **66 subjects** covering STEM, Social Sciences, Humanities, and professional certifications (e.g., Real Estate, Clinical Psychology, and Law). This leaderboard provides an interactive platform to compare model performance across these diverse domains.

## 📊 Live Interactive Leaderboard
We provide an interactive dashboard that offers more than just raw scores:
- **Search & Filter:** Find specific models instantly.
- **Visual Analytics:** Compare performance via Discipline Radar Maps and Category Bar Charts.
- **Nested Drill-down:** Click on a model to see Major Disciplines, and expand those to see scores for all 66+ individual subjects.
- **General Benchmarks:** Includes external evaluations like DRCD, TW-RAG, and GSM8K.

👉 **[Access the Interactive Leaderboard Here](https://muhammadsaqlainaslam.github.io/tmmlu-leaderboard/)**

## 📂 Repository Structure
```text
├── .github/ISSUE_TEMPLATE/  # Submission form configuration
├── docs/
│   └── index.html           # Website Frontend (Plotly, PapaParse, Bootstrap)
├── results/
│   └── benchmark.csv        # Central Data Source (Update this to add models)
└── README.md                # Project Documentation

## 🚀 How to Submit Results
We welcome contributions from researchers and developers. To add your model to the leaderboard:

1. Prepare Data: Ensure your results are calculated using the TMMLU+ methodology and formatted to match results/benchmark.csv.

2. Submit an Issue: Click the "Submit Your Model Results" button on the live leaderboard website to fill out a pre-formatted request.

3. Pull Request: Alternatively, fork this repo, add your model's column to the CSV, and submit a PR.

Maintained by: Muhammad Saqlain Aslam

Built for the Traditional Chinese NLP Community.
