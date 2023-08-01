from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    priority = 1.0   # on a scale of 0.0 to 1.0
    protocol = 'https'  # use https when you deploy your website and are using a secure connection

    def items(self):
        return ['about', 'index', 'client-interest',  'application']
    def location(self, item):
        return reverse(item)