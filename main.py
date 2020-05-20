from app import create_app, db
from app.models import Word


app = create_app()

# make available our main app variable
app.app_context().push()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Word': Word}


if __name__ == "__main__":
    print('we came here!!!')
    app.run(debug=True, host="0.0.0.0")
    #app.run(ssl_context="adhoc", debug=True, host="0.0.0.0")
