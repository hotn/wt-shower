# Wrongtown Shower System

## System Requirements

### System Packages

Run the following to install system packages:

``` bash
apt install espeak redis-server sqlite3 virtualenv espeak-ng
```

### Python

The shower app currently requires Python 3.7 and will not run correctly on some newer versions of Python.
To install Python 3.7, first install [pyenv](https://github.com/pyenv/pyenv).

The first option for installing on pyenv Linux won't work on Raspberry Pi because the version of Linux
running on the Pi is not compatible with Homebrew. Instead, use the "Automatic Installer option" by running the following:

``` bash
curl https://pyenv.run | bash
```

Once pyenv is installed, install Python3.7:

``` bash
pyenv install 3.7.17
```

Then switch to that version of python, either globally:

``` bash
pyenv global 3.7.17
```

Or only for the shower project by navigating to the project directory and running:

``` bash
pyenv local 3.7.17
```

### Virtual Environment

To create and set up the virtual environment for the app, run the following within the project directory:

``` bash
virtualenv -p python3.7 .venv
. .venv/bin/activate
pip install -r requirements.txt
python create_db.py
```

### NFC Reader

verify nfc reader. Look for `Sony Corp.`

``` bash
lsusb
```

enable nfc reader

``` bash
python -m nfc
```

i.e.
``` bash
sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c1\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
sudo udevadm control -R # then re-attach device
```


## Seed Data

Enter the Sqlite shell for the app database:

``` bash
sqlite3 app.db
```

Then import data from CSV files:

``` sqlite3
.mode csv
.import data/users.csv users
.import data/showers.csv showers
.import data/phrases.csv phrases
```

## Run

main site

``` bash
python app.py
```

workers

``` bash
celery -A app.celery worker -l info -E
celery -A app.celery beat -l info
```

switch control

``` bash
python hello_gpio3.py
```

nfc reader

``` bash
python nfc_reader.py
```

## systemd

restart

``` bash
sudo systemctl restart shower-app shower-worker shower-beater shower-gpio shower-nfc

```

logs

``` bash
journalctl -f -u shower-app -o cat | ccze
journalctl -f -u shower-worker -o cat | ccze
journalctl -f -u shower-beater -o cat | ccze
#journalctl -f -u shower-gpio | ccze
journalctl -f -u shower-nfc | ccze
journalctl -f -u shower-1 | ccze
journalctl -f -u shower-2 | ccze
```


## Mac Development

install emulator

``` bash
pip install git+https://github.com/nosix/raspberry-gpio-emulator/
```


## Debug

``` bash
watch -n1 gpio readall
watch -n1 "sqlite3 -header app.db 'select * from showers' "
```

## Fonts

``` bash
sudo apt-get install fonts-noto fonts-symbola
```
