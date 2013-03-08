from django.utils.cache import patch_response_headers
from django.shortcuts import render

from allauth.socialaccount import providers
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
from allauth.socialaccount import requests

from allauth.socialaccount.models import SocialAccount, SocialLogin
from provider import StackExchangeProvider
from forms import StackExchangeConnectForm

from allauth.utils import valid_email_or_none, get_user_model

User = get_user_model()

class StackExchangeOAuth2Adapter(OAuth2Adapter):
    provider_id = StackExchangeProvider.id
    authorize_url = 'https://stackexchange.com/oauth'
    access_token_url = 'https://stackexchange.com/oauth/access_token'
    profile_url = 'https://api.stackexchange.com/me'

    def complete_login(self, request, app, token):
        resp = requests.get(self.profile_url,
                            params={ 'access_token': token.token,
                                     'key': StackExchangeProvider.key,
                                     'site': StackExchangeProvider.site })
        print resp.json
                        
        extra_data = resp.json['items'][0]
        uid = str(extra_data['user_id'])
        name_parts = extra_data.get('display_name', '').split(' ', 1)
        if len(name_parts) == 2:
            first_name, last_name = name_parts
        else:
            first_name, last_name = name_parts[0], ''
        user_kwargs = {'first_name': first_name, 
                       'last_name': last_name}
        user = User(username='',
                    email='',
                    **user_kwargs)
        account = SocialAccount(user=user,
                                uid=uid,
                                extra_data=extra_data,
                                provider=self.provider_id)
        return SocialLogin(account)

oauth2_login = OAuth2LoginView.adapter_view(StackExchangeOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(StackExchangeOAuth2Adapter)
