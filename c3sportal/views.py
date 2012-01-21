from pyramid.view import view_config
from pyramid.renderers import render
from pyramid.i18n import (
    get_locale_name,
    default_locale_negotiator,
    )


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
    #
#   if '_LOCALE_' in request.params and request.params['_LOCALE_'] is not None:
    #    print("request.params['_LOCALE_']" + request.params['_LOCALE_'])
    #else:
    #    print("request.params['_LOCALE_'] is not or None")
    #print("Browser: request.accept_language: " + request.accept_language)

    languages = 'de en fr it'.split()
    locale = default_locale_negotiator(request)
    #print("locale from default_locale_negotiator: " + str(locale))
    #print(type(request.accept_language))  # XXX check output with nose
    if locale is None and request.accept_language:
        locale = request.accept_language.best_match(languages)
    else:
        locale = 'af'

    #print("best match: " + str(locale))
    #print("request.cookies: ")
    #print(request.cookies)
    request.cookies['_LOCALE_'] = locale
    #print("request.cookies after setting locale ")
    #print(request.cookies)

    return {'footer': footer_view(request)}


@view_config(route_name='about', renderer='templates/about.pt')
def about_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='support', renderer='templates/support.pt')
def support_view(request):
    return {'footer': footer_view(request)}


def footer_view(request):
    return render('templates/footer.pt', {'foo': 'bar'})
