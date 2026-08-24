# 🔍 Research Agent

An AI-powered research agent built with LangChain and Groq that autonomously searches the web, gathers information, and produces a structured research output on any given topic.

---

## 🤖 What It Does

Give it a topic — it searches the web, thinks through the results, and returns a clean structured response with a summary, key facts, and conclusion.

The agent uses a **ReAct loop** (Reasoning + Acting) — it thinks, searches, reads results, and repeats until it has enough information to produce a final answer.

---

## 🧠 Concepts Covered

- **AI Agent** vs a regular chatbot
- **Agent Loop** — think → act → observe → repeat
- **System Prompts** — giving the LLM its role and behavior
- **Tool Calling** — letting the LLM decide when to search the web
- **Prebuilt Tools** — DuckDuckGo search via LangChain
- **Custom Tools** — building tools from scratch using `@tool` decorator
- **Pydantic** — enforcing structured output from the LLM
- **Message History** — how agents remember what they already did

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| LangChain | Agent and tool framework |
| Groq | LLM provider (llama-3.3-70b-versatile) |
| DuckDuckGo Search | Free web search tool |
| Pydantic | Structured output validation |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure

```
research_agent/
├── main.py                  # Main agent code with agent loop
├── tools.py                 # Prebuilt + custom tools
├── groq_connection_test.py  # Script to test Groq API connection
├── requirements.txt         # Project dependencies
├── .env                     # API keys (not committed)
└── .gitignore               # Ignores venv, .env, __pycache__
```

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/your-username/research_agent.git
cd research_agent
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root folder:
```
YOUR_GROQ_API_KEY=your_groq_api_key_here
```

Get your free Groq API key at: https://console.groq.com

**5. Run the agent**
```bash
python main.py
```

---

## 📤 Example Output

```
Agent starting...
Agent using tool: duckduckgo_search
With input: {'query': 'Black Holes in space'}

Agent has the answer. No tools needed...

---------- RESEARCH RESULTS ----------
Topic:      Black Holes
Summary:    Black holes are regions in space where gravity is so strong
            that nothing, not even light, can escape...
Key Facts:  ['Formed from collapsing massive stars',
             'Contain a singularity at their center',
             'Event horizon marks the point of no return']
Conclusion: Black holes remain one of the most fascinating and
            mysterious objects in the known universe.
```

---

## 📦 Requirements

```
langchain
langchain-groq
langchain-community
pydantic
python-dotenv
ddgs
```

---

## 🚀 What I Learned

This project taught me how a real AI agent works under the hood — not just calling an LLM and getting a response, but building the full loop where the agent autonomously decides what tools to use, when to use them, and when it has enough information to stop.
---
