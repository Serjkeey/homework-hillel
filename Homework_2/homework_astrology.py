import datetime
import calendar

user_date = int(input('Введіть день народження:  '))
user_month = int(input('Введіть місяць свого народження:  '))
max_day = calendar.monthrange(2023, user_month)[1]

if not (1 <= user_date <= max_day and 1 <= user_month <= 12):
    print('Помилка, щось введено не вірно!')
    exit()

user_date = datetime.date(2023, user_month, user_date)
if datetime.date(2023, 3, 21) <= user_date <= datetime.date(2023, 4, 20):
    print('Овен : \nСьогодні у вас був важкий день, лягайте спати раніше, бо завтра день буде ще ваще!')

elif datetime.date(2023, 4, 21) <= user_date <= datetime.date(2023, 5, 21):
    print('Телець  : \nСьогодні ви з\'їли булочку з маком та випили чай, це ваша винагорода за те, що ви витримали цей день!' )

elif datetime.date(2023, 5, 22) <= user_date <= datetime.date(2023, 6, 21):
    print('Близнята  : \nВчити Пайтон ніколи не пізно, починайте вже сьогодні, і ваше життя змінится на краще ')

elif datetime.date(2023, 6, 22) <= user_date <= datetime.date(2023, 7, 22):
    print('Рак  : \nЯкщо ви рак, то вам вже нічого не допоможе')

elif datetime.date(2023, 7, 23) <= user_date <= datetime.date(2023, 8, 21):
    print('Лев  : \nСьогодні до вас підійде роздягненний незнайомець, він у вас попросить одяг і мотоцикл, дайте йому все, бо він прилетів з майбутнього спасати людство' )

elif datetime.date(2023, 8, 22) <= user_date <= datetime.date(2023, 9, 23):
    print('Діва  : \nПобалуйте себе сьогодні якимось подарунком :)')

elif datetime.date(2023, 9, 24) <= user_date <= datetime.date(2023, 10, 23):
    print('Терези  : \nСьогодні краще відмовитись від роботи, і весь день провести за улюбленним серіалом')

elif datetime.date(2023, 10, 24) <= user_date <= datetime.date(2023, 11, 22):
    print('Скорпіон  : \nСьогодні у вас весь день буде поганий настрій, щоб він покращився, сходіть до зоопарку та покорміть капібару')

elif datetime.date(2023, 11, 23) <= user_date <= datetime.date(2023, 12, 21):
    print('Стрілець  : \nСтрільці - це самий крутий знак зодіаку, я це знаю, бо сам стрілець :)')

elif datetime.date(2023, 12, 22) <= user_date <= datetime.date(2023, 1, 20):
    print('Козеріг  : \nСьогодні саме той день, коли варто передивитися ваш улюбленний фільм')

elif datetime.date(2023, 1, 21) <= user_date <= datetime.date(2023, 2, 18):
    print('Водолій  :  \nЯкщо вашого друга збила машина, то він вам більше не друг, бо друзі, на дорозі не валяються ')

elif datetime.date(2023, 2, 19) <= user_date <= datetime.date(2023, 3, 20):
    print('Риби  :  \nСьогодні саме той день, щоб зібратись з друзями на шашлики')
