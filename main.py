

# Required Packages.
from dotenv import load_dotenv
from typing import Tuple, Any
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from external_bots.linkedin import linkedin_scraper
from agent.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser, Summary


# Function for
def ice_breaker_with(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_information = linkedin_scraper(linkedin_profile_link=linkedin_url)

    summary_template = """
            From the given LinkedIn information {information} about a person create following"
            1. A short summary.
            2. Two interesting facts about them.
            
            \n{format_instructions} 
        """

    summary_prompt_template = PromptTemplate(input_variables=["information"],
                                             template=summary_template,
                                             partial_variables={"format_instructions": summary_parser.get_format_instructions()},)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": linkedin_information})

    return res, linkedin_information.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker!")

    result, pic = ice_breaker_with(name='Nicholas Salter Space Cow')
    print(result.to_dict())
    print(result.summary)
    print(result.facts)



