from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from bika.lims.browser.dashboard import DashboardView


class CustomDashboardView(DashboardView):

    template = ViewPageTemplateFile("dashboard.pt")
