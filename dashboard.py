# -*- coding: utf-8 -*-
"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'billboard.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'billboard.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name
from admin_tools.dashboard import modules


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for billboard.
    """
    def __init__(self, **kwargs):
            Dashboard.__init__(self, **kwargs)
            self.children.append(
                modules.ModelList(
                    title = u'Объявления',
                    models=(
                        'orders.models.Order',
                        'orders.models.Sentence',
                        'orders.models.Company',
                        'orders.models.City',
                    ),
                )
            )
            self.children.append(
                modules.ModelList(
                    title = u'Пользователи',
                    models=(
                        'profiles.models.UserProfile',
                    ),
                )
            )
            
            

        
        


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for billboard.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
