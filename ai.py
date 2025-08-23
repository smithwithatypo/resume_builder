import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")    # sonnet 4
# model = init_chat_model("claude-3-5-haiku-20241022", model_provider="anthropic")   # haiku 3.5
# model = init_chat_model("claude-3-7-sonnet-latest", model_provider="anthropic")    # sonnet 3.7