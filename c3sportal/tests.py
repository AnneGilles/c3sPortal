import unittest
import transaction

from pyramid import testing
from pyramid.decorator import reify

#from .models import DBSession


class DummyReqWithAcceptLangAttr(testing.DummyRequest):
    """
    extend testing.DummyRequest to carry a 'user' attribute

    used in test_playlist_add_validating,
    """
    @reify
    def accept_language(self):
        from webob.acceptparse import AcceptLanguage
        #def best_match(self):
        #    return 'bar'
        return AcceptLanguage('foo')


class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        #from sqlalchemy import create_engine
        #engine = create_engine('sqlite://')
        #from .models import (
        #    Base,
        #    MyModel,
        #    )
        #DBSession.configure(bind=engine)
        #Base.metadata.create_all(engine)
        #with transaction.manager:
        #    model = MyModel(name='one', value=55)
        #    DBSession.add(model)

    def tearDown(self):
        #DBSession.remove()
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = DummyReqWithAcceptLangAttr()
        info = my_view(request)
        self.assertTrue('footer' in info)

    def test_about_view(self):
        from .views import about_view
        request = DummyReqWithAcceptLangAttr()
        info = about_view(request)
        self.assertTrue('footer' in info)

    def test_support_view(self):
        from .views import support_view
        request = DummyReqWithAcceptLangAttr()
        info = support_view(request)
        self.assertTrue('footer' in info)
