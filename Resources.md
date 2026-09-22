
# AI 101 — Learning Resources & Study Guide

**Duration:** 101 Days  
**Focus:** Applied AI, AI Engineering, and Automation  
**Learning approach:** Study → Practice → Build → Explain

This file maps the learning resources to the AI 101 roadmap.

I will use these resources to learn concepts, implement practical examples, and build projects. I do not need to complete every course in full; I will focus on the lessons relevant to the current stage.

---

# Stage 00 — Setup & Skill Assessment
**Days 1–3**

## 1. Python Tutorial
Link: https://docs.python.org/3/tutorial/

### Study
- Data structures: lists, dictionaries, sets, tuples
- Conditions and loops
- Functions and modules
- File handling
- Exceptions
- Classes
- Virtual environments and packages

### Practice
- Read and write files.
- Process JSON data.
- Create reusable Python functions.
- Handle invalid inputs and exceptions.

### Build
A small Python utility that reads a file, processes its contents, and generates a useful output.

## 2. Pro Git
Link: https://git-scm.com/book/en/v2

### Study
- Getting started with Git
- Recording changes
- Viewing commit history
- Branching and merging
- Working with remote repositories

### Practice
- Create commits.
- Create and merge a branch.
- Inspect changes using `git diff`.
- Push changes to GitHub.

### Build
Set up the AI 101 repository and maintain it using Git.

## 3. GitHub Getting Started
Link: https://docs.github.com/en/get-started

### Study
- Repositories
- README files
- Commits
- Branches
- Pull requests
- Repository organization

### Apply
Maintain this AI 101 repository with meaningful commits and documented progress.

---

# Stage 01 — AI Foundations, LLMs & RAG Basics
**Days 4–15**

## 4. Introduction to Machine Learning
Link: https://developers.google.com/machine-learning/intro-to-ml

### Study
- What machine learning is
- Supervised learning
- Features and labels
- Training and inference
- Traditional ML vs. generative AI

### Apply
Explain how a traditional ML model differs from an LLM-powered application.

## 5. Hugging Face LLM Course
Link: https://huggingface.co/learn/llm-course/chapter0/1

### Study
- Transformer fundamentals
- Tokenizers
- Models and inference
- Using pretrained models
- Hugging Face ecosystem

### Apply
Run a pretrained model and inspect its input and output.

## 6. Prompt Engineering for Developers
Link: https://www.deeplearning.ai/courses/chatgpt-prompt-engineering-for-developers/

### Study
- Writing clear instructions
- Providing context
- Summarization
- Information extraction
- Transforming text
- Structured outputs
- Iterative prompt improvement

### Apply
Try different prompts on the same task and compare the outputs.

## 7. Understanding and Applying Text Embeddings
Link: https://www.deeplearning.ai/courses/understanding-and-applying-text-embeddings/

### Study
- What embeddings are
- Semantic similarity
- Similarity search
- Embedding applications

### Apply
Generate embeddings for sentences and compare their similarity.

## 8. Building Applications with Vector Databases
Link: https://www.deeplearning.ai/courses/building-applications-vector-databases/

### Study
- Vector database concepts
- Similarity search
- Indexing
- Retrieving relevant information

### Apply
Store text chunks and retrieve the most relevant chunks for a query.

## 9. Retrieval-Augmented Generation
Link: https://www.deeplearning.ai/courses/retrieval-augmented-generation/

### Study
- Why RAG is used
- Document ingestion
- Retrieval and generation
- Context construction
- Grounded answers
- RAG limitations

### Build
**AI Document Assistant — Version 1**

Create a basic application that:
1. Accepts a document.
2. Splits it into chunks.
3. Creates embeddings.
4. Retrieves relevant chunks.
5. Uses an LLM to answer questions from the retrieved context.

---

# Stage 02 — Tools, Workflows & AI Agents
**Days 16–25**

## 10. Hugging Face Agents Course
Link: https://huggingface.co/learn/agents-course

### Study
- Agent fundamentals
- Tools and actions
- Agent execution cycles
- Planning and execution
- Agent frameworks
- Agent limitations

### Apply
Build a simple tool that an AI system can call.

## 11. Hugging Face Agents Course — Unit 1: Introduction
Link: https://huggingface.co/learn/agents-course/unit1/introduction

### Study
- What an AI agent is
- The role of tools
- Agent execution cycles
- How agents interact with their environment

### Apply
Explain the difference between a fixed workflow and an agent that selects tools.

## 12. Microsoft AI Agents for Beginners
Link: https://github.com/microsoft/ai-agents-for-beginners

### Study selectively
- Agent concepts
- Tool use
- Planning
- Memory
- Multi-agent concepts
- Responsible agent design

### Apply
Compare a fixed workflow with an agent that selects tools.

### Build
**AI Document Assistant — Version 2**

Extend the assistant with a controlled tool or workflow.

Include:
- Input validation
- Error handling
- Clear stopping conditions
- Human approval for important actions

---

# Stage 03 — AI Evaluation & Reliability
**Days 26–35**

## 13. Building Systems with the ChatGPT API
Link: https://www.deeplearning.ai/courses/building-systems-with-the-chatgpt-api/

### Study
- Multi-step AI systems
- Input and output processing
- Classification and evaluation
- System-level design

### Apply
- Create a fixed set of test questions.
- Record expected answers and source documents.
- Test retrieval and answer quality.
- Identify failure cases.
- Compare results after changing the system.

### Build
**AI Document Assistant — Evaluation Suite**

Create a repeatable evaluation process for the assistant.

---

# Stage 04 — RAG Engineering
**Days 36–47**

## 14. Embeddings and Vector Databases

Links:
- https://www.deeplearning.ai/courses/understanding-and-applying-text-embeddings/
- https://www.deeplearning.ai/courses/building-applications-vector-databases/

### Study
- Chunking strategies
- Semantic similarity
- Retrieval behavior
- Metadata and filtering

## 15. Retrieval-Augmented Generation
Link: https://www.deeplearning.ai/courses/retrieval-augmented-generation/

### Study
- Document processing
- Context selection
- Retrieval strategies
- Grounded generation

### Practice
Compare:
- Different chunk sizes
- Different overlap settings
- Keyword retrieval
- Semantic retrieval
- Hybrid retrieval
- Reranking, where practical

### Build
**AI Document Assistant — RAG Upgrade**

Improve the assistant using experiments and evaluation results rather than guessing.

---

# Stage 05 — Multimodal AI
**Days 48–61**

## 16. Hugging Face Learn
Link: https://huggingface.co/learn

### Study selectively
- Computer vision
- Vision-language models
- Pretrained model usage
- Image and text workflows

## 17. OpenCV Documentation
Link: https://docs.opencv.org/

### Study
- Loading and displaying images
- Image transformations
- Color spaces
- Thresholding
- Contours
- Basic image processing

### Practice
- Process a sample image using OpenCV.
- Experiment with a vision-language model.
- Compare the approaches on a visual task.
- Record errors and limitations.

### Build
**Visual Document Assistant**

Create a small application that processes images or visual documents and answers questions about their contents.

---

# Stage 06 — Production AI Engineering
**Days 62–75**

## 18. FastAPI Tutorial
Link: https://fastapi.tiangolo.com/tutorial/

### Study
- Creating APIs
- Request and response models
- Data validation
- Error handling
- Dependency injection
- Testing

### Apply
Expose an AI application through a REST API.

## 19. Docker Getting Started
Link: https://docs.docker.com/get-started/

### Study
- Images and containers
- Dockerfiles
- Building and running containers
- Configuration
- Basic networking

### Apply
Containerize an AI application.

## 20. Spring Boot
Link: https://spring.io/projects/spring-boot

### Study selectively
- REST API development
- Configuration
- Dependency injection
- Application structure
- Testing

### Apply
Explore how Java and Spring Boot could integrate with AI services through APIs.

## 21. GitHub Actions
Link: https://docs.github.com/en/actions

### Study
- Workflows
- Events
- Jobs and steps
- Automated testing

### Apply
Create a workflow that runs project tests when code changes are pushed.

## 22. Full Stack Deep Learning
Link: https://fullstackdeeplearning.com/

### Study selectively
- AI project lifecycle
- Evaluation
- Deployment
- Monitoring
- Production system design

### Build
**Deployable AI Application**

Add an API, tests, Docker configuration, and clear setup instructions to one of the earlier projects.

---

# Stage 07 — Applied Machine Learning
**Days 76–87**

## 23. Google Machine Learning Crash Course
Link: https://developers.google.com/machine-learning/crash-course

### Study
- Regression
- Classification
- Dataset preparation
- Training and validation
- Evaluation metrics
- Overfitting and underfitting
- Feature engineering

### Apply
- Prepare a small dataset.
- Train a baseline model.
- Evaluate its performance.
- Analyze errors and limitations.

## 24. Hugging Face LLM Course
Link: https://huggingface.co/learn/llm-course/chapter0/1

### Study selectively
- Pretrained models
- Inference
- Relevant fine-tuning concepts

### Apply
Compare the practical roles of:
- Prompting
- RAG
- Fine-tuning

### Build
**Applied ML Experiment**

Train and evaluate a small model, then document the approach and results.

---

# Stage 08 — Independent Capstone
**Days 88–100**

Use the documentation that matches the project I choose.

### Potential references
- Python: https://docs.python.org/3/tutorial/
- Hugging Face: https://huggingface.co/learn
- FastAPI: https://fastapi.tiangolo.com/tutorial/
- Docker: https://docs.docker.com/get-started/
- GitHub Actions: https://docs.github.com/en/actions

### Work independently
1. Define a real problem.
2. Set measurable success criteria.
3. Design the architecture.
4. Choose appropriate tools and models.
5. Build the core application.
6. Test and evaluate it.
7. Improve failures.
8. Document setup, architecture, and limitations.

### Deliverables
- Working project
- Source code
- Project README
- Evaluation results
- Architecture documentation
- Demonstration

---

# Stage 09 — Final Demonstration
**Day 101**

### Review
- What can I explain without notes?
- What can I implement independently?
- Which projects can I demonstrate?
- What problems did I solve?
- What limitations remain?
- What should I learn next?

### Final Deliverable
A final capstone demonstration and a written retrospective of the 101-day journey.

---

# Study Rules

- Follow the current roadmap stage.
- Study only the relevant sections of each resource.
- Do not try to finish every course.
- Write notes in my own words.
- Build small examples before integrating them into projects.
- Test what I build.
- Record failures and fixes.
- Revisit concepts through active recall.
- Use documentation to solve real implementation problems.

**The goal is not to finish links. The goal is to gain skills I can demonstrate.**
