# AI 101 — Learning Resources

> Resources mapped to the 101-day Applied AI and Automation roadmap.

The purpose of this file is to identify what I should learn from each resource, not to collect courses.

I will use documentation when I need it, study courses selectively, and prioritize implementation over completion.

---

# Stage 00 — Setup

**Days 1–3**

## What to Learn

- Python virtual environments
- Package management
- API keys
- `.env` files
- Git workflow
- Basic API requests
- Logging

## Python Tutorial

https://docs.python.org/3/tutorial/

### Use for

Python refresher and reference.

### Focus on

- Functions
- Data structures
- Modules
- File handling
- Exceptions
- Classes
- Packages

**Approach:** Skim only. I already have Python experience.

## Pro Git

https://git-scm.com/book/en/v2

### Use for

Git workflow and version control.

### Focus on

- Repositories
- Commits
- Branches
- Merging
- Remote repositories
- History
- `diff`

**Approach:** Skim only and use Git practically throughout the project.

## GitHub Getting Started

https://docs.github.com/en/get-started

### Use for

- Repository management
- GitHub workflow
- README files
- Pull requests
- Repository organization

**Approach:** Reference when needed rather than completing the entire documentation.

## OpenAI API Documentation

https://platform.openai.com/docs

### Use for

- API authentication
- Model requests
- Structured outputs
- Tool/function calling
- Vision inputs
- API usage patterns

## Anthropic Documentation

https://docs.claude.com

### Use for

- API authentication
- Prompting
- Structured outputs
- Tool use
- Vision inputs

### Stage 00 Build

Create a Python script that:

1. Loads an API key from `.env`.
2. Calls an LLM API.
3. Sends a simple prompt.
4. Receives the response.
5. Logs the response.
6. Handles basic errors.

---

# Stage 01 — LLMs, Prompting & Structured Outputs

**Days 4–13**

## What to Learn

- Tokens
- Context windows
- Temperature
- Hallucinations
- System prompts
- User prompts
- Few-shot examples
- Delimiters
- Structured outputs
- JSON schemas
- Validation
- Retries
- Function calling

## Andrej Karpathy — Intro to Large Language Models

Search:

**"Andrej Karpathy Intro to Large Language Models"**

### Use for

Building a conceptual mental model of:

- What LLMs are
- Training
- Tokens
- Transformers
- Inference
- How LLM applications work

## DeepLearning.AI — ChatGPT Prompt Engineering for Developers

https://www.deeplearning.ai/courses/chatgpt-prompt-engineering-for-developers/

### Focus on

- Clear instructions
- Context
- Few-shot examples
- Summarization
- Classification
- Information extraction
- Transformation

**Approach:** Warm-up/reference. Do not spend excessive time completing the whole course.

## Hugging Face LLM Course

https://huggingface.co/learn/llm-course/chapter0/1

### Focus on the early chapters

- LLM fundamentals
- Transformers
- Tokenizers
- Models
- Inference

**Approach:** Build conceptual understanding rather than attempting the entire course.

## Pydantic

https://docs.pydantic.dev

### Focus on

- Models
- Fields
- Validation
- Type handling
- JSON/schema validation

## OpenAI Documentation

https://platform.openai.com/docs

### Focus on

- Prompting
- Structured outputs
- Tool/function calling

## Anthropic Documentation

https://docs.claude.com

### Focus on

- Prompting
- Structured outputs
- Tool use

### Stage 01 Build

**Messy Email → Validated JSON**

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

The application should validate the output and retry or handle invalid responses.

---

# Stage 02 — Workflows, Integrations & Agents

**Days 14–27**

## What to Learn

- Workflow vs agent
- Tool calling
- Webhooks
- APIs
- Email automation
- Google Sheets
- Slack
- WhatsApp
- n8n
- Prompt-injection awareness

## Anthropic — Building Effective Agents

https://www.anthropic.com/engineering/building-effective-agents

### Focus on

- Workflows
- Agents
- When to use workflows
- When to use agents
- Tool use
- Simplicity vs complexity

## n8n Documentation

https://docs.n8n.io

### Focus on

- Workflows
- Nodes
- Triggers
- Webhooks
- HTTP requests
- Credentials
- Expressions
- AI nodes
- Error handling

### Practical goal

Build the same basic automation:

1. Once using Python.
2. Once using n8n.

Compare the two approaches.

## WhatsApp Cloud API

https://developers.facebook.com/docs/whatsapp/cloud-api

### Focus on

- Sending messages
- Receiving messages
- Webhooks
- Authentication
- Message payloads

Use only if the project requires WhatsApp integration.

## Hugging Face Agents Course

https://huggingface.co/learn/agents-course

### Focus on

- Agents
- Tools
- Agent loops
- Tool execution
- Agent architecture

### Required section

**Unit 1 — Introduction**

https://huggingface.co/learn/agents-course/unit1/introduction

## Microsoft — AI Agents for Beginners

https://github.com/microsoft/ai-agents-for-beginners

### Use for

Additional explanations and examples of:

- Agents
- Tools
- Memory
- Planning
- Multi-agent systems

**Status:** Optional.

### Stage 02 Build

**AI Email / Lead Triage Automation**

Example flow:

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
Optional notification
```

Build the workflow both:

- In code
- In n8n

---

# Stage 03 — Evaluation & Observability

**Days 28–35**

## What to Learn

- Test sets
- Expected outputs
- Error categorization
- LLM-as-judge
- Regression testing
- Tracing
- Logging
- Before/after comparison

## DeepLearning.AI — Building Systems with the ChatGPT API

https://www.deeplearning.ai/courses/building-systems-with-the-chatgpt-api/

### Focus on

- Multi-step systems
- Evaluation
- Classification
- Processing pipelines
- System design

## Hamel Husain — Your AI Product Needs Evals

https://hamel.dev/blog/posts/evals/

### Focus on

- Why evaluations matter
- Creating useful test cases
- Error analysis
- Evaluating AI products

## Langfuse

https://langfuse.com/docs

### Focus on

- Tracing
- Observability
- LLM calls
- Latency
- Token usage
- Debugging

## Ragas

https://docs.ragas.io

### Focus on

- RAG evaluation
- Retrieval evaluation
- Answer evaluation
- Metrics

### Stage 03 Build

Create a **30–50 case evaluation dataset** for the Stage 02 project.

Track:

- Expected result
- Actual result
- Pass/fail
- Failure category
- Model/prompt version

Run the test before and after changes.

---

# Stage 04 — RAG Engineering

**Days 36–51**

## What to Learn

- Embeddings
- Vector stores
- PDF parsing
- Tables
- Chunking
- Metadata
- Keyword search
- Vector search
- Hybrid search
- Reranking
- Citations
- "I don't know" behavior

## DeepLearning.AI — Understanding and Applying Text Embeddings

https://www.deeplearning.ai/courses/understanding-and-applying-text-embeddings/

### Focus on

- Embeddings
- Semantic similarity
- Retrieval

## DeepLearning.AI — Building Applications with Vector Databases

https://www.deeplearning.ai/courses/building-applications-vector-databases/

### Focus on

- Vector databases
- Indexing
- Similarity search
- Retrieval

## DeepLearning.AI — Retrieval-Augmented Generation

https://www.deeplearning.ai/courses/retrieval-augmented-generation/

### Focus on

- RAG architecture
- Document ingestion
- Retrieval
- Context construction
- Generation

## Chroma

https://docs.trychroma.com

### Use for

- Vector storage
- Collections
- Embeddings
- Similarity search

## pgvector

https://github.com/pgvector/pgvector

### Use for

Vector search inside PostgreSQL.

This is particularly useful because of my existing SQL/MySQL background.

## Docling

Search:

**"Docling official documentation"**

### Use for

- PDF parsing
- Document structure
- Tables
- Document conversion

## Unstructured

Search:

**"Unstructured official documentation"**

### Use for

- Document parsing
- PDF processing
- Structured document elements

### Stage 04 Build

**Document Q&A with Citations**

The system should:

1. Load documents.
2. Parse them.
3. Split them into chunks.
4. Add metadata.
5. Generate embeddings.
6. Retrieve relevant content.
7. Generate an answer.
8. Provide citations.
9. Say "I don't know" when evidence is insufficient.

Evaluate it using the Stage 03 evaluation approach.

### Milestone

Get **one real user** to try the application by the end of this stage.

---

# Stage 05 — Multimodal Extraction

**Days 52–57**

## What to Learn

- Vision model inputs
- Invoice extraction
- Form extraction
- OCR
- OCR vs vision models
- Cost
- Speed
- Accuracy
- Confidence checks
- Human review

## OpenAI Documentation

https://platform.openai.com/docs

### Focus on

Vision/image inputs and structured extraction.

## Anthropic Documentation

https://docs.claude.com

### Focus on

Vision/image inputs and structured extraction.

## Tesseract OCR

https://tesseract-ocr.github.io/

### Focus on

- OCR
- Text extraction
- Image preprocessing

## OpenCV Documentation

https://docs.opencv.org/

### Focus on

- Resizing
- Cropping
- Thresholding
- Denoising
- Image preprocessing

Existing OpenCV knowledge can be used here rather than relearning the basics.

### Stage 05 Build

**Invoice Extractor**

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

Measure accuracy against a labeled sample.

Compare:

```text
OCR
vs
Vision Model
```

---

# Stage 06 — Production AI Engineering

**Days 58–73**

## What to Learn

- API serving
- FastAPI
- Docker
- Deployment
- CI
- Cost
- Latency
- Caching
- Model selection
- Token budgets
- Retries
- Error handling
- Logging
- Monitoring
- API security
- Prompt injection
- Data leakage
- Guardrails
- Spring Boot integration

## FastAPI

https://fastapi.tiangolo.com/tutorial/

### Focus on

- Routes
- Request models
- Response models
- Validation
- Error handling
- Dependencies
- Testing

## Docker

https://docs.docker.com/get-started/

### Focus on

- Images
- Containers
- Dockerfiles
- Builds
- Environment variables
- Networking

## GitHub Actions

https://docs.github.com/en/actions

### Focus on

- Workflows
- Jobs
- Steps
- Automated tests
- CI

## OWASP Top 10 for LLM Applications

https://genai.owasp.org/llm-top-10/

### Focus on

- Prompt injection
- Sensitive information disclosure
- Excessive agency
- Insecure output handling
- Other major LLM application risks

## Render Documentation

https://render.com/docs

### Use for

Learning one practical deployment path.

Alternative:

**Railway**

Search: `Railway official documentation`

## Spring Boot

https://spring.io/projects/spring-boot

### Focus on

- REST APIs
- Configuration
- Dependency injection
- HTTP clients
- Testing

### Apply

Build a Spring Boot service that communicates with an LLM API.

## Chip Huyen — AI Engineering

**Book:** *AI Engineering*

### Use for

Reference material on:

- AI application architecture
- Model selection
- Evaluation
- Deployment
- AI engineering practices

Do not attempt to read the entire book during the 101 days unless it fits naturally into the schedule.

### Stage 06 Build

Take the strongest AI project from previous stages and turn it into a deployable application.

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
External Services / Database
```

Include:

- Tests
- Docker
- CI
- Logging
- Error handling
- Deployment
- Basic security

Also build a small **Spring Boot → LLM** integration.

---

# Stage 07 — Applied ML Survey

**Days 74–77**

## What to Learn

- Training
- Validation
- Testing
- Error analysis
- Basic classification/regression
- Prompting vs RAG vs fine-tuning

## Google Machine Learning Crash Course

https://developers.google.com/machine-learning/crash-course

### Study selectively

Focus on:

- Classification
- Regression
- Dataset preparation
- Training
- Validation
- Metrics
- Overfitting
- Error analysis

Do not attempt to complete the entire course during this stage.

## Hugging Face LLM Course

https://huggingface.co/learn/llm-course/chapter0/1

### Focus on

Relevant model and fine-tuning sections.

### Stage 07 Build

Build:

1. A small baseline ML model.
2. A one-page decision guide comparing:

```text
Prompting
RAG
Fine-tuning
Traditional ML
```

The guide should be written in my own words.

---

# Stage 08 — AI Product & Freelance Skills

**Days 78–85**

## What to Learn

- Turning vague AI requests into defined projects
- Requirements gathering
- Scope definition
- Estimation
- Fixed-price vs hourly work
- Value-based pricing concepts
- Proposals
- Scope creep
- Handover
- Maintenance
- Case studies

## Jonathan Stark — Ditching Hourly

**Book:** *Ditching Hourly*

### Use for

Understanding alternative approaches to pricing professional services.

## Brennan Dunn

Search:

**"Brennan Dunn pricing proposals consulting"**

### Use for

- Proposals
- Pricing
- Client communication
- Scope definition

## Upwork

https://www.upwork.com

### Use for

Observing what clients actually request.

Look for:

- AI automation
- Chatbots
- Document processing
- RAG
- Workflow automation
- API integration

Do not copy listings. Use them to understand real-world requirements.

## Fiverr

https://www.fiverr.com

### Use for

Understanding how AI automation services are described and packaged.

### Stage 08 Build

Create:

- AI project proposal template
- Requirements/scoping checklist
- Pricing/estimation worksheet
- Handover checklist
- Case study template

Create case studies for selected projects from AI 101.

---

# Stage 09 — Independent Capstone

**Days 86–100**

## Learning Approach

No new course is required.

Use documentation only when a specific technical problem appears.

## Possible Business Contexts

Choose one realistic problem such as:

- Clinic
- Small shop
- Agency
- Manufacturing business
- Internal business operations
- Document-heavy workflow

The exact problem should be chosen independently.

## Capstone Requirements

### 1. Problem

Define:

- User
- Problem
- Current workflow
- Pain point
- Proposed solution

### 2. Requirements

Define:

- Functional requirements
- Non-functional requirements
- Success criteria
- Constraints

### 3. Architecture

Document:

- Components
- APIs
- Models
- Database/vector store
- External services
- Data flow

### 4. Implementation

Build a working application.

### 5. Evaluation

Measure:

- Accuracy
- Reliability
- Latency
- Cost where practical
- Failure cases

### 6. Deployment

Deploy a usable version where practical.

### 7. Handover

Provide:

- Setup instructions
- Configuration
- Environment variables
- API documentation
- Maintenance notes

### 8. Case Study

Document:

- Problem
- Solution
- Architecture
- Results
- Limitations
- Lessons learned

---

# Stage 10 — Final Demo & Review

**Day 101**

## Review

Answer:

- What can I explain without notes?
- What can I build independently?
- What can I debug independently?
- Which AI architectures do I understand?
- What failures did I encounter?
- How did I evaluate my systems?
- What can I demonstrate?
- What do I still need to learn?

---

# Resource Rules

## 1. Do not complete courses for the sake of completion.

A resource is a tool, not the goal.

## 2. Prefer official documentation for implementation.

Use courses for concepts and documentation for actual development.

## 3. Build immediately.

Do not spend several days watching content before writing code.

## 4. Search when stuck.

If the documentation does not answer a specific implementation question, search for the specific problem.

## 5. Avoid resource accumulation.

Do not add another course simply because it looks interesting.

## 6. Reuse knowledge.

Every new stage should improve or extend something already built where practical.

## 7. Document failures.

Errors, failed experiments, and fixes are part of the proof of learning.

---

# Resource Priority

## Core

These are the main resources:

- OpenAI documentation
- Anthropic documentation
- Python documentation
- Pro Git
- DeepLearning.AI Prompt Engineering
- Hugging Face LLM Course
- Hugging Face Agents Course
- Anthropic Building Effective Agents
- n8n documentation
- DeepLearning.AI Building Systems
- Hamel Husain Evals
- Langfuse
- Ragas
- DeepLearning.AI Embeddings
- DeepLearning.AI Vector Databases
- DeepLearning.AI RAG
- Chroma
- pgvector
- FastAPI
- Docker
- GitHub Actions
- OWASP LLM Top 10
- Spring Boot
- Google ML Crash Course

## Supporting / Optional

- Microsoft AI Agents for Beginners
- Full Stack Deep Learning
- Chip Huyen — AI Engineering
- Brennan Dunn
- Jonathan Stark
- Upwork
- Fiverr

---

# Resource Completion Philosophy

I do not need to finish every resource.

Instead:

```text
Resource
   ↓
Relevant concept
   ↓
Implementation
   ↓
Experiment
   ↓
Evaluation
   ↓
Documentation
```

**The goal is not to finish links.**

**The goal is to gain skills I can demonstrate.**
