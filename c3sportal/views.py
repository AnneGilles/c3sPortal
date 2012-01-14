from pyramid.view import view_config
from pyramid.renderers import render


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='definition', renderer='templates/definition.pt')
def about_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='background', renderer='templates/background.pt')
def background_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='motivation', renderer='templates/motivation.pt')
def motivation_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='goals', renderer='templates/goals.pt')
def goals_view(request):
    return {'footer': footer_view(request)}


@view_config(route_name='roadmap', renderer='templates/roadmap.pt')
def roadmap_view(request):
    return {'footer': footer_view(request)}


def footer_view(request):
    #    footer =
    return render('templates/footer.pt', {'foo': 'bar'})
