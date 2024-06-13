from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

MODEL_PATH = "./llama-2-7b-chat.ggmlv3.q4_0.bin"

# 1. Create a function to load Llama model
# 2. Create a function to load prompt


def create_prompt() -> PromptTemplate:
    """Creates prompt template"""

    # Prompt copied from langchain docs
    _DEFAULT_TEMPLATE: str = """Assistant is a large language model trained by OpenAI.

    Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

    Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

    Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

    Human: {question}
    Assistant:"""

    prompt: PromptTemplate = PromptTemplate(
        input_variables=["question"],
        template=_DEFAULT_TEMPLATE
    )

    return prompt


def load_model() -> LLMChain:
    """Loads Llama model"""
    callback_manager: CallbackManager = CallbackManager(
        [StreamingStdOutCallbackHandler()])
    n_gpu_layers = 40
    n_batch = 512

    Llama_model: LlamaCpp = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.5,
        n_gpu_layers = n_gpu_layers,
        n_batch = n_batch,
        max_tokens=2000,
        top_p=1,
        callback_manager = callback_manager,
        verbose=True
    )

    prompt: PromptTemplate = create_prompt()

    llm_chain = LLMChain(
        llm=Llama_model,
        prompt=prompt
    )

    return llm_chain


llm_chain = load_model()

prompt: str = """ What is the largest country on Earth?"""

response: str = llm_chain.run(prompt)