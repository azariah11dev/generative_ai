# **Generative AI – Small Practice Projects**
## Why this repo exists

I’m trying to understand how generative AI systems actually work beyond just calling an API and getting an answer back.

Instead of reading more articles or watching tutorials, I decided to build a few small, focused projects that each explore one idea at a time. The projects here are intentionally simple so I can reason about what’s happening and see where things break.

This is mainly a learning repo.

## How I’m approaching this

1. Keep projects small and self-contained
2. Focus on one concept per project
3. Build something end-to-end, even if it’s basic
4. Favor clarity over completeness

If a project feels “too easy,” that’s usually a good sign — it means I can actually understand it.

## **Projects**
# Text Summarizer API

A very simple API that takes text and returns a summary.

## What I’m trying to learn

    - How prompts affect output
    - Token limits and truncation
    - Response consistency

# Chatbot with Memory

A basic chatbot that keeps some form of conversation history.

## What I’m trying to learn

    - How context windows work
    - Different ways to store and reuse past messages
    - What breaks when conversations get long

# Embedding Search Engine

A small search tool using embeddings instead of keywords.

## What I’m trying to learn

    - How embeddings represent meaning
    - How similarity search actually behaves
    - When results feel “right” vs misleading

# Simple RAG Pipeline

A minimal retrieval-augmented generation setup.

## What I’m trying to learn

    - Why models hallucinate
    - How retrieval helps (and when it doesn’t)
    - How chunking and context size matter

# FastAPI Endpoint Calling a Model

A basic API endpoint that wraps a model call.

## What I’m trying to learn

    - How LLMs fit into real services
    - Request/response boundaries
    - Error handling and latency issues

# Synthetic Data Generator (Notebook)

A notebook that generates fake data using a model.

## What I’m trying to learn

    - How controllable generated data really is
    - Where bias shows up
    - When synthetic data is useful vs misleading

# **What this repo is not**

    - Not production-ready code
    - Not a polished tutorial
    - Not optimized or benchmarked

This is mostly for experimentation and notes.

# **How I plan to use this**

    - Build one project at a time
    - Break things on purpose
    - Change assumptions and see what happens
    - Write down what I didn’t expect

The goal is to build intuition, not just features.