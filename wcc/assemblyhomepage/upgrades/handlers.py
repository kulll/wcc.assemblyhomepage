from collective.grok import gs
from Products.CMFCore.utils import getToolByName

# -*- extra stuff goes here -*- 


@gs.upgradestep(title=u'Upgrade wcc.assemblyhomepage to 3',
                description=u'Upgrade wcc.assemblyhomepage to 3',
                source='2', destination='3',
                sortkey=1, profile='wcc.assemblyhomepage:default')
def to3(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.assemblyhomepage.upgrades:to3')
    catalog = getToolByName(context, 'portal_catalog')

    for brain in catalog(portal_type=[
            'wcc.assemblyhomepage.homepage',
            'wcc.assemblyhomepage.newsmediahomepage'],
            Language='all'):

        obj = brain.getObject()
        obj.reindexObject()


@gs.upgradestep(title=u'Upgrade wcc.assemblyhomepage to 2',
                description=u'Upgrade wcc.assemblyhomepage to 2',
                source='1', destination='2',
                sortkey=1, profile='wcc.assemblyhomepage:default')
def to2(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-wcc.assemblyhomepage.upgrades:to2')
