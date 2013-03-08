from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider

from allauth.socialaccount import app_settings

class StackExchangeAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('link')
    def get_avatar_url(self):
        return self.account.extra_data.get('profile_image')
    def __unicode__(self):
        dflt = super(StackExchangeAccount, self).__unicode__()
        return self.account.extra_data.get('display_name', dflt)

class StackExchangeProvider(OAuthProvider):
    id = 'stackexchange'
    name = 'StackExchange'
    package = 'allauth.socialaccount.providers.stackexchange'
    key = app_settings.STACKEXCHANGE_KEY
    site = app_settings.STACKEXCHANGE_SITE
    account_class = StackExchangeAccount
    
    # Uncomment below if the token should not expire
    """
    def get_default_scope(self):
        scope = []
        scope.append('no_expiry')
        return scope
    """

providers.registry.register(StackExchangeProvider)
