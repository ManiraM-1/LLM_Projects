# Inorder to remeber the previous convo/context, for example, if you're building a chatbot, previous convosersation is required 
# so, some data has to be stored 
# Langchain provides this functionality too.

from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
name_chain = LLMChain(llm = llm_model, prompt=prompt_template_name, memory=memory)
name = name_chain.run("Mexican")
print(name)

# OUTPUT : Azalea Cantina

name = name_chain.run("Indian")
print(name)

# OUTPUT : Maharani

print(name_chain.memory.buffer)

# OUTPUT : 
# Human: Mexican
# AI: Azalea Cantina
# Human: Indian
# AI: Maharani
