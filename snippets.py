import rumps
import xerox
import os

rumps.debug_mode = True

datafile = "data.txt"


def copy(text):
    print text.title
    xerox.copy(text.title)

def add(_):
    print "add clicked"
    print xerox.paste()
    with open(datafile, "a") as f:
        f.write(xerox.paste() + "\n")
    app.menu.clear()
    app.menu.update(generate_menu())

def generate_menu():
    menu = [rumps.MenuItem("add", callback=add)]
    data = []

    if os.path.isfile(datafile):
        with open(datafile) as f:
            data = f.read().strip().splitlines()
    else:
        open(datafile, "w").write("")

    for line in data:
        menu.append(rumps.MenuItem(line, callback=copy))

    return menu

if __name__ == "__main__":
    app = rumps.App(" S ", quit_button="quit")
    app.menu = generate_menu()
    app.run()