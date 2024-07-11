

# Required packages
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub
from tools.tools import get_profile_url_tavily

load_dotenv()


# Function for looking up the linkedin profiles.
def lookup(name: str) -> str:
    # Initializing an LLM.
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    '''
    Defining the template, as shown in the below template, the first line defines what needs to be done.
    The second line defines the output format, this is very important to get the output in proper consumable format.
    '''
    template = """Given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
    Your answer should contain only URL"""

    '''
    Initializing the prompt template, here the above defined template is assigned along with the input. 
    This input is user input.
    '''
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    '''
    Creating the tools for agent. In the there are going to be all the tools that the agent needs to use in order to
    perform the given task. For this example we are going to use only one tool.
    PARMS: 
        name: This name is the tool name that the agent will refer to. This is will be displayed in the logs.
        func: This is the pattern function that this tool will use.
        description: This is very important parameter, because this will instruct the LLM which and when the particular 
        tool is going to be used.
    '''
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    # WHAT THE FUCK IS THIS???
    react_prompt = hub.pull("hwchase17/react")

    '''
    Creating the agent, this agent will use the above given template, tools, and prompt.
    '''
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == '__main__':
    linkedin_url = lookup(name='Bhairavsingh Ghorpade')
    print(linkedin_url)

