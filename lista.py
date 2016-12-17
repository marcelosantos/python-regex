#*-* coding=utf-8 *-*
import re

lista = ['1teste', '4qualquer', 'maisuma5', 'teste6']

pat = r'^\d'
pat2 = r'.*\d$'
for element in lista:

	m = re.match(pat, element)
	if m:
		print('START: ', element)

	m = re.match(pat2, element)
	if m:
		print('  END: ', element)
