# Homework

## Installation
- make a virtualenv: `python3 -m venv venv` 
- activate virtualenv: `. ./venv/bin/activate`
- install dependences: `pip install -r requirements.txt`

## run the web app
- flask run

## Test w/ curl
- `curl localhost:5000`
- `curl -H "Accept: application/json" localhost:5000`

## Run unit tests
- python tests.py

## logging
- logs to `hw.log` -- b/c of some flask magic that I'm not yet aware of, flask is logging some stuff at INFO to the log that's redundant.  Since the instructions called for a DEBUG message, I'm leaving the redundancy for now.
