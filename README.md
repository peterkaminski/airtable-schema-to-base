# Airtable Schema to Base

## Overview

Takes an `appXXXXXXXXXXXXXX.json` file as written by [airtable-schema](https://github.com/cape-io/airtable-schema) and uploads it to an empty, preconfigured Airtable base.

(You may wish to use this fork, [peterkaminski/airtable-schema](https://github.com/peterkaminski/airtable-schema), with an updated `package.json`.)

The current version of **Airtable Schema to Base** takes a shortcut to linking its tables, having you do the actual linking. You will create the linked fields as single-line text, rather than linked fields. The script will populate the records, and then you will convert the fields to "Link to another record", and Airtable will automatically link everything properly.

A future version will be able to read the output tables to find records IDs for inter-table linking, and will perform and maintain the linking by itself.

The long-term vision is to expand this tool so that it will help create and maintain a multi-base data dictionary.

**Airtable Schema to Base** is written in Python 3.

## Setting Up Data Dictionary Base

Create a new, empty base to receive the schema data. For this document, let's call this "My Data Dictionary Base".

Create the following tables and fields. Make the fields single-line text unless noted otherwise.

* Bases
 * Name
 * Base ID
 * Base URL - URL
 * Description - Long text
 * Last Imported - Date
* Tables
 * Name
 * Base
 * Description - Long text
 * Last Imported - Date
* Fields
 * Name
 * Table
 * Type
 * Description - Long text
 * Last Imported - Date

## Installation

Clone or download the repository.

```shell
git clone https://github.com/peterkaminski/airtable-schema-to-base.git && cd git clone https://github.com/peterkaminski/airtable-schema.git
```

## Script Configuration

Copy `env.sh-template` to `env.sh`, and then replace the dummy API key value with your own Airtable API key.

Find these pieces of information:

* ID of the base you want to examine, `appXXXXXXXXXXXXXX`
* Name of the base you want to examine, "My Base"
* ID of your "My Data Dictionary Base", `appYYYYYYYYYYYYYY`

Run `airtable-schema` on the base you want to examine, and remember the path to the output file, `appXXXXXXXXXXXXXX.json`.

## Python Configuration

To isolate the libraries and versions used by this script, create a venv, then install the libraries.

```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Airtable Schema to Base

Run the `airtable-schema-to-base.py` script.

```shell
./airtable-schema-to-base.py -j appXXXXXXXXXXXXXX.json -i appXXXXXXXXXXXXXX -n Backline -d appYYYYYYYYYYYYYY
```

The script will read the JSON file, and transfer the structure it has mapped to your "My Data Dictionary Base". It will take a few minutes, and there is no output. If you have your "My Data Dictionary Base", you will see data being populated into it.

After the script has finished, open the base.

Go to the "Tables" table. Convert the "Base" field to a link to the "Bases" table. Turn off "Allow linking to multiple records".

Go to the "Fields" table. Convert the "Table" field to a link to the "Tables" table. Turn off "Allow linking to multiple records".

You may now rearrange your tables. For instance:

* On the "Fields" table, hide the "Table" field, and group by "Table".
* On the "Tables" table, hide the "Base" and "Fields" table, and group by "Base".

## Feedback, Suggestions, Bugs

Feedback is welcome either as Issues or Pull Requests at the [Airtable Schema to Base repo](https://github.com/peterkaminski/airtable-schema-to-base).

## License

Copyright (c) 2020 Peter Kaminski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
