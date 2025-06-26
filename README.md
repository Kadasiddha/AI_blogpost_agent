# 🧠 Multi-Agent Blog Generation System

This project leverages [CrewAI](https://github.com/joaomdmoura/crewai) to automate blog creation using a team of collaborative AI agents: **Content Planner**, **Content Writer**, and **Editor**.

Each agent has a well-defined role and collaborates on generating a factually accurate, SEO-optimized, and well-edited blog post.

---

## 🚀 Features

- Multi-agent collaboration for blog creation
- Uses LLMs like `mistral-small` via OpenAI-compatible API
- SEO keyword integration and editorial proofreading
- Markdown-formatted output ready for publication
- Easily extendable for any blog topic

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multiagent-blog-generator.git
cd multiagent-blog-generator


2. Install Dependencies

pip install crewai openai python-dotenv markdown2


3. Set Up API Key and Model
Create a .env file in the root directory with:

OPENAI_API_KEY=your_mistral_api_key_here

Or update your shell environment variables directly:

export OPENAI_API_KEY="your_mistral_api_key_here"


🧩 How It Works

Agents:
Content Planner: Researches the topic, outlines content structure, and identifies SEO keywords.

Content Writer: Drafts the blog based on the plan, maintaining voice and flow.

Editor: Polishes the blog for grammar, tone, and consistency.

Tasks:
Defined with clear goals and expected outputs.

Executed sequentially by the Crew using the specified LLM.

📄 Example Usage
Run the main script:

python3 multiagents.py


Generate a blog on the topic: Multi Agentic AI

Display it in Markdown (if in a Jupyter-like environment)

Save the output as: blog_post.md

🧠 Change the Topic
Edit this line in multiagents.py:
result = crew.kickoff(inputs={"topic": "Your Desired Topic"})


Output

Blog is saved as YourTopic.md

Formatted in Markdown and ready to publish or convert to HTML


📌 Notes
mistral-small model is used via OpenAI-compatible API (https://api.mistral.ai/v1)

You can switch to gpt-3.5-turbo or gpt-4o by changing environment variables

Ensure the API base is correctly set if you're using a non-OpenAI endpoint


📬 License
MIT License © 2025 [Kadasiddha Kullolli]

🙌 Acknowledgements
CrewAI

Mistral AI

OpenAI-compatible APIs
