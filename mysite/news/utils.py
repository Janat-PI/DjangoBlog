from django.db.models import Count, F

from .models import Category


class MyMixin(object):
    mixin_prop = ' '

    def test(self):
        return Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()

