# 🛡️ GuildOps

**GuildOps** is a modern Mission Control System designed to orchestrate operations with precision. Built with a robust **FastAPI** backend and powered by **LangChain** & **LangGraph** for intelligent workflows, it serves as the central hub for managing missions, resources, and operational planning.

---

## 🚀 Tech Stack

### Backend
*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/) - High performance, easy to learn, fast to code, ready for production.
*   **Language:** Python 3.10+
*   **Database:** SQLite (Async via `aiosqlite`) & SQLAlchemy ORM.
*   **AI & Orchestration:** 
    *   [LangChain](https://www.langchain.com/) - Building applications with LLMs.
    *   [LangGraph](https://python.langchain.com/docs/langgraph) - Building stateful, multi-actor applications with LLMs.
*   **Validation:** Pydantic V2.

### Frontend
*   *(Coming Soon)*

---

## 📂 Project Structure

```text
guildops/
├── backend/                # FastAPI Backend Application
│   ├── app/
│   │   ├── api/            # API Route Handlers
│   │   ├── core/           # Core Configuration & Database Setup
│   │   ├── langgraph_flows/# AI Agent Workflows
│   │   ├── models/         # SQLAlchemy Database Models
│   │   ├── schemas/        # Pydantic Schemas (Data Transfer Objects)
│   │   ├── services/       # Business Logic
│   │   └── main.py         # Application Entry Point
│   ├── requirements.txt    # Python Dependencies
│   └── .env                # Environment Variables
├── frontend/               # Frontend Application (Placeholder)
└── README.md               # Project Documentation
```

---

## ⚡ Getting Started

### Prerequisites
*   Python 3.10 or higher
*   Git

### 1. Clone the Repository
```bash
git clone https://github.com/tommyc10/guildops.git
cd guildops
```

### 2. Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the `backend/` directory with the following variables:
```env
# Database
DATABASE_URL=sqlite+aiosqlite:///./guildops.db

# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# App Settings
APP_NAME=GuildOps
DEBUG=True
```

### 4. Run the Server
Start the development server with hot-reload:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Access the interactive API docs at `http://127.0.0.1:8000/docs`.

---

## ✅ Current Status

*   **Backend Initialization:** Core FastAPI application structure is set up.
*   **Configuration Management:** Robust settings management using Pydantic Settings.
*   **Health Check:** Operational `/health` endpoint to verify system status.
*   **Database Connection:** Async SQLite database configuration ready.

## 🗺️ Roadmap

- [ ] Implement Mission CRUD API endpoints.
- [ ] Develop LangGraph planning workflows.
- [ ] Initialize Frontend application.
- [ ] Integrate AI-driven mission generation.

---

*Built with ❤️ by [tommyc10](https://github.com/tommyc10)*
