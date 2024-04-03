from app import app
@app.route('/movie/add')
def movieAdd():
    return "This is a page for adding movie"