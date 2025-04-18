import openai

def query_openai(user_query):
    client = openai.OpenAI()  # Initialize OpenAI client

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}],
    )

    return response.choices[0].message.content
