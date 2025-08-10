# Wrongtown Shower System

## System Requirements

### System Packages

Run the following to install system packages:

``` bash
apt install espeak redis-server sqlite3 virtualenv espeak-ng fonts-noto fonts-symbola tmux ccze
```

Package purposes:

- `espeak` - 
- `redis-server` - Session state management
- `sqlite3` - Database
- `virtualenv` - Python virtual environments
- `espeak-ng` - Text-to-speech
- `fonts-noto` - Font package
- `fonts-symbola` - Emoji font support
- `tmux` - Multi-window console
- `ccze` - Log colorizer

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

### Logging In

Logging in can be achieved in two different ways:

- PIN
  
  Users may be assigned a PIN to use for logging in. If a user has a PIN, they may select their name from the dropdown list of camp members, then tap the PIN Code input field on the form to bring up the 10-key display for PIN entry.
  
  _Note: This option is probably best limited to admin users only. Providing this option to all camp members adds an additional thing to teach camp members as well as expands the number of features to support. It also prevents people from stealing other peoples' PINs and using their credits without their knowledge._

- Scan Codes

  Scan code logins could consist of a variety of forms. In the past, NFC tags were used for scan codes. Currently, QR codes are used for scan codes. In either case, the app will allow logging in by simply scanning the code while on the login screen.

  _Note: With certain approaches to enabling code scan logins, it may nearly impossible to prevent user input on other screens, so consideration for what input on all other screens may do is important. For example, barcode readers may simply send input signals for each character in the barcode as if it were a keyboard. If there are text input areas that have important significance, the barcode scanner will be able to input text if a barcode is scanned._

## systemd

restart

``` bash
sudo systemctl restart shower-app shower-worker shower-beater shower-gpio

```

logs

``` bash
journalctl -f -u shower-app -o cat | ccze
journalctl -f -u shower-worker -o cat | ccze
journalctl -f -u shower-beater -o cat | ccze
#journalctl -f -u shower-gpio | ccze
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

**NOT NEEDED, INSTALLED ABOVE**

``` bash
sudo apt-get install fonts-noto fonts-symbola
```
