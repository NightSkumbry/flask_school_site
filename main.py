from flask import Flask, render_template


app = Flask(__name__)


class BarElem:
    def __init__(self, id_: str, href: str, text: str, bar: str, father: None | str = None):
        self.id = str(id_)
        self.text = str(text)
        self.href = str(href)
        self.active = 'none'
        self.father = father
        self.bar = bar

    def set_active(self, state: str):
        self.active = state
        if state != 'none' and self.father is not None:
            set_active_elem(self.father, 'parent')

    def __str__(self):
        return f'{self.id}, {self.active}, {self.father}'


bars_list: dict[str, BarElem] = {
    'home': BarElem(id_='home', href='/', text='Главная', bar='nav'),
    'tasks': BarElem(id_='tasks', href='/tasks', text='Задачи', bar='nav'),
    'it': BarElem(id_='it', href='/tasks/it', text='Информатика', bar='task', father='tasks'),
    'encoder': BarElem(id_='encoder', href='/tasks/it/encoder', text='Кодирование', bar='it', father='it'),
    'maths': BarElem(id_='maths', href='/tasks/maths', text='Математика', bar='task', father='tasks')
}


def set_active_elem(id_, state: str = 'self'):
    if state == 'self':
        for i in bars_list.values():
            i.set_active('none')
    if id_ in bars_list.keys():
        bars_list[id_].set_active(state)
    else:
        for i in bars_list.values():
            i.set_active('none')


@app.route('/')
def index():
    set_active_elem('home')
    return render_template('index.html', bars_list=list(bars_list.values()))


@app.route('/tasks')
def tasks():
    set_active_elem('tasks')
    return render_template('tasks.html', bars_list=list(bars_list.values()))


@app.route('/tasks/it')
def it():
    set_active_elem('it')
    return render_template('tasks/it.html', bars_list=list(bars_list.values()))


@app.route('/tasks/it/encoder')
def encoder():
    # print([str(x) for x in bars_list.values()])
    set_active_elem('encoder')
    return render_template('tasks/it/encoder.html', bars_list=list(bars_list.values()))


@app.route('/secret_page')
def secret_page():
    set_active_elem(None)
    return render_template('not_ready.html', bars_list=list(bars_list.values()))


if __name__ == '__main__':
    app.run(debug=True)
