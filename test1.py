'''Тест на чесність.
Поставте 1 бал за відповіді "так" на запитання:
1, 3, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 , 25, 28, 29, 30, 31, 32, 33, 34 
і за відповіді "ні" на питання: 2, 4, 7, 13, 26, 27.
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n",'--name', type=str,
                    help= "Write your name please.")

parser.add_argument("-a", '--age', type=str,
                    help= "Write your age.")

args = parser.parse_args()

name = args.name
age = args.age

level = [
	'Такий результат говорить про яскраво виражену схильність до брехні.\nВірити словами представника'+
	' спільноти "тотальних брехунів" не можна,\nа в спілкуванні, і вже тим більше в справах, з ним треба бути акуратніше.',

	'Трохи чесніше абсолютного брехуна. Люди такого складу люблять прикрашати себе і свою поведінку.\n' + 
	'Вони схильні думати, що все навколо – брехня і всі брехуни.\nОднак насправді ці думки не про інших, а про себе самого.'+
	' Подумайте, чим ви будете займатися у своєму житті,\nякщо будь-які стоять справи в цьому світі будуються на довірі,'+
	' \nа оточуючі вже ставляться до ваших слів критично.',

	'Приклад людини зі здоровою чесністю. Бажанням збрехати не страждає,\nале і патологічною чесністю не наділений.'+
	' Звичайно, така людина зрідка може прикрасити себе,\nсвою поведінку і досягнення, але без шкоди для себе і суспільства.\n'+
	'Він приймає різні свої сторони і іноді дозволяє собі недосказати правду або навіть збрехати, але робить це усвідомлено,\n'+
	'а значить, не грузнучи в брехні. У виправдання цієї брехні слід сказати, що будувати своє життя\nна шаблонах із серії "одна брехня? '+
	'– все одно брехня", "малої брехні не буває", "далі – більше" можна, але не потрібно.\nАдже життя – це не чорно-біле кіно, де все має чіткі межі.'+
	' У реальному житті бувають обставини, в яких говорити абсолютну правду\nіноді небезпечно для життя, та й не завжди доречно.'+
	' Висновок – смиряти чесність потрібно, але головне – не дозволяти собі виходити за рамки\nі не використовувати брехню'+
	' в якості засобу маніпуляції.\nЦе дозволить не перетворитися на запеклого брехуна.',

	'Начебто відповідь напрошується сам собою: ви – найчесніша у світі людина. \nОднак такий високий результат'+
	"може бути пов'язаний не стільки з високою особистісної чесністю,\nскільки з навмисним перекручуванням відповідей і дуже неправильною самооцінкою.\n"+
	'Такий результат насторожує не менше перших двох. Навіть якщо він правдивий і спотворення відповідей не було, то виходить,\n'+
	'що ми маємо справу з явним перекосом чесності, яскрава ознака якого – хамство.\nСказати горбатому, що він горбатий – правдиво, але нерозумно. '+
	'І в такому випадку \nвиникає головне питання: "навіщо і кому це потрібно?". А ще, кажучи таку правду, добре б подумати,\nчи не завдасть вона моральну травму вашому візаві. '+
	'Носіям такої чесності не варто дивуватися тому,\nщо їх можуть не любити навіть близькі люди, адже саме їм і дістається в першу чергу від таких правдолюбців.\n'+
	'Ще одна сторона капітальної чесності – гординя і неймовірно завищена самооцінка, які просто не дозволяють людині\nвизнати в собі хоч крапельку чогось неідеального.'
]

questions = [
	'Буває, що я сміюсь над непристойним анегдотом?',
	'Якщо до мене звертаються вічливо, то я теж завжди відповідаю вічливо.',
	'У мене бувають фінансові труднощі.',
	'Мені завжди приємно, коли люжина, що не імпонує мені, досягає заслуженого успіху.',
	'Бувало, відкладав (-ла) те що потрібно було зробити негайно.',
	'В компанії я веду себе не так як вдома.',
	'Я абсолютно вільний від будь-яких забобонів.',
	'Я не завжди говорю правду.',
	'Коли я з кимось граю, мені завжди хочеться перемогти.',
	'Часом я серджусь.',
	'У своє виправдання я інколи щось придумував.',
	'Буває, інколи я виходжу з себе.',
	'В дитинстві я одразу і без суперечок робив все, що від мене вимагалося.',
	'Часом я роздратований чимось.',
	'Буває, що я сміхом реагую на непристойний жарт.',
	'Бувало я спізнювався на домовлений час.',
	'Часом я люблю попліткувати.',
	'Серед людей, котрих я знаю, є такі котрі мені особливо не подобаються.',
	'Мене особливо не засмучують невдачі людини, котру я не можу терпіти.',
	'Часом я спізнювався.',
	'Мені властиво часом прихвалитись.',
	'Часом немає жодного бажання чимось займатися.', 
	'У мене інколи бувають думки, про які соромно розповісти іншим.',
	'Інколи я був причиною поганого настрою когось з оточуючих.',
	'Бувало, що я говорив не правду.',
	'Всі мої звички є позитивними.',
	'Якщо я щось пообітцяв, я завжди дотримуюсь слова, не дивлячись ні на що.',
	'Часом можу похвалитись.',
	'Будучи підлітком, я проявляв інтерес до заборонених тем.',
	'Іноді я відкладаю на завтра те, що потрібно зробити сьогодні.',
	'У мене бувають думки, яких слід було б соромитись.',
	'Часом я сперечаюсь про речі, про які замало знаю.',
	'Я люблю не всіх своїх знайомих.',
	'Я можу про когось сказати погано.'
]

def var(x):
	if(x == 'y' or x == 'n'): return True
	else: return False

def test(quest):
	count = 0
	no = [1, 3, 6, 12, 25, 26]
	yorn = ' (y / n) '

	for s in quest:
		anser = input(s + yorn)

		while(not var(anser)):
			print('введіть коректну відповідь: "y", або "n" ')
			anser = input(s + yorn)
		else:
			if(anser == 'n' and no.count(quest.index(s)) == 1):
				count += 1
			elif(anser == 'y' and no.count(quest.index(s)) == 0):
				count += 1
			
	return count

if(name == None and age == None):
	print('Please, set your name and age!')
	print('try: -h or --halp')
else:
	print('Цей тест показує на скільки ви чесна людина.\n'+
		'Інструкція:\n'+
		'Уважно прочитайте речення. Залежно від того, чи згодні ви з кожним з них, \n'+
		'дайте відповідь "y" - якщо так, та "n" - якщо ні.\n'+
		'Не думайте над відповіддю довго: перша, яка прийшла в голову, і буде правильною.\n')
	print('Готові розпочати тест? Натисніть "Enter".')
	input()

	result = test(questions)
	print('\nВітаємо ' + name + '!!!')
	print('Щоб отримати результат натисніть "Enter"')
	input()

	if(result >= 0 and result <= 5):
		print(level[0])
	elif(result >= 6 and result <= 13):
		print(level[1])
	elif(result >= 14 and result <= 29):
		print(level[2])
	elif(result >= 30 and result <= 34):
		print(level[3])