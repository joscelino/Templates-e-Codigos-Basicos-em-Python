# -*- coding: utf-8 -*-
"""
Validacao de CPFs
Usar site: https://regex101.com/ patra ver o funcionamento das expressoes regulares
"""
# Importacao das bibliotecas
import re

regex = r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})\d{3}\.\d{3}\.\d{3}-\d{2}$"

test_str = ("199.921.858-21\n"
	"252.758.222-95\n"
	"125.632.856-71\n"
	"153.050.858-96\n\n\n"
	"000.000.000-00\n"
	"111.111.111-11\n"
	"222.222.222-22\n"
	"333.333.333-33\n"
	"444.444.444-44\n"
	"555.555.555-55\n"
	"666.666.666-66\n"
	"777.777.777-77\n"
	"888.888.888-88\n"
	"999.999.999-99")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

