from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def hello_agtech(): 
  html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Agtech</title>
        </head>
        <body>
            <h1>Hello from Agtech</h1>
        </body>
    </html>
    """
  return render_template_string(html)


if __name__ == '__main__':
  app.run(debug=True)