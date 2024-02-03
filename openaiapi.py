from openai import AsyncOpenAI
import asyncio
from getnewsapi import load_json_file

class OpenAIAPI:
    def __init__(self):
        keys = load_json_file('apikeys.json')
        apikey = keys["openai"]
        self.chatLogs = {}
        self.openai = AsyncOpenAI(
            api_key=apikey
        )

    async def newChat(self, prompt):
        return await self.openai.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt, stream=True)


if __name__ == '__main__':
    api = OpenAIAPI()
    print(api.newChat("Hello! How are you?"))