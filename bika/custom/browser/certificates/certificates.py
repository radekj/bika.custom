from collections import defaultdict

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView


class CertificatesListingView(BrowserView):
    """
    View class definition
    """

    def get_certificates(self):
        """
        Return list of certificates as dict of 'Active' and 'NonActive'
        certificates:
            {
                'Active': [
                    {'Title': 'Cert 1', 'url': '/cert1'},
                    {'Title': 'Cert 2', 'url': '/cert2'}
                ],
                'NonActive': [
                    {'Title': 'Cert 3', 'url': '/cert3'},
                ]
            }
        """
        result = defaultdict(list)

        catalog = getToolByName(self.context, 'portal_catalog')
        certificates = catalog(portal_type='Certificate')

        for cert in certificates:
            active_key = 'Active' if cert.isActive else 'NonActive'
            result[active_key].append(
                {
                    'Title': cert.Title,
                    'URL': cert.getURL(),
                }
            )

        return result
