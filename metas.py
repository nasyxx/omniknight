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
    "是否浏览过相关文档却没找到解决方案？",
    "是否Google过却没有有价值的信息？",
    "请阐述你的需求",
    "请说明你做过的尝试，若有代码请贴出（最小化可复现片段）",
    "请贴出完整的相关错误/日志信息/得到的结果"
)
CHECK = "问问题前做了这些检查了吗？\n  " + "\n  ".join(CHECK_LISTS)

PASTEBIN = "https://pastebin.com/"
GIST = "https://gist.github.com/"

PIN = "t.me/pythonzh/166473"

BOOK = "t.me/pythonzh/6605"

# METAS | key: output string.
METAS = {
    "check": CHECK,
    "long": f"长代码放在这儿:\n{PASTEBIN}\n{GIST}",
    "pin": f"置顶消息是: {PIN}",
    "suggest_book": f"推荐书籍: {BOOK}",
}

# METAS DESCRIPTIONS | key: description
METASD = {
    "check": "Check List",
    "long": "长代码",
    "pin": "置顶消息",
    "suggest_book": "推荐书籍",
}


__all__ = ["METAS", "METASD"]  # pylint: disable=W0612
