# -*- coding: utf-8 -*-
"""
Validacao de emails por expressoes regulares utlizando a ferramenta Regex
"""


"""
Básica
^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$
https://regex101.com/r/9s4bgv/1/
Básica 2
^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$
https://regex101.com/r/mH4ChC/2/
rfc 5322
^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$
https://regex101.com/r/fkxI15/1/
"""
# Importacao da biblioteca
import re

# Expressap regular

#regex = (r"^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$")
regex = (r"^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$")


# Emails para Validacao
test_str = ("emails = \"\"\"\n"
	"Valid email addresses\n"
	"otavio@gmail.com\n"
	"o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br\n"
	"simple@example.com\n"
	"very.common@example.com\n"
	"disposable.style.email.with+symbol@example.com\n"
	"other.email-with-hyphen@example.com\n"
	"fully-qualified-domain@example.com\n"
	"user.name+tag+sorting@example.com\n"
	"x@example.com\n"
	"example-indeed@strange-example.com\n"
	"example@s.example\n"
	"a@a.com.br.br.br\n"
	"mailhost!username@example.org\n"
	"user%example.com@example.org\n"
	"email@example.com\n"
	"firstname.lastname@example.com\n"
	"email@subdomain.example.com\n"
	"firstname+lastname@example.com\n"
	"email@123.123.123.123\n"
	"\"email\"@example.com\n"
	"1234567890@example.com\n"
	"email@example-one.com\n"
	"_______@example.com\n"
	"email@example.name\n"
	"email@example.museum\n"
	"email@example.co.jp\n"
	"firstname-lastname@example.com\n\n\n"
	"Invalid email addresses\n"
	"Abc.example.com\n"
	"<aqui-te-um@email-pra-validar.com.br>\n"
	"A@b@c@example.com\n"
	"a\"b(c)d,e:f;g<h>i[j\\k]l@example.com\n"
	"just\"not\"right@example.com\n"
	"this is\"not\\allowed@example.com\n"
	"this\\ still\\\"not\\\\allowed@example.com\n"
	"plainaddress\n"
	"#@%^%#$@#$@#.com\n"
	"@example.com\n"
	"<email@example.com>\n"
	"email.example.com\n"
	"email@example@example.com\n"
	".email@example.com\n"
	"email.@example.com\n"
	"email..email@example.com\n"
	"あいうえお@example.com\n"
	"email@example\n"
	"email@-example.com\n"
	"email@example..com\n"
	"Abc..123@example.com\n"
	"”(),:;<>[\\]@example.com\n"
	"just”not”right@example.com\n"
	"this\\ is\"really\"not\\allowed@example.com\n"
	"\"\"\"\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.