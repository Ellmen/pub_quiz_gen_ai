from openai import OpenAI
from read_source import get_descs

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

descs = get_descs()
finish_reason = 'blah'
for name in descs:
    print(name)
    prompt = f"""{descs[name]}

    Please summarize the above in the form of a haiku. Just give me the haiku and nothing else. Finish after 3 lines.
    """

    while finish_reason != 'stop':
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100,
            temperature=0.6,
            top_p=0.9,
            stream=False,
        )
        poem = completion.choices[0].message.content
        print(poem)
    poem = completion.choices[0].message.content
    print(poem)
    with open(f'run3/{name}.txt', 'w') as f:
        f.write(poem)
    print(prompt, completion.choices[0])

