from aiogram import Router
import sqlite3

db_router = Router()

conn = sqlite3.connect('db/data_base_01.db', check_same_thread=False)
cursor = conn.cursor()

async def add_new_user(user_id: int, user_name: str):
	cursor.execute('INSERT INTO user_all (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
	conn.commit()

async def view_task(user_id: int):
	tasks = [list(i) for i in list(cursor.execute(f'SELECT * FROM users_tasks where user_id={user_id}'))]
	names = []
	dates = []

	for i in range(len(tasks)):
		for j in range(0,4):
			if j == 2:
				names.append(tasks[i][j])
			elif j == 3:
				dates.append(tasks[i][j])

	return names, dates

	
async def generate_num_task(user_id: int,):
	a,b = await view_task(user_id)
	if a == []:
		return 1
	else:
		return len(a) + 1

async def add_new_task(user_id: int, text_task: str, date_deadline: str, task_id: int):
	cursor.execute('INSERT INTO users_tasks (user_id, text_task, date_deadline, task_id) VALUES (?, ?, ?, ?)', (user_id, text_task, date_deadline, task_id))
	conn.commit()
	

async def list_users():
	user_list = [i[0] for i in list(cursor.execute(f'SELECT user_id FROM user_all'))]
	return user_list

async def del_task(id_task: int, user_id: int):
	cursor.execute(f'DELETE FROM users_tasks WHERE task_id={id_task} and user_id={user_id}')
	conn.commit()
	
async def rename_task(new_name: str, task_id: int, user_id: int):
	cursor.execute('UPDATE users_tasks SET text_task = ? WHERE task_id = ? and user_id = ?', (new_name, task_id, user_id))
	conn.commit()

async def redate_task(new_date: str, task_id: int, user_id:int):
	cursor.execute('UPDATE users_tasks SET date_deadline = ? WHERE task_id = ? and user_id = ?', (new_date, task_id, user_id))
	conn.commit()