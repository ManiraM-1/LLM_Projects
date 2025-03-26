# Now, let's first Understand Simple Sequential Chain and then we'll proceed to Sequential Chain

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

# Sequential Chain 

# Here, in the above example, Simple Sequential Chain is only printing one output
# i.e, it is taking the restaurant name as input and printing the menu items 
# it is not printing the initial restaurant name
# so, to print that, we'll use Sequential chain, not the SimpleSequentialChain

# Sequential Chain implemenatation

# model creation
llm_model = GoogleGenerativeAI(model = "gemini-1.5-pro", temperature = 0.7)

# Prompt template-1
prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I would love to open an {cuisine} Restaurant. Suggest a fancy and attractive name for it, just a name"
)
#Chain-1
name_chain = LLMChain(llm = llm_model, prompt=prompt_template_name, output_key = "restaurant_name") #adding one extra parameter output_key for storing

# Prompt template-2
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template = "Suggest some menu items for {restaurant_name}. Return it as comma seperated values"
)
#Chain-2
items_chain=LLMChain(llm = llm_model,prompt=prompt_template_items,output_key="menu_items")

from langchain.chains import SequentialChain
chain = SequentialChain(
    chains=[name_chain,items_chain],
    input_variables = ['cuisine'],
    output_variables=['restaurant_name','menu_items']
)
chain({'cuisine':'Arabic'})
#Here, we don't use the .run fuction, we directly pass the argument, since, there could be any possible cuisines, we use a disctionary for arguments
