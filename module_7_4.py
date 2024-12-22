# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Использование %
string_with_team1_num = "В команде Мастера кода участников: %d !" % team1_num
print(string_with_team1_num)

string_with_both_teams = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(string_with_both_teams)

# Использование format()
string_score_2 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(string_score_2)

string_team2_time = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(string_team2_time)

# Использование f-строк
string_scores = f"Команды решили {score_1} и {score_2} задач."
print(string_scores)

string_challenge_result = f"Результат битвы: {challenge_result}"
print(string_challenge_result)

string_tasks_and_time = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
print(string_tasks_and_time)
