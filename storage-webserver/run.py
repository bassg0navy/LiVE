from storage import app # IMPORTED FROM THE INIT MODULE (__INIT__.PY) IN THIS PACKAGE

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')