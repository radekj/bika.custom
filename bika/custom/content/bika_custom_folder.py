from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.content import schemata
from Products.Archetypes import atapi
from plone.app.folder import folder
from zope.interface import implements

from bika.lims.interfaces import IHaveNoBreadCrumbs
from bika.custom.interfaces import IBikaCustomFolder
from bika.custom.config import PROJECTNAME

schema = folder.ATFolderSchema.copy()
schema['id'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}
schema['title'].widget.visible = {'edit': 'visible', 'view': 'invisible'}


class BikaCustomFolder(folder.ATFolder):
    implements(IBikaCustomFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(BikaCustomFolder, PROJECTNAME)
