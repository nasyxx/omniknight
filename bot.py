#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Apr  8, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : bot.py
project  : Omniknight
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
from typing import Tuple

# Other Packages
from telegram import InputTextMessageContent, InlineQueryResultArticle
from telegram.ext import Updater, CallbackContext, InlineQueryHandler
from telegram.update import Update

from metas import METAS, METASD
from config import TOKEN as BOT_TOKEN


def query_meta(s: str) -> Tuple[str, ...]:
    """Query meta data."""
    return tuple(filter(lambda m: s in m, METAS)) or tuple(METAS)


def meta(update: Update, context: CallbackContext) -> None:
    """Response the metadata."""
    (
        lambda qs, ans, id_: qs
        and ans(
            id_,
            list(
                map(
                    lambda q: InlineQueryResultArticle(
                        id=q,
                        title=q,
                        description=METASD[q],
                        input_message_content=InputTextMessageContent(
                            METAS[q],
                            parse_mode="Markdown",
                            disable_web_page_preview=False,
                        ),
                    ),
                    qs,
                )
            ),
        )
    )(
        query_meta(update.inline_query.query.lower().lstrip("meta_")),
        context.bot.answer_inline_query,
        update.inline_query.id,
    )


def main() -> None:
    """Main funcion."""
    bot = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = bot.dispatcher
    dispatcher.add_handler(InlineQueryHandler(meta))
    bot.start_polling()


if __name__ == "__main__":
    main()
