import ingest
from openai import OpenAI

client = OpenAI()
index = ingest.load_index()

def search(query):
    boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results

prompt_template = """
You're an expert in Toronto restaurants. Make three recommendations to the QUERY based on the CONTEXT from our restaurant database.
Use only the facts from the CONTEXT when making a recommendation. If possible mention the direction, displayname, and phone of the restaurant.
Do not use bold or italics.

QUERY: {question}

CONTEXT:
{context}
""".strip()

entry_template = """
nationalphonenumber: {nationalphonenumber}
formattedaddress: {formattedaddress}
rating: {rating}
displayname: {displayname}
primarytype: {primarytype}
editorialsummary: {editorialsummary}
reviews: {reviews}
""".strip()

def build_prompt(query, search_results):
    context = ""
    
    for doc in search_results:
        context = context + entry_template.format(**doc) + "\n\n"

    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt, model='gpt-4o-mini'):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def rag(query, model='gpt-4o-mini'):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer