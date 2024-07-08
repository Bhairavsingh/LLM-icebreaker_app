

# Required Packages.
from dotenv import load_dotenv
import os

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI


information = """
"""

if __name__ == "__main__":
    load_dotenv()
    print(os.environ['API_KEY'])

    summary_template = """
        From the given information {information} about a person create following"
        1. A short summary.
        2. Two interesting facts about them.
    """

    summary_prompt_tenplate = PromptTemplate(input_variables = ["information"], template = summary_template)

    llm = ChatOpenAI(temperature = 0, model_name = "gpt-3.5-turbo")

    chain = summary_prompt_tenplate | llm

    res = chain.invoke(input = {"information" : information})

    pass