from django import template                                                                                                                                                        

register = template.Library()

@register.filter
def mul(x, y):
    return x * y

def add(x, y):
    return x + y
