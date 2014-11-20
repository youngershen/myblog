from jinja2 import nodes
from jinja2.ext import Extension

__author__ = 'youngershen'


class MyExt(Extension):
    """ test ext """
    tags = set(['myext'])

    def parse(self, parser):

        lineno = parser.stream.next().lineno
        print "==============="
        #print lineno
        node = nodes.ExprStmt(lineno=lineno)
        #node.node = parser.parse_tuple()
        # print "================"
        # print node.node
        # return node
        body = parser.parse_statements(['name:endmyext'], drop_needle=True)
        print body
        return body