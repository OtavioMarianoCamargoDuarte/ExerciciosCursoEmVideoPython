import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://google.com.br')
except urllib.error.URLError:
    print('O site GOOGLE não está acessível no momento.')
else:
    print('Consegui acessar o site GOOGLE com sucesso!')