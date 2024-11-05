from openai import OpenAI
from read_source import get_descs

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# A one sentence summary of the above for toddlers is:
# A summary of the above in the form of a haiku is:

descs = get_descs()
finish_reason = 'blah'
for name in descs:
    print(name)
    prompt = f"""{descs[name]}

    Please summarize the above in the form of a haiku. Just give me the haiku and nothing else. Finish after 3 lines.
    """
    # prompt = f"""{descs[name]}

    # The above is a research description. Please summarize what this researcher does differently compared to other researchers in data driven drug designin exactly one brief sentence using 10 words or less.
    # """

    while finish_reason != 'stop':
        # completion = client.completions.create(
        #     model="meta-llama/Llama-3.2-3B-Instruct",
        #     prompt=prompt,
        #     max_tokens=40,
        #     # temperature=0.2,
        #     # top_p=0.2,
        # )
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=100,
            temperature=0.6,
            top_p=0.9,
            stream=False,
        )
        finish_reason = completion.choices[0].finish_reason
        print(finish_reason)
        poem = completion.choices[0].message.content
        # poem = completion.choices[0].text
        print(poem)
        # print(prompt, completion.choices[0].text)
    finish_reason = 'blah'
    # poem = completion.choices[0].text
    poem = completion.choices[0].message.content
    print(poem)
    with open(f'run3/{name}.txt', 'w') as f:
        f.write(poem)
    print(prompt, completion.choices[0])

