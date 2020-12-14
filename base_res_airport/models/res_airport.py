import logging
from requests import request

from odoo import api, fields, models

AIRPORT_DATA_URL = 'http://ourairports.com/data/airports.csv'
_logger = logging.getLogger(__name__)


class ResAirport(models.Model):
    _name = 'res.airport'
    _description = 'Airport'
    _rec_name = 'iata'

    name = fields.Char(string='Name')
    icao = fields.Char(string='ICAO')
    iata = fields.Char(string='IATA')
    city = fields.Char(string='City')
    country_id = fields.Many2one('res.country', string='Country')
    elevation = fields.Char(string='Elevation')
    lat = fields.Char(string='Latitude')
    lon = fields.Char(string='Longitude')

    @api.model
    def cron_fetch_airports_data(self):
        """
        Cron job to fetch IATA codes from the
        ourairports project repo
        """

        _logger.warning(f'Reading file from: {AIRPORT_DATA_URL}')

        # use the requests library to download
        # the csv file
        res = request('GET', AIRPORT_DATA_URL)

        # split the data into lines, each
        # line represents an airport
        lines = res.content.decode('utf-8').splitlines()

        # get all the IATA codes
        # in the system(odoo)
        odoo_airports = self.search([]).mapped('iata')

        # list to store newly created airports
        new_airports = []

        # skip the first line as
        # it is the title
        for line in lines[1:]:

            # convert the line into a list
            line = line.split(',')

            # get the iata code from the list
            iata_code = line[13].replace('"', '')

            # if IATA code not on the system
            # add it to the list as a dict
            if iata_code and iata_code not in odoo_airports:

                # try to get the external id
                # if not present continue
                try:

                    # get the country object in odoo using
                    # the xml id
                    country_xml_id = 'base.' + line[8].replace('"', '').lower()

                    # for UK
                    if country_xml_id == 'base.gb':
                        country_xml_id = 'base.uk'

                    # get country
                    country = self.env.ref(country_xml_id)
                except ValueError as e:
                    continue

                # add the newly created
                # airports as dicts to
                new_airports.append({
                    'name': line[3].replace('"', ''),
                    'iata': line[13].replace('"', ''),
                    'icao': line[1].replace('"', ''),
                    'city': line[10].replace('"', ''),
                    'country_id': country.id if country else False,
                    'elevation': line[6].replace('"', ''),
                    'lat': line[4].replace('"', ''),
                    'lon': line[5].replace('"', ''),
                })

                _logger.warning(f'Adding new airport {line[3]}, '
                                f'IATA code: {line[13]} ')

        # create the newly created
        # airports in odoo
        for airport in new_airports:
            self.create(airport)

        return True
