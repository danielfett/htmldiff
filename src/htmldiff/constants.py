"""Constants."""
import re

COMMENT_RE = re.compile(br'<!--.*?-->', re.S)
TAG_RE = re.compile(br'<(script|style).*?>.*?</\1>|<.*?>', re.S)
HEAD_RE = re.compile(br'<\s*head\s*>', re.S | re.I)
WS_RE = re.compile(br'^([ \n\r\t]|&nbsp;)+$')
WORD_RE = re.compile(
    br'([^ \n\r\t,.&;/#=<>()-]+|(?:[ \n\r\t]|&nbsp;)+|[,.&;/#=<>()-])'
)


STOPWORDS = (
    'a',
    'about',
    'an',
    'and',
    'are',
    'as',
    'at',
    'be',
    'by',
    'for',
    'from',
    'have',
    'how',
    'I',
    'in',
    'is',
    'it',
    'of',
    'on',
    'or',
    'that',
    'the',
    'this',
    'to',
    'was',
    'what',
    'when',
    'where',
    'who',
    'will',
    'with',
)
