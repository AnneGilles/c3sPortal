from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    #engine = engine_from_config(settings, 'sqlalchemy.')
    #DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # prepare to use the base template
    config.add_subscriber('c3sportal.subscribers.add_base_template',
                          'pyramid.events.BeforeRender')
    config.add_subscriber('c3sportal.subscribers.add_locale_to_cookie',
                          'pyramid.events.NewRequest')
    config.add_translation_dirs('c3sportal:locale')
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('benefits', '/benefits')
    config.add_route('support', '/support')
    config.add_route('imprint', '/imprint')
    config.scan()
    return config.make_wsgi_app()
