from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def encrypt():
    to = str(request.form.get('to', None))
    text = str(request.form.get('text', None))

    return '<h1>' + rotate_string(text, to) + '</h1>'

form = """ 
  <!DOCTYPE html>
  <html>
    <head>
      <style>
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        text area {
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }
      </style>
    </head>
    <body>
    <form action="/" method = "POST">
      <label for="rot">Rotate by:</label>
      <input id="rot" name="rot" type="text" placeholder="0"/>
      <br>
      <textarea name="text"></textarea>
      <input type="submit" value="Submit">
    </body>
  </html>

"""

@app.route("/")
def index():
  return form

if __name__ == "__main__":
  app.run()