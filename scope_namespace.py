x = 'global'

def scope_local():
    x = 'local'
    print(x)


def using_global_scope():
    global x
    print(x)


def scope_local_recieving_global_as_args(x):
    print(f'recieved global: {x}')
    x = 'local'
    print(f'changed to: {x}')


def scope_local_modifying_global_scope():
    global x
    x = 'global modified in function'
    print(x)
    

scope_local()
using_global_scope()
scope_local_recieving_global_as_args(x)
print(f'global x stills not change: {x}')
scope_local_modifying_global_scope()
print(f'Now x global is {x}')




