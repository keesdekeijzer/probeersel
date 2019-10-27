#!/usr/bin/env python3

"""
Dit programma leest een favorieten export bestand uit
Firefox 'bookmarks.html' in en verwijdert de overbodige code en
maakt er een nieuwe webpagina van met de naam 'favoriten.html'
"""


def vervang(regel, begintekst, eindtekst, vervangtekst):
    """
    Tekst vervangen die begint met
    begintekst en eindigt met eindtekst in
    regel door vervangtekst
    """
    verv = ""
    locatie1 = regel.find(begintekst)
    if (locatie1 > -1):
        locatie2 = regel.find(eindtekst, locatie1)
        verv = regel[locatie1:locatie2]
        regel = regel.replace(verv, vervangtekst)
    return regel


with open("bookmarks.html", "r") as f:
    data = f.readlines()

bestand = open("favoriten.html", "w")
for line in data:
    line = line.replace("\n", "")
    line = line.replace("      ", "")
    line = line.replace("   ", "")

    line = vervang(line, "ICON", ">", "")
    line = vervang(line, "ADD_DATE", "LAST", "")
    line = vervang(line, "LAST_MODIFIED", ">", "")

    line = line.replace("<DT><A HREF", "<li><a href")
    line = line.replace("</A>", "</a></li>")
    line = line.replace("DL>", "ul>")
    line = line.replace("<HR>", "")
    line = line.replace("<DD>", "")
    line = line.replace("<DT><H3", "<h3")
    line = line.replace("</H3>", "</h3>\n")
    line = line.replace("<h3 ", "<h3")
    line = line.replace("<DT><A FEEDURL", "<li><a feedurl")
    line = line.replace("<p>", "")
    line = line.replace("</ul>", "</ul>\n")
    line = line.replace("H1>", "h1>")
    line = line.replace("</h1>", "</h1>\n")
    line = line.replace("TITLE>", "title>")
    line = line.replace("</title>", "</title>\n</head>\n<body>\n")
    line = line.replace("</li>", "</li>\n")
    line = line.replace("<ul>", "<ul>\n")
    line = line.replace("<!-- This is an automatically generated file.", "\n")
    line = line.replace("<!DOCTYPE NETSCAPE-Bookmark-file-1>", "<!DOCTYPE html>\n<html>\n<head>\n")
    line = line.replace("<META", "\n<meta")

    for letter in line:
        if ord(letter) > 255:
            line = line.replace(letter, " ")
    y = len(line)
    if y > 0:
        if line[0] == '<':
            bestand.write(line)
bestand.write('</body></html>')
bestand.close()
