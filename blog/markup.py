from markdown import markdown
from typogrify.filters import typogrify

def markup(text):
    extensions = [
    #    'abbr',
    #    'def_list',
        'fenced_code',
        'footnotes',
        'tables',
        'smart_strong',
        'admonition',
        'headerid',
        'nl2br',
        'sane_lists',
        'smarty',
    #    'toc',
    ]
    return markdown(text, output_format='html5', extensions=extensions)
