from ZxForm.handler import RedisHandler


class GroupHandler(RedisHandler):
    # @
    async def post(self):
        re_data = {}

        await self.finish()