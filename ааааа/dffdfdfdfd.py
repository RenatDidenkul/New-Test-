import random

truths = [
    "Ты ел крабов?",
    "Какую еду ты ненавидишь больше всего?",
    "Как выглядела твоя школа?",
    "Если бы ты мог стать кем угодно на один день, кем бы ты стал и почему?",
    "Ты любиш ходить по улицах?"
]

dares = [
    "Сделай курицу.",
    "Попробуй сделать сальто назад.",
    "Напиши письмо соседу сверху.",
    "Позвони своему другу.",
    "Скажи привет."
]

def truth_or_dare():
    players = []
    num_players = int(input("Введите количество игроков: "))

    for i in range(num_players):
        player_name = input("Введите имя игрока {}: ".format(i+1))
        players.append(player_name)

    while True:
        player = random.choice(players) 
        choice = input("\n{}: Правда или Действие? (введите 'п' или 'д'): ".format(player)).lower()

        if choice == 'п':
            truth = random.choice(truths)
            print("{} отвечает: {}".format(player, truth))
        elif choice == 'д':
            dare = random.choice(dares)
            print("{} должен: {}".format(player, dare))
        else:
            print("Неправильный ввод! Пожалуйста, введите 'п' или 'д'.")

        play_again = input("\nПродолжаем игру? (да/нет): ").lower()
        if play_again != 'да':
            print("Игра окончена.")
            break

truth_or_dare()