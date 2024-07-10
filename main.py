

# Required Packages.
from dotenv import load_dotenv
import os

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from linkedin import linkedin_scraper


if __name__ == "__main__":
    load_dotenv()

    summary_template = """
        From the given LinkedIn information {information} about a person create following"
        1. A short summary.
        2. Two interesting facts about them.
    """

    summary_prompt_template = PromptTemplate(input_variables = ["information"], template = summary_template)
    llm = ChatOpenAI(temperature = 0, model_name = "gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    linkedin_information = linkedin_scraper(linkedin_profile_link = "https://www.linkedin.com/in/bhairavsingh-ghorpade/")
    res = chain.invoke(input = {"information" : linkedin_information})
    print(res)
