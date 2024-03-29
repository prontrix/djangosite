<h1 align = "center">Простой блог на Python-Django</h1>

## **Описание**

<p>Полностью рабочий сайт, написанный на Python с использованием Django Framework.</p>

<p>Представляет из себя блог со статьями об известных певицах и актрисах.</p> 

<p>На главной странице выводятся посты с информацией и изображением. Можно прочитать статью полностью.</p> 

<img src = "https://user-images.githubusercontent.com/60534525/227756543-399b31c6-e1dd-4bfa-8836-baffa4908e0c.jpg" width = 500 />

<p>Есть возможность добавлять новые посты. Присутствует форма обратной связи.</p> 

<p>На сайте реализована регистрация и авторизация.</p>

<p>Есть рабочая панель администратора, с возможностью добавления/редактирования статей и категорий</p>

<img src = "https://user-images.githubusercontent.com/60534525/227756630-3e7da06f-8f69-4a37-9d25-2ebea5e08b4a.jpg" width = 500 />

## **Ограничения**

<p>Сайт готов для запуска только на локальной машине пользователя (127.0.0.1).</p>
<p>Для использования на рабочем сервере, нужно обратиться за инструкцией по установке к своему хостинг-провайдеру</p>

## **Установка и запуск**

1. Устанавливаем Python 3й версии, если его еще нет в системе
2. Создаем папку, где будет находиться проект
3. Клонируем репозиторий `git clone https://github.com/prontrix/djangosite.git` или скачиваем ZIP-архив и распаковываем в нашу папку

   <img src = "https://user-images.githubusercontent.com/60534525/227757131-e73de31f-9c33-4d2a-9cab-16ea5eee143a.jpg" width = 300 />
   
4. Открываем папку `djangosite` (или `djangosite-main`) 
5. Устанавливаем виртуальное окружение `python -m venv venv`
6. Активируем виртуальное окружение для Linux: `source venv/Scripts/activate`, для Windows: `venv\Scripts\activate`
7. Обновляем pip `python -m pip install --upgrade pip`
8. Устанавливаем нужные зависимости для проекта `python -m pip install --no-cache-dir -r requirements.txt`
9. Запускаем локальный сервер `python manage.py runserver`
10. Если все прошло корректно, без ошибок, то сайт будет доступен по адресу `http://127.0.0.1:8000`

## **Дополнительно**

<p>В папке с проектом находится заполненная база данных в файле db.sqlite3. Посмотреть данные можно через программу <a href = "https://sqlitestudio.pl" target=_blank>SQLiteStudio</a></p>

Логин для входа в панель администратора `admin`. Пароль меняется с помощью команды `python manage.py changepassword admin`

## **Источник**

Огромная благодарность Сергею Балакиреву, автору канала на youtube <a href = "https://www.youtube.com/@selfedu_rus/" target = "_blank">selfedu</a> за легкую и доступную подачу материала о создании сайта на Django Framework. Ссылка на плейлист: <a href="https://www.youtube.com/watch?v=FyTL1bnUx5I&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F" target = _blank>Django 3 для python (уроки)</a>

