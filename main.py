from website import create_app



app = create_app()

app.app_context().push()
if __name__ == '__main__':
    app.app_context().push()
    app.run(debug=True)