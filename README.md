# advent-of-code
Repository to hold Advent of Code (http://adventofcode.com/) solutions.

## Setup

* Set up a virtual environment `python -m venv venv`
* Activate it `source venv/bin/activate`
* Install requirements `pip install -r requirements.txt`
* Set up PYTHONPATH `export PYTHONPATH="${PYTHONPATH}:/path/to/advent-of-code"` eg `export PYTHONPATH=/workspaces/advent-of-code`
* Use `python util.py` to set up each day
* Run each day using `python year_2023/day01/trebuchet.py`
* Update tox.ini to set default year for testing
