from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Number, Operator, Generic, Punctuation, Text

# One Dark Pro style
class OneDarkProStyle(Style):
    background_color = ""
    default_style = "bg: #282c34"
    styles = {
        Comment:                'italic #5C6370', # Example
        Keyword:                '#c678dd',
        Name:                   '#e06c75',
        Name.Function:          '#61AFEF',
        Name.Class:             '#E5C07B',
        String:                 '#98c379',
        Operator:               '#abb2bf',
        Generic:                '#FFFFFF',
        Punctuation:            '#abb2bf',
        Number:                 '#d19a66'
    }