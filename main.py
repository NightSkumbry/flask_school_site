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
        if self.father is not None:
            set_active_elem(self.father, 'parent')

    def __str__(self):
        return f'{self.id}, {self.active}, {self.father}'


nav_bar_list: dict[str, BarElem] = {
    'home': BarElem('home', '/', 'Главная', 'nav'),
    'tasks': BarElem('tasks', '/tasks', 'Задачи', 'nav'),
    'solver': BarElem('solver', '/tasks/solver', 'Кодирование', 'tasks', 'tasks')
}


def set_active_elem(id_, state: str = 'self'):
    if state == 'self':
        for i in nav_bar_list.values():
            i.set_active('none')
    if id_ in nav_bar_list.keys():
        nav_bar_list[id_].set_active(state)
    else:
        for i in nav_bar_list.values():
            i.set_active('none')


@app.route('/')
def index():
    set_active_elem('home')
    return render_template('index.html', nav_list=list(nav_bar_list.values()))


@app.route('/tasks')
def tasks():
    set_active_elem('tasks')
    return render_template('tasks.html', nav_list=list(nav_bar_list.values()))


@app.route('/tasks/solver')
def solver():
    print([str(x) for x in nav_bar_list.values()])
    set_active_elem('solver')
    return render_template('solver.html', nav_list=list(nav_bar_list.values()))


@app.route('/secret_page')
def secret_page():
    set_active_elem(None)
    return render_template('not_ready.html', nav_list=list(nav_bar_list.values()))


if __name__ == '__main__':
    app.run(debug=True)
