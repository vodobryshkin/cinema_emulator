# Приложение для админинистрирования, а также вазимодействия с кинотеатром(ПРОЕКТ ЯНДЕКС ЛИЦЕЙ).
Программа с использованием QT (pyqt5), и Sql, которая может использоваться для администрирования системы кинотеатра, а так же для использования её от лица клиента кинотеатра.
1. Проект.

 Приложение-помощник для дистанционной работы с системой кинотеатра.

  Приложение имеет следующие функции:

    	1)Создание зала кинотеатра.
	2)Создание сеанса в определённом зале кинотеатра.
	3)Удаление сеанса из кинотеатра.
	4)Создание и обновление товаров в магазине.
	5)Создание рекламного буклета на отдельный сеанс(файл в формате docx).
	6)Создание детализированного отчёта на все залы кинотеатра(презентация в формате pptx).
	7)Покупка билета на отдельный сеанс с получением чека(файл в формате txt).
	8)Покупка товара из магазина с получением чека(файл в формате txt).
	9)Вход в систему с помощью логина и пароля.
	10)Регистрация нового пользователя.
	
  2. Использованные технологии:
	1)PyQt5(PyQt5)
	2)SQL(sqlite3)
	3)python-docx
	4)python-pptx
	5)random
	6)datetime

  3. Работа с приложением.

 В приложении два главных окна: Админский режим взаимодействия и Обычный режим взаимодействия. Отдельными виджетами реализована система регистрации и авторизации. 

    1)Админский режим взаимодействия:
      На таблицах отображаются: списки залов кинотеатра с их размерами; списки сеансов с информацией о времени сеанса, даты сеанса, ценой билета на сеанс, названием фильма на сеанс, количеством свободных мест, залом в котором проходит сеанс, уникальным ID каждого сеанса; списки товаров в магазине кинотеатра с их названием, количеством на складе, уникальным ID каждого товара. Через кнопки, а также прилегающие к окну виджеты реализуются:
	1)Создание зала кинотеатра.
	2)Создание сеанса в определённом зале кинотеатра.
	3)Удаление сеанса из кинотеатра.
	4)Создание и обновление товаров в магазине.
	5)Создание рекламного буклета на отдельный сеанс.
	6)Создание детализированного отчёта на все залы кинотеатра.
	7)Выход из окна к меню авторизации.

    2)Обычный режим взаимодействия:
      На таблицах отображаются: списки сеансов с информацией о времени сеанса, даты сеанса, ценой билета на сеанс, названием фильма на сеанс, количеством свободных мест, залом в котором проходит сеанс, уникальным ID каждого сеанса; списки товаров в магазине кинотеатра с их названием, количеством на складе, уникальным ID каждого товара. Через кнопки, а также прилегающие к окну виджеты реализуются:
    	1)Покупка билета на отдельный сеанс с получением чека.
	2)Покупка товара из магазина с получением чека.
	3)Выход из окна к меню авторизации.

    3)Система авторизации и регистрации
	Система, состоящая из трёх виджетов позволяет делать:
	1)Вход в систему с помощью логина и пароля.
	2)Регистрация нового пользователя.
	3)Переключаться между окнами.
