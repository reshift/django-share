import urlparse
from django.template import Library, TemplateSyntaxError, Node
from django.utils.http import urlquote
from django.conf import settings
from share.settings import *
from django.template.loader import render_to_string

register = Library()


@register.simple_tag
def share_css():
    return "<link href='" + settings.STATIC_URL + "css/share.css' type='text/css' rel='stylesheet' />"


@register.simple_tag
def share_js():
    return "<script src='" + settings.STATIC_URL + "js/share.js' type='text/javascript'></script>"


@register.simple_tag
def share_fbsdk():
    if settings.SHARE_FACEBOOK_LANGUAGE:
        fbLanguage = settings.SHARE_FACEBOOK_LANGUAGE
    else:
        fbLanguage = settings.LANGUAGE_CODE
    return "<div id='fb-root'></div><script>(function(d, s, id) { var js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src = '//connect.facebook.net/" + fbLanguage + "/all.js#xfbml=1'; fjs.parentNode.insertBefore(js, fjs); }(document, 'script', 'facebook-jssdk'));</script>"


class ShareNode(Node):
    def __init__(self, providers=None, fbLanguage=None):
        self.providers = providers

        if settings.SHARE_FACEBOOK_LANGUAGE:
            self.fbLanguage = settings.SHARE_FACEBOOK_LANGUAGE
        else:
            self.fbLanguage = settings.LANGUAGE_CODE

    def render(self, context):
        return render_to_string('share/links.html', {'providers': self.providers, 'fbLanguage': self.fbLanguage, 'url': context['request'].build_absolute_uri()}, context_instance=context)


@register.tag
def share(parser, token):
    args = token.split_contents()

    if len(args) == 1:
        providers = SHARE_PROVIDERS
    else:
        args.pop(0)
        providers = args

    return ShareNode(providers)
