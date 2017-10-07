participant  = {'name':'Kate', 'country':'Ukraine', 'favourite_numbers':[3, 7, 15]}
print(participant['name'])
participant['fav_lang'] = 'rus'
print(participant['fav_lang'])
participant.pop('fav_lang')
print(participant)
2<5
2 < 5
print(2 < 5)
print(2*10<5)
print(5 == 5)
print(5!= 2)
print(5!= 5)
print(True and True)
print(True or True)
a = 2
b = a+4
def func(participant):
	if (participant.get('name') == 'Kate') and (participant.get('country') == 'Ukraine'):
		print('OK')
	elif (participant.get('name') == 'Kate') and (participant.get('country') != 'Ukraine'):
		print('Name OK')
	else:
		print('Not OK')
func(participant)
participant['country'] = 'China'
func(participant)
def hi(name):
	print('hi,', name)
	print('how are you?')
hi ('Nata')

girls = ['Kate', 'Ola', 'Yulia', 'Natalia']
# for name in girls:
# 	hi (name)
# 	print('Next girl!')

for name in range((len(girls)-2), len(girls)):
	print('_____________')
	hi (girls[name])
	print('Next girl!')
