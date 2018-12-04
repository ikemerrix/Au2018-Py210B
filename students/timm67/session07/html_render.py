#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    _tag = str('html')
    _indent_count = 0 * 5
    _indent = ''

    def __init__(self, content=None):
        if content is not None:
            self._content = [content]
        else:
            self._content = []

    def append(self, new_content):
        if new_content is not None:
            self._content.append(new_content)

    def render(self, out_fd, indent_in=''):
        if not indent_in:
            if self._indent_count > 0:
                self._indent = ' ' * self._indent_count
        else:
            self._indent = indent_in

        out_fd.write('{0}<{1}>\n'.format(self._indent, self._tag))
        # loop through the list of contents:

        for content in self._content:
            try:
                try:
                    content.render(out_fd, indent_in)
                except AttributeError:
                    out_fd.write('{0}{1}\n'.format(self._indent + (5 * ' '), content))
            except IOError:
                print("I/O Error")
                return

        out_fd.write('{0}</{1}>\n'.format(self._indent, self._tag))

    @property
    def indent(self):
        print("in indent getter")
        return str(self._indent)

class Html(Element):
    _tag = str('html')
    _indent_count = 0 * 5

class Body(Element):
    _tag = str('body')
    _indent_count = 1 * 5

class P(Element):
    _tag = str('p')
    _indent_count = 2 * 5
