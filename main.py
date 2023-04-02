import sys
import os
import httpx
import asyncio
from datetime import datetime

openai_api_key = os.getenv("OPENAI_API_KEY")


async def request_openai(prompt):
    endpoint = 'https://api.openai.com/v1/chat/completions'
    headers = {
            'Content-Type':  'application/json',
            'Authorization': f"Bearer {openai_api_key}"
    }
    data = {
            'model':    'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': prompt}]
    }
    timeout = 30

    async with httpx.AsyncClient() as openai_client:
        response = await openai_client.post(
                endpoint,
                json = data,
                headers = headers,
                timeout = timeout
        )

        response.raise_for_status()

        return response.json()


def save_to_markdown(answer, directory):
    current_time = datetime.now().strftime("%Y%m%d_%H:%M:%S")
    file_name = f"{current_time}.md"

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, file_name), "w") as file:
        file.write(answer)
    print(f"Saved to {directory}/{file_name}")


async def main():
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        prompt = f"{input_text}"

        directory = "ChatGPT"  # ディレクトリ名を指定

        if '--markdown' in sys.argv or '-m' in sys.argv:
            prompt += "\n\n回答はマークダウン形式で出力してください。"

        response = await request_openai(prompt)
        answer = response['choices'][0]['message']['content']

        if '--markdown' in sys.argv or '-m' in sys.argv:
            save_to_markdown(answer, directory)
        else:
            print(f"{answer}")
    else:
        print("AIにききたいことを入力して下さい。")


if __name__ == "__main__":
    asyncio.run(main())