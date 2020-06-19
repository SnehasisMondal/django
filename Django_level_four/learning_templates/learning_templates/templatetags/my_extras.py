from django import relative_url_templates

register=template.Library()

@register.filter(name='cut')
def cutfunc(value,arg):
    """
    This cuts all values of arg from the string.
    """
    return value.replace(arg,'')

#register.filter('cut',cutfunc)
