# AI 101 — 101-Day Roadmap

> **101 days. One journey. Real skills.**
>
> A hands-on roadmap for learning Applied AI, LLM application development, automation, agents, RAG, multimodal AI, production engineering, applied ML, and AI product skills.

---

# How to Use This Roadmap

This roadmap is designed around:

**Learn → Practice → Build → Test → Evaluate → Improve → Document → Explain**

The day ranges are targets, not deadlines. A stage is complete when its practical objectives and deliverables are completed.

The goal is **not** to finish every course. The goal is to develop skills that can be demonstrated through working projects, experiments, evaluations, deployments, and documentation.

---

# Stage 00 — Setup

**Days 1–3**

## Objective

Set up the development environment and establish the workflow that will be used throughout AI 101.

## Learn

- Python virtual environments
- Package management
- API keys
- `.env` files
- Basic API requests
- Logging
- Git workflow
- GitHub repository workflow

## Resources

- Python Tutorial
- Pro Git
- GitHub Getting Started
- OpenAI API Documentation
- Anthropic Documentation

See [RESOURCES.md](RESOURCES.md) for links and study guidance.

## Build

Create a Python script that:

1. Loads an API key from `.env`.
2. Calls an LLM API.
3. Sends a simple prompt.
4. Receives the response.
5. Logs the response.
6. Handles basic API errors.

## Deliverables

- Working Python environment
- `.env.example`
- First LLM API script
- Git repository initialized
- Initial GitHub push
- First meaningful commit

---

# Stage 01 — LLMs, Prompting & Structured Outputs

**Days 4–13**

## Objective

Understand how modern LLM applications work and learn to produce reliable structured outputs.

## Learn

### LLM Fundamentals

- Tokens
- Context windows
- Temperature
- Inference
- Hallucinations
- Basic transformer concepts

### Prompting

- System prompts
- User prompts
- Clear instructions
- Context
- Delimiters
- Few-shot examples
- Prompt iteration

### Structured Outputs

- JSON outputs
- Schemas
- Pydantic validation
- Invalid output handling
- Retries
- Function/tool calling

## Resources

- Andrej Karpathy — Intro to Large Language Models
- DeepLearning.AI — ChatGPT Prompt Engineering for Developers
- Hugging Face LLM Course
- Pydantic documentation
- OpenAI documentation
- Anthropic documentation

## Build

### Messy Email → Validated JSON Extractor

Input:

```text
Messy natural-language email
```

Output:

```json
{
  "customer": "...",
  "request_type": "...",
  "priority": "...",
  "deadline": "...",
  "summary": "..."
}
```

The system should:

- Call an LLM.
- Request structured output.
- Validate the result.
- Handle invalid output.
- Retry when appropriate.
- Log failures.

## Deliverables

- Working extractor
- Prompt experiments
- Pydantic schema
- Validation logic
- Error handling
- README documenting the approach

---

# Stage 02 — Workflows, Integrations & Agents

**Days 14–27**

## Objective

Learn how AI connects to external systems and understand the difference between deterministic workflows and agents.

## Learn

### Workflows

- Sequential workflows
- Conditional logic
- State
- Triggers
- Webhooks
- API integrations

### Automation

- Email
- Google Sheets
- Slack
- WhatsApp
- HTTP APIs
- n8n

### Agents

- Workflow vs agent
- Tools
- Tool calling
- Agent loops
- Planning
- Memory
- Stopping conditions
- Human approval
- Prompt-injection awareness

## Resources

- Anthropic — Building Effective Agents
- n8n documentation
- WhatsApp Cloud API documentation
- Hugging Face Agents Course
- Hugging Face Agents Course Unit 1
- Microsoft AI Agents for Beginners — optional

## Build

### AI Email / Lead Triage Automation

Example:

```text
Incoming Email
      ↓
LLM
      ↓
Classify / Extract
      ↓
Decision
      ↓
Google Sheets
      ↓
Optional Notification
```

Build the same core automation:

1. Once using Python.
2. Once using n8n.

Then compare:

- Complexity
- Flexibility
- Maintainability
- Development speed
- Integration effort

## Deliverables

- Code-based automation
- n8n workflow
- External integration
- Tool-calling example
- Agent/workflow comparison
- Error handling
- Basic prompt-injection notes

---

# Stage 03 — Evaluation & Observability

**Days 28–35**

## Objective

Learn to measure AI application quality instead of relying on subjective impressions.

## Learn

- Test datasets
- Expected outputs
- Pass/fail criteria
- Error categorization
- Failure analysis
- LLM-as-judge
- Limitations of LLM-as-judge
- Regression testing
- Prompt versioning
- Tracing
- Logging
- Latency and token tracking

## Resources

- DeepLearning.AI — Building Systems with the ChatGPT API
- Hamel Husain — Your AI Product Needs Evals
- Langfuse
- Ragas

## Build

### Evaluation Suite

Create a **30–50 case test set** for the Stage 02 automation.

For each case record:

| Field | Purpose |
|---|---|
| Input | Original test case |
| Expected result | Correct behavior |
| Actual result | System output |
| Pass/Fail | Evaluation |
| Failure category | Type of error |
| Prompt/model version | Reproducibility |

Run the evaluation:

1. Before improvements.
2. After prompt/system changes.

## Deliverables

- Test dataset
- Scoring script
- Failure categories
- Before/after results
- Evaluation README
- Basic tracing/logging

---

# Stage 04 — RAG Engineering

**Days 36–51**

## Objective

Build reliable document-grounded AI systems and understand how retrieval design affects answer quality.

## Learn

### Retrieval Foundations

- Embeddings
- Semantic similarity
- Vector stores
- Similarity search

### Document Processing

- PDF parsing
- Tables
- Text extraction
- Document structure
- Metadata

### Retrieval Engineering

- Chunking
- Chunk size
- Chunk overlap
- Metadata filtering
- Keyword search
- Vector search
- Hybrid search
- Reranking

### Answer Quality

- Context selection
- Citations
- Grounding
- "I don't know" behavior
- Retrieval failures
- RAG evaluation

## Resources

- DeepLearning.AI — Understanding and Applying Text Embeddings
- DeepLearning.AI — Building Applications with Vector Databases
- DeepLearning.AI — Retrieval-Augmented Generation
- Chroma documentation
- pgvector
- Docling
- Unstructured

## Build

### Document Q&A with Citations

The system should:

```text
Documents
   ↓
Parsing
   ↓
Chunking
   ↓
Metadata
   ↓
Embeddings
   ↓
Retrieval
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer + Citations
```

It should also respond appropriately when the available evidence is insufficient.

## Evaluate

Reuse the evaluation approach from Stage 03.

Measure:

- Retrieval quality
- Answer quality
- Citation correctness
- Failure cases
- "I don't know" behavior

## Milestone

Get **one real user** to try the application by the end of this stage.

## Deliverables

- RAG application
- Document ingestion pipeline
- Vector store
- Retrieval experiments
- Evaluation results
- Citation support
- Documentation

---

# Stage 05 — Multimodal Extraction

**Days 52–57**

## Objective

Understand how AI systems process images and visual documents, and compare OCR with vision models.

## Learn

- Vision-model inputs
- Invoice extraction
- Form extraction
- OCR
- OCR vs vision models
- Accuracy
- Cost
- Speed
- Confidence checks
- Human-review fallbacks
- Image preprocessing

## Resources

- OpenAI documentation — vision inputs
- Anthropic documentation — vision inputs
- Tesseract documentation
- OpenCV documentation

## Build

### Invoice Extractor

Input:

```text
Invoice image / PDF
```

Output:

```json
{
  "vendor": "...",
  "invoice_number": "...",
  "date": "...",
  "total": "...",
  "items": []
}
```

Create a labeled sample and measure extraction accuracy.

Compare:

```text
OCR
vs
Vision Model
```

## Deliverables

- Invoice extraction application
- Labeled test sample
- Accuracy results
- OCR experiment
- Vision-model experiment
- Human-review fallback
- Comparison report

---

# Stage 06 — Production AI Engineering

**Days 58–73**

## Objective

Turn an AI prototype into a more reliable, testable, secure, and deployable application.

## Learn

### APIs

- FastAPI
- Request validation
- Response validation
- Error handling
- API architecture

### Deployment

- Docker
- Containers
- Cloud deployment
- Environment configuration
- CI/CD

### Reliability

- Retries
- Timeouts
- Logging
- Monitoring
- Failure handling

### Performance

- Latency
- Token budgets
- Model selection
- Caching
- Cost control

### Security

- API key protection
- Prompt injection
- Data leakage
- Insecure outputs
- Guardrails

### Java Integration

- Spring Boot
- REST APIs
- HTTP clients
- LLM integration

## Resources

- FastAPI documentation
- Docker documentation
- GitHub Actions documentation
- OWASP Top 10 for LLM Applications
- Render documentation or Railway
- Spring Boot documentation
- Chip Huyen — AI Engineering

## Build

### Production AI Application

Take the strongest project from earlier stages and make it production-oriented.

Target architecture:

```text
Client
  ↓
API
  ↓
AI Application
  ↓
LLM / RAG / Tools
  ↓
Database / External Services
```

Include:

- API
- Validation
- Tests
- Docker
- CI
- Logging
- Error handling
- Deployment
- Basic security
- Cost/latency considerations

### Additional Build

Create a small:

```text
Spring Boot → LLM API
```

integration.

## Deliverables

- Production-oriented application
- API
- Automated tests
- Docker configuration
- CI workflow
- Deployment
- Logging
- Security notes
- Spring Boot integration
- Architecture documentation

---

# Stage 07 — Applied ML Survey

**Days 74–77**

## Objective

Understand enough practical machine learning to choose between traditional ML and modern AI approaches.

## Learn

- Training
- Validation
- Testing
- Classification
- Regression
- Metrics
- Overfitting
- Error analysis
- Baseline models
- Prompting vs RAG vs fine-tuning
- Traditional ML vs LLM-based approaches

## Resources

- Google Machine Learning Crash Course — selected lessons
- Hugging Face LLM Course — relevant model/fine-tuning sections

## Build

### 1. Small Baseline ML Model

Train and evaluate a basic model.

### 2. Decision Guide

Create a one-page guide in your own words:

```text
Prompting
    ↓
When?
    ↓
RAG
    ↓
When?
    ↓
Fine-tuning
    ↓
When?
    ↓
Traditional ML
    ↓
When?
```

## Deliverables

- Dataset
- Baseline model
- Evaluation results
- Error analysis
- Decision guide

---

# Stage 08 — AI Product & Freelance Skills

**Days 78–85**

## Objective

Learn how to turn an AI capability into a clearly scoped, deliverable project.

## Learn

- Problem discovery
- Requirements gathering
- Scope definition
- Estimation
- Fixed-price projects
- Hourly projects
- Value-based pricing concepts
- Proposals
- Scope creep
- Handover
- Maintenance
- Case studies

## Resources

- Jonathan Stark — *Ditching Hourly*
- Brennan Dunn — pricing and proposal material
- Upwork listings
- Fiverr listings

## Build

Create:

- AI project proposal template
- Requirements/scoping checklist
- Pricing/estimation worksheet
- Handover checklist
- Case study template

Create case studies for selected AI 101 projects.

## Deliverables

- Proposal template
- Scope checklist
- Estimation/pricing worksheet
- Handover checklist
- At least one case study

---

# Stage 09 — Independent Capstone

**Days 86–100**

## Objective

Independently design and build a realistic AI solution using the skills developed throughout AI 101.

## Rule

No new course is required.

Use documentation only when a specific technical problem appears.

## Choose a Realistic Problem

Possible contexts:

- Clinic
- Small shop
- Agency
- Manufacturing business
- Internal business operations
- Document-heavy workflow

The final problem should be selected independently.

## Phase 1 — Problem Definition

Document:

- User
- Problem
- Current workflow
- Pain point
- Proposed solution

## Phase 2 — Requirements

Define:

- Functional requirements
- Non-functional requirements
- Success criteria
- Constraints

## Phase 3 — Architecture

Document:

- Components
- APIs
- Models
- Database/vector store
- External services
- Data flow

## Phase 4 — Implementation

Build a working application.

## Phase 5 — Evaluation

Measure where practical:

- Accuracy
- Reliability
- Latency
- Cost
- Failure cases

## Phase 6 — Deployment

Deploy a usable version where practical.

## Phase 7 — Handover

Provide:

- Setup instructions
- Configuration
- Environment variables
- API documentation
- Maintenance notes

## Phase 8 — Case Study

Document:

- Problem
- Solution
- Architecture
- Results
- Limitations
- Lessons learned

## Capstone Deliverables

- Working application
- Source code
- README
- Architecture documentation
- Evaluation dataset/results
- Deployment
- Handover documentation
- Published case study

---

# Stage 10 — Final Demo & Review

**Day 101**

## Objective

Demonstrate the skills developed during the 101-day journey and identify the next learning direction.

## Final Review

Answer:

- What can I explain without notes?
- What can I build independently?
- What can I debug independently?
- Which AI architectures do I understand?
- What failures did I encounter?
- How did I evaluate my systems?
- What can I demonstrate?
- What do I still need to learn?

## Final Demonstration

Present:

1. The capstone problem.
2. The architecture.
3. The implementation.
4. The evaluation.
5. The deployment.
6. The major challenges.
7. The improvements made.
8. The limitations.
9. What I learned.

## Final Deliverables

- Capstone demo
- Final README
- Evaluation results
- Case study
- Learning retrospective
- Next-step learning plan

---

# Cross-Stage Learning Habits

These practices should continue throughout all 101 days.

## Active Recall

Before checking notes, try to explain the concept from memory.

## Build Before Perfecting

Create a small working version before optimizing it.

## Keep a Failure Log

Record:

- Error
- Cause
- Investigation
- Fix
- Lesson

## Evaluate Changes

Whenever possible, compare:

```text
Before
vs
After
```

## Document Decisions

For meaningful technical choices, record:

- What I chose
- Why I chose it
- Alternatives considered
- Trade-offs
- Result

## Use Git Meaningfully

Commit working milestones rather than making empty daily commits.

Example:

```text
feat: add structured email extraction
fix: handle invalid JSON responses
test: add extraction evaluation cases
docs: document prompt experiments
refactor: separate LLM client from parser
```

---

# Proof-of-Work Standard

A Git commit proves that a change was made.

It does not prove mastery.

The repository should progressively contain evidence such as:

- Working code
- Experiments
- Tests
- Evaluation datasets
- Results
- Failure analysis
- Architecture diagrams
- Deployment configuration
- Case studies
- Reflections
- Meaningful Git history

The goal is to show the complete engineering process:

```text
Learn
  ↓
Build
  ↓
Fail
  ↓
Investigate
  ↓
Fix
  ↓
Measure
  ↓
Improve
  ↓
Deploy
  ↓
Explain
```

---

# Completion Criteria

A stage is considered complete when:

- The core concepts have been studied.
- The practical build has been completed.
- The implementation has been tested.
- Important failures have been documented.
- Results have been evaluated where appropriate.
- The work is committed to Git.
- I can explain the main concepts in my own words.

The schedule can move if necessary.

**Understanding the skill is more important than obeying the calendar.**

---

# Final Outcome

At the end of AI 101, this repository should demonstrate:

```text
LLM Fundamentals
      ↓
Prompting
      ↓
Structured Outputs
      ↓
Automation
      ↓
Agents
      ↓
Evaluation
      ↓
RAG
      ↓
Multimodal AI
      ↓
Production Engineering
      ↓
Applied ML
      ↓
AI Product Skills
      ↓
Independent Capstone
```

The objective is not to claim mastery of every area.

The objective is to finish the 101 days with a strong practical foundation, real projects, measurable experiments, and the ability to continue learning independently.
