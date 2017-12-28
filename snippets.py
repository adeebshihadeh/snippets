import rumps
import xerox
import os

rumps.debug_mode = True

datafile = "data.txt"
data = []

def copy(text):
    print text.title
    xerox.copy(text.title)

def add(_):
    print "add clicked"
    print xerox.paste()
    
    if xerox.paste() not in data:
        with open(datafile, "a") as f:
            f.write((xerox.paste() + "\n").encode("utf8"))
        app.menu.clear()
        app.menu.update(generate_menu())

def clear(_):
    if rumps.alert(title="snippets",
        message="clear all entries?",
        ok="yes",
        cancel="no") == 1:
        open(datafile, "w").write("")
        app.menu.clear()
        app.menu.update(generate_menu())

def quit(_):
    rumps.quit_application()

def generate_menu():
    menu = [rumps.MenuItem("add", callback=add),
            rumps.MenuItem("quit", callback=quit),
            rumps.MenuItem("clear", callback=clear)]
    global data
    data = []

    if os.path.isfile(datafile):
        with open(datafile) as f:
            data = f.read().decode("utf8").strip().splitlines()
    else:
        open(datafile, "w").write("")

    for line in data:
        menu.append(rumps.MenuItem(line, callback=copy))

    return menu

if __name__ == "__main__":
    app = rumps.App(" S ", quit_button=None)
    app.menu = generate_menu()
    app.run()