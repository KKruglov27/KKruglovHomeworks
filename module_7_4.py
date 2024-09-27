
team1_num = 5
team2_num = 6
score_1 = 44
score_2 = 44
team1_time = 2225.34535
team2_time = 2230.44566
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / (score_1 + score_2)
challenge_result = 'Победа команды'
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'


print('В команде "Мастера кода" участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d:' % (team1_num, team2_num))

print('Команда {team2} решила задач {score}!'.format(team2=team2_name, score=score_2))
print('{team2} решили задачи за {time} c!'.format(team2=team2_name, time=team2_time))

print(f'Команды решили {score_1} и {score_2} задач')

if score_1 == score_2 and team1_time == team2_time:
    print(f'Результат битвы: Ничья!')
else:
    print(f'Результат битвы: {challenge_result} {team2_name if score_2 > score_1 else team1_name}!' and
f'Результат битвы: {challenge_result} {team2_name if score_2 == score_1 and team2_time < team1_time else team1_name}!')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!')
