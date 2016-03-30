#!/usr/bin/python
import sqlparse
import sys
import re

from sys import stdin

pat = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}).*org.hibernate.SQL\s+:\s+(.+)')

for line in sys.stdin.readlines():
    match = pat.match(line)
    if not match:
        continue

    time = match.group(1)
    sql = match.group(2)

    sql = re.compile(r'select .{41,} from').sub('select columns_removed from', sql)
    sqlformatted = sqlparse.format(sql, reindent=False, keyword_case='upper', identifier_case='lower')
    print("%s,\"%s\"" % (time, sqlformatted))
