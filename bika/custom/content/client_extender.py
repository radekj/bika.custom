from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes import atapi
from Products.Archetypes import PloneMessageFactory as _

from bika.lims.interfaces import IClient


class ExtensionLinesField(ExtensionField, atapi.LinesField):
    pass


class ClientExtender(object):
    adapts(IClient)
    implements(ISchemaExtender)

    fields = [
        ExtensionLinesField(
            'Certificates',
            multiValued=1,
            vocabulary_factory='client.certificates',
            widget=atapi.MultiSelectionWidget(
                label=_(u'Certificates'),
                description=_(u'Choose certificates'),
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
