import json


class ChatClient:
    def __init__(self, bot):
        self.bot = bot

    async def send(self, channel_dict, message):
        return await self.execute({
            "method": "send",
            "params": {
                "options": {
                    "channel": channel_dict,
                    "message": {"body": message}
                }
            }
        })

    async def react(self, channel_dict, message_id, reaction):
        return await self.execute({
            "method": "reaction",
            "params": {
                "options": {
                    "channel": channel_dict,
                    "message_id": message_id,
                    "message": {"body": reaction}
                }
            }
        })

    async def execute(self, command):
        return await self.bot.submit("keybase chat api", json.dumps(command).encode('utf-8'))
