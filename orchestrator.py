"""
Orchestrator
------------
Coordinates the 3-agent pipeline:
  1. ResearchAgent  -> research brief
  2. WriterAgent    -> title + article body
  3. DocumentAgent  -> DOCX / PDF file(s)

This is the "manager" that ties everything together. In bigger
frameworks (CrewAI/LangGraph) this role is built-in; here we do it
explicitly with plain Python so every step is visible and easy to
explain/debug.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

from agents import ResearchAgent, WriterAgent, DocumentAgent

load_dotenv()


class ArticlePipeline:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment (.env file)")

        genai.configure(api_key=api_key)

        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()
        self.document_agent = DocumentAgent(output_dir="output")

    def run(self, topic: str, formats: list[str]) -> dict:
        print(f"\n=== STEP 1/3: RESEARCH AGENT ===")
        research_brief = self.research_agent.run(topic)

        print(f"\n=== STEP 2/3: WRITER AGENT ===")
        article = self.writer_agent.run(topic, research_brief)

        print(f"\n=== STEP 3/3: DOCUMENT AGENT ===")
        files = self.document_agent.run(article["title"], article["body"], formats)

        return {
            "topic": topic,
            "title": article["title"],
            "research_brief": research_brief,
            "article_body": article["body"],
            "files": files,
        }
