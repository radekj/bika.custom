from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName


class ClientCertificatesVocabularyFactory(object):

    def __call__(self, context):
        portal_catalog = getToolByName(context, 'portal_catalog')
        certificates = portal_catalog(
            portal_type='Certificate', isActive=True
        )
        terms = []

        for cert in certificates:
            terms.append(
                SimpleVocabulary.createTerm(
                    cert.id, str(cert.id), cert.Title
                )
            )

        return SimpleVocabulary(terms)
