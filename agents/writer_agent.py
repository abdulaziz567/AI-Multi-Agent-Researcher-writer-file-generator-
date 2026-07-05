"""
Writer Agent
------------
Job: Take the research brief produced by the Research Agent and turn it
into a polished, well-structured article with a title, introduction,
body sections (with headings), and a conclusion. Uses Gemini (free).
"""

import google.generativeai as genai


class WriterAgent:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def run(self, topic: str, research_brief: str, word_count: int = 900) -> dict:
        """
        Returns a dict: {"title": str, "body": str}
        body uses Markdown-style headings (##) so the Document Agent
        can convert it cleanly into DOCX / PDF.
        """
        print("[WriterAgent] Writing article...")

        prompt = (
            "You are a professional article writer. You write clear, "
            "engaging, well-structured articles for a general audience, "
            "based strictly on the research brief you are given. "
            "Do not invent facts that are not supported by the brief. "
            "Use Markdown formatting: '# ' for the article title (only "
            "once, on the first line), '## ' for section headings, and "
            "plain paragraphs for body text.\n\n"
            f"Topic: {topic}\n\n"
            f"Research brief:\n{research_brief}\n\n"
            f"Write a complete article of about {word_count} words. "
            "Structure: a compelling title, a short introduction, 3-5 "
            "clearly headed body sections, and a conclusion. "
            "Do not include the raw source URLs inline, but you may add "
            "a short 'Sources' section at the end listing them."
        )

        response = self.model.generate_content(prompt)
        full_text = response.text.strip()

        # Extract title (first line starting with "# ") and body (rest)
        lines = full_text.split("\n")
        title = topic
        body_start = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("# "):
                title = line.strip().lstrip("# ").strip()
                body_start = i + 1
                break

        body = "\n".join(lines[body_start:]).strip()
        return {"title": title, "body": body}
