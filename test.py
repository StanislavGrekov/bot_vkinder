from main import users_insert, pretendents_insert, favourites_insert,pretendents_output,favourites_output,vk_users_param_output, delete_user
from pprint import pprint

if __name__ == '__main__':
###############################Вносим пользователей ВК################################
    # print(users_insert(123457222,  'Стас', 'Михайлов', 'Новгород', 25, 2))
    # print(users_insert(123457159, 'Александр', 'Семенов', 'Витебск', 30, 2))
    # print(users_insert(123457279, 'Михаил', 'Кайгородов', 'Кайгородово ', 30, 2))

###############################Вносим претендентов ################################
    # print(pretendents_insert(123457222, 159753759, 'Александра', 'Жмаева',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493' ))
    #
    # print(pretendents_insert(123457222, 159753154, 'Ирина', 'Клементьева',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493' ))
    #
    # print(pretendents_insert(123457222, 1597535852, 'Александра', 'Семенова',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493' ))
    # #
    # print(pretendents_insert(123457159, 159753552, 'Екатерина', 'Букина',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493' ))
    #
    # print(pretendents_insert(123457159, 1597535895, 'Наталья', 'Ростова',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493' ))


##############################Вносим избранных ################################
    # print(favourites_insert(123457222, 159753759, 'Александра', 'Жмаева',
    #                     'https://vk.com/photo51800929_457257493',
    #                     'https://vk.com/photo51800929_457257493',
    #                     'https://vk.com/photo51800929_457257493'))
    # print(favourites_insert(123457159, 1597535895, 'Наталья', 'Ростова',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493',
    #                    'https://vk.com/photo51800929_457257493'))

###############################Вытаскиваем претендентов ################################
    # pprint(pretendents_output(123457222))
    # pprint(pretendents_output(123457159))


###############################Вытаскиваем избранных ################################
    # pprint(favourites_output(123457222))
    # pprint(favourites_output(123457159))



###############################Получаем город,пол,возраст пользователя вк ################################
    # pprint(vk_users_param_output(123457222))
    # pprint(vk_users_param_output(123457159))

###############################Удаление пользователя######################################################
   print(delete_user(123457279))


