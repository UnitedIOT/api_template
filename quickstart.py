# coding=utf-8
import app

if __name__ == '__main__':
    app.create_app().run(host='0.0.0.0', port=6000, debug=True)
