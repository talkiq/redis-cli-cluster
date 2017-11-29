from .cluster import StrictRedisCluster


def repl(host, port):
    client = StrictRedisCluster(host=host, port=port)

    while True:
        try:
            data = input('{}:{}> '.format(host, port))
        except (EOFError, KeyboardInterrupt):
            return

        cmd, *args = data.split()
        cmd = cmd.lower()

        try:
            if cmd == 'del':
                cmd = 'delete'

            fx = getattr(client, cmd)
            if cmd == 'cluster':
                ret = fx(args[0], *args[1:])
            else:
                ret = fx(*args)

            if ret is True:
                print('OK')
            else:
                print('"{}"'.format(ret))
        except AttributeError:
            print("(error) ERR unknown command '{}'".format(cmd))
        except (IndexError, TypeError):
            print("(error) ERR wrong number of arguments for '{}' "
                  'command'.format(cmd))
