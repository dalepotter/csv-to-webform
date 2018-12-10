# csv-to-webform

Proof-of-concept to demonstrate automated data entry (from a CSV file to a webform).

Uses the [Splinter library](https://splinter.readthedocs.io/) to enter data from a known CSV (`sample_data.csv`) into a [corresponding webform](https://goo.gl/forms/D8DLeJawU91srNCB2).

Developed for python 3.6.7

# Setup

```
# Create and activate a virtual environment
python3 -m venv pyenv
source pyenv/bin/activate

# Install geckodriver - a plugin allowing python to interact with Gecko-based browsers (such as Firefox)
# Follow instructions from: https://stackoverflow.com/a/40208762

# Install required python libraries
pip install -r requirements.txt
```

# Running the script
```
python data_entry.py
```
