def bold(func):
    def wrap():
        return "<b>" + func() + "</b>"
    return wrap

def italic(func):
    def wrap():
        return "<i>" + func() + "</i>"
    return wrap
@bold
@italic
def get_text():
    return "Hello, kowshik biswas kakon!"

print(get_text())  