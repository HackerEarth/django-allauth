from django.conf import settings

from allauth.account import app_settings as account_settings

# Request e-mail address from 3rd party account provider? E.g. OpenID AX
QUERY_EMAIL = getattr(settings, "SOCIALACCOUNT_QUERY_EMAIL", 
                      account_settings.EMAIL_REQUIRED)

# Attempt to bypass the signup form by using fields (e.g. username,
# email) retrieved from the social account provider. If a conflict
# arises due to a duplicate e-mail signup form will still kick in.
AUTO_SIGNUP = getattr(settings, "SOCIALACCOUNT_AUTO_SIGNUP", True)

# Enable support for django-avatar. When enabled, the profile image of
# the user is copied locally into django-avatar at signup.
AVATAR_SUPPORT = getattr(settings, "SOCIALACCOUNT_AVATAR_SUPPORT",
                         'avatar' in settings.INSTALLED_APPS)

# Provider specific settings
PROVIDERS = getattr(settings, "SOCIALACCOUNT_PROVIDERS", {})

# The OAuth format supported by StackExchange is a little different
# from the rest, along with application id and cliet secret, it
# requires an additional key. This would require adding another
# field in the SocialApp model, instead we will save the key
# in this file, not the cleanest method, but saves you a database
# migration and the key is not required elsewhere
STACKEXCHANGE_KEY = getattr(settings, "STACKEXCHANGE_KEY", '')

# Since StackExchange is linked with multiple sites, while making
# an request one needs to specify a site for instance
# stackoverflow.com or askubuntu.com etc. The default taken here
# is stackoverflow.com
STACKEXCHANGE_SITE = getattr(settings, "STACKEXCHANGE_SITE", 'stackoverflow.com')
