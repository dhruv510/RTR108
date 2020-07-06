Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import socket
>>> mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>> mysock.connect(('data.pr4e.org', 80))
>>> cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
>>> mysock.send(cmd)
47
>>> while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode(),end='')

	
HTTP/1.0 200 OK
Date: Mon, 06 Jul 2020 06:46:38 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Content-Type: text/plain
Content-Length: 167

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
>>> mysock.close()
>>> # Code: http://www.py4e.com/code3/socket1.py
>>> HTTP/1.1 200 OK
SyntaxError: invalid syntax
>>> b'Hello world'
b'Hello world'
>>> 'Hello world'.encode()
b'Hello world'
>>> import socket
>>> 