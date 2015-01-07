#!/usr/bin/env python
"""Management utility for the Gate server"""

from gateserver.main import serve

import nacl.raw as nacl
import psycopg2
import os, sys

def check_args(given, exp):
    if len(given) != len(exp):
        usage(actions, 'takes {} arguments: {}'.format(len(exp), ' '.join(exp)))

def walk_actions(action, argv):
    here = 0
    while here < len(argv) and isinstance(action[1], dict):
        action = action[1][argv[here]]
        here += 1
    return action, argv[here:]

def dispatch_action(actions, argv):
    try:
        (_, action), args = walk_actions(actions, argv)
        if isinstance(action, dict): usage(actions, 'not enough arguments')
        else: return action(args)
    except ValueError as e:
        usage(actions, e)

def help(action, prepend):
    doc, this = action
    if isinstance(this, dict): # we must go deeper!
        res = [prepend+':\n\t'+doc]
        for cmd, subs in this.items():
            res += help(subs, prepend+' '+cmd)
        return res
    else:
        return [prepend+':\n\t'+doc]

def usage(actions, err=None):
    if err: sys.stderr.write('Error: {}\n'.format(err))
    print('Usage:')
    try:
        sub, remains = walk_actions(actions, sys.argv[1:])
        valid = len(sys.argv) - len(remains)
    except ValueError:
        sub = actions
        valid = 0
    print('\n'.join(help(sub, ' '.join(sys.argv[:valid]))))
    sys.exit(64)

################################################################################

def exec_sql(query, args=(), read=False):
    with psycopg2.connect(os.environ.get('DB_URL')) as conn:
        cur = conn.cursor()
        cur.execute(query, args)
        if read: return cur.fetchall()

def ctrl_add(args):
    check_args(args, ['MAC', 'IP'])
    mac, ip = args
    key = nacl.randombytes(nacl.crypto_secretbox_KEYBYTES)
    exec_sql("CREATE TABLE IF NOT EXISTS controllers"
             "(mac macaddr PRIMARY KEY, ip inet UNIQUE, key bytea)")
    exec_sql("INSERT INTO controllers (mac, ip, key)"
             "VALUES (%s, %s, %s)",  (mac, ip, key))

def ctrl_delete(args):
    check_args(args, ['MAC'])
    mac = args[0]
    exec_sql("DELETE FROM controllers WHERE mac = %s", (mac,))

def ctrl_list(args):
    check_args(args, [])
    for mac, ip in exec_sql("SELECT mac, ip FROM controllers", read=True):
        print('{}\t{}'.format(mac, ip))

################################################################################

actions = (__doc__, {
    'serve'     : ('launch the server', lambda _: serve()),
    'controller': ('manage the controllers database.', {
        'add'   : ('add a new controller, generating a random key', ctrl_add),
        'delete': ('delete the given controller', ctrl_delete),
        'list'  : ('list all controllers', ctrl_list),
        }),
})

################################################################################

def load_dotenv():
    """
    Read the .env file if exists, and load it into os.environ.
    """
    if os.path.exists('.env'):
        for line in open('.env', 'r'):
            line = line.strip()
            if line == '' or line.startswith('#') or '=' not in line: continue
            k, v = line.split('=')
            v = v.strip("'").strip('"')
            os.environ.setdefault(k, v)

if __name__ == '__main__':
    load_dotenv()
    sys.exit(dispatch_action(actions, sys.argv[1:]))
