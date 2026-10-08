# 🤖 AI Data Analyst Agent

An **AI-powered Data Analyst Agent** that allows users to upload datasets and interact with their data using **natural language**. The system performs automated data analysis, generates business insights, and uses an agentic workflow to route questions between deterministic Pandas-based analysis and LLM-powered reasoning.

## 🚀 Features

* 📂 Upload multiple dataset formats such as CSV, Excel, JSON, Parquet, and TXT
* 📊 Automatic dataset profiling
* 🔍 Missing-value and duplicate detection
* 📈 Revenue, sales, category, region, and product analysis
* 🧮 Statistical analysis using Pandas
* 💬 Ask questions about datasets using natural language
* 🤖 Gemini-powered AI reasoning
* 🔄 LangGraph-based agentic workflow
* 🧠 Intelligent routing between local data analysis and AI reasoning
* 🛡️ Reduces hallucination by performing numerical calculations locally
* 🌐 Interactive Streamlit web interface

## 🏗️ Project Workflow

User Uploads Dataset
        ↓
Data Loading & Profiling
        ↓
User Question
        ↓
Question Analysis
        ↓
 ┌──────────────────────┐
 │   Intelligent Router │
 └──────────┬───────────┘
            ↓
     ┌──────┴──────┐
     ↓             ↓
Pandas Analysis   Gemini LLM
     ↓             ↓
     └──────┬──────┘
            ↓
       Final Answer

## 🛠️ Tech Stack

* **Programming:** Python
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Plotly
* **LLM:** Google Gemini
* **Frameworks:** LangChain, LangGraph
* **Frontend:** Streamlit
* **Environment:** Python-dotenv
* **File Processing:** OpenPyXL, PyArrow, xlrd

## 📁 Project Structure

AI-Data-Analyst-Agent/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── data/
│
└── src/
    ├── __init__.py
    ├── llm.py
    ├── data_loader.py
    ├── data_profiler.py
    ├── analysis.py
    ├── agent.py
    └── graph.py

## 🔑 How It Works

### 1. Dataset Upload

The user uploads a dataset through the Streamlit interface.

### 2. Data Profiling

The system automatically identifies:

* Number of rows and columns
* Missing values
* Duplicate records
* Numeric columns
* Revenue/Sales columns
* Product, Category, Region, Customer, and Date columns

### 3. Local Data Analysis

For questions requiring exact calculations, the system uses **Pandas** instead of relying on the LLM.

Examples:

What is the total revenue?
Which product generated the highest revenue?
Show revenue by category.
Which region has the highest sales?
Give me the statistical summary.

### 4. AI Reasoning

For business-oriented questions that require interpretation, the system can use **Google Gemini** to generate meaningful insights and recommendations.

Examples:

What are the important business insights?
What trends do you observe?
What factors may affect revenue?
Give me business recommendations.

### 5. Agentic Workflow

**LangGraph** manages the workflow and routes the user's question to the appropriate analysis path.

This approach combines:

**Deterministic Data Analysis + LLM Reasoning = Reliable AI Data Analysis**

## 💡 Example Questions

How many rows are in the dataset?

Are there any missing values?

What is the total revenue?

What is the average revenue?

Which product generated the highest revenue?

Show the top 5 products by revenue.

Which category generated the highest revenue?

Which region has the highest revenue?

Give me important business insights from this dataset.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Data-Analyst-Agent.git
cd AI-Data-Analyst-Agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Never commit your `.env` file to GitHub.

## ▶️ Run the Application

python -m streamlit run app.py

The application will open in your browser.

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Agentic AI, LLMs, LangChain, LangGraph, and traditional data analysis techniques** can be combined to build an intelligent data analytics application.

The project focuses on using **Pandas for accurate numerical calculations** while leveraging an **LLM for natural-language understanding and business reasoning**.

## 🔮 Future Enhancements

* SQL Agent for database analysis
* Multi-agent architecture
* Automated chart generation
* Data visualization recommendations
* Conversational memory
* Advanced business KPI analysis
* Automated report generation
* PDF/Excel report export
* Deployment using Streamlit Cloud
* Support for additional LLM providers

## 👨‍💻 Skills Demonstrated

* Python
* Data Analysis
* Pandas & NumPy
* Generative AI
* Large Language Models
* LangChain
* LangGraph
* Agentic AI
* Prompt Engineering
* Natural Language Processing
* Streamlit
* Business Intelligence
* Data Visualization

## 📌 Project Highlights

> Built an AI-powered Data Analyst Agent that combines **Pandas-based deterministic analysis with Gemini-powered reasoning**, using **LangGraph for intelligent workflow routing** and **Streamlit for an interactive user interface**.
