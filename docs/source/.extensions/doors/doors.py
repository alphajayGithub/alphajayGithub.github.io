# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.roles import set_classes
from docutils import utils

import sphinx

def doors_reference_role(role, rawtext, text, lineno, inliner,
                       options={}, content=[]):

    ref ="https://gates.nsn-net.net/search?phrase={id}&ctx=root-directory&scope=/".format(id=text)
    set_classes(options)
    node = nodes.reference(rawtext, utils.unescape(text), refuri=ref,
                           **options)
    return [node], []


def setup(app):
    roles.register_canonical_role('doors', doors_reference_role)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
