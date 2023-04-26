# from app import create_app
#
# app = create_app()
#
#
# app.debug = True
# if __name__ == '__main__':
# 	app.run()create


from flask import Flask
from app import create_app
app: Flask = create_app()

if __name__ =='__main__':
	app.run(host='0.0.0.0', port=25000)
