from colorama.ansi import clear_screen
import os
os.system('clear')
clear_screen
from colorama import Fore, Back
print(Fore.GREEN, Back.LIGHTBLACK_EX)
os.system("figlet -f smslant 'FSCounter'")
print('__________________________________________' + Back.RESET, Fore.WHITE)
print('Привет эта программа поможет посчитать необходимое кол-во слитков на изготовление какого-либо предмета в FS...')
print(Fore.LIGHTGREEN_EX)
print('Что изготавливаем?')
print(Fore.GREEN)
print('1.Двигатели;')
print('2.Манипуляторы;')
print('3.Турбины;')
print('4.Эл.компоненты;')
print('5.Микросхемы;')
print('6.Процессоры;')
print('7.Нагрев.элементы;')
print('8.Сплавы...')
print(Fore.RED)
l = 0
choise = int(input('~$ '))
if choise not in range(1, 9) :
    print(Fore.BLACK + Back.RED + 'Program incorupted, reason: 82736266(Долбоёб)')
    print(Fore.RESET, Back.RESET)
if choise in range(1,7) :
    Kolvo = int(input('Количество: '))
    a = 0
if choise == 1 :
    if int(Kolvo) % 2 !=0 :
        a = a+1
    print(Fore.YELLOW)
    print('В металлоформовщик (Подшипники): ' + str(Kolvo*3) + ' слитков;')
    print('В металлоформовщик (Стержни): ' + str(int((Kolvo + a) / 2)) + ' слитков;')
    print('В металлоформовщик (Шестерни): '+ str(Kolvo * 2) + ' слитков;')
    print('В сборщик механизмов (Роторы): '+ str(Kolvo) + ' слитков;')
    print('В сборщик механизмов (Статоры): '+ str(Kolvo) +' слитков;')
    print('В формовщик проводов: ', str(Kolvo * 2), ' слитков;')
    print('Итого: '+ str(Kolvo * 2) +' слитков на провода,'+ str(int((Kolvo*7) + ((Kolvo + a) / 2))) + ' слитков на остальные части.')
    print('L - Сборщик механизмов, * - Металоформовщик,')
    print('C - Формовщик проводов, - - Конвейер')
    print('                                ')
    print(' L'+str(Kolvo)+'*'+str(Kolvo*3)+'*'+str(int((Kolvo+a)/2)))
    print(' L-------                       ')
    print(' L'+str(Kolvo)+'*'+str(Kolvo*2)+'C'+str(Kolvo*2))
if choise == 2 :
    d = Kolvo * 5 / 2
    if Kolvo % 2 != 0 :
        d = ((Kolvo * 5 + 1) / 2)
    print(Fore.YELLOW)
    print('В сборщик механизмов (Манипуляторы): ', str(Kolvo*3), ' слитков')
    print('В металлофорщик (Стержни): ', str(int(d)) , ' слитков')
    print('В металлофорщик (Подшипники): ', str(Kolvo * 3), ' слитков')
    print('В формовщик проводов->сборщик эл.компонентов: ', str(Kolvo*4), ' слитков')
    print('В формовщик проводов->сборщик эл.компонентов->сборщик микросхем: ', str(Kolvo*4), ' слитков и ', str(Kolvo), ' слитков на пластины')
    print('Итого: ', str(Kolvo * 4 * 2), ' слитков на провода,', str(int(Kolvo*3 + d + Kolvo*3)), ' слитков на остальные части и ', Kolvo, ' слитков на пластины')
    print('L - Сборщик мех., * - Металлоформовщик,')
    print('C - Формовщик проводов, U-Сборщик эл.комп.')
    print('# - сборщик эл.схем, - - конвейер')
    print('                                      ')
    print('    *'+str(int(d))+'#UC'+str(Kolvo*4)  )
    print('    L'+str(Kolvo*3)+'-------          ')
    print('    *'+str(Kolvo * 3)+'UC'+str(Kolvo*4))
    print('                                      ')
if choise == 3 :
    print(Fore.YELLOW)
    print(str(Kolvo*6), ' слитков на пластины')
    print(str(Kolvo), ' слитков в металлоформовщик (стержни)')
    print(str(Kolvo*2), ' слитков в металлоформовщик (подшипники)')
    print('Итого: ', str((Kolvo*6)+(Kolvo*2)+Kolvo), ' слитков.')
    print('* - Металлоформовщик, = - Пресс')
    print('L - Сборщик механизмов')
    print('                           ')
    print('     *'+str(Kolvo)          )
    print('     L='+str(Kolvo*2)       )
    print('     *'+str(Kolvo*3)        )
if choise == 4 :
    print(Fore.YELLOW)
    print('В формовщик проводов->сборщик электрокомпонентов ', str(Kolvo*2), ' слитков.')
    print('Итого: ', str(Kolvo*2), ' слитков.')
    print('U - Сборщик эл.комп., C - Формовщик проводов')
    print('                                      ')
    print('                                      ')
    print('   UC'+str(Kolvo*2)                    )
if choise == 5 :
    print(Fore.YELLOW)
    print('В формовщик проводов->сборщик эл.компонентов->сборщик эл.схем ', str(Kolvo*4), ' слитков.')
    print('Итого: ', str(Kolvo*4), ' слитков на провода и ', str(Kolvo), ' слитков на пластины.')
    print('# - Сборщик эл.схем, U - сборщик эл.комп')
    print('C - Формовщик проводов')
    print('                                      ')
    print('                                      ')
    print('    #'+str(Kolvo)+'UC'+str(Kolvo*4)    )
if choise == 6 :
    Yadra = int(input('Кол-во ядер: '))
    print(Fore.YELLOW)
    print('В формовщик проводов->сборщик эл.компонентов->сборщик эл.схем ', str(int(Kolvo) * 4 * int(Yadra)), ' слитков и ', str(Yadra), ' пластин из вольф.стали');
    print('В формовщик проводов->сборщик эл.компонентов(Охл.элементы) ', str(Kolvo * Yadra), ' слитков платины.');
    print('В формовщик продов->сборщик эл.комп.->сборщик эл.схем->сборщик эл.комп.(Охл.элемнты) ', str(int(Kolvo) * 4 * int(Yadra)), ' слитков платины и ', str(Yadra), ' пластин из вольф.стали');
    print('В гидр.прес->сборщик эл.комп.(охл.эл) ', str(Yadra), ' слитков золота');
    print('Итого: ', str(int(Kolvo) * 4 * int(Yadra)), ' слитков на эл.схемы, ', str((int(Kolvo) * 4 * int(Yadra)) + (int(Kolvo) * int(Yadra))), ' слитков платины на охл.элементы и ', str(int(Yadra) * 2), ' слитков вольф.стали на пластины');
if choise == 7 :
    print(Fore.YELLOW)
    print(str(Kolvo), ' слитков олова в формовщик проводов->сборщик эл.комп.(Нагрев.элементы)')
    print(str(Kolvo), ' слитков железа в гидр.прес->сборщик эл.комп.(Нагрев.элементы)')
    print(str(Kolvo * 4), ' слитков олова и ', str(Kolvo), ' в формовщик проводов->сборщик эл.комп.->сборщик эл.схем->сборщик эл.комп.(Нагрев.элементы)')
if choise == 8 :
    l = 1
    print()
    print(Fore.LIGHTRED_EX + '1.Бронза;')
    print(Fore.WHITE + '2.Сталь;')
    print(Fore.LIGHTMAGENTA_EX + '3.Нерж.сталь;')
    print(Fore.YELLOW + '4.Электрум;')
    print(Fore.LIGHTBLACK_EX + '5.Вольф.сталь;')
    print(Fore.LIGHTWHITE_EX + '6.Платинин;')
    print(Fore.LIGHTMAGENTA_EX + '7.Титан-вольфрам;')
    print(Fore.MAGENTA + '8.Тантал-титан;')
    print(Fore.LIGHTBLUE_EX + '9.Осмиридиум;')
    print(Fore.BLUE + '10.Неоридиум.')
    print(Fore.RED)
    choiseB = int(input('~$ '))
    if choiseB in range(1, 11) :
        Kolvo = int(input('Количество: '))
    else :
        print(Fore.BLACK + Back.RED + 'Program incorupted, reason: 82736266(Долбоёб)')
        print(Back.RESET, Fore.RESET)
    print(Fore.YELLOW)
    if choiseB == 1 :
        while Kolvo % 4 != 0 :
            Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков меди и ' + str(SlitokB) + ' слитков олова')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков бронзы')
    if choiseB == 2 :
        while Kolvo % 4 != 0 :
            Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков железа и ' + str(SlitokB) + ' угля')
    if choiseB == 3 :
        while Kolvo % 4 != 0 :
            Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков стали и ' + str(SlitokB) + ' слитков хрома')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков нерж.стали')
        print('Вы можете посчитать кол-во компонентов для стали в этой программе, перезапустив её.')
    if choiseB == 4 :
        while Kolvo % 8 != 0 :
                Kolvo += 1
        b = Kolvo // 8
        SlitokA = b * 5
        SlitokB = b * 3
        print(str(SlitokA) + ' слитков серебра и ' + str(SlitokB) + ' слитков золота')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков электрума')
    if choiseB == 5 :
        while Kolvo % 5 != 0 :
                Kolvo += 1
        b = Kolvo // 5
        SlitokA = b * 3
        SlitokB = b * 2
        print(str(SlitokA) + ' слитков стали и ' + str(SlitokB) + ' слитков вольфрама')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков вольф.стали')
        print('Вы можете посчитать кол-во компонентов для стали в этой программе, перезапустив её')
    if choiseB == 6 :
        while Kolvo % 3 != 0 :
                Kolvo += 1
        b = Kolvo // 3
        SlitokA = b * 2
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков платины и ' + str(SlitokB) + ' слитков серебра')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков платинина')
    if choiseB == 7 :
        while Kolvo % 4 != 0 :
                Kolvo += 1
        b = Kolvo // 4
        SlitokA = b * 3
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков титана и ' + str(SlitokB) + ' слитков вольфрама')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков вольфрам-титана')
    if choiseB == 8 :
        while Kolvo % 8 != 0 :
                Kolvo += 1
        b = Kolvo // 8
        SlitokA = b * 5
        SlitokB = b * 3
        print(str(SlitokA) + ' слитков тантала и ' + str(SlitokB) + ' слитков титана')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков тантал-титана')
    if choiseB == 9 :
        while Kolvo % 2 != 0 :
                Kolvo += 1
        b = Kolvo // 2
        SlitokA = b * 1
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков иридия и ' + str(SlitokB) + ' слитков осмия')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков осмиридия')
    if choiseB == 10 :
        while Kolvo % 3 != 0 :
                Kolvo += 1
        b = Kolvo // 3
        SlitokA = b * 2
        SlitokB = b * 1
        print(str(SlitokA) + ' слитков неодима и ' + str(SlitokB) + ' слитков иридия')
        print('Вы получите ' + str(SlitokA + SlitokB) + ' слитков неоридиума')
print(Fore.WHITE)
yn = str(input('Перезапумтить программу?(y/n): '))
if yn == 'y' or 'Y' :
    os.system('python FSCounter.py')