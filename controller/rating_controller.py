from app import app
@app.route('/movie/rating/add')
def ratingAdd():
    return "This is a page for adding rating for a specific movie"