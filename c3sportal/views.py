from pyramid.view import view_config

from .models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    return {'one': one, 'project': 'C3S'}


@view_config(route_name='definition', renderer='templates/definition.pt')
def about_view(request):
    return {'project': 'C3S'}


@view_config(route_name='background', renderer='templates/background.pt')
def background_view(request):
    return {'project': 'C3S'}


@view_config(route_name='motivation', renderer='templates/motivation.pt')
def motivation_view(request):
    return {'project': 'C3S'}


@view_config(route_name='goals', renderer='templates/goals.pt')
def goals_view(request):
    one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    return {'one': one, 'project': 'C3S'}


@view_config(route_name='roadmap', renderer='templates/roadmap.pt')
def roadmap_view(request):
    one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    return {'one': one, 'project': 'C3S'}
