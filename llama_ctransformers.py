from langchain_community.llms import LlamaCpp # 取代 langchain.llms
from langchain_community.llms import CTransformers
# from langchain.callbacks.manager import CallbackManager
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

MODEL_PATH = "./llama-2-7b-chat.ggmlv3.q4_0.bin"

# 1. Create a function to load Llama model


def load_model() -> CTransformers:
    """Loads Llama model"""
    callback_manager: CallbackManager = CallbackManager(
        [StreamingStdOutCallbackHandler()])

    Llama_model: CTransformers = CTransformers(
        model=MODEL_PATH,
        model_type="llama",
        verbose=True,
        temperature=0.5,
        max_new_token=512,
        callback_manager=callback_manager
    )

    return Llama_model


llm = load_model()

model_prompt: str = """
Question: What is the largest country on Earth?
"""

response: str = llm(model_prompt)