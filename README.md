# Intelligent Alert Optimization Layer

## Overview

This project implements an ML-powered decision layer designed to enhance a surveillance system.
It focuses on improving alert accuracy by integrating machine learning–based risk scoring and experimentation.

---

## Key Components

* **Event Simulation** – Generates structured behavioral data
* **ML Risk Scoring (Python)** – Predicts anomaly probability using Scikit-learn
* **Decision Engine (Java, Spring Boot)** – Triggers alerts based on model output
* **Experimentation Layer** – Compares rule-based vs ML-based strategies

---

## System Flow

```id="flow123"
Event → Risk Scoring → Decision → Alert → Evaluation
```

---

## Tech Stack

* Java, Spring Boot
* Python, Scikit-learn, FastAPI
* Pandas

---

## Example

Input:

```id="example123"
bet_amount = 8000  
win_rate = 0.9  
session_time = 20  
```

Output:

```id="output123"
risk_score = 0.82 → ALERT
```

---

## Purpose

This project demonstrates how to integrate machine learning into a backend system for real-time decision-making and strategy optimization.

---
