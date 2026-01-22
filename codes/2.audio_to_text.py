from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

class AudioToText:
    def __init__(self,audio_base64):
        self.audio_base64 = audio_base64

    def order(self):
        model = init_chat_model(
            model="zai-org/GLM-4.6V",
            model_provider="openai",
            base_url="https://api.siliconflow.cn/v1",
            api_key="sk-sxftwjczgxixpdjmydjejwqxwzvtqaapmrtyxuxyyolahkfu",
        )

        agent = create_agent(
            model=model,
            system_prompt="将语音转为文本",
        )

        response = agent.invoke(
            {"messages": [
                {"role": "user",
                 "content": [
                     {
                         "type": "audio_url",
                         "audio_url": {
                             "url": f"data:image/jpeg;base64,{self.audio_base64}"
                         }
                     },
                     {
                         "type": "text",
                         "text": "将语音转为文本"

                     }
                 ]
                 }
            ]
            }
        )
        return response