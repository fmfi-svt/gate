server: the DB + "manager"
==========================

Communicates with the controllers.

Setup
-----

**Required Python version: 3.4**

1. Create virtualenv if necessary: `pyvenv ./venv` (or `pyvenv-3.4 ./venv`)
2. Activate virtualenv:
   - bash, zsh: `source venv/bin/activate`
   - fish: `. venv/bin/activate.fish`
   - csh, tcsh: `source venv/bin/activate.csh`
3. Install dependencies if necessary: `pip install -r requirements.txt`
4. Configure by setting environment variables: `PORT` and `DB_URL`.  
   You can also write it to `.env`, `./manage.py run` will load it.
   `cp .env{.example,}; $EDITOR .env` to get started.
5. add controller entries to the DB: `./manage.py controller MAC IP`

Run with `./manage.py run`.
