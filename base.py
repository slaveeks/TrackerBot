import asyncio


class CommandBase:

    def __init__(self, sdk):
        self.sdk = sdk


class CommandSome:

    def __init__(self, collables):
        self.callables = collables

    async def __call__(self, payload):
        await asyncio.wait([obj(payload) for obj in self.callables])