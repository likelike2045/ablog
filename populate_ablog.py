import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
	'ablog.settings')

import django
django.setup()

from theblog.models import Post
from django.contrib.auth.models import User


def populate():
	print('starting script')
	post = [
		{'title':'Official Python Tutorial1',
		'body':'Everything is possible'},
		{'title':'Official Django Tutorial2',
		'body':'How to Tango with Django'},
		{'title':'Django Rocks3',
		'body':"Don't look down yourself"},
		{'title':'Django Rocks4',
		'body':"Don't look down yourself"},
		{'title':'Django Rocks5',
		'body':"Don't look down yourself"},
		{'title':'Django Rocks6',
		'body':"Don't look down yourself"},
		{'title':'Django Rocks7',
		'body':"Don't look down yourself"},
		{'title':'Django Rocks8',
		'body':"Don't look down yourself"},
		{'title':'Django Rocks9',
		'body':"Don't look down yourself"},]

	for p in post:
		q = Post(title=p['title'], body=p['body'])
		q.save()

populate()



if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()