def func_decor(fun, count):
    def inner(*args, **kwargs):
        return f'<p>{fun(*args,**kwargs)}</p>'
    return inner

@func_decor(count=5)
def get_str(name):
    return name

print(get_str('Serhii'))