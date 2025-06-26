import os

def get_openai_api_key():
    """
    Retrieves the OpenAI API key from environment variable.
    Ensure that the 'OPENAI_API_KEY' environment variable is set.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
    return api_key