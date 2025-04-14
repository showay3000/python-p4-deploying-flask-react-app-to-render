app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',  # Serve static files from React
    template_folder='../client/build'  # Serve HTML from React
)

# Catch-all route for client-side routing
@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")