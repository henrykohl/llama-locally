# llama-locally
[How to Run LLaMA Locally on CPU or GPU | Python &amp; Langchain &amp; CTransformers Guide](https://www.youtube.com/watch?v=SvjWDX2NqiM) (Youtube Lecture Video)

## 設定環境

* 下載一個 Model
> `wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin --quiet`

* 建立一個virtual environment
> `virtualenv mchatbot --python=python3.8`

* 啟動 virtual environment
> `source ./mchatbot/bin/activate` (在github.dev的codespace環境下)
>
> `source ./mchatbot/Sctipts/activate` (在Windows 7下)

* 安裝必要的packages
> `pip install -r requirements.txt`

## 開始執行
*  在 github.dev的codespace中只有CPU，所以只能執行以下兩個檔案
> `python llama_cpu.py`
>
> `python llama_ctransformers.py`

* 與 Lecture 不同，安裝了 `langchain_community` ，以上兩個檔案，已針對相關 Deprecated 的方法做出修正

* 另外兩個檔案必需要用 GPU 執行，相關 Deprecated 的方法，並沒有被修改

## 補充
* `llama_cpp_python-0.2.77-cp38-cp38-win_amd64.whl` 在 Windows 執行時，可能會用到，但在`Colab`或是`Codespace`(github.dev)不需要

* 更多關於 GGML 模型加載細節與問題，參考[the Ipynb in GitHub](https://github.com/henrykohl/Machine-Learning-demo-repo/tree/master/NaturalLanguage/LLaMALocally)

* [the reference](https://python.langchain.com.cn/docs/use_cases/chatbots/voice_assistant) used in `llama_llchain.py`





