LEPRICONE_RU: dict[str, str] = {
    '/help': '<b>Этот бот поможет вам управлять задачами.</b>\n\n'
             'Доступные команды:\n\n'
             '/view_task - просмотреть текущие задачи (возможность редактировать и удалять).\n'
             '/new_task - создать новую задачу.\n'
             '/help - справка по работе бота.\n\n'
             'Если задач пока нет, самое время их создать!',
    '/start': '<b>Привет!</b>\n\n'
              'Это бот для хранения и управления задачами.\n\n'
              'Чтобы узнать доступные команды, введите /help.',
    '/view_task': '<b>Ваши задачи:</b>',
    'no_task': 'У вас пока нет задач.',
    'view_tasks': '<b>Список ваших задач:</b>',
    'create_new_task_name': '<b>Новая задача? Отлично!</b>\n\n'
                            'Введите название или краткое описание задачи.',
    'greate_task': '<b>Замечательно!</b>\n\n'
                   'Укажите, пожалуйста, дату завершения задачи в формате: <i>ДД.ММ.ГГГГ ЧЧ:ММ</i>.',
    'new_task_ready': '<b>Готово!</b>\n\n',
    'cancel': 'Отмена',
    'cancel_view': 'Закрываем список задач.',
    'cancel_text': 'Создание задачи отменено.',
    'edit': 'Редактировать',
    'edit_name': 'Название/Описание',
    'edit_name_text': 'Введите новое название или описание.',
    'edit_date': 'Дата',
    'edit_date_text': 'Введите новую дату в формате: <i>ДД.ММ.ГГГГ ЧЧ:ММ</i>.',
    'edit_task_text': 'Выберите задачу для редактирования.',
    'edit_one_task_text': '<b>Редактирование задачи</b>\n\n'
                          'Что вы хотите изменить?',
    'delete': 'Удалить',
    'delete_one_task_text': '<b>Удаление задачи</b>\n\n'
                            'Какую задачу вы хотите удалить?',
    'delete_task': 'Задача успешно удалена!',
    'greate_edit': 'Задача успешно отредактирована!'
}




LEPRICONE_COMMANDS: dict[str, str] = {
    '/help':'Справка по работе бота',
    '/view_task':'Просмотр задач',
    '/new_task':'Создать новую задачу'
}