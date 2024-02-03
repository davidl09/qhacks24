import openai
from openai import AsyncOpenAI
import asyncio
import sentimentAnalysis
import server


class OpenAIAPI:
    def __init__(self):
        keys = sentimentAnalysis.load_json_file('apikeys.json')
        openai.api_key = keys["openai"]
        self.id = server.session.get("user")
        self.chatLogs = []
        #self.openai = AsyncOpenAI()
        '''self.openai = OpenAIAPI(
            api_key=apikey
        )'''

    async def newChat(self, prompt):
        try:
            response = openai.Completion.create(
                engine="KevInvest",  # Or whichever GPT model you're using
                prompt=prompt,
                temperature=0.7,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                user=self.id  # Assuming the API supports custom user identifiers
            )
            # Append both the user's message and GPT's response to the conversation history
            self.chatLogs.append({"user": prompt, "gpt": response.choices[0].text.strip()})
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Sorry, I couldn't process your request."
        return self.openai.Completions.create(model="KevInvest", prompt=prompt, stream=True)


if __name__ == '__main__':
    api = OpenAIAPI()
    print(api.newChat("Hello! How are you?"))