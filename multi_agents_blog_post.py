# warning control
import warnings
warnings.filterwarnings('ignore')

# core imports
import os
from utils import get_openai_api_key
from crewai import Agent, Task, Crew

# API key and model setup
openai_api_key = get_openai_api_key()
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_MODEL_NAME"] = "mistral-small"
os.environ["OPENAI_API_BASE"]="https://api.mistral.ai/v1"


# Define agents
planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory=(
        "You are responsible for planning a blog article on the topic: {topic}. "
        "Your primary role is to research and gather accurate, timely, and insightful information that educates the audience and empowers them to make informed decisions. The structure, direction, and depth of the final article depend on your well-crafted outline, "
        "which serves as the foundation for the Content Writer’s work."
    ),
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
    backstory=(
        "You are tasked with writing a compelling opinion piece on the topic: {topic}. Your writing is guided by a detailed content plan provided by the Content Planner, which includes context, structure, and key insights. While crafting the article, you offer well-reasoned, fact-supported analysis and clearly distinguish between personal viewpoints and objective information. Your goal is to engage the audience while maintaining clarity, accuracy, and transparency throughout."
    ),
    allow_delegation=False,
    verbose=True
)

editor = Agent(
    role="Editor",
    goal="Edit a given blog post to align with the writing style of the organization.",
    backstory=(
        "You are the final reviewer of the blog post written by the Content Writer. Your responsibility is to ensure the piece adheres to journalistic best practices, maintains a consistent and professional tone, presents balanced perspectives, and avoids unnecessary controversy. You refine the content for clarity, grammar, coherence, and alignment with the organization’s editorial guidelines before it is published."
    ),
    allow_delegation=False,
    verbose=True
)

# Define tasks
plan = Task(
    description=(
        "1. Leverage the content plan to write a compelling and informative blog post on {topic}."
        "2. Integrate SEO keywords seamlessly and naturally throughout the content."
        "3. Craft clear, engaging section headings that capture reader interest."
        "4. Follow a well-structured format, including an attention-grabbing introduction, a logically organized body, and a concise conclusion with a call to action."
        "5. Ensure the content is thoroughly proofread for grammar, spelling, and consistency with the brand’s tone and voice."
    ),
    expected_output="A comprehensive content plan document with an outline, audience analysis, SEO keywords, and resources.",
    agent=planner,
)

write = Task(
    description=(
        "1. Develop a compelling and well-researched blog post on {topic}, using the content plan as your foundation."
        "2. Seamlessly incorporate relevant SEO keywords to enhance search visibility without disrupting the natural flow of the content."
        "3. Structure the blog post with engaging, reader-friendly section titles that reflect the content’s tone and purpose."
        "4. Maintain a clear narrative flow with a strong introduction, informative body sections, and a concise, impactful conclusion that may include a call to action."
        "5. Review and polish the post to ensure it is free of grammatical errors and aligned with the brand’s editorial voice and style guidelines."
    ),
    expected_output="A well-written blog post in markdown format, each section with 2-3 paragraphs.",
    agent=writer,
)

edit = Task(
    description="Proofread the blog post for grammar and alignment with brand voice.",
    expected_output="Final blog post in markdown format, ready for publication.",
    agent=editor
)

# Run the crew
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=True
)

result = crew.kickoff(inputs={"topic": "Multi Agentic Ai"})

# Display result as Markdown
try:
    from markdown2 import markdown
    from IPython.display import display, HTML

    display(HTML(markdown(str(result))))
except ImportError:
    print("\nMarkdown2 or IPython not available. Output below:\n")
    print(result)

# Save to file
with open("blog_post.md", "w", encoding="utf-8") as f:
    f.write(str(result))  # Safe fix for CrewOutput object

print("\n✅ Blog post saved .md")
