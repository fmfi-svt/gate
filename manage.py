#!/usr/bin/env python
"""Management utility for the Gate server."""

import run

import nacl.raw as nacl
import psycopg2
import os, sys

def controller(args):
    """Manage controllers.
    
    If args[1] is 'delete', deletes the given controller from the DB.
    Otherwise adds the controller to the DB, generating a new random key.
    """
    try:
        mac, ip = args
    except ValueError:
        mac, ip = input('MAC addr (ID): '), input('IP addr: ')
    with psycopg2.connect(**config.DB) as conn:
        cur = conn.cursor()
        if ip == 'delete':
            cur.execute("DELETE FROM controllers WHERE id = %s", (mac,))
        else:
            key = nacl.randombytes(nacl.crypto_secretbox_KEYBYTES)
            cur.execute("CREATE TABLE IF NOT EXISTS controllers"
                        "(id macaddr PRIMARY KEY, ip inet UNIQUE, key bytea);")
            cur.execute("INSERT INTO controllers (id , ip, key)"
                        "VALUES (%s, %s, %s);",  (mac, ip, key))
        cur.close()

actions = {
    'controller': controller,
    'run'       : lambda _: run.main()
}

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
    try:
        actions[sys.argv[1]](sys.argv[2:])
    except (IndexError, KeyError):
        actions_str = '|'.join(sorted(actions.keys()))
        print('Usage: {} {} [extra arguments]'.format(sys.argv[0], actions_str))
