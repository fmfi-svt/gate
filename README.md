server: the DB + "manager"
==========================

Communicates with the controllers.

Setup
-----

**Required Python version: 3.4**

1. create virtualenv if necessary: `pyvenv .` (or `pyvenv-3.4 .`)
2. activate virtualenv:
   - bash, zsh: `source bin/activate`
   - fish: `. bin/activate.fish`
   - csh, tcsh: `source bin/activate.csh`
3. install dependencies if necessary: `pip install -r requirements.txt`
4. configure: `cp config.py{.example,}; $EDITOR config.py`
5. add controller entries to the DB: `.manage.py controller MAC IP`

Run with `./run.py` or `./manage.py run`.
