from flask import Flask, request, render_template, \
    redirect, url_for, json

app = Flask(__name__)

lesson_dictionary = {
    'lesson_name': 'Math'
}

work_dictionary = {
    'work_name': 'Labs',
    'work_mark': '10'
}


@app.route('/api/<action>', methods=['GET'])
def api_get(action):
    if action == 'lesson':
        return render_template('lesson.html', data=lesson_dictionary)

    elif action == 'work':
        return render_template('work.html', data=work_dictionary)

    elif action == 'all':
        return render_template('all.html', data=[lesson_dictionary, work_dictionary])

    else:
        return render_template('error.html',
                               list_name_tables=['lesson', 'work'],
                               action=action), 404



@app.route('/api', methods=['POST', 'GET'])
def api_post():
    if request.method == 'POST':

        if request.form.get('work') == 'Send':
            work_dictionary['work_name'] = request.form['work_name']
            work_dictionary['work_mark'] = request.form['work_mark']

        if request.form.get('lesson') == 'Send':
            lesson_dictionary['lesson_name'] = request.form['lesson_name']

    return redirect(url_for('api_get', action='all'))


if __name__ == '__main__':
    app.run(debug=True)

