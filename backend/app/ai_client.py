from openai import OpenAI
import os


def create_ai_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured")

    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )
    
def test_ai_connection():
    client = create_ai_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": "Reply with exactly: FieldFix AI connection successful",
            }
        ],
    )

    return response.choices[0].message.content