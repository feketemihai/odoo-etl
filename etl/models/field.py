# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from odoo import models, fields, api, _
from odoo.exceptions import Warning


class field(models.Model):
    """"""

    _name = 'etl.field'
    _description = 'field'

    name = fields.Char(
        string='Name',
        required=True
        )
    field_description = fields.Char(
        string='Field Description',
        required=True
        )
    relation = fields.Char(
        string='Relation'
        )
    relation_field = fields.Char(
        string='Relation Field'
        )
    ttype = fields.Char(
        string='Type',
        required=True
        )
    required = fields.Char(
        string='Required'
        )
    function = fields.Char(
        string='Function'
        )
    model_id = fields.Many2one(
        'etl.external_model',
        ondelete='cascade',
        string='Model'
        )
    type = fields.Selection(
        related='model_id.type',
        string='Type',
        readonly=True,
        )

    _constraints = [
    ]

