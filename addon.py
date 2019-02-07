import xbmcaddon
import xbmcgui
import requests

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1 = "Hello World!"
line2 = "We can write anything we want here"
line3 = "Using Python"
url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
r.json()
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
