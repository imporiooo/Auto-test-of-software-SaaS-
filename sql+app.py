from flask import Flask, make_response, request, render_template, redirect, url_for, session
import subprocess, sqlite3
from hashlib import sha256

app = Flask(__name__, static_folder="static")


@app.route('/')
def transfer():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

    # TASK 1


@app.route('/tasks/task1')
def task1():
    return render_template('task1.html')


@app.route('/tasks/task1/submit', methods=['POST'])
def submit_code1():
    user_code1 = request.form['user_code']
    print(user_code1)

    with open('user_code1.py', 'w') as file:
        file.write(user_code1)

    # Запуск тестов
    result = subprocess.run(['pytest', 'test_user_code1.py'], capture_output=True, text=True)

    # Проверяем результат выполнения тестов
    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

        # TASK 2


@app.route('/tasks/task2')
def task2():
    return render_template('task2.html')


@app.route('/tasks/task2/submit', methods=['POST'])
def submit_code2():
    user_code2 = request.form['user_code']
    print(user_code2)

    with open('user_code2.py', 'w') as file:
        file.write(user_code2)

    result = subprocess.run(['pytest', 'test_user_code2.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

        # TASK 3


@app.route('/tasks/task3')
def task3():
    return render_template('task3.html')


@app.route('/tasks/task3/submit', methods=['POST'])
def submit_code3():
    user_code3 = request.form['user_code']
    print(user_code3)

    with open('user_code3.py', 'w') as file:
        file.write(user_code3)

    result = subprocess.run(['pytest', 'test_user_code3.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

        # TASK 4


@app.route('/tasks/task4')
def task4():
    return render_template('task4.html')


@app.route('/tasks/task4/submit', methods=['POST'])
def submit_code4():
    user_code4 = request.form['user_code']
    print(user_code4)

    with open('user_code4.py', 'w') as file:
        file.write(user_code4)

    result = subprocess.run(['pytest', 'test_user_code4.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correct.html')
    else:
        return render_template('incorrect.html')

        # TASK 5


@app.route('/tasks/task5')
def task5():
    return render_template('task5.html')


@app.route('/tasks/task5/submit', methods=['POST'])
def submit_code5():
    user_code5 = request.form['user_code']
    print(user_code5)

    with open('user_code5.py', 'w') as file:
        file.write(user_code5)

    result = subprocess.run(['pytest', 'test_user_code5.py'], capture_output=True, text=True)

    if result.returncode == 0:
        return render_template('correctved.html')
    else:
        return render_template('incorrect.html')


@app.route("/profile")
def profileuser():
    return render_template('profile.html')

# Функция для хэширования пароля
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Функция для проверки хэша пароля
def check_password(input_password, stored_password):
    return hash_password(input_password) == stored_password

# Роут для страницы регистрации
@app.route('/Profile/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Подключение к базе данных
        conn = sqlite3.connect('login_database.db')
        cursor = conn.cursor()

        # Проверка, что пользователь с таким именем еще не зарегистрирован
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Пользователь с таким именем уже существует
            conn.close()
            return render_template('register.html', error='Username already exists')

        # Хэшируем пароль
        hashed_password = hash_password(password)

        # Вставка данных в таблицу
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, hashed_password))
        conn.commit()

        # Закрываем соединение
        conn.close()

        # Редирект на страницу авторизации после успешной регистрации
        return redirect(url_for('login'))

    return render_template('register.html')

# Роут для страницы авторизации
@app.route('/Profile/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Подключение к базе данных
        conn = sqlite3.connect('login_database.db')
        cursor = conn.cursor()

        # Поиск пользователя в базе данных по имени пользователя
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()

        if user and check_password(password, user[2]):
            # Авторизация успешна, сохраняем имя пользователя в сессии
            session['username'] = username
            conn.close()
            return redirect(url_for('dashboard'))
        else:
            # Неправильное имя пользователя или пароль
            conn.close()
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

# Роут для страницы "Dashboard"
@app.route('/Profile/dashboard')
def dashboard():
    # Проверяем, авторизован ли пользователь
    if 'username' in session:
        return f'Hello, {session["username"]}! This is your dashboard.'
    else:
        return redirect(url_for('login'))

# Роут для выхода из системы
@app.route('/Profile/logout')
def logout():
    # Удаляем имя пользователя из сессии
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id), 200, {'Content-Type': 'text/markdown'}


if __name__ == "__main__":
    app.run(debug=True)