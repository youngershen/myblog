from coffin import template
register = template.Library()

#handlebars tag
def handlebars(parser, token):
    nodelist = parser.parse(('endhandlebars'),)
    return HandleBarsNode()

class HandleBarsNode(template.Node):
    def __init__(self):
        super(HandleBarsNode, self).__init__()

    def render(self, context):
        return