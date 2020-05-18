# -*- coding: utf-8 -*-
"""
Validando numeros de telefones celulares utilizando expressoes regulares e a ferramenta Regex
https://regex101.com/ p
"""
import re

regex = r"^(\(\d{2}\)\s*)?(9\s)(\d{4}-\d{4})$"

test_str = ("(21) 9 8852-5214\n"
	"(11) 9 9955-1231\n"
	"(35) 9 9975-4521\n"
	"(31) 3851-2587\n"
	"9 8571-5213\n\n"
	"1234-5647\n"
	"0000-0000\n"
	"1111-1111\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

