from AccessControl import ClassSecurityInfo
from zope.interface import implements
from Products.Archetypes import atapi
# from Products.Archetypes.public import *

from bika.lims.content.bikaschema import BikaSchema
from bika.lims import bikaMessageFactory as _

from bika.custom.config import PROJECTNAME
from bika.custom.interfaces import ICertificate


schema = BikaSchema.copy() + atapi.Schema((
    atapi.LinesField(
        'Producer',
        vocabulary=atapi.DisplayList([
            ('acme', 'ACME'),
            ('smasung', 'Samsung'),
            ('inglot', 'Inglot'),
        ]),
        widget=atapi.SelectionWidget(
            label=_(u'Producer'),
            description=_(u'Select one of producers.'),
        ),
    ),

    atapi.BooleanField(
        'Active',
        default=False,
    ),
))


class Certificate(atapi.BaseContent):
    implements(ICertificate)
    security = ClassSecurityInfo()
    schema = schema

atapi.registerType(Certificate, PROJECTNAME)
