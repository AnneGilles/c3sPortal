from pyramid.view import view_config
from pyramid.renderers import render
from pyramid.i18n import (
    get_locale_name,
    default_locale_negotiator,
    )


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='benefits', renderer='templates/benefits.pt')
def benefits_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='about', renderer='templates/about.pt')
def about_view(request):

    team = [
        'Marcel Hennes',
        'Simona Levi',
        'm.eik michalke',
        'Christoph Scheid',
        'Holger Schwetter',
        'Wolfgang Senges',
        'Michael Weller',
        ]

    supporters = [
        'Paul Schwanse',
        'Sandra Schappert',
        'anonymous',
        'anonymous',
        'Sven Wendt',
        'Volker Grassmuck',
        ]

    import random
    random.shuffle(team)
    random.shuffle(supporters)

    return {
        'footer': footer_view(request),
        'team': team,
        'supporters': supporters,
        }


@view_config(route_name='support', renderer='templates/support.pt')
def support_view(request):
    return {'footer': footer_view(request)}


def footer_view(request):
    return render('templates/footer.pt', {'foo': 'bar'})
