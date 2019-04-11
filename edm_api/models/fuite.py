# -*- coding: utf-8 -*-

from odoo import api, models, fields
import json


class Fuite(models.Model):
    _name = 'edm_api.fuite'

    name = fields.Char('Intitulé')
    ville = fields.Many2one('edm_api.ville')
    marche = fields.Many2one('edm_api.marche')
    adresse = fields.Char('Adresse')
    attachment_ids = fields.Many2many('ir.attachment', 'class_ir_attachments_rel', 'class_id', 'attachment_id', 'Attachments')
    lat = fields.Char('Latitude')
    lng = fields.Char('Longitude')
    map = fields.Char('Map')

    @api.one
    def clear_record_data(self):
        maps_loc = {u'position': {u'lat': float(self.lat), u'lng': float(self.lng)}, u'zoom': 18}
        json_map = json.dumps(maps_loc)
        print(self.attachment_ids)
        self.map = json_map

    @api.onchange('map')
    def update_lat_lng(self):
        if self.map:
            position = json.loads(self.map)['position']
            self.lat = position['lat']
            self.lng = position['lng']

    @api.model
    def create(self, values):
        rec = super(Fuite, self).create(values)
        print(values)
        return rec


class Ville(models.Model):
    _name = 'edm_api.ville'

    name = fields.Char('Intitulé')


class Marche(models.Model):
    _name = 'edm_api.marche'
    _rec_name = 'name'

    name = fields.Char('Intitulé')
