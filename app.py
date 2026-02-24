from flask import Flask

app = Flask(__name__)

# Endpoint / (Halaman Utama)
@app.route('/')
def index():
    return '''
    <h1>Instruksi Penggunaan:</h1>
    <p>Tambahkan <b>/hello/Hafifa Mulyana</b> pada URL di browser.</p>
    <p>Contoh: <a href="/hello/Hafifa">localhost:5000/hello/Hafifa</a></p>
    '''

# Endpoint /hello/<nama> (Sesuai Hint Tugas)
@app.route('/hello/<nama>')
def hello(nama):
    return f'<h1>Halo, {nama}!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)