AI News Analyzer

This is a simple Python project that analyzes news articles using a local AI model (Ollama Gemma3). 
You give it a news URL and it generates a structured analysis report with summary, impact, risk level, 
stakeholders, and a final takeaway.

How it works
1. Fetches the news webpage content
2. Sends it to a local LLM through Ollama
3. Generates a clean News Intelligence Report

Requirements
- Python 3
- Ollama installed
- Gemma3 model downloaded

Setup
pip install -r requirements.txt

Run
python summarizer.py

Notes
This runs fully locally. No API keys required.
