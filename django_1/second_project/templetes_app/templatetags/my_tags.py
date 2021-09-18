from django import template

register = template.Library()

#decorators
@register.filter(name='cut')
def cut(value,args):
    return args.replace(args,"")

#register.filter('cut',cut)
