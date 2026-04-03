#### 🛡️ **FactGuard AI: Autonomous Deep Research \& Fact-Checker**



###### **1. Business Problem**



In the era of Generative AI, hallucinations (where AI generates confident but false information) and the rapid spread of misinformation pose significant risks to businesses, journalists, and researchers. Relying on a single LLM "brain" often results in outdated or biased data. There is a critical need for a system that doesn't just "chat," but actively researches, cross-references, and validates information against primary sources before presenting it to the user.



###### **2. Possible Solution**



A multi-agent orchestrator that separates the "thinking" process into distinct roles:

* **A Searcher :** To find real-time data from the live web.
* **An Analyst :** To filter noise and extract core facts.
* **A Critic (Guardrail) :** To act as a final quality gate, ensuring the output matches the evidence and isn't just an LLM guess.



###### **3. Implemented Solution**



FactGuard AI is a multi-agent system built on CrewAI and powered by Google Gemini 2.5 Flash. It uses a Sequential Agentic Pattern to verify user claims:

* **Lead Researcher** : Breaks the claim into queries and uses Tavily Search to find 5+ high-authority sources.
* **Data Analyst** : Processes the raw search results into structured factual bullet points.
* **Fact-Check Critic** : Compares the final report against the gathered evidence to calculate a Confidence Score and flag inconsistencies.



###### **4. Tech Stack Used**



* **Orchestration Framework** : CrewAI
* **LLM (Brain)** : Google Gemini 2.5 Flash
* **Search Infrastructure** : Tavily AI
* **Interface** : Streamlit
* **Deployment** : Hugging Face Spaces
* **Environment Management** : Python 3.12, python-dotenv



###### **5. Architecture Diagram**



%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#e1f5fe', 'edgeLabelBackground':'#ffffff', 'tertiaryColor': '#fff'}}}%%

graph TD

&#x20;   %% User Interface Layer

&#x20;   User\[👤 User] -->|1. Enters Claim/Topic| ST\_UI\[💻 Streamlit UI]

&#x20;   ST\_UI -->|2. Triggers Workflow| Main\_Orch\[⚙️ Main Orchestrator (main.py)]



&#x20;   %% Agent \& Orchestration Layer

&#x20;   subgraph CrewAI\_Framework \[🕵️‍♂️ CrewAI Multi-Agent Squad]

&#x20;       direction TB

&#x20;       Main\_Orch -->|3. Kickoff| Agent\_Res\[🔍 Lead Researcher]

&#x20;       Agent\_Res -->|4. Collects Data| Agent\_Ana\[📊 Data Analyst]

&#x20;       Agent\_Ana -->|5. Structures Facts| Agent\_Cri\[🛡️ Fact-Check Critic]

&#x20;       

&#x20;       %% Handoff/Feedback Loop

&#x20;       Agent\_Cri -.->|6a. Hallucination Alert -> Loop Back| Agent\_Res

&#x20;   end



&#x20;   %% External Tools \& LLM Layer

&#x20;   subgraph External\_Integrations \[🌐 External Tools \& Brain]

&#x20;       Agent\_Res -->|7. Search Query| Tool\_Tavily\[🌐 Tavily Search API]

&#x20;       Tool\_Tavily -->|8. Raw Search Results| Agent\_Res



&#x20;       %% The "Brain" of the Agents

&#x20;       Agent\_Res \& Agent\_Ana \& Agent\_Cri <-->|9. Reasoning \& Synthesis| LLM\_Gemini\[🧠 Google Gemini 2.5 Flash]

&#x20;   end



&#x20;   %% Final Output Layer

&#x20;   Agent\_Cri -->|10. Final Verified Report| Main\_Orch

&#x20;   Main\_Orch -->|11. Displays Results| ST\_UI

&#x20;   ST\_UI -->|12. Presents Findings \& Sources| User



&#x20;   %% Styling

&#x20;   classDef ui fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000;

&#x20;   classDef orch fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#000;

&#x20;   classDef agent fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,stroke-dasharray: 5 5,color:#000;

&#x20;   classDef tool fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000;

&#x20;   classDef brain fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000;



&#x20;   class User,ST\_UI ui;

&#x20;   class Main\_Orch orch;

&#x20;   class Agent\_Res,Agent\_Ana,Agent\_Cri agent;

&#x20;   class Tool\_Tavily tool;

&#x20;   class LLM\_Gemini brain;



###### **6. How to Run Locally**



* **Prerequisites:** Python 3.12
* **API Keys:** Google AI Studio (Gemini), Tavily AI.
* **Setup Steps:**

&#x20;       i) Clone the Repo:

&#x20;             git clone https://github.com/yourusername/FactGuard-AI.git

&#x20;             cd FactGuard-AI

&#x20;       ii) Create Virtual Environment:

&#x20;             python -m venv venv

&#x20;             .\\venv\\Scripts\\activate

&#x20;       iii) Install Dependencies:

&#x20;              pip install -r requirements.txt

&#x20;       iv) Configure Environment:   

&#x20;              Create a .env file in the root:

&#x20;                GOOGLE\_API\_KEY=your\_gemini\_key

&#x20;                TAVILY\_API\_KEY=your\_tavily\_key

&#x20;        v) Run the App:

&#x20;               streamlit run app.py

###### 

###### **7. Problems Faced \& Solutions**



1. **Problem:** Open AI Quota Limit: Encountered 429 Insufficient Quota during testing.
**Solution:** Migrated the LLM backend to Google Gemini 2.5 Flash using langchain-google-genai for a more sustainable free tier.
2. **Problem:** Python Version Conflict: Python 3.14 (bleeding edge) caused library installation failures.
**Solution:** Downgraded local environment to Python 3.12, ensuring compatibility with pre-built "wheels" for NumPy and CrewAI.
3. **Problem:** Agent Hallucinations: Initial researcher agents accepted blog posts as "facts."

&#x20;      **Solution:** Refined the Critic Agent's system prompt to strictly enforce a "Source-First" policy, requiring 100% citation for every claim.



###### **8. References and Resources**



* CrewAI Documentation
* Google AI Studio (Gemini API)
* Tavily Search API Guide
* Hugging Face Streamlit Deployment Guide



###### **9. Recording**



🎥 Click Here to Watch the Demo Video(Showcasing Local Run, Agent Logic, and Hugging Face Deployment)



###### **10. Screenshots**



Note: Replace these with your actual images!

