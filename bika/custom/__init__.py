from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore.utils import ContentInit

from bika.custom.config import *
from bika.custom.content.certificate import Certificate


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME
    )

    allTypes = zip(content_types, constructors)
    for atype, constructor in allTypes:
        kind = "%s: Add %s" % (config.PROJECTNAME, atype.portal_type)
        perm = ADD_CONTENT_PERMISSIONS.get(
            atype.portal_type, ADD_CONTENT_PERMISSION
        )
        ContentInit(
            kind,
            content_types=(atype,),
            permission=perm,
            extra_constructors=(constructor,),
            fti=ftis,
        ).initialize(context)
