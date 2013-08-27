from five import grok
from plone.directives import dexterity, form
from wcc.assemblyhomepage.content.homepage import IHomepage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IHomepage)
    grok.require('zope2.View')
    grok.template('homepage_view')
    grok.name('view')

    def slider_items(self):
        data = []
        for i in self.context.slider_items:
            obj = i.to_object
            if obj is None:
                continue
            title = getattr(obj, 'slider_title', None)
            if not title:
                title = obj.Title()
            description = getattr(obj, 'slider_description', None)
            if not description:
                description = obj.Description()

            width = 455
            height = 210

            scales = obj.restrictedTraverse('@@images')

            if getattr(obj, 'slider_image', None):
                image = scales.scale('slider_image', width=width,
                                    height=height)
            else:
                image = None

            if image:
                image_url = image.url
            else:
                image_url = 'http://placehold.it/%sx%s' % (width, height)

            data.append({
                'title': title,
                'description': description,
                'image_url': image_url,
                'url': obj.absolute_url(),
                'slide_css':
                    """
                        height: %spx;
                        width: %spx;
                        background-image:url('%s');
                    """ % (
                        height, width, image_url
                    )
            })
        return data
