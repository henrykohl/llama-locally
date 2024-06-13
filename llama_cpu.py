from langchain_community.llms import LlamaCpp # 取代 langchain.llms
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

MODEL_PATH = "./llama-2-7b-chat.ggmlv3.q4_0.bin"

# 1. Create a function to load Llama model


def load_model() -> LlamaCpp:
    """Loads Llama model"""
    callback_manager: CallbackManager = CallbackManager([StreamingStdOutCallbackHandler()])

    Llama_model: LlamaCpp = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.5,
        max_tokens=2000,
        top_p=1,
        callback_manager = callback_manager,
        verbose=True
    )

    return Llama_model

llm = load_model()

model_prompt: str = """
Question: What is the largest country on Earth?
"""

response: str = llm(model_prompt)