#*-* coding=utf-8 *-*
import re

text = ("para Contatar "
		  "r. corrego, 551 3º prédio "
		  "Opas - São Paulo Brasil "
		  "+55 31 3261 8083 "
		  "contato@ti.com.br "
		  "11/08/2016")

#primeiro busca a primeira palavra que começa com letra maiúcula
pattern = r'\b[A-Z]\w+'
match = re.search(pattern, text)
if match:
	print(match.group())
else:
	print('não casou')

#buscar data
pattern = r'\b[0-9]\w+'
match = re.search(pattern, text)
if match:
	print(match.group())
else:
	print('não casou')

#buscar o telefone
pattern = r'\+\d{2}.\d{2}.\d{4}.\d{4}'
match = re.search(pattern, text)
if match:
	print(match.group())
else:
	print('não casou')
