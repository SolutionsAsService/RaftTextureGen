from flask import Flask, render_template, send_file
from io import BytesIO
import os
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/raft')
def raft_image():
    image = generator.generate_raft_image()
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/favicon.ico')
def favicon():
    return send_file(os.path.join(app.root_path, 'static/favicon.ico'), mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
