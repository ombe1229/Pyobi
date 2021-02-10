from flask import Flask, render_template
from utils.requester import Requester


app = Flask('HiyobiViewer')
requester = Requester()


@app.route('/')
def home():
    title = 'Pyhobi - Page 1'
    mlist = requester.get_list(1)
    data = {
        'title': title,
        'mlist': mlist
    }
    return render_template('list.html', data=data)


@app.route('/list/<page>')
def list_page(page):
    title = f'Pyobi - Page {page}'
    mlist = requester.get_list(page)
    data = {
        'title': title,
        'mlist': mlist
    }
    return render_template('list.html', data=data)


@app.route('/reader/<index>')
def viewer(index):
    title = requester.get_title(index)
    page_list = requester.get_page_list(index)
    data = {
        'title': title,
        'page_list': page_list
    }
    return render_template('reader.html', data=data)


@app.errorhandler(404)
@app.errorhandler(500)
def error_page(error):
    return render_template('error.html', error=error)


app.run(host='127.0.0.1', port=8080)
