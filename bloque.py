from flask import requests

ver_form()

for campo, valor in request.form.items():
    print(campo, valor)

