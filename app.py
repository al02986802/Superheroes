from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

superheroes = [
    {'real_name': 'Bruce Wayne', 'hero_name': 'Batman', 'photo_url': 'https://example.com/batman.jpg', 'info': 'Vigilante de Gotham.'},
    {'real_name': 'Clark Kent', 'hero_name': 'Superman', 'photo_url': 'https://example.com/superman.jpg', 'info': 'El último hijo de Krypton.'}
]

@app.route('/')
def index():
    return render_template('index.html', superheroes=superheroes)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        real_name = request.form['real_name']
        hero_name = request.form['hero_name']
        photo_url = request.form['photo_url']
        info = request.form['info']
        superheroes.append({'real_name': real_name, 'hero_name': hero_name, 'photo_url': photo_url, 'info': info})
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    hero = superheroes[index]
    if request.method == 'POST':
        hero['real_name'] = request.form['real_name']
        hero['hero_name'] = request.form['hero_name']
        hero['photo_url'] = request.form['photo_url']
        hero['info'] = request.form['info']
        return redirect(url_for('index'))
    return render_template('edit.html', hero=hero, index=index)

@app.route('/delete/<int:index>')
def delete(index):
    superheroes.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
