import re

if __name__ == '__main__':
    # otwarcie pliku xml
    f = open("370035.xml", "rt", encoding="utf8")

    # regex
    pattern = r'<provenance type="composed">\D*<placeName.*ref="(?P<y>.+)">(?P<x>.+)<\/placeName>'

    # kompilowanie regexu do obiektu
    regex = re.compile(pattern)

    # wyszukuje tekst spełniający regex i zwraca znalezione fragmentyjako iteratory
    for match in regex.finditer(f.read(), re.IGNORECASE | re.DOTALL):
        print("Miejsce powstania dokumentu: ", match.group('x'))
        print("Odnośnik do bazy danych: ", match.group('y'))
