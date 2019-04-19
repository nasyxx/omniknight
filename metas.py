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
filename : metas.py
project  : Omniknight
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
CHECK_LISTS = (
    "是否认真阅读了错误提示并明白它在说什么？",
    "是否浏览过文档的相关章节却没找到解决方案？",
    "是否  Google 过却没得到有价值的信息？",
    "请阐述你的需求",
    "请描述你尝试的步骤，若有代码请贴出（最小化可复现片段）",
    "请贴出完整的相关错误/日志信息/得到的结果",
    "[提问的技巧](https://t.me/pythonzh/105952)",
)
CHECK = "问问题前做了这些检查了吗？\n  " + "\n  ".join(CHECK_LISTS)

PEP8 = "https://www.python.org/dev/peps/pep-0008/"

PASTES = [
    "https://pastebin.com/",
    "https://gist.github.com/",
    "https://paste.ubuntu.com/",
]

PIN = "t.me/pythonzh/196856"

BOOK = "t.me/pythonzh/6605"

WPG = "https://frostming.com/2019/03-13/where-do-your-packages-go"

ME = "https://github.com/nasyxx/omniknight"

WARN = "禁止广告、引战、开车、拼车、黑产、过激言论、作弊及有偿任务，将警告或封禁。"

# METAS | key: output string.
METAS = {
    "check list": CHECK,
    "pep8": PEP8,
    "long": f"长代码放在这儿:\n" + "\n".join(PASTES),
    "where do your packages go": WPG,
    "pin": f"置顶消息是: {PIN}",
    "warn": WARN,
    "suggest book": f"推荐书籍: {BOOK}",
    "me": ME,
}

# METAS DESCRIPTIONS | key: description
METASD = {
    "check list": "Check List",
    "pep8": "PEP 8",
    "long": "长代码",
    "where do your packages go": "你的包去哪儿了？",
    "pin": "置顶消息",
    "warn": "警告⚠️️",
    "suggest book": "推荐书籍",
    "me": "Who am I?",
}

# METAS EXTRA OPTIONS

METASEX = {"me": {"parse_mode": None}}

__all__ = ["METAS", "METASD", "METASEX"]  # pylint: disable=W0612
