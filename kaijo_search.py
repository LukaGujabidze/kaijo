from re import search
import webbrowser as web

search_g = input()

url = 'https://www.google.com/search?client=firefox-b-d&q=' + search_g

web.open_new_tab(url)