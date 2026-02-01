from api import flask_app

# Export the WSGI app for gunicorn
app = flask_app

if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0", port=5000)
