import lightbulb
import hikari
from env import *

plugin = lightbulb.Plugin("vxtwitterfix")


def load(bot):
    bot.add_plugin(plugin)


@plugin.listener(hikari.MessageCreateEvent)
async def reply(event: lightbulb.events) -> None:
    if not event.is_human or event.message.content is None:
        return
    if "https://twitter.com/" in event.message.content:
        message = event.message.content

        message = message.replace("https://twitter.com/", "https://vxtwitter.com/")

        await event.message.respond(message)
    elif "https://x.com/" in event.message.content:
        message = event.message.content

        message = message.replace("https://x.com/", "https://vxtwitter.com/")

        await event.message.respond(message)
