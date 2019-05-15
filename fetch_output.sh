#!/bin/bash
wget -O evropapotrebuje.cz/index.html http://localhost:8011/ 

PAGES="program en en/what-we-want en/how-to-vote sk/ako-volit kandidati zapoj-se kandidati/marcel-kolaja kandidati/marketa-gregorova kandidati/mikulas-peksa kandidati/lukas-blazej kandidati/jana-kolarikova kandidati/ondrej-kolek kandidati/nina-spitalnikova kandidati/eva-ticha kandidati/lukas-lev-cervinka kandidati/marek-necada kandidati/michal-gill kandidati/jiri-hoskovec kandidati/david-frantisek-wagner kandidati/michal-salomoun kandidati/magdalena-dankova kandidati/matej-sandor kandidati/linda-matuskova kandidati/petr-jirman kandidati/dan-lestina kandidati/frantisek-kopriva kandidati/hynek-melichar kandidati/jiri-jansa kandidati/jan-licka kandidati/michael-polak kandidati/ladislav-koubek kandidati/pavel-tauer kandidati/simon-barczi kandidati/milos-vlach kandidati/jiri-lehejcek program/spolecny-eu-pirati program/spolecny-eu-pirati/preambule program/spolecny-eu-pirati/zemedelstvi program/spolecny-eu-pirati/obcanska-spolecnost program/spolecny-eu-pirati/financovani program/spolecny-eu-pirati/vzdelani-kultura-sport program/spolecny-eu-pirati/zivotni-prostredi program/spolecny-eu-pirati/lidska-prava program/spolecny-eu-pirati/svobodny-software program/spolecny-eu-pirati/otevrena-data program/spolecny-eu-pirati/zasady-site-internet program/spolecny-eu-pirati/mezinarodni-zalezitosti program/spolecny-eu-pirati/socialni-veci-a-zdravotni-pece program/spolecny-eu-pirati/vesmirny-program program/spolecny-eu-pirati/doprava jak-volit"

for PAGE in $PAGES; do
    echo $PAGE
    mkdir -p evropapotrebuje.cz/$PAGE
    wget -O evropapotrebuje.cz/$PAGE/index.html http://localhost:8011/$PAGE/
done;

rm -rf evropapotrebuje.cz/static
cd src
tar -c static_files | tar -x -C ../evropapotrebuje.cz
cd ..
mv evropapotrebuje.cz/static_files evropapotrebuje.cz/static
