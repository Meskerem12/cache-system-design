# Student Data Cache System

This project implements three cache eviction policies (FIFO, LRU, LFU) to optimize retrieval of student records from a CSV dataset. It also includes a Redis-based fixed-window rate limiter to simulate request throttling.

---

## Overview

Retrieving data from large CSV files can be slow. This project:

- Implements FIFO (First-In-First-Out), LRU (Least Recently Used), and LFU (Least Frequently Used) cache policies.
- Demonstrates speed improvement when using caches versus direct CSV reads.
- Simulates cache hits and misses to illustrate how eviction policies work.
- Includes a Redis-based rate limiter to restrict user requests per time window.

---

## Features

- **FIFO Cache**: Evicts the oldest inserted record when capacity is exceeded.
- **LRU Cache**: Evicts the least recently used record. Accessing a record updates its recency.
- **LFU Cache**: Evicts the least frequently accessed record. Ties are broken by insertion order.
- **Cache Timing Test**: Compares retrieval speed from CSV and caches.
- **Redis Rate Limiter**: Limits the number of requests a user can make per time window.

---

## Project Structure

```text
cache-system-design/
├─ data/
│   └─ student_dataset.csv       # CSV file with student records
├─ src/
│   ├─ load_data.py              # Function to load CSV into dictionary
│   ├─ fifo_cache.py             # FIFO Cache implementation
│   ├─ lru_cache.py              # LRU Cache implementation
│   ├─ lfu_cache.py              # LFU Cache implementation
│   ├─ redis_rate_limiter.py     # Redis fixed-window rate limiter
│   ├─ test_cache.py             # Cache hit/miss simulation and timing
│   └─ test_retrieval_time.py    # Concise timing comparison
└─ README.md
