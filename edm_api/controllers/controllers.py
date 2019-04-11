# -*- coding: utf-8 -*-
from odoo import http

# class EdmApi(http.Controller):
#     @http.route('/edm_api/edm_api/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edm_api/edm_api/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edm_api.listing', {
#             'root': '/edm_api/edm_api',
#             'objects': http.request.env['edm_api.edm_api'].search([]),
#         })

#     @http.route('/edm_api/edm_api/objects/<model("edm_api.edm_api"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edm_api.object', {
#             'object': obj
#         })