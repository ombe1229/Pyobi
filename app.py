from flask import Flask, render_template
from utils.requester import Requester


app = Flask('HiyobiViewer')
requester = Requester()


@app.route('/viewer/<index>')
def viewer(index):
    title = requester.get_title(index)
    page_list = requester.get_page_list(index)
    data = {
        'title': title,
        'page_list': page_list
    }
    return render_template('viewer.html', data=data)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('internal_server_error.html')


app.run(host='127.0.0.1', port=8080)