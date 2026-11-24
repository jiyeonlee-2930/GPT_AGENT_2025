# 🤖 LLM & AI Agent Development

LangChain과 OpenAI API를 활용한 LLM 기반 챗봇, AI Agent 및 RAG(Retrieval-Augmented Generation) 개발 실습 프로젝트입니다.

한라대학교 AI정보보안학과의 LLM 교육 및 프로그래밍 실습을 목적으로 구성되었습니다.

## 1. 프로젝트 목표 (Objectives)

- OpenAI API의 이해 및 활용
- LangChain의 기본 구조와 동작 원리 이해
- 대화 이력을 활용한 Multi-turn Chatbot 구현
- LCEL을 활용한 Chain 구성
- Tool Calling 기반 AI Agent 기능 구현
- Embedding 및 Vector Database 이해
- RAG 기반 문서 검색 및 질의응답 시스템 구현
- Streamlit을 활용한 웹 서비스 개발

## 2. 개발 환경 (Development Environment)

| 구분 | 기술 |
|---|---|
| Language | Python 3.11 |
| IDE | Visual Studio Code |
| LLM | GPT-4o, GPT-4o-mini |
| Framework | LangChain |
| Embedding | text-embedding-3-large |
| Vector Database | ChromaDB |
| Web Framework | Streamlit |
| Version Control | Git & GitHub |

## 3. 프로젝트 구성 (Project Structure)

| 파일 및 폴더 | 설명 |
|---|---|
| `langchain_chatbot.ipynb` | LangChain 기본 챗봇 실습 |
| `langchain_multiturn.py` | 멀티턴 대화 구현 |
| `langchain_simple_chat_streamlit.py` | Streamlit 기반 챗봇 |
| `lcel.ipynb` | LCEL 기반 Chain 구성 실습 |
| `langchain_tool.ipynb` | Tool Calling 실습 |
| `langchain_streamlit_tool_0.py` | Tool Calling 기반 챗봇 실습 |
| `langchain_streamlit_tool.py` | Tool Calling 기반 웹 챗봇 |
| `rag_practice.ipynb` | 문서 처리, 임베딩 및 벡터 DB 구축 |
| `retriever.py` | 문서 검색 및 RAG Chain 구성 |
| `rag.py` | Streamlit 기반 RAG 챗봇 |
| `chroma_store/` | 임베딩된 문서의 벡터 데이터베이스 |
| `data/` | 실습용 PDF 데이터 |
| `requirements.txt` | Python 라이브러리 목록 |
| `.gitignore` | Git 업로드 제외 설정 |

## 4. 학습 과정 (Learning Roadmap)

### Step 1. Basic Chatbot

OpenAI API와 LangChain을 활용하여 기본적인 질의응답 챗봇을 구현합니다.

### Step 2. Multi-turn Chatbot

대화 이력을 저장하고 이전 대화의 문맥을 활용하는 챗봇을 구현합니다.

### Step 3. LCEL

LangChain Expression Language를 활용하여 Prompt, LLM, Output Parser를 연결합니다.

### Step 4. Tool Calling

LLM이 사용자의 질문에 따라 외부 함수와 도구를 활용하도록 구현합니다.

### Step 5. RAG

PDF 문서의 로딩, 분할, 임베딩, 벡터 저장, 유사도 검색 및 답변 생성 과정을 실습합니다.

### Step 6. Web Application

Streamlit을 활용하여 사용자와 상호작용할 수 있는 웹 기반 챗봇을 구현합니다.

## 5. RAG 시스템 구조 (RAG Architecture)

**벡터 데이터베이스 구축**

PDF Document → Document Loader → Text Splitter → Embedding → ChromaDB

**질의응답 시스템**

User Query → Query Augmentation → Retriever → Relevant Documents → LLM → Answer

사용자의 질문과 관련된 문서를 벡터 데이터베이스에서 검색하고, 검색된 문서를 LLM에 전달하여 문서 기반 답변을 생성합니다.

## 6. 설치 및 실행 (Installation & Execution)

### Step 1. Clone Repository

    git clone https://github.com/jiyeonlee-2930/GPT_AGENT_2025.git
    cd GPT_AGENT_2025

### Step 2. Create Virtual Environment

    python -m venv venv

Windows PowerShell:

    .\venv\Scripts\Activate.ps1

### Step 3. Install Libraries

    pip install -r requirements.txt

### Step 4. Set OpenAI API Key

프로젝트 폴더에 `.env` 파일을 생성하고 본인의 OpenAI API 키를 입력합니다.

    OPENAI_API_KEY=your_openai_api_key

API 키는 외부에 공개하지 않으며 GitHub에 업로드하지 않습니다.

### Step 5. Run Streamlit Application

Basic Chatbot:

    python -m streamlit run langchain_simple_chat_streamlit.py

Tool Calling Chatbot:

    python -m streamlit run langchain_streamlit_tool.py

RAG Chatbot:

    python -m streamlit run rag.py

## 7. 실습 데이터 (Dataset)

- 2040 Seoul Urban Plan
- OneNYC 2050 Strategic Plan

대용량 파일 제한으로 OneNYC 원본 PDF는 GitHub 저장소에서 제외하였습니다.

기존에 구축된 ChromaDB를 활용하여 RAG 실습을 진행할 수 있습니다. 벡터 데이터베이스를 새로 구축하려면 원본 PDF를 별도로 준비해야 합니다.

## 8. 참고 자료 (References)

- [OpenAI](https://platform.openai.com/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)
- Do it! AI 에이전트
- 테디노트의 RAG 비법노트 기본편

## 9. Author

**Jiyeon Lee, Ph.D.**

Department of AI Information Security

Halla University, Republic of Korea

## 10. Purpose

This repository is designed for educational and research purposes, focusing on Large Language Models, AI Agents, and Retrieval-Augmented Generation.
