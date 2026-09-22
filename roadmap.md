
# AI 101 — 101-Day Learning Roadmap

## Overview

**Duration:** 101 days  
**Focus:** Applied AI, AI Engineering, and Automation  
**Approach:** Learn by building, testing, documenting, and explaining.

This roadmap is designed to move from foundational concepts to practical AI applications and an independent capstone project.

The schedule is a learning plan, not a guarantee of mastery. Topics may require additional practice depending on my understanding and implementation progress.

---

# Stage 00 — Setup and Skill Assessment

**Days 1–3**

### Objective
Prepare the development environment and assess my existing programming and Git skills.

### Topics
- Python fundamentals refresher
- Virtual environments and package management
- Git and GitHub workflow
- Project organization
- Basic debugging

### Practical Work
- Set up the project environment.
- Review Python functions, collections, files, and exceptions.
- Practice creating branches, commits, and a remote repository.
- Build a small Python utility without following a complete tutorial.

### Deliverables
- Working development environment
- Initial GitHub repository
- Python skill-check exercise
- Initial learning progress tracker

---

# Stage 01 — AI Foundations, LLMs, and RAG Basics

**Days 4–15**

### Objective
Understand the foundations of modern AI applications and build a basic LLM-powered application.

### Topics
- AI, machine learning, and deep learning
- Traditional ML vs. generative AI
- Neural networks at a conceptual level
- Large language models (LLMs)
- Tokens and context windows
- Model inference
- Prompt engineering
- Structured outputs
- Embeddings and semantic similarity
- Vector databases
- Retrieval-augmented generation (RAG)

### Practical Work
- Experiment with different prompts.
- Compare model responses.
- Generate structured outputs.
- Create embeddings and compare semantic similarity.
- Store and retrieve document chunks.
- Build a basic document question-answering application.

### Project
**AI Document Assistant — Version 1**

A basic application that accepts documents, retrieves relevant information, and answers user questions using the available context.

### Deliverables
- LLM and prompting experiments
- Embedding and retrieval exercises
- Basic RAG implementation
- Project documentation

---

# Stage 02 — Tools, Workflows, and AI Agents

**Days 16–25**

### Objective
Understand how AI applications use tools and execute controlled multi-step workflows.

### Topics
- Function and tool calling
- Tool schemas and input validation
- Workflow orchestration
- AI agents vs. fixed workflows
- State and memory
- Planning and execution
- Stopping conditions
- Error handling
- Human approval and control
- Agent limitations

### Practical Work
- Build a tool that an LLM can call.
- Validate tool inputs and outputs.
- Create a multi-step workflow.
- Add error handling and stopping conditions.
- Experiment with human approval before important actions.

### Project
**AI Document Assistant — Version 2**

Extend the document assistant with controlled tools and additional workflow capabilities.

### Deliverables
- Tool-calling examples
- Workflow implementation
- Agent experiment
- Updated document assistant

---

# Stage 03 — AI Evaluation and Reliability

**Days 26–35**

### Objective
Learn how to evaluate AI application behavior instead of relying only on subjective impressions.

### Topics
- AI evaluation fundamentals
- Test datasets and expected outcomes
- Retrieval quality
- Answer correctness and relevance
- Hallucination analysis
- Citation and grounding checks
- Regression testing
- Failure analysis
- Evaluation limitations

### Practical Work
- Create a fixed set of test questions.
- Record expected answers and relevant source documents.
- Test retrieval and answer quality.
- Identify common failure cases.
- Compare results before and after changes.
- Create repeatable evaluation scripts.

### Project
**AI Document Assistant — Evaluation Suite**

Build a small evaluation process for the document assistant.

### Deliverables
- Test dataset
- Evaluation script
- Results and failure analysis
- Documented improvements

---

# Stage 04 — RAG Engineering

**Days 36–47**

### Objective
Understand how retrieval design affects the quality and reliability of AI applications.

### Topics
- Document ingestion
- Text extraction and cleaning
- Chunking strategies
- Chunk size and overlap
- Metadata filtering
- Keyword retrieval
- Semantic retrieval
- Hybrid retrieval
- Reranking
- Context construction
- Source attribution and citations
- Retrieval failure analysis

### Practical Work
- Experiment with different chunk sizes.
- Compare chunking strategies.
- Add metadata to document chunks.
- Compare keyword and semantic retrieval.
- Experiment with hybrid retrieval.
- Evaluate reranking and citation behavior.

### Project
**AI Document Assistant — RAG Upgrade**

Improve retrieval quality and source-grounded answers using measured experiments.

### Deliverables
- Chunking comparison
- Retrieval experiments
- Updated RAG pipeline
- Evaluation results and documentation

---

# Stage 05 — Multimodal AI

**Days 48–61**

### Objective
Explore AI applications that work with more than text, particularly images and visual documents.

### Topics
- Multimodal AI fundamentals
- Vision-language models (VLMs)
- Image understanding
- OCR and document extraction
- Text and image inputs
- Traditional computer vision vs. VLMs
- Image-based question answering
- Visual document processing
- Multimodal evaluation
- Limitations of visual models

### Practical Work
- Experiment with image-question answering.
- Extract text from visual documents.
- Compare OCR-based extraction with vision-language models.
- Test visual reasoning on selected examples.
- Analyze errors and limitations.

### Project
**Visual Document Assistant**

Build a small application that can process visual documents or images and answer questions about their content.

### Deliverables
- Image and document experiments
- OCR/VLM comparison
- Working multimodal prototype
- Evaluation notes

---

# Stage 06 — Production AI Engineering

**Days 62–75**

### Objective
Learn how to turn an AI prototype into a more reliable, testable, and maintainable application.

### Topics
- Application architecture
- REST API development
- FastAPI fundamentals
- Request and response validation
- Configuration and environment variables
- API keys and secrets management
- Logging and error handling
- Unit and integration testing
- Latency and cost awareness
- Authentication and access control
- Docker fundamentals
- Deployment basics
- Monitoring and observability
- Continuous integration

### Practical Work
- Expose an AI application through an API.
- Validate incoming requests.
- Add structured error handling and logging.
- Write automated tests.
- Containerize the application.
- Deploy a working version where practical.
- Document configuration and setup.

### Project
**Deployable AI Application**

Package one of the earlier projects as a maintainable application with an API, tests, and deployment documentation.

### Deliverables
- API implementation
- Automated tests
- Docker configuration
- Deployment or local-run instructions
- Basic operational documentation

---

# Stage 07 — Applied Machine Learning

**Days 76–87**

### Objective
Strengthen practical ML understanding and learn how to choose an appropriate approach for a problem.

### Topics
- Supervised learning
- Classification and regression
- Dataset preparation
- Train, validation, and test splits
- Data leakage
- Feature engineering
- Baseline models
- Evaluation metrics
- Overfitting and underfitting
- Model comparison
- Pretrained models
- Prompting vs. RAG vs. fine-tuning
- Practical model selection

### Practical Work
- Prepare a small dataset.
- Train a baseline model.
- Evaluate it using appropriate metrics.
- Analyze errors and overfitting.
- Compare alternative approaches.
- Document why a particular approach fits the task.

### Project
**Applied ML Experiment**

Build a small ML solution and compare its behavior against a simple baseline.

### Deliverables
- Dataset and preprocessing workflow
- Baseline model
- Evaluation results
- Experiment report
- Model selection explanation

---

# Stage 08 — Independent Capstone

**Days 88–100**

### Objective
Apply the skills developed throughout the challenge to an independently designed and implemented project.

### Activities
- Identify a practical problem.
- Define the project scope and success criteria.
- Research relevant approaches.
- Design the system architecture.
- Select models, tools, and frameworks.
- Build the core implementation.
- Test and evaluate the system.
- Analyze failures and improve the solution.
- Document setup, architecture, and limitations.
- Prepare a final demonstration.

### Capstone Expectations
The project should demonstrate:

- A clearly defined problem
- Appropriate use of AI or automation
- A working implementation
- Meaningful testing or evaluation
- Technical decisions explained in my own words
- Reproducible setup instructions
- Honest documentation of limitations

### Deliverables
- Working capstone
- Source code
- README and setup instructions
- Evaluation results
- Architecture documentation
- Demonstration material

---

# Stage 09 — Final Demonstration and Review

**Day 101**

### Objective
Review the complete journey and demonstrate what I can independently build and explain.

### Activities
- Demonstrate the capstone.
- Review the repository and project history.
- Explain the architecture and important technical decisions.
- Discuss failures, limitations, and lessons learned.
- Identify topics that need further practice.
- Write a final reflection on the 101-day journey.

### Final Deliverables
- Completed capstone demonstration
- Final project documentation
- Learning retrospective
- List of skills strengthened
- Next learning goals

---

# Daily Learning and Retention Cycle

For each learning day, use the following cycle where practical:

1. **Recall:** Review what I learned previously without immediately checking notes.
2. **Learn:** Study one focused concept.
3. **Implement:** Apply the concept through code or an experiment.
4. **Test:** Check whether the implementation behaves as expected.
5. **Explain:** Write a short explanation in my own words.
6. **Reflect:** Record what was difficult and what needs revisiting.

The goal is to make learning active and measurable rather than simply consuming content.

---

# Progress and Completion Criteria

A topic is not considered complete merely because I watched a video or read documentation.

I should be able to:

- Explain the main concept in my own words.
- Implement a small example.
- Test or inspect its behavior.
- Identify at least one limitation or failure case.
- Record useful notes and code in this repository.

Some topics may require continued practice beyond their scheduled days. The roadmap is a guide, not a reason to rush past gaps in understanding.
