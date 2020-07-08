#Question: Print out the text of this file http://www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.

#Expected output: 

#Distant regions of space are assumed to exist and to be part of reality as much as we are, even though we can neverxxxx

import requests

print(dir(requests))

r = requests.get('http://www.pythonhow.com/data/universe.txt', headers= {'user-agent': 'customUserAgent'})

print(r.text)

print(r.headers)

# O/P: {'Date': 'Wed, 08 Jul 2020 22:17:33 GMT', 'Content-Type': 'text/plain', 'Content-Length': '333', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d4e47dc9bc2367d39a55ae07dcb29f6181594246653; expires=Fri, 07-Aug-20 22:17:33 GMT; path=/; domain=.pythonhow.com; HttpOnly; SameSite=Lax', 'Vary': 'Accept-Encoding', 'Last-Modified': 'Thu, 01 Dec 2016 17:07:55 GMT', 'Accept-Ranges': 'bytes', 'Content-Encoding': 'gzip', 'Referrer-Policy': 'no-referrer-when-downgrade', 'CF-Cache-Status': 'DYNAMIC', 'cf-request-id': '03d21a7e920000ced81b931200000001', 'Server': 'cloudflare', 'CF-RAY': '5afd2d10eb21ced8-IAD'}

