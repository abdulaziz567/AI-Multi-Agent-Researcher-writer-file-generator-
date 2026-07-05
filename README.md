# Multi-Agent Article Generator

A simple **3-agent pipeline** (plain Python, no framework) that:

1. **Research Agent** — takes a topic, searches the live web (Tavily API), and asks Gemini (free) to turn the raw results into a clean research brief.
2. **Writer Agent** — takes the research brief and asks Gemini (free) to write a full, structured article (title + sections + conclusion).
3. **Document Agent** — takes the final article and exports it as a **DOCX** and/or **PDF** file, saved locally, and prints the file path (download link) to the user.

An `orchestrator.py` acts as the "manager" that runs the three agents in sequence and passes data between them. `main.py` is the chat-style entry point where the user types the topic and picks the output format.

## Project structure

```
multi_agent_article_system/
├── agents/
│   ├── __init__.py
│   ├── research_agent.py     # Agent 1: Research
│   ├── writer_agent.py       # Agent 2: Write article
│   └── document_agent.py     # Agent 3: Generate DOCX/PDF
├── orchestrator.py           # Coordinates all 3 agents
├── main.py                   # CLI entry point (topic + format input)
├── requirements.txt
├── .env.example
└── README.md
```

## Setup (step by step)

### 1. Install Python packages
```bash
pip install -r requirements.txt
```

### 2. Get your API keys
- **Google Gemini API key (FREE, no card)** → https://aistudio.google.com/apikey
- **Tavily (web search) API key** → https://tavily.com/ (free tier is enough)

### 3. Configure environment variables
Copy `.env.example` to `.env` and fill in your keys:
```bash
cp .env.example .env
```
```
GEMINI_API_KEY=AIzaSy-xxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxx
```

### 4. Run it
```bash
python main.py
```

You will be asked:
```
Enter the topic you want an article about: <type your topic>
Which output format do you want?
  1. DOCX
  2. PDF
  3. Both
Enter 1 / 2 / 3:
```

After it finishes, it prints something like:
```
DONE!
Article title: The Future of Renewable Energy
Download your file(s) here:
  [DOCX] /full/path/output/the_future_of_renewable_energy_20260705_143210.docx
  [PDF]  /full/path/output/the_future_of_renewable_energy_20260705_143210.pdf
```
Open that path (or the `output/` folder) to get your file.

## How the multi-agent flow works

```
User Topic
   │
   ▼
┌─────────────────┐
│ 1. Research      │  Tavily web search + Gemini (free) synthesis
│    Agent         │  → structured research brief
└────────┬─────────┘
         ▼
┌─────────────────┐
│ 2. Writer        │  Gemini (free) turns brief into a full article
│    Agent         │  → title + body (Markdown-style headings)
└────────┬─────────┘
         ▼
┌─────────────────┐
│ 3. Document      │  python-docx / fpdf2
│    Agent         │  → .docx and/or .pdf saved to output/
└────────┬─────────┘
         ▼
   Download link printed to user
```

Each agent is a separate Python class with a single responsibility (separation of concerns) — this is the "multi-agent" pattern: independent agents, each doing one job well, coordinated by an orchestrator.

## Notes for your assignment / viva

- **Why plain Python instead of CrewAI/LangChain?** Easier to read, no framework "magic", every step (search → synthesize → write → export) is visible in the code — good for explaining logic line-by-line.
- isma edit kro isma mer name lkdo Muhammad Abdul Aziz tum mjy dedo edit krka ma direct girhuvb ma replace krdonaREADME mein naam update krne ka plan banayaREADME mein naam update krne ka plan banayaBilkul, poora updated README niche hai — ise copy karo aur GitHub pe jaake replace kardo:Show full updated README content to give to userShow full updated README content to give to usermarkdown# Multi-Agent Article Generator

**Author:** Muhammad Abdul Aziz

A simple **3-agent pipeline** (plain Python, no framework) that:

1. **Research Agent** — takes a topic, searches the live web (Tavily API), and asks Gemini (free) to turn the raw results into a clean research brief.
2. **Writer Agent** — takes the research brief and asks Gemini (free) to write a full, structured article (title + sections + conclusion).
3. **Document Agent** — takes the final article and exports it as a **DOCX** and/or **PDF** file, saved locally, and prints the file path (download link) to the user.

An `orchestrator.py` acts as the "manager" that runs the three agents in sequence and passes data between them. `main.py` is the chat-style entry point where the user types the topic and picks the output format.

## Project structure
multi_agent_article_system/
├── agents/
│   ├── init.py
│   ├── research_agent.py     # Agent 1: Research
│   ├── writer_agent.py       # Agent 2: Write article
│   └── document_agent.py     # Agent 3: Generate DOCX/PDF
├── orchestrator.py           # Coordinates all 3 agents
├── main.py                   # CLI entry point (topic + format input)
├── requirements.txt
├── .env.example
└── README.md

## Setup (step by step)

### 1. Install Python packages
```bash
pip install -r requirements.txt
```

### 2. Get your API keys
- **Google Gemini API key (FREE, no card)** → https://aistudio.google.com/apikey
- **Tavily (web search) API key** → https://tavily.com/ (free tier is enough)

### 3. Configure environment variables
Copy `.env.example` to `.env` and fill in your keys:
```bash
cp .env.example .env
```
GEMINI_API_KEY=AIzaSy-xxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxx

### 4. Run it
```bash
python main.py
```

You will be asked:
Enter the topic you want an article about: <type your topic>
Which output format do you want?

DOCX
PDF
Both
Enter 1 / 2 / 3:


After it finishes, it prints something like:
DONE!
Article title: The Future of Renewable Energy
Download your file(s) here:
[DOCX] /full/path/output/the_future_of_renewable_energy_20260705_143210.docx
[PDF]  /full/path/output/the_future_of_renewable_energy_20260705_143210.pdf
Open that path (or the `output/` folder) to get your file.

## How the multi-agent flow works
User Topic
│
▼
┌─────────────────┐
│ 1. Research      │  Tavily web search + Gemini (free) synthesis
│    Agent         │  → structured research brief
└────────┬─────────┘
▼
┌─────────────────┐
│ 2. Writer        │  Gemini (free) turns brief into a full article
│    Agent         │  → title + body (Markdown-style headings)
└────────┬─────────┘
▼
┌─────────────────┐
│ 3. Document      │  python-docx / fpdf2
│    Agent         │  → .docx and/or .pdf saved to output/
└────────┬─────────┘
▼
Download link printed to user

Each agent is a separate Python class with a single responsibility (separation of concerns) — this is the "multi-agent" pattern: independent agents, each doing one job well, coordinated by an orchestrator.

## Notes for your assignment / viva

- **Why plain Python instead of CrewAI/LangChain?** Easier to read, no framework "magic", every step (search → synthesize → write → export) is visible in the code — good for explaining logic line-by-line.
- **Why Tavily for research?** It gives the Research Agent real, current web results instead of relying only on the LLM's training data — makes the article factually current.
- **Extending it:** you could add a 4th "Editor/Reviewer Agent" that fact-checks or proofreads the article before the Document Agent runs, or a "SEO Agent" that adds meta descriptions/keywords.
GitHub pe replace karne ke steps:

Repo kholo → README.md pe click karo
Right side pencil icon (✏️) pe click karo
Sab kuch select karo (Ctrl+A) aur delete kardo
Upar wala poora content paste kardo
Neeche scroll karke "Commit changes" button dabao
author mtlb\"Author" ka matlab hota hai "likhne wala" ya "banane wala" — jaise kisi book ka author, waise hi is project/code ka author.
Yahan iska matlab hai ke README mein likha ja raha hai ke yeh project tumne (Muhammad Abdul Aziz) banaya hai — assignment mein ownership/credit dikhane ke liye. Jab teacher ya koi aur repo kholega, unhe pata chal jayega ke yeh code kisne likha hai.
Yeh koi technical cheez nahi hai, sirf ek credit line hai README ke top pe.author ki jaga kch or lkhoWeighed alternative terminology for author attributionWeighed alternative terminology for author attributionKoi baat nahi, options hain — konsa pasand hai?

Submitted by: Muhammad Abdul Aziz (assignment submission ke liye best)
Developed by: Muhammad Abdul Aziz
Created by: Muhammad Abdul Aziz
Made by: Muhammad Abdul Aziz

Assignment ke liye mera suggestion "Submitted by" hai, kyunki yeh clearly bata deta hai ke yeh submission hai kisi assignment ki. Batao konsa use karna hai, ya khud kuch aur likhna chaho to wo bhi bata do.ya lkfdo usma Created by: Muhammad Abdul AzizTheek hai, README update kar deta hoon:Change Author label to Created byChange Author label to Created byHo gaya. Ab yeh poora updated content copy karo aur GitHub pe replace kardo:
markdown# Multi-Agent Article Generator

**Created by:** Muhammad Abdul Aziz
- **Why Tavily for research?** It gives the Research Agent real, current web results instead of relying only on the LLM's training data — makes the article factually current.
- **Extending it:** you could add a 4th "Editor/Reviewer Agent" that fact-checks or proofreads the article before the Document Agent runs, or a "SEO Agent" that adds meta descriptions/keywords.
"# AI-Multi-Agent-Researcher-writer-file-generator-" 
