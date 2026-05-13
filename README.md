# ForgeMind — Continual Learning Operational AI System

## Overview

ForgeMind is a prototype continual-learning operational AI system designed to capture, verify, govern, and retrieve undocumented operational knowledge from workers in real time.

The system focuses on a core industrial AI problem:

> How can AI safely learn tribal knowledge from human workers without poisoning itself?

Instead of acting as a simple chatbot wrapper, ForgeMind introduces:

* operational memory
* conflict detection
* anti-poisoning workflows
* human review governance
* temporal memory
* continual knowledge integration

The project simulates a factory AI assistant that continuously improves through worker interactions.


**[Watch Demo Video](https://drive.google.com/file/d/1aG1McRpAZThrCny_Dxfc43QOWU34LP9g/view?usp=sharing)**


---

# Core Features

## Knowledge Acquisition

The system converts worker conversations into structured operational knowledge.

Example:

Worker says:

```text
Station 3 overheats after lunch on Tuesday.
Reduce current by 5%.
```

Extracted memory:

```json
{
  "entity": "station 3",
  "condition": "after lunch on Tuesday",
  "action": "reduce current by 5%",
  "outcome": "prevent overheating"
}
```

---

## Structured Operational Memory

Instead of storing raw chat history, ForgeMind stores:

* entity
* condition
* action
* outcome
* confidence
* source worker
* timestamp
* operational status

This creates operational memory instead of conversation logs.

---

## Verification Layer

Each operational claim receives:

* confidence scoring
* verification status

Possible statuses:

* accepted
* observed
* quarantined
* conflict

This prevents blind self-learning.

---

## Conflict Detection

The system detects contradictory operational knowledge.

Example:

Worker A:

```text
Reduce current by 5%
```

Worker B:

```text
Increase current by 5%
```

Result:

```json
{
  "status": "conflict",
  "confidence": 0.2
}
```

---

## Anti-Poisoning Workflow

Low-confidence or conflicting claims are quarantined instead of immediately trusted.

This prevents operational memory poisoning.

---

## Human Review Queue

Suspicious claims enter a supervisor review queue.

Supervisors can:

* approve claims
* reject claims

Endpoints:

* `/review_queue`
* `/approve/{claim_id}`
* `/reject/{claim_id}`

---

## Knowledge Supersession

When conflicting knowledge is approved:

* older contradictory knowledge is removed
* newer approved knowledge replaces it

This prevents contradictory operational retrieval.

---

## Temporal Memory

Operational memory includes timestamps.

Outdated knowledge can be ignored during retrieval to avoid stale operational behavior.

---

## Retrieval System

Workers can later retrieve learned operational knowledge.

Example:

```json
POST /ask
{
  "question": "Why is station 3 overheating?"
}
```

Response:

```text
Entity: station 3
Condition: after lunch on Tuesday
Action: increase current by 5%
Outcome: prevent overheating
```

---

## Metrics and Measurable Learning

The system tracks:

* accepted claims
* conflicts
* quarantined claims
* retrieval hits

Example:

```json
{
  "accepted_claims": 1,
  "conflicts": 1,
  "quarantined": 1,
  "retrieval_hits": 1
}
```

This demonstrates measurable continual learning behavior.

---

# System Architecture

```text
Worker Conversation
        ↓
Knowledge Extraction
        ↓
Verification Layer
        ↓
Conflict Detection
        ↓
Quarantine / Human Review
        ↓
Operational Memory
        ↓
Retrieval System
        ↓
Future Worker Conversations
```
<img src="/System_Architecture_and_Flow.png" width="700">

---

# Tech Stack

| Component    | Technology         |
| ------------ | ------------------ |
| Backend      | FastAPI            |
| Local LLM    | Ollama + TinyLlama |
| Language     | Python             |
| Memory Store | ChromaDB           |
| API Testing  | Swagger UI         |

---

# API Endpoints

| Endpoint                 | Purpose                             |
| ------------------------ | ----------------------------------- |
| POST /learn              | Learn from worker conversations     |
| POST /ask                | Retrieve operational knowledge      |
| GET /metrics             | View learning metrics               |
| GET /review_queue        | View quarantined/conflicting claims |
| POST /approve/{claim_id} | Approve a claim                     |
| POST /reject/{claim_id}  | Reject a claim                      |

---

# Example Tests

## Learning Operational Knowledge

```json
POST /learn
{
  "conversation": "Station 3 overheats after lunch on Tuesday. Reduce current by 5%.",
  "worker_id": "worker_1"
}
```

Result:

```json
{
  "status": "accepted",
  "confidence": 0.63
}
```

---

## Conflict Detection

```json
POST /learn
{
  "conversation": "Station 3 overheats after lunch on Tuesday. Increase current by 5%.",
  "worker_id": "worker_2"
}
```

Result:

```json
{
  "status": "conflict",
  "confidence": 0.2
}
```

---

# Current Limitations

This project is still a prototype.

Not yet implemented:

* semantic retrieval
* embedding-based memory
* contextual reasoning
* dynamic worker reputation
* GraphRAG
* real speech-to-text pipeline
* production dashboard

---

# Future Improvements

Planned future upgrades:

* vector search retrieval
* semantic memory layer
* adaptive trust scoring
* contextual operational reasoning
* real-time voice pipeline
* graph-based memory systems
* supervisor dashboard

---

# Run Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Ollama

```bash
ollama run tinyllama
```

---

## Start API

```bash
uvicorn app.main:app --reload
```

---

## Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Project Goal

ForgeMind focuses on operational knowledge governance rather than generic chatbot interaction.

The project explores:

* continual learning
* operational memory
* knowledge verification
* anti-poisoning systems
* conflict resolution
* human-in-the-loop AI governance

for industrial AI environments.
