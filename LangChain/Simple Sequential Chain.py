import os
from langchain_google_genai import GoogleGenerativeAI
from api_keys import gemini_api #importing my api key
from langchain.prompts import PromptTemplate

# Simple Sequential Chain implementation
# Here, one output of the chain is used as the input of another chain, hence only final output is retreived
# If we want to retreive the intermediary output results, we could use Sequential Chain, not the Simple Sequential Chain

# model creation
llm_model = GoogleGenerativeAI(model = "gemini-1.5-pro", temperature=0.7)

# Prompt template-1
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template = "I would love to open an {cuisine} Restaurant. Suggest a fancy and attractive name for it, just a name"
)
# Chain-1
name_chain = LLMChain(llm = llm_model, prompt = prompt_template_name)

# Prompt template-2
prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Suggest some menu items for {restaurant_name}. Return it as comma seperated values"
)
#Chain-2
food_items_chain = LLMChain(llm = llm_model, prompt = prompt_template_items)

#importing the SimpleSequentialChain
from langchain.chains import SimpleSequentialChain

chain = SimpleSequentialChain(chains = [name_chain,food_items_chain])
response=chain.run("India")
print(response)
