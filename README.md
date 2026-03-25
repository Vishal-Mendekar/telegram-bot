Mini RAG Telegram Bot
Overview
This project implements a Telegram-based chatbot powered by a Retrieval-Augmented Generation (RAG) pipeline.
The bot answers user queries using a custom knowledge base built from local documents.
The system uses:
•	Local embeddings for semantic search
•	SQLite as a vector store
•	Llama (Llama3) for local LLM inference
Features
•	Telegram bot interface
•	Retrieval-Augmented Generation (RAG)
•	Local embeddings using all-MiniLM-L6-v2
•	SQLite-based vector storage
•	Local LLM via Ollama (Llama3)
•	Conversational memory (last 3 interactions)
•	Query caching for faster responses
•	Source attribution in responses
•	/summarize command for conversation summary
 
Architecture
User → Telegram Bot → Handler → Router
                                 ↓
                               (RAG)
                                 ↓
                    Retriever (SQLite + embeddings)
                                 ↓
                        LLM (Ollama - Llama3)
                                 ↓
                           Final Response
 
Tech Stack
Component	Technology
Bot Framework	python-telegram-bot
Embeddings	sentence-transformers (MiniLM)
Vector Store	SQLite
LLM	Ollama (Llama3)
Language	Python
 
How It Works
1.	Documents are loaded from data/docs
2.	Text is split into chunks
3.	Each chunk is converted into embeddings
4.	Embeddings are stored in SQLite
5.	User query is embedded and matched with stored chunks
6.	Top-k relevant chunks are retrieved
7.	Context + query is passed to LLM
8.	Answer is generated and returned with source references
 
Setup Instructions
1. Unzip the code
 
2. Create virtual environment
python3.11 -m venv venv
source venv/bin/activate
 
3. Install dependencies
pip install -r requirements.txt
 
4. Setup environment variables
Create a .env file:
TELEGRAM_BOT_TOKEN=”tokens_here”
 
5. Setup Ollama
Install Ollama and run:
ollama serve
ollama pull llama3
 
6. Ingest documents
python app/rag/ingest.py
 
7. Run the bot
python run.py
 
Usage
Open Telegram and interact with your bot:
/ask What is expense policy?
/ask What is leave policy?
/summarize
/help
 
Example Output
Employees must submit expenses within 30 days.

Sources:
policy.md
 
Design Decisions
•	The system follows a strict RAG approach, meaning:
o	Answers are generated only from retrieved context
o	If information is not found → responds with "I don't know"
 
Enhancements Implemented
Compared to basic assignment, the following improvements were added:
•	Conversational memory (last 3 interactions)
•	Query caching for faster retrieval
•	Source attribution for transparency
•	Summarization of recent conversations
•	Smart routing for better UX
 
Future Improvements
•	Add /image command (image captioning using BLIP/LLaVA)
•	Replace SQLite with FAISS or Pinecone
•	Add LLM-based intent classification
•	Deploy using Docker
 
Author
Vishal Mendekar
![Uploading image.png…]()
