from bs4 import BeautifulSoup


def parse_html(html):
    elem = BeautifulSoup(html, features="html.parser")
    text = ''
    for i, e in enumerate(elem.descendants):

        if isinstance(e, str):
            text += e.strip()
        elif e.name in ['br', 'p', 'h1', 'h2', 'h3', 'h4', 'tr', 'th'] and i > 0:
            text += '\n'
        elif e.name == 'li':
            text += '\n- ' if i > 0 else '-'
    return text
