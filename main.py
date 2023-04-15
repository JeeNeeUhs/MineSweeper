from random import randint
import mine

from colorama import Fore, Back, Style

nums = {}

for i in range(1, 26):
    nums[str(i)] = 0

sides = {
  '1' : [1 ,6 ,7] ,
  '2' : [1 ,3 ,6 ,7 ,8] ,
  '3' : [2 ,4 ,7 ,8 ,9] ,
  '4' : [3 ,5 ,8 ,9 ,10] ,
  '5' : [4 ,9 ,10] ,
  '6' : [1 ,2 ,7 ,11 ,12] ,
  '7' : [1 ,2 ,3 ,6 ,8 ,11 ,12 ,13] ,
  '8' : [2 ,3 ,4 ,7 ,9 ,12 ,13 ,14] ,
  '9' : [3 ,4 ,5 ,8 ,10 ,13 ,14 ,15] ,
  '10' : [4 ,5 ,9 ,14 ,13 ,15] ,
  '11' : [6 ,7 ,12 ,16 ,17] ,
  '12' : [6 ,7 ,8 ,11 ,13 ,16 ,17 ,18] ,
  '13' : [7 ,8 ,9 ,12 ,14 ,17 ,18 ,19] ,
  '14' : [8 ,9 ,10 ,13 ,15 ,18 ,19 ,20] ,
  '15' : [9 ,10 ,14 ,19 ,20] ,
  '16' : [11 ,12 ,17 ,21 ,22] ,
  '17' : [11 ,12 ,13 ,16 ,18 ,21 ,22 ,23] ,
  '18' : [12 ,13 ,14 ,17 ,19 ,22 ,23 ,24] ,
  '19' : [13 ,14 ,15 ,18 ,20 ,23 ,24 ,25] ,
  '20' : [14 ,15 ,19 ,24 ,25] ,
  '21' : [16 ,17 ,22] ,
  '22' : [16 ,17 ,18 ,21 ,23] ,
  '23' : [17 ,18 ,19 ,22 ,24] ,
  '24' : [18 ,19 ,20 ,23 ,25] ,
  '25' : [19 ,20 ,24] ,
   
}


selection = int(input('bir sayi yaz: '))

mines = mine.select(selection)



for x in mines:
   y = sides[str(x)] 
   for x in y:
      nums[str(x)] = nums[str(x)] + 1
   
   
for x in mines:
  nums[str(x)] = '*' #determine mines

    

def board() :
    print(Fore.CYAN + str(0) + Style.RESET_ALL, '|', Fore.CYAN + str(1) + Style.RESET_ALL, '|', Fore.CYAN + str(2) + Style.RESET_ALL, '|', Fore.CYAN + str(3) + Style.RESET_ALL, '|', Fore.CYAN + str(4) + Style.RESET_ALL, '|', Fore.CYAN + str(5) + Style.RESET_ALL)
    print('~', '|', '~~~~~~~~~~~~~~~~~')
    print(Fore.CYAN + str(1) + Style.RESET_ALL, '|', nums['1'], '|', nums['2'], '|',nums['3'], '|', nums['4'], '|', nums['5'])
    print('~', '|', '~~~~~~~~~~~~~~~~~')
    print(Fore.CYAN + str(2) + Style.RESET_ALL, '|', nums['6'], '|', nums['7'], '|',nums['8'], '|', nums['9'], '|', nums['10'])
    print('~', '|', '~~~~~~~~~~~~~~~~~')
    print(Fore.CYAN + str(3) + Style.RESET_ALL, '|', nums['11'], '|', nums['12'], '|',nums['13'], '|', nums['14'], '|', nums['15'])
    print('~', '|', '~~~~~~~~~~~~~~~~~')
    print(Fore.CYAN + str(4) + Style.RESET_ALL, '|', nums['16'], '|', nums['17'], '|',nums['18'], '|', nums['19'], '|', nums['20'])
    print('~', '|', '~~~~~~~~~~~~~~~~~')
    print(Fore.CYAN + str(5) + Style.RESET_ALL, '|', nums['21'], '|', nums['22'], '|',nums['23'], '|', nums['24'], '|', nums['25'])

board()

