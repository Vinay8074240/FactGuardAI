#### 🛡️ **FactGuard AI: Autonomous Deep Research \& Fact-Checker**



###### **1. Business Problem**



In the era of Generative AI, hallucinations (where AI generates confident but false information) and the rapid spread of misinformation pose significant risks to businesses, journalists, and researchers. Relying on a single LLM "brain" often results in outdated or biased data. There is a critical need for a system that doesn't just "chat," but actively researches, cross-references, and validates information against primary sources before presenting it to the user.



###### **2. Possible Solution**



A multi-agent orchestrator that separates the "thinking" process into distinct roles:

* **A Searcher :** To find real-time data from the live web.
* **An Analyst :** To filter noise and extract core facts.
* **A Critic (Guardrail) :** To act as a final quality gate, ensuring the output matches the evidence and isn't just an LLM guess.



###### **3. Implemented Solution**



FactGuard AI is a multi-agent system built on CrewAI and powered by Groq / Llama-3-8B. It uses a Sequential Agentic Pattern to verify user claims:

* **Lead Researcher** : Breaks the claim into queries and uses Tavily Search to find 5+ high-authority sources.
* **Data Analyst** : Processes the raw search results into structured factual bullet points.
* **Fact-Check Critic** : Compares the final report against the gathered evidence to calculate a Confidence Score and flag inconsistencies.



###### **4. Tech Stack Used**



* **Orchestration Framework** : CrewAI
* **LLM (Brain)** : Groq / Llama-3-8B
* **Search Infrastructure** : Tavily AI
* **Interface** : Streamlit
* **Deployment** : Hugging Face Spaces
* **Environment Management** : Python 3.12, python-dotenv



###### **5. Architecture Diagram**



```mermaid
graph TD
    %% User and Interface
    User[User] -->|1. Enters Claim| UI(Streamlit Web Interface)
    
    %% Orchestration Layer
    subgraph Orchestrator ["CrewAI Agentic Orchestrator"]
        Researcher[Lead Researcher Agent]
        Analyst[Data Analyst Agent]
        Critic[Fact-Check Critic Agent]
    end
    
    UI -->|2. Kickoff Crew| Orchestrator
    
    %% Tool and API Layer
    subgraph DataTools ["Real-Time Data Layer"]
        Tavily[Tavily Search API]
    end
    
    subgraph Intelligence ["LLM Inference Layer"]
        Groq[Groq / Llama-3-8B]
    end
    
    %% Agent Communication and Tool Calls
    Orchestrator -->|Internal Handoff| Researcher
    Researcher -->|3. Tool Call| Tavily
    Tavily -->|4. Search Snippets| Researcher
    
    Researcher -->|5. Forward Facts| Analyst
    Analyst -->|6. Call LLM for Logic| Intelligence
    Intelligence -->|7. Factual Inference| Analyst
    
    Analyst -->|8. Forward Analysis| Critic
    Critic -->|9. Hallucination Check| Intelligence
    Intelligence -->|10. Validation & Score| Critic
    
    %% Final Output
    Critic -->|11. Final Report| Orchestrator
    Orchestrator -->|12. Display Result| UI
    UI -->|13. Final Verdict| User

    %% Styling
    style User fill:#fff,stroke:#333,stroke-width:2px
    style UI fill:#e1f5fe,stroke:#0277bd,stroke-width:2px
    style Orchestrator fill:#fff,stroke:#000,stroke-width:2px,stroke-dasharray: 5 5
    style Researcher fill:#f9fbe7,stroke:#827717,stroke-width:2px
    style Analyst fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style Critic fill:#e0f2f1,stroke:#00695c,stroke-width:2px
```



###### **6. How to Run Locally**



* **Prerequisites:** Python 3.12
* **API Keys:** Groq , Tavily AI.
* **Setup Steps:**


&#x20;       i) Clone the Repo:

&#x20;             git clone https://github.com/Vinay8074240/FactGuardAI.git

&#x20;             cd FactGuardAI

&#x20;       ii) Install Dependencies:

&#x20;              pip install -r requirements.txt

&#x20;       iii) Configure Environment:

&#x20;              Create a .env file in the root:

&#x20;                GROQ\_API\_KEY=your\_groq\_key

&#x20;                TAVILY\_API\_KEY=your\_tavily\_key

&#x20;        iv) Run the App:

&#x20;               streamlit run app.py


###### 

###### **7. Problems Faced \& Solutions**



1. **Problem:** Open AI Quota Limit: Encountered 429 Insufficient Quota during testing.
**Solution:** Migrated the LLM backend to  Groq / Llama-3-8B using crewai[litellm] for a more sustainable free tier.
2. **Problem:** Python Version Conflict: Python 3.14 (bleeding edge) caused library installation failures.
**Solution:** Downgraded local environment to Python 3.12, ensuring compatibility with pre-built "wheels" for NumPy and CrewAI.
3. **Problem:** Agent Hallucinations: Initial researcher agents accepted blog posts as "facts."

&#x20;      **Solution:** Refined the Critic Agent's system prompt to strictly enforce a "Source-First" policy, requiring 100% citation for every claim.



###### **8. References and Resources**



* CrewAI Documentation
* Tavily Search API Guide
* Hugging Face Streamlit Deployment Guide



###### **9. Recording**




https://github.com/user-attachments/assets/46bfa03c-dc5e-46df-87d9-51547b006ed0





###### **10. Screenshots**


![FactGuard UI](assets/ss3.png)

![FactGuard UI](assets/ss2.png)

![FactGuard UI](assets/ss1.png)

