from plone.app.content.browser.interfaces import IFolderContentsView
from zope.interface import implements

from bika.lims.browser.clientfolder import ClientFolderContentsView
from bika.lims import bikaMessageFactory as _


class BikaCustomFolderView(ClientFolderContentsView):

    implements(IFolderContentsView)

    def __init__(self, context, request):
        super(BikaCustomFolderView, self).__init__(context, request)
        self.title = self.context.translate(_("Custom Folder"))
