# Support Ticket Issue Intelligence System

An AI-powered system that analyzes customer support tickets to automatically detect recurring issues and trends.

This project demonstrates how machine learning and natural language processing can help support teams understand customer problems at scale.

---

# Overview

Customer support teams receive thousands of tickets containing unstructured text.
Manually identifying recurring issues and monitoring trends is time-consuming.

This system automatically:

• preprocesses support ticket text
• generates semantic embeddings
• classifies ticket categories
• groups similar issues using clustering
• detects trends over time
• visualizes insights through an interactive dashboard

---

# System Architecture

Ticket Ingestion
↓
Text Preprocessing
↓
Embedding Generation
↓
Issue Classification (Logistic Regression)
↓
Issue Clustering (KMeans)
↓
Trend Detection
↓
FastAPI Backend
↓
Frontend Dashboard

---

# Features

### Automatic Issue Detection

Support tickets are grouped into clusters representing recurring issues.

### Ticket Classification

A Logistic Regression model classifies tickets into predefined categories using the **Ticket Type** label.

### Trend Analysis

The system compares issue frequency across time windows to determine whether issues are:

• Increasing
• Decreasing
• Stable

### Interactive Dashboard

The dashboard displays:

• total tickets
• issue clusters
• emerging issues
• ticket distribution
• issue trends

---

# Tech Stack

### Backend

Python
FastAPI
Pandas
Scikit-learn
Sentence Transformers

### Frontend

HTML
CSS
JavaScript
Chart.js

### Machine Learning

Sentence Embeddings
Logistic Regression Classification
KMeans Clustering

---

# Project Structure

```
support-ticket-intelligence
│
├── backend
│   ├── api.py
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── embeddings.py
│   ├── classification.py
│   ├── clustering.py
│   ├── issue_labeler.py
│   └── trend_detection.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data
│   └── support_tickets.csv
│
├── requirements.txt
└── README.md
```

---

# Running the Project

## 1. Install dependencies

```
pip install -r requirements.txt
```

---

## 2. Start Backend

```
uvicorn backend.api:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 3. Start Frontend

Navigate to the frontend folder:

```
cd frontend
```

Run a simple server:

```
python -m http.server 5500
```

Open the dashboard:

```
http://localhost:5500
```

---

# Example API Endpoints

### Get Issue Clusters

```
GET /issues
```

Example response:

```
[
 {
  "cluster": 1,
  "issue": "payment failure",
  "category": "Billing",
  "mentions": 1139
 }
]
```

---

### Get Issue Trends

```
GET /trends
```

Example response:

```
[
 {
  "cluster": 1,
  "previous": 10,
  "current": 15,
  "trend": "Increasing"
 }
]
```

---

# Example Dashboard Insights

The dashboard visualizes:

• issue clusters
• cluster distribution
• trend analysis
• example tickets



# Future Improvements

• real-time ticket ingestion
• advanced topic modeling (BERTopic)
• issue severity prediction
• alert system for emerging issues
• authentication and role-based access



