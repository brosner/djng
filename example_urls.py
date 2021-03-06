import djng

app = djng.ErrorWrapper(
    djng.Router(
        (r'^hello$', lambda request: djng.Response('Hello, world')),
        (r'^goodbye$', lambda request: djng.Response('Goodbye, world')),
    ),
    custom_404 = lambda request: djng.Response('404 error'),
    custom_500 = lambda request: djng.Response('500 error')
)

if __name__ == '__main__':
    djng.serve(app, '0.0.0.0', 8888)
