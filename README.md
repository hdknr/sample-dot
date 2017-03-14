# sample-dot

Django OAuth Toolkit samle

## django-oauth-toolkit

- [github](https://github.com/evonove/django-oauth-toolkit)
- [docs](https://django-oauth-toolkit.readthedocs.io/en/latest/)


## Install

~~~py
$ python manage.py migrate
$ python manage.py createsuperuser
~~~

## Create an `Application` for a Relying Party

Login as an administrator:

    - http://shop.local:8000/admin/

Register an `Application` for [sampple-psa#oauth2](https://github.com/hdknr/sample-psa/tree/oauth2):

    - http://shop.local:8000/accounts/o/applications/


~~~bash
$ python manage.py dumpdata oauth2_provider.application  --indent=2
~~~

~~~json
[
{
  "model": "oauth2_provider.application",
  "pk": 1,
  "fields": {
    "client_id": "Df73U5JJvlxS1cRHr6NQKuw76M3W0SDh5gvlvqHG",
    "user": 1,
    "redirect_uris": "http://develop.local:9100/accounts/social/complete/shop/",
    "client_type": "confidential",
    "authorization_grant_type": "authorization-code",
    "client_secret": "jxhfVXRb4HVeoY0CwSoPeqgwaNMJbVzVuf8uaSE7i95Np2ofXPifElid5aG55UbqdONUqX9Qef7dNRbZAKuQmriryubzIpM9UmZbTOSNIQOHMGDOu9F1guwWNgK9PYhf",
    "name": "shop",
    "skip_authorization": false
  }
}
]
~~~
