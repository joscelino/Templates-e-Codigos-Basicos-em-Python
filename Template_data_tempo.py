# -*- coding: utf-8 -*-
''' Template para manipulacao de dados de tempo'''
# Importacao das bibliotecas
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
from pytz import timezone
import calendar

# Conversoes simples
dia_a = timedelta(days= 2, hours=6)
dia_b = timedelta(hours=4.5)

# Converter strings em datetimes
text = '2020-05-20'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)

# Somando variaveis
soma_days = dia_a + dia_b

# Visualizando conversoes 
soma_days.days
soma_days.seconds
soma_days.seconds/3600
soma_days.total_seconds()/3600

# Outras operacoes com datas
dia_aa = datetime(2020, 3, 1)
dia_bb = datetime(2020, 2, 28)

(dia_aa - dia_bb)
(dia_aa - dia_bb).days

dia_a + relativedelta(months=+3)
relative_days = relativedelta(dia_bb, dia_aa)
relativedelta(months =+2, days =+ 28)

relative_days.months
relative_days.days

# Proxima Sexta-feira
print(datetime.now() + relativedelta(weekday=FR))

# Ultima Sexta-feira
print(datetime.now() + relativedelta(weekday=FR(-1)))

