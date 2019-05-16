# stručně: je to prasárna, pokud chcete poradit zavolejte mi

virtualenv venv
. venv/bin/activate
dnf install postgresql-server postgresql-devel # je to prasarna, ten web databazy nepotrebuje a nema
sudo systemctl start postgresql
pip install -r pip-requirements.txt

chmod -R 0777 . #kvuli vytvarneni uzivatelu v postgre


TODO vytvorit databazi a usera + propojit

psql -h localhost -d piratieuweb -U piratieuweb # overeni ze databaze bezi

# cp pirati_cz_euro2019.html pirati_cz.html

./manage.py migrate
./run.sh
