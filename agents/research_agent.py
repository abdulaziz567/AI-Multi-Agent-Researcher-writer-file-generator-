"""
Research Agent
--------------
Job: Given a topic, search the web (Tavily) for current, relevant
information, then use Gemini (free) to distill the raw search results
into a clean, structured research brief that the Writer Agent can use.
"""

import os
from tavily import TavilyClient
import google.generativeai as genai


class ResearchAgent:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        tavily_key = os.getenv("TAVILY_API_KEY")
        if not tavily_key:
            raise ValueError("TAVILY_API_KEY not found in environment (.env file)")

        self.tavily = TavilyClient(api_key=tavily_key)
        self.model = genai.GenerativeModel(model_name)

    def search_web(self, topic: str, max_results: int = 6) -> list[dict]:
        """Run a real web search via Tavily and return raw results."""
        print(f"[ResearchAgent] Searching the web for: {topic}")
        response = self.tavily.search(
            query=topic,
            search_depth="advanced",
            max_results=max_results,
            include_answer=True,
        )
        return response.get("results", [])

    def build_brief(self, topic: str, results: list[dict]) -> str:
        """Ask Gemini to turn raw search snippets into a structured brief."""
        print("[ResearchAgent] Synthesizing research brief...")

        sources_text = ""
        for i, r in enumerate(results, start=1):
            sources_text += (
                f"\nSource {i}: {r.get('title', 'Untitled')}\n"
                f"URL: {r.get('url', 'N/A')}\n"
                f"Content: {r.get('content', '')}\n"
                f"---\n"
            )

        prompt = (
            "You are a meticulous research analyst. You are given raw web "
            "search snippets about a topic. Produce a clean, well-organized "
            "research brief that a professional writer can use to write an "
            "article. Include: key facts, important statistics/data points, "
            "different perspectives if relevant, and a short list of the "
            "source URLs used. Do not write the article itself -- only the "
            "research brief.\n\n"
            f"Topic: {topic}\n\n"
            f"Raw web search results:\n{sources_text}\n\n"
            "Please produce a structured research brief (headings + bullet "
            "points) covering the most important and up-to-date information "
            "on this topic."
        )

        response = self.model.generate_content(prompt)
        return response.text

    def run(self, topic: str) -> str:
        """Full research pipeline: search -> synthesize -> return brief."""
        results = self.search_web(topic)
        if not results:
            print("[ResearchAgent] No search results found, using LLM knowledge only.")
            results = []
        brief = self.build_brief(topic, results)
        return brief
