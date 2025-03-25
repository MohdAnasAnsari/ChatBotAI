# from langchain_community.llms import Ollama

# # Load the Mistral model in Langchain
# llm = Ollama(model="mistral")

# print("🤖 Chatbot is ready! Type 'exit' to stop.\n")

# while True:
#     user_input = input("You: ")
    
#     if user_input.lower() == "exit":
#         print("Chatbot: Goodbye! 👋")
#         break

#     response = llm.invoke(user_input)
    
#     print("Chatbot:", response)

from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Load Ollama model
llm = Ollama(model="mistral")

# Define memory to store chat history
memory = ConversationBufferMemory()

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["history", "user_input"],
    template="You are a helpful chatbot. Here is the conversation so far:\n{history}\nUser: {user_input}\nChatbot:"
)

# Create a Langchain conversation chain
chatbot = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

print("🤖 Chatbot with Memory is ready! Type 'exit' to stop.\n")

# Chat loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    response = chatbot.invoke(user_input)
    
    print("Chatbot:", response)
