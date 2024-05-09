# tenzor_second_testwork

*Инструкция для Windows:*

**Скачиваем проект:**

* git clone git@github.com:sabina-045/tenzor_second_testwork.git

**Устанавливаем и активируем виртуальное окружение**
* python -m venv venv
* source venv/Scripts/activate

**Устанавливаем зависимости:**
* pip install -r requirements.txt --upgrade pip

**Запускаем браузер Chrome с удаленным подключением:**
* C:\Program Files\Google\Chrome\Application> .\Chrome --remote-debugging-port=9222

**Запускаем тесты:**
* python -m test_project/tests
