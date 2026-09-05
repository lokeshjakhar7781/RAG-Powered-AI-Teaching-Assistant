# 🎓 RAG AI Teaching Assistant

<p align="center">
  <b>Retrieval-Augmented Generation System for Video-Based Learning</b>
</p>

---

## 📌 Overview

This project implements an end-to-end **RAG-based AI Teaching Assistant** that allows users to ask questions about their own video-based course content.

The system processes course videos, converts speech into searchable text, generates semantic embeddings, retrieves the most relevant content, and uses an LLM to generate contextual answers.

The assistant can also identify **which video and timestamp** contains the relevant information.

---

## ✨ Key Features

* 🎥 Video-to-audio conversion using FFmpeg
* 🎙️ Hindi speech transcription using Whisper
* 📝 Automatic transcript generation with timestamps
* 🔗 Transcript chunk merging for improved retrieval
* 🧠 BGE-M3 semantic embeddings
* 🔍 Cosine similarity-based semantic search
* 🤖 Llama 3.1-powered answer generation
* ⏱️ Video and timestamp-based content guidance
* 💾 Embedding storage using Joblib
* 📚 Course-specific question answering

---

## 🧠 RAG Workflow

```text
                    ┌──────────────────┐
                    │  Course Videos   │
                    │     videos/      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Video → MP3    │
                    │     FFmpeg       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ MP3 → Transcript │
                    │     Whisper      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  JSON Chunks     │
                    │  + Timestamps    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Merge Chunks    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  BGE-M3          │
                    │  Embeddings      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ embeddings.joblib│
                    └────────┬─────────┘
                             │
                       User Question
                             │
                             ▼
                    ┌──────────────────┐
                    │ Query Embedding  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Cosine Similarity│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Top 5 Relevant   │
                    │     Chunks       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Llama 3.1     │
                    │   Answer Gen.    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Answer + Video   │
                    │   + Timestamp    │
                    └──────────────────┘
```

---

## 🛠️ Technologies Used

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| 🐍 Python       | Core development          |
| 🎥 FFmpeg       | Video-to-audio conversion |
| 🎙️ Whisper     | Speech transcription      |
| 🧠 BGE-M3       | Semantic embeddings       |
| 🤖 Llama 3.1    | Answer generation         |
| 🦙 Ollama       | Local AI model serving    |
| 🔍 Scikit-learn | Cosine similarity         |
| 🔢 NumPy        | Numerical operations      |
| 📊 Pandas       | Data processing           |
| 💾 Joblib       | Embedding storage         |
| 📄 JSON         | Transcript storage        |

---

## 📂 Project Structure

```text
RAG-AI-Teaching-Assistant/
│
├── 📁 videos/
│   └── Course videos
│
├── 📁 audios/
│   └── Extracted MP3 files
│
├── 📁 oldjsons/
│   └── Whisper transcripts
│
├── 📁 newjsons/
│   └── Processed transcript chunks
│
├── 📄 video_to_mp3.py
├── 📄 mp3_to_json.py
├── 📄 merge_chunks.py
├── 📄 preprocess_json.py
├── 📄 process_incoming.py
│
├── 🤖 embeddings.joblib
├── 📝 prompt.txt
├── 💬 response.txt
└── 📖 README.md
```

### File Description

**`video_to_mp3.py`**
Converts course videos into MP3 audio files using FFmpeg.

**`mp3_to_json.py`**
Uses Whisper to transcribe the audio and stores the transcript with video metadata and timestamps.

**`merge_chunks.py`**
Combines smaller transcript segments into larger chunks for better retrieval.

**`preprocess_json.py`**
Generates BGE-M3 embeddings for transcript chunks and saves them as a Joblib file.

**`process_incoming.py`**
Accepts the user's question, retrieves relevant chunks using cosine similarity, and generates the final answer using Llama 3.1.

**`embeddings.joblib`**
Stores transcript chunks together with their generated embeddings.

---

## ⚙️ Data Processing

### Video to Audio

```text
Course Videos
      ↓
     FFmpeg
      ↓
   MP3 Files
```

### Audio to Transcript

```text
MP3 Files
    ↓
Whisper large-v2
    ↓
JSON Transcripts
    ↓
Timestamps + Text
```

### Transcript to Embeddings

```text
JSON Chunks
    ↓
BGE-M3
    ↓
Vector Embeddings
    ↓
embeddings.joblib
```

---

## 🔍 Retrieval Process

When a user asks a question, the system:

1. Generates an embedding for the question.
2. Compares it with stored transcript embeddings.
3. Calculates cosine similarity.
4. Retrieves the top 5 relevant chunks.
5. Passes the retrieved content to Llama 3.1.
6. Generates a course-specific response.

The retrieved information includes the **video title, video number, timestamps, and transcript text**.

---

## 🤖 LLM Response Generation

The retrieved course content is provided to **Llama 3.1** as contextual information.

The model is instructed to explain:

* What content answers the user's question
* Which video contains the relevant information
* The approximate timestamp
* Where the learner should go to study the topic

Questions unrelated to the course are not answered by the system.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/lokeshjakhar7781/RAG-Powered-AI-Teaching-Assistant.git
cd RAG-Powered-AI-Teaching-Assistant
```

### 2. Install Dependencies

```bash
pip install openai-whisper requests pandas joblib scikit-learn numpy
```

### 3. Install FFmpeg

Make sure **FFmpeg** is installed and available in your system PATH.

### 4. Install Ollama Models

Install Ollama and download the required models:

```bash
ollama pull bge-m3
ollama pull llama3.1
```

### 5. Add Your Videos

Place all course videos inside:

```text
videos/
```

### 6. Run the Pipeline

Convert videos to audio:

```bash
python video_to_mp3.py
```

Generate transcripts:

```bash
python mp3_to_json.py
```

Merge transcript chunks:

```bash
python merge_chunks.py
```

Generate embeddings:

```bash
python preprocess_json.py
```

Run the AI Teaching Assistant:

```bash
python process_incoming.py
```

---

## 🔄 How the Program Works

### First Stage — Data Preparation

The system processes the course material in multiple stages:

```text
Videos
  ↓
Audio Extraction
  ↓
Speech Transcription
  ↓
JSON Generation
  ↓
Chunk Processing
  ↓
Embedding Generation
```

### Second Stage — Question Answering

Once the embeddings are created:

```text
User Question
      ↓
Query Embedding
      ↓
Semantic Similarity Search
      ↓
Top 5 Relevant Chunks
      ↓
Contextual Prompt
      ↓
Llama 3.1
      ↓
Final Answer
```

---

## 💡 Example

### User Question

```text
What is the concept of backpropagation?
```

### AI Teaching Assistant

```text
Backpropagation is explained in Video 8 around 12:35.

You can go to Video 8 and start from approximately
12:35 to learn about this topic.
```

---

## 📊 Output

The system generates:

```text
prompt.txt
```

containing the contextual prompt sent to the LLM.

The generated answer is saved in:

```text
response.txt
```

The answer is based on the most relevant retrieved course chunks.

---

## 🎯 Project Goal

The goal of this project is to make long video-based courses **searchable, interactive, and easier to learn from**.

Instead of manually searching through hours of lectures, users can simply ask a question and receive the relevant explanation along with the **video and timestamp** where the topic is taught.

```text
Long Video Course
        ↓
  AI Processing
        ↓
Semantic Search
        ↓
Relevant Lecture
        ↓
Video + Timestamp
        ↓
Faster Learning
```

---

<p align="center">
  <b>🎓 Turning Video Courses into an Intelligent Learning Experience 🤖</b>
</p>
