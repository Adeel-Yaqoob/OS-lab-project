# OS-lab-project

# Real-Time Interactive CPU Scheduling Simulator with Adaptive Feedback

## Overview

This project is a GUI-based CPU Scheduling Simulator developed in Python using CustomTkinter. The simulator demonstrates the working of different CPU scheduling algorithms in real-time with live visualization, performance metrics, and adaptive feedback.

The project was developed as a Complex Computing Problem (CCP) for the Operating Systems course at Bahria University.


# Features

- Real-time CPU scheduling simulation
- Interactive GUI using CustomTkinter
- Dynamic process insertion during execution
- Live Gantt Chart visualization
- Ready Queue and Completed Process tables
- Runtime algorithm switching
- Performance metrics calculation
- Adaptive scheduling recommendation engine
- Pause, Resume, and Reset functionality


# Scheduling Algorithms Implemented

- First Come First Served (FCFS)
- Shortest Job First (SJF)
- Shortest Remaining Time First (SRTF)
- Priority Scheduling
- Round Robin (RR)
- Multilevel Feedback Queue (MLFQ)


# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CustomTkinter | GUI development |
| Tkinter Canvas | Gantt chart visualization |
| Threading | Real-time simulation |
| OOP | Modular system design |

# Project Structure

```text
cpu_scheduler_simulator/
│
├── main.py
├── models.py
├── schedulers.py
├── simulation_engine.py
├── analytics.py
├── adaptive_engine.py
├── gantt.py
├── theme.py
└── requirements.txt
```

# File Description

| File Name | Purpose |
|---|---|
| main.py | Main executable GUI file |
| models.py | Process class definition |
| schedulers.py | Scheduling algorithms |
| simulation_engine.py | Core simulation logic |
| analytics.py | Performance metrics |
| adaptive_engine.py | Recommendation system |
| gantt.py | Gantt chart drawing |
| theme.py | GUI color theme |

# Installation

## Step 1: Install Python

Download Python from:

https://www.python.org/downloads/


## Step 2: Install Required Library

```bash
pip install customtkinter
```

---

# Running the Project

Run the following command:

```bash
python main.py
```

# Performance Metrics

The simulator calculates:

- Average Waiting Time
- Average Turnaround Time
- Response Time
- CPU Utilization
- Throughput
- Process Completion Order

# Adaptive Feedback Mechanism

The system analyzes workload conditions and provides recommendations for the most suitable scheduling algorithm based on:

- Waiting time
- Starvation detection
- CPU-bound workload
- Interactive workload behavior


# GUI Components

- Control Panel
- Ready Queue Table
- Completed Process Table
- Live Gantt Chart
- Metrics Panel
- Recommendation Terminal


# Learning Outcomes

This project helped in understanding:

- CPU scheduling algorithms
- Operating system concepts
- Threading and concurrency
- GUI development
- Performance analysis
- Object-Oriented Programming


# Author

Adeel Yaqoob  
BS Computer Science  
Operating Systems CCP Project  

