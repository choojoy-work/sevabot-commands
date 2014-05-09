#!/sevabot

from __future__ import unicode_literals

import re, urllib2, logging

from sevabot.bot.stateful import StatefulSkypeHandler
from sevabot.utils import ensure_unicode, get_chat_id

logger = logging.getLogger("Tasks")

# Set to debug only during dev
logger.setLevel(logging.INFO)

logger.debug("Tasks module level load import")

class UrlInfoHandler(StatefulSkypeHandler):
    def get_title(self, url):
        response = urllib2.urlopen(url)
        html = response.read()
        tre = re.compile("<title>(.+?)</title>")
        return tre.search(html).group(1)

    def handle_message(self, msg, status):
        body = ensure_unicode(msg.Body)
        logger.debug(body)
        r = re.search("(?P<url>https?://[^\s]+)", body)
        if r:
            for url in r.groups():
                msg.Chat.SendMessage(self.get_title(url))

sevabot_handler = UrlInfoHandler()

__all__ = ["sevabot_handler"]