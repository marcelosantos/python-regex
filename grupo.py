#*-* coding=utf-8 *-*
import re

text = ("para Contatar "
		  "r. corrego, 551 3º prédio "
		  "Opas - São Paulo Brasil "
		  "+55 31 3261 8083 "
		  "contato@ti.com.br "
		  "11/08/2016")

#buscando a data
pattern = r'\b(\d\d)\/(\d\d)\/(\d{4})'
match = re.search(pattern, text)
if match:
	print(match.group())
	print(match.group(1))
	print(match.group(2)) #etc.
	print(match.group(3)) #etc.
	print(match.span()) #traz ambas as posições
	print(match.start())#posição do ínicio do texto casado
	print(match.end())#posição do fim do texto casado
else:
	print('não casou')

#buscando o email
pattern = r'(\w+)@(\w+)([.combr]+)'
match = re.search(pattern, text)
if match:
	print(match.group())
	print(match.group(1))
	print(match.group(2)) #etc.
	print(match.span()) #traz ambas as posições
	print(match.start())#posição do ínicio do texto casado
	print(match.end())#posição do fim do texto casado
else:
	print('não encontrou')
