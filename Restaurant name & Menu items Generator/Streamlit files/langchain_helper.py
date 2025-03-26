import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from api_keys import gemini_api #using the api key saved in another .py file

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = gemini_api

# Load Gemini model
llm_model = GoogleGenerativeAI(model = "gemini-1.5-pro", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Sequential Chain

    #llm_model = GoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I would love to open an {cuisine} Restaurant. Suggest a fancy and attractive name for it, just a name"
    )
    name_chain = LLMChain(llm=llm_model, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}. Return it as comma seperated values"
    )
    items_chain = LLMChain(llm=llm_model, prompt=prompt_template_items, output_key="menu_items")

    from langchain.chains import SequentialChain
    chain = SequentialChain(
        chains=[name_chain, items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response = chain({'cuisine': cuisine})
    return response

#if __name__ == "__main__":
#    print(generate_restaurant_name_and_items("Italian"))
