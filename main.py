from flask import Flask, render_template


app = Flask(__name__)


class Nav_bar_elem:
    def __init__(self, id, href, text):
        self.id = str(id)
        self.text = str(text)
        self.href = str(href)
        self.active = False

    def set_active(self, state):
        self.active = bool(state)


nav_bar_list = [
    Nav_bar_elem('home', '/', 'Главная'),
    Nav_bar_elem('solver', '/solver', 'Решатель задач')
]


def set_active(id):
    id = '' if id is None else str(id)
    return list(map(lambda x: x.set_active(True if x.id == id else False), nav_bar_list))


@app.route('/')
def index():
    set_active('home')
    return render_template('index.html', nav_list=nav_bar_list)


@app.route('/solver')
def info():
    set_active('solver')
    return render_template('solver.html', nav_list=nav_bar_list)

@app.route('/not_ready')
def nr():
    set_active(None)
    return render_template('not_ready.html', nav_list=nav_bar_list)


if __name__ == '__main__':
    app.run(debug=True)
