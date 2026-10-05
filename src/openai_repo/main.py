import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main() -> None:
    print("Hello from openai-repo!")

    summary_template = """Given the information about a {person_or_company}, generate a concise summary of the person or company. The summary should be informative, engaging, and highlight the key aspects of the {person_or_company}.

    A short story about the {person_or_company}
    
    Four Interesting Facts about the {person_or_company}"""

    prompt_template = PromptTemplate(
        input_variables=["person_or_company"],
        template=summary_template,
    )

    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-5"), temperature=0)
    #llm = ChatOllama(model=os.getenv("OPENAI_MODEL", "gemma3:270m"), temperature=0)
    
    summary_chain = prompt_template | llm

    response = summary_chain.invoke({"person_or_company": "Srinivasa Kukatla"})
    print(response.content)


if __name__ == "__main__":
    main()
