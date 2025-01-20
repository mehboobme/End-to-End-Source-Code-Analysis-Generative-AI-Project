# End-to-End-Source-Code-Analysis-Generative-AI-Project

# How to run steps:

# Step 1. Clone the repository

```bash
Project repo: 
```
# Step 2. Create a conda environment after opening the repository

``` bash
conda create -n llmapp python=3.10 -y
```

```bash
conda activate medibot
```

# Step 3. install the requirements
```bash
pip install -r requirements.txt
```
### create a `.env` file in the root directory and add your pinecone & OPENAI credentials as follows:

```ini
PINECONE_API_KEY="................."
OPENAI_API_KEY="..................."

```bash
# run the following command to store embeddings to pinecone
python store_index.py

```bash
# finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```

### Techstack Used:

- Python
- Langchain
- GPT
- Pinecone

