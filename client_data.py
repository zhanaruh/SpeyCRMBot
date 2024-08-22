#!/usr/bin/env python
# coding: utf-8

# In[7]:


from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import mysql.connector


# In[15]:


pip install PyMySQL


# In[25]:


import pymysql
from pymysql import MySQLError

def connect_db():
    """Создает подключение к базе данных MySQL"""
    try:
        connection = pymysql.connect(
            host='TeAche.mysql.pythonanywhere-services.com',
            port=3306,
            user='TeAche',
            password='*SpeyCRMBot88',
            database='TeAche$app_data'
        )
        print('Successfully connected to the database')
        return connection
    except MySQLError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

if __name__ == "__main__":
    connection = connect_db()
    if connection:
        connection.close()


# In[27]:


import mysql.connector
from mysql.connector import Error

def connect_db():
    """Создает подключение к базе данных MySQL через SSH-туннель"""
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',  # Локальный адрес
            port=3306,  # Локальный порт
            database='TeAche$app_data',
            user='TeAche',
            password='*SpeyCRMBot88'
        )
        if connection.is_connected():
            print('Successfully connected to the database')
            return connection
    except Error as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

if __name__ == "__main__":
    connection = connect_db()
    if connection:
        connection.close()


# In[28]:


def generate_user_id():
    """для user_id рандомно"""
    import random
    return random.randint(100000000, 999999999)


# In[35]:


def add_user(connection, name, surname, email, position_name, region_name, team_name):
    cursor = connection.cursor()

    # Проверка и добавление позиции
    cursor.execute("SELECT id FROM positions WHERE position_name = %s", (position_name,))
    position = cursor.fetchone()
    if position:
        position_id = position[0]
    else:
        print("Position not found. Please add it to the positions table.")
        return

    # Проверка и добавление региона
    cursor.execute("SELECT id FROM regions WHERE region_name = %s", (region_name,))
    region = cursor.fetchone()
    if region:
        region_id = region[0]
    else:
        print("Region not found. Please add it to the regions table.")
        return

    # Проверка и добавление команды
    cursor.execute("SELECT id FROM teams WHERE team_name = %s", (team_name,))
    team = cursor.fetchone()
    if team:
        team_id = team[0]
    else:
        print("Team not found. Please add it to the teams table.")
        return

    # Добавление пользователя
    user_id = generate_user_id()
    access_level = 'user'

    insert_query = """
        INSERT INTO users (user_id, user_name, user_surname, user_email, position_id, region_id, team_id, access_level)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (user_id, name, surname, email, position_id, region_id, team_id, access_level))
    connection.commit()
    print("User added successfully.")
    
    cursor.close()

def main():
    connection = connect_db()
    if connection:
        add_user(connection, 'Yeslyamova', 'Zhanaru', 'zhanaruh@gmail.com', 'Админ', 'АЛА', 'Бета')
        connection.close()

if __name__ == "__main__":
    main()


# In[ ]:




