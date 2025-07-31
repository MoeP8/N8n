from dotenv import load_dotenv
load_dotenv()

import sys
# Ensure stdout can handle any unicode characters returned by the APIs
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
import os

template = """Create a Facebook ad copy for:
Business: {business}
Offer: {offer}
Target audience: {audience}

Ad Copy:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["business", "offer", "audience"]
)

models = {
    "OpenAI": ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
    "Claude": ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.7),
    "Gemini": ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
}

input_data = {
    "business": "Local gym in Mississauga",
    "offer": "50 percent off first month",
    "audience": "Young professionals aged 25 to 40"
}

full_prompt = prompt.format(**input_data)
print("Full prompt being sent:")
print(repr(full_prompt))
print("\nChecking for non-ASCII characters...")
for i, char in enumerate(full_prompt):
    if ord(char) > 127:
        print(f"Found non-ASCII at position {i}: {repr(char)}")

print("\n" + "="*60)
for name, llm in models.items():
    try:
        chain = prompt | llm
        output = chain.invoke(input_data)
        print(f"\n{name}'s Ad Copy:")
        print("-" * 40)
        if hasattr(output, 'content'):
            print(output.content)
        else:
            print(output)
        print("-" * 40)
    except Exception as e:
        print(f"\n{name} Error: {str(e)}")
        print("-" * 40)

print("\n" + "="*60)
print("Choose the option that best reflects your gym's brand and target audience. Good luck!")
