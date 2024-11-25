from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_code():
    user_code = request.form['user_code']
    print(user_code)

    # Сначала сохраняем новый код во временный файл
    with open('user_code.py', 'w') as file:
        file.write(user_code)

    # Запуск тестов
    result = subprocess.run(['pytest', 'test_user_code.py'], capture_output=True, text=True)

    # Проверяем результат выполнения тестов
    if result.returncode == 0:
        return "Задача успешно решена!"
    else:
        return f"Задача решена неправильно."

if __name__ == '__main__':
    app.run(debug=True)
