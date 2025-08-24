# Cricket World Cup 2023 Analysis

A complete data analysis project on CWC 2023 performance metrics, including batting and bowling data cleaning, visualizations, and deployment as a responsive dashboard using Flask, Docker, and Render with CI/CD.

![Python](https://img.shields.io/badge/python-3.11-blue.svg) ![Flask](https://img.shields.io/badge/flask-2.0-lightgrey.svg) ![Docker](https://img.shields.io/badge/docker-ready-blue.svg) ![Render](https://img.shields.io/badge/deployed%20on-Render-green.svg) ![License](https://img.shields.io/badge/license-MIT-yellow.svg) ![Status](https://img.shields.io/badge/status-active-success.svg) 

##  Live Demo
Explore the dashboard live at:  
https://cwc-23-analysis-1.onrender.com

##  Project Overview

This repository captures the entire lifecycle of a data science project—from raw data to a live web app:

1. **Data Cleaning & Exploration**  
   - `cleaning_batting_summary.ipynb` and `cleaning_bowling_summary.ipynb` convert raw match summary data (`batting_summary.csv`, `bowling_summary.csv`) into tidy datasets (`cleaned_batsman_data.csv`, `cleaned_bowlers_data.csv`).

2. **Data Analysis & Visualization**  
   - `analysis.ipynb` performs exploratory analysis and generates interactive Plotly charts (e.g., most runs, boundaries, averages).
   - Visuals are exported as standalone HTML files located in the `templates/` directory.

3. **Web Dashboard**  
   - `app.py` uses Flask to serve an `index.html` dashboard linking to each interactive plot.
   - The dashboard UI is responsive and minimalist—built with semantic HTML and CSS for quick navigation.

4. **Containerization & Deployment**  
   - `Dockerfile` packages the Flask app in a lightweight Python 3.11 container.
   - `render.yaml` (infrastructure-as-code) enables seamless CI/CD deployment on Render. Every push to GitHub triggers a rebuild and deployment.

## Repository Structure
```
├── app.py                 # Flask server setup
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker container definition
├── render.yaml            # Render deployment config
├── templates/             # HTML plot files + index.html
│   ├── index.html
│   ├── highest_avg.html
│   ├── most_runs.html
│   └── ... other plots
├── *.ipynb                # Jupyter notebooks (cleaning + analysis)
├── *.csv                  # Raw and cleaned data files
```

##  How to Run Locally

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
2. **Launch Flask Server**
   ```bash
   python app.py
3. **Run with Docker**
   ```bash
   docker build -t cwc23-flask .
   docker run -p 5000:5000 cwc23-flask

