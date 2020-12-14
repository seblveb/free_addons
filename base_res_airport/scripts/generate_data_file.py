########################################
# This is a python script that reads   #
# the airport.json file and extracts   #
# the information to generate the file #
# res_airport_data.xml                 #
########################################

import json


def main():

    # open the json file
    with open('airports.json', 'r') as input_file:

        # load the data in a dict
        data = json.load(input_file)

        # create an output xml file and output
        # the records into it
        with open('res_airport_data.xml', 'w') as output_file:
            output_file.write(
f"""<?xml version="1.0" encoding="utf-8"?>
    <odoo>
        <data noupdate="1">
                               """)
            for airport in data:
                if data[airport]['iata']:
                    record = f"""
                <record id="{data[airport]['icao']}" model="res.airport">
                    <field name="name">{data[airport]['name'].replace('&', 'and')}</field>
                    <field name="icao">{data[airport]['icao']}</field>
                    <field name="iata">{data[airport]['iata']}</field>
                    <field name="city">{data[airport]['city']}</field>
                    <field name="country_id" ref="base.{data[airport]['country'].lower()}"/>
                    <field name="elevation">{data[airport]['elevation']}</field>
                    <field name="lat">{data[airport]['lat']}</field>
                    <field name="lon">{data[airport]['lon']}</field>
                </record>
                              """
                    output_file.write(record)
            output_file.write(f"""
        </data>
    </odoo>
                               """)


if __name__ == '__main__':
    main()
