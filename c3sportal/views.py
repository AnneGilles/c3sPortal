from pyramid.view import view_config
from pyramid.renderers import render


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='about', renderer='templates/about.pt')
def about_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='support', renderer='templates/support.pt')
def about_view(request):
    return {'footer': footer_view(request)}


def footer_view(request):
    return render('templates/footer.pt', {'foo': 'bar'})
