from langchain_ollama import ChatOllama


def get_model(role: str):

    models = {
        "teacher": "qwen3:14b",
        "architect": "deepseek-r1:14b",
        "developer": "qwen3:14b",
        "reviewer": "deepseek-r1:14b",
        "technical_writer": "llama3.2:3b",
    }

    return ChatOllama(model=models[role], temperature=0.2, num_ctx=32768)
