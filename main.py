"""
Main entry point.

Run:
    python main.py

Flow:
    1. Ask user for a topic (chat input)
    2. Ask user which output format they want: docx / pdf / both
    3. Run the 3-agent pipeline (Research -> Write -> Document)
    4. Print the download path(s) for the generated file(s)
"""

import os
import sys
from orchestrator import ArticlePipeline


def ask_format() -> list[str]:
    print("\nWhich output format do you want?")
    print("  1. DOCX")
    print("  2. PDF")
    print("  3. Both")
    choice = input("Enter 1 / 2 / 3: ").strip()

    if choice == "1":
        return ["docx"]
    elif choice == "2":
        return ["pdf"]
    elif choice == "3":
        return ["docx", "pdf"]
    else:
        print("Invalid choice, defaulting to Both.")
        return ["docx", "pdf"]


def main():
    print("=" * 60)
    print(" MULTI-AGENT ARTICLE GENERATOR ")
    print(" Research Agent -> Writer Agent -> Document Agent ")
    print("=" * 60)

    topic = input("\nEnter the topic you want an article about: ").strip()
    if not topic:
        print("Topic cannot be empty. Exiting.")
        sys.exit(1)

    formats = ask_format()

    pipeline = ArticlePipeline()
    result = pipeline.run(topic, formats)

    print("\n" + "=" * 60)
    print(" DONE! ")
    print("=" * 60)
    print(f"Article title: {result['title']}")
    print("\nDownload your file(s) here:")
    for fmt, path in result["files"].items():
        if path:
            abs_path = os.path.abspath(path)
            print(f"  [{fmt.upper()}] {abs_path}")


if __name__ == "__main__":
    main()
