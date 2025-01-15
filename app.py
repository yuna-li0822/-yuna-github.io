from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Serve your HTML file

@app.route('/static/<path:filename>')
def custom_static(filename):
    if filename.endswith('.js'):
        return send_from_directory('static', filename, mimetype='text/javascript')
    return send_from_directory('static', filename)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
