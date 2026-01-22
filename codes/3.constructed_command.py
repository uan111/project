from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

class ConstructedCommand:
    def __init__(self,base64_image,order):
        self.base64_image = base64_image
        self.order = order

    def constructed_command(self):
        model = init_chat_model(
            model="zai-org/GLM-4.6V",
            model_provider="openai",
            base_url="https://api.siliconflow.cn/v1",
            api_key="sk-sxftwjczgxixpdjmydjejwqxwzvtqaapmrtyxuxyyolahkfu",
        )

        SYSTEM_PROMPT = """你是投资专家，根据user的交易命令和图片输出交易的信息。
        请按照此格式回复，全部用英文和数字，不要出现中文：price=..., qty=..., code=..., trd_side=...,order_type=OrderType.NORMAL

        price指订单价格，如果user的交易命令指定了价格就直接输出此价格，如果user的交易命令出现了‘在当前价格提高(降低)百分之多少的时候买入(卖出)’则输出图片中的价格进行相应运算之后的价格，输出完整小数，不要四舍五入；qty指订单数量，根据user的交易命令确定；code指股票的代码，根据图片确定；trd_side指交易方向，根据user的交易命令输出TrdSide.BUY或TrdSide.SELL；order_type指订单类型，如果user的交易命令中有价格信息(直接指定或者需要运算都算有价格信息)就是OrderType.NORMAL，没有价格信息则是OrderType.MARKET

        示例：price=510.0, qty=100, code=00700, trd_side=TrdSide.BUY, order_type=OrderType.NORMAL

        你有工具可以使用，已知的的价格是a，百分数或者倍数是b，比如若交易命令为以20元的30%为价格买入5股则相当于以20乘以30%的价格买入5股即以6元的价格买入5股."""

        agent = create_agent(
            model=model,
            tools=[],
            system_prompt=SYSTEM_PROMPT,
        )

        response = agent.invoke(
            {"messages": [
                {"role": "user",
                 "content": [
                     {
                         "type": "image_url",
                         "image_url": {
                             "url": f"data:image/jpeg;base64,{self.base64_image}"
                         }
                     },
                     {
                         "type": "text",
                         "text": f"交易命令：{self.order}"

                     }
                 ]
                 }
            ]
            }
        )
        return response