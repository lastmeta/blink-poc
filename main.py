from message_board import MSGBoard
from node import Actor


def foo(bar, baz, nay):
    return bar + baz + nay


def bar():
    return 3


def baz():
    return 30


def kay():
    return 300


def jay():
    return 3000


def nay(kay, jay):
    return kay + jay


def show(foo):
    print(foo)
    return True


actor_foo = Actor(verbose=True, functions={
    'foo': (foo, ('bar', 'baz', 'nay')),
})
actor_bar = Actor(verbose=True, functions={
    'bar': (bar, tuple()),
})
actor_baz = Actor(verbose=True, functions={
    'baz': (baz, tuple()),
})
actor_kay = Actor(verbose=True, functions={
    'kay': (kay, tuple()),
})
actor_jay = Actor(verbose=True, functions={
    'jay': (jay, tuple()),
})
actor_nay = Actor(verbose=True, functions={
    'nay': (nay, ('kay', 'jay')),
})
actor_user = Actor(verbose=True, functions={
    'show': (show, ('foo',)),
})

thoughts = MSGBoard('thoughts')

actor_foo.listen(thoughts, debug=True)
actor_bar.listen(thoughts, debug=True)
actor_baz.listen(thoughts, debug=True)
actor_kay.listen(thoughts, debug=True)
actor_jay.listen(thoughts, debug=True)
actor_nay.listen(thoughts, debug=True)
actor_user.listen(thoughts,debug=True)

new_id = thoughts.produce_id()
message = {'id': new_id, 'ref_id': new_id, 'request': 'show', 'substitions': {'foo':'nay'}}

actor_user.say(message, thoughts)
