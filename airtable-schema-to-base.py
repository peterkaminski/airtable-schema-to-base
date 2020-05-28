#!/usr/bin/env python

################################################################
#
# airtable-schema-to-base
#
# Read an airtable-schema JSON file, populate an Airtable base.
#
# Copyright 2020 Peter Kaminski. Licensed under MIT License.
#
################################################################

from airtable import Airtable # pip install airtable-python-wrapper
import argparse # pip install argparse
import json # core
import os # core
import pendulum # pip install pendulum

# Set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Read an airtable-schema JSON file, populate an Airtable base.')
    parser.add_argument('--json', '-j', required=True, help='path to a JSON file as output by airtable-schema')
    parser.add_argument('--name', '-n', required=True, help='name of base represented by JSON file (My Base)')
    parser.add_argument('--id', '-i', required=True, help='ID of base represented by JSON file (appXXXXXXXXXXXXXX)')
    parser.add_argument('--destination', '-d', required=True, help='ID of base to write schema to (appXXXXXXXXXXXXXX)')
    return parser

def main():
    # get run time
    run_time = pendulum.now('UTC').to_w3c_string()

    # get API key from environment
    airtable_api_key = os.environ['AIRTABLE_API_KEY']

    # get arguments
    argparser = init_argparse();
    args = argparser.parse_args();

    # set up Airtable connections
    bases_table = Airtable(args.destination, 'Bases', api_key=airtable_api_key)
    tables_table = Airtable(args.destination, 'Tables', api_key=airtable_api_key)
    fields_table = Airtable(args.destination, 'Fields', api_key=airtable_api_key)

    # create base record
    data = {
        'Name': args.name,
        'Base ID': args.id,
        'Base URL': 'https://airtable.com/' + args.id,
        'Last Imported': run_time
    }
    bases_table.insert(data)

    # parse JSON, write to base
    with open(args.json) as json_file:
        schema = json.load(json_file)
        for table in schema:
            # write table record
            table = schema[table]
            data = {
                'Name': table['name'],
                'Base': args.name,
                'Last Imported': run_time
            }
            tables_table.insert(data)
            for field in table['columns']:
                # write field record
                data = {
                    'Name': field['name'],
                    'Table': table['name'],
                    'Type': field['type'],
                    'Last Imported': run_time
                }
                fields_table.insert(data)

# Run this script
if __name__ == "__main__":
    exit(main())
