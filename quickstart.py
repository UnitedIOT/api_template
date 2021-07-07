# coding=utf-8
import api

if __name__ == '__main__':
    api.create_app().run(host='0.0.0.0', port=5000, debug=True)
