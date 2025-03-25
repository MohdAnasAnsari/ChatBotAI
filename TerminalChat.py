from langchain_community.llms import Ollama

# Load the local Mistral model
llm = Ollama(model="mistral")

# Ask a question
user_input = input("Ask something: ")
response = llm.invoke(user_input)

print("\nAI Response:", response)
