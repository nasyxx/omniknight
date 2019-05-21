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

PEP = "https://www.python.org/dev/peps/pep-{}/"

PASTES = [
    "https://pastebin.com/",
    "https://gist.github.com/",
    "https://paste.ubuntu.com/",
    "https://hastebin.com/",
]

PIN = "t.me/pythonzh/196856"

DOCS = [
    "[官方文档](https://docs.python.org/zh-cn/3/)",
    "[编程小白的第一本 Python 入门书](http://www.ituring.com.cn/book/1863)",
    "[Cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/)",
    r"[免费的书](https://github.com/EbookFoundation/free-programming-books/"
    "blob/master/free-programming-books-zh.md#python)",
]

EDITORS = [
    "[Emacs](https://www.gnu.org/software/emacs/)",
    "[Visual Studio Code](https://code.visualstudio.com/)",
    "[PyCharm](https://www.jetbrains.com/pycharm/)",
    "[Vim](https://www.vim.org/)",
]

WPG = "https://frostming.com/2019/03-13/where-do-your-packages-go"

ME = "https://github.com/nasyxx/omniknight"

WARN = "禁止广告、引战、开车、拼车、黑产、过激言论、作弊及有偿任务，将警告或封禁。"

FONTS = [
    "FiraCode",
    "Operator Mono",
    "Source Code Pro",
    "Ubuntu Mono",
    "SF Mono",
    "Consolas",
    "Inconsolata",
    "[在线字体预览](https://app.programmingfonts.org/)",
]

# METAS | key: output string.
METAS = {
    "check list": CHECK,
    "pep8": PEP.format("0008"),
    "pep257": PEP.format("0257"),
    "long": f"长代码放在这儿:\n" + "\n".join(PASTES),
    "where do your packages go": WPG,
    "docs": "\n".join(DOCS),
    "editors": "\n".join(EDITORS),
    "pin": f"置顶消息是: {PIN}",
    "warn": WARN,
    "me": ME,
    "fonts": "\n".join(FONTS),
}

# METAS DESCRIPTIONS | key: description
METASD = {
    "check list": "Check List",
    "pep8": "PEP 8",
    "pep257": "PEP 257",
    "long": "长代码",
    "where do your packages go": "你的包去哪儿了？",
    "docs": "推荐手册",
    "editors": "编辑器推荐",
    "pin": "置顶消息",
    "warn": "警告⚠️️",
    "me": "Who am I?",
    "fonts": "编程字体推荐",
}

# METAS EXTRA OPTIONS

METASEX = {
    "me": {"parse_mode": None},
    "long": {"disable_web_page_preview": True},
    "docs": {"disable_web_page_preview": True},
    "editors": {"disable_web_page_preview": True},
    "check list": {"disable_web_page_preview": True},
}

__all__ = ["METAS", "METASD", "METASEX"]  # pylint: disable=W0612
