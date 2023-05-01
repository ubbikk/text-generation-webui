from llama_cpp import Llama

fp = 'models/OpenAssistant-Llama-30b-4bit/openassistant-llama-30b-ggml-q4_1.bin'
llm = Llama(model_path=fp)
prompt = """You are a helpful assistant called Joi trained by OpenAssistant on large corpus of data, you will now help user to answer the question as concise as possible
User: What is the capital of Ukraine?

Joi:"""
output = llm(prompt, max_tokens=200, stop=[], echo=True)
print(output)