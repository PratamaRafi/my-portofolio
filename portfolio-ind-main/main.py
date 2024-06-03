#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

# Simpan form feedback
@app.route('/submit',methods=['POST'])
def submit():
    email = request.form.get('email')
    comment = request.form.get('text')


    return render_template('result.html',
                           email = email,
                           comment = comment)
@app.route('/')
def discord_project():
    return render_template('https://github.com/PratamaRafi/discord-chatbot/blob/main/bot.py')

if __name__ == "__main__":
    app.run(debug=True)
