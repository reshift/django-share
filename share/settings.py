from django.conf import settings

providers = {
  'main': ['facebook_like', 'facebook', 'twitter', 'pinterest', 'googleplus', ],
  'more': ['email', 'print', ],
}
fbLanguage = settings.LANGUAGE_CODE

SHARE_PROVIDERS = getattr(settings, 'SHARE_PROVIDERS', providers)
SHARE_FACEBOOK_LANGUAGE = getattr(settings, 'SHARE_FACEBOOK_LANGUAGE', fbLanguage)
