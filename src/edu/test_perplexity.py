from dotenv import load_dotenv
import os
load_dotenv()

from langchain_community.chat_models import ChatPerplexity
from langchain_core.messages import HumanMessage

# Initialize LLM without additional complexity
try:
    chat = ChatPerplexity(
        api_key=os.getenv("PERPLEXITY_API_KEY"),
        model="llama-3.1-sonar-large-128k-online"
    )
    print("LLM initialized successfully.")
    
    # Test with a simple message
    messages = [HumanMessage(content="Say hello!")]
    response = chat.invoke(messages)
    print("Response:", response.content)
    
except Exception as e:
    print(f"Error initializing LLM: {e}")