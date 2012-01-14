from pyramid.renderers import get_renderer


def add_base_template(event):
    base = get_renderer('templates/base.pt').implementation()
    #    footer = get_renderer('templates/footer.pt').implementation()
    event.update({
            #            'footer': footer,
            'base': base,
            })
