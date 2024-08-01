from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import Config
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/tatlilar')
def tatlilar():
    tatli_listesi = [
        {"name": "Fıstıklı Baklava", "price": "190 TL", "image": "Baklava.png"},
        {"name": "Fıstıklı Kadayıf", "price": "110 TL", "image": "kadayif.webp"},
        {"name": "Fıstıklı Lokum", "price": "120 TL", "image": "lokum.jpg"},
        {"name": "Fıstıklı Künefe", "price": "285 TL", "image": "kunefe.jpg"},
        {"name": "Fıstıklı Sütlaç", "price": "140 TL", "image": "sutlac.jpg"},
        {"name": "Fıstıklı Katmer", "price": "270 TL", "image": "katmer.jpg"},
    ]
    return render_template('tatlilar.html', tatli_listesi=tatli_listesi)

@app.route('/sepete_ekle/<string:tatli_adi>', methods=['POST'])
def sepete_ekle(tatli_adi):
    try:
        if 'sepet' not in session:
            session['sepet'] = []
        sepet = session['sepet']
        item_found = False
        for item in sepet:
            if item['name'] == tatli_adi:
                item['quantity'] += 1
                item_found = True
                break
        if not item_found:
            sepet.append({"name": tatli_adi, "quantity": 1})
        session['sepet'] = sepet
        session.modified = True
        return redirect(url_for('sepet'))
    except Exception as e:
        print(f"Error in sepete_ekle: {e}")
        return redirect(url_for('tatlilar'))

@app.route('/sepete_azalt/<string:tatli_adi>', methods=['POST'])
def sepete_azalt(tatli_adi):
    try:
        if 'sepet' in session:
            sepet = session['sepet']
            for item in sepet:
                if item['name'] == tatli_adi:
                    if item['quantity'] > 1:
                        item['quantity'] -= 1
                    else:
                        sepet.remove(item)
                    break
            session['sepet'] = sepet
            session.modified = True
        return redirect(url_for('sepet'))
    except Exception as e:
        print(f"Error in sepete_azalt: {e}")
        return redirect(url_for('tatlilar'))

@app.route('/sepet')
def sepet():
    sepet = session.get('sepet', [])
    return render_template('sepet.html', sepet=sepet)

@app.route('/odeme_yapildi', methods=['POST'])
def odeme_yapildi():
    session.pop('sepet', None)  # Sepeti temizle
    return render_template('odeme_yapildi.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
