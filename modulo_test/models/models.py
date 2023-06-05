# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulo_test(models.Model):
     _name = 'modulo_test.modulo_test'
     _description = 'modulo_test.modulo_test'

     nombre = fields.Char()
     telefono = fields.Char()

    
