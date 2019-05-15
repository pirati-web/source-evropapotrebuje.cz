virtualenv venv
. venv/bin/activate
dnf install postgresql-server postgresql-devel # je to prasarna, ten web databazy nepotrebuje a nema
sudo systemctl start postgresql
pip install -r pip-requirements.txt

chmod -R 0777 . #kvuli vytvarneni uzivatelu v postgre

TODO

psql -h localhost -d piratieuweb -U piratieuweb # overeni ze databaze bezi

