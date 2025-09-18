# 🤖 QA Assistant with RAG & LangChain

This project is an **AI-powered Question-Answering (QA) Assistant** that allows users to upload CSV files, store them in a database, and then query the data in **natural language**. The assistant uses **RAG (Retrieval-Augmented Generation)** with **LangChain** to process queries and generate human-friendly responses along with explanations.  

The project is built with a **beautiful and interactive UI in Streamlit**.

---

## ✨ Features
- 📂 **Upload CSV files** → Automatically stored into the database.  
- 🔎 **Ask natural language queries** → Get results without writing SQL manually.  
- 🧠 **RAG + LangChain** → Connects LLMs with database for intelligent query answering.  
- 📊 **Database-backed** → Ensures structured and efficient querying.  
- 🖥️ **Streamlit UI** → Simple, clean, and user-friendly interface.  
- 💡 **Explanation included** → Along with query results, assistant provides reasoning.  

---

## 🛠️ Tech Stack
- **Python**  
- **LangChain** – LLM orchestration  
- **RAG (Retrieval-Augmented Generation)** – Context-aware responses  
- **SQL Database** – Storing CSV data for structured queries  
- **Streamlit** – Frontend UI
- **Flask**
- **LLM Integration** – For natural language query understanding  

---

## 📂 Project Workflow
1. **Upload CSV file** via Streamlit interface.  
2. **Data stored** into SQL database automatically.  
3. User asks a **natural language query**.  
4. **LangChain + RAG pipeline** converts the query into structured retrieval.  
5. The assistant executes SQL queries behind the scenes.  
6. **Results + Explanation** are displayed on the UI.  

---

## 🚀 How to Run Locally
  1. Clone the repository:
      ```bash
       git clone https://github.com/<your-username>/QA-Assistant.git
       cd QA-Assistant
     ```
 2. Create and activate a virtual environment:
      ```bash
        python -m venv venv
        source venv/bin/activate   # On Linux/Mac
        venv\Scripts\activate 
     ```
 3. Install dependencies:
    ```bash
       pip install -r requirements.txt
     ```
 4. Run the Streamlit app:
    ```bash
       streamlit run app.py
     ```

## 📌 Future Improvements

  - Support for more file formats (Excel, JSON).
  - Improved visualization (charts & graphs).
  - Option to connect with external APIs.
  - Multi-user support with authentication.

# 💼 AI & Data Science Enthusiast | Exploring GenAI, LangChain & RAG
  

