# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductIssues(models.Model):
    _name = 'product.issues'
    _description = 'Container of the UIDs to work'

    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
    drawing_owner = fields.Many2one(
        comodel_name='res.partner',
        string='Drawing owner',
    )
    drawing_number = fields.Char(
        size=50,
        string='Drawing number',
    )
    drawing_review = fields.Char(
        size=50,
        string='Drawing review',
    )
    drawing_date_revision = fields.Datetime(
        size=50,
        string='Drawing date revision',
    )
    drawing_file = fields.Many2many(
        'ir.attachment',
        string="Attachment",
        help='You can attach the copy of your Letter'
    )
    see_production = fields.Selection(
        [
            ('yes', 'Yes'),
            ('no', 'No'),
        ],
        string="See production?",
    )
    drawing_type = fields.Selection(
        [
            ('AC - Critical areas', 'AC - Critical areas'),
            ('AM - Assembly of the mold', 'AM - Assembly of the mold'),
            ('AV - Part cut', 'AV - Part cut'),
            ('AV - Reload cut', 'AV - Reload cut'),
            ('AV - Acceptance criteria', 'AV - Acceptance criteria'),
            ('AV - Demoulding', 'AV - Demoulding'),
            ('AV - Detailed', 'AV - Detailed'),
            ('AV - Detailed radios', 'AV - Detailed radios'),
            ('AV - Hardness', 'AV - Hardness'),
            ('AV - Print', 'AV - Print'),
            ('AV - Ceramic Staples', 'AV - Ceramic Staples'),
            ('AV - Wax Injection', 'AV - Wax Injection'),
            ('AV - Marking', 'AV - Marking'),
            ('AV - Molding', 'AV - Molding'),
            ('AV - Polished', 'AV - Polished'),
            ('AV - Polished', 'AV - Polished'),
            ('AVC - Reload cut', 'AVC - Reload cut'),
            ('AVM - Marking', 'AVM - Marking'),
            ('AVME - Measurement', 'AVME - Measurement'),
            ('AVT - Tensioner', 'AVT - Tensioner'),
            ('AVTT - visual aid of Heat Treatment', 'AVTT - visual aid of Heat Treatment'),
            ('BA - Baloneado', 'BA - Baloneado'),
            ('BOM - Bill of Materials', 'BOM - Bill of Materials'),
            ('CA - Acceptance Criteria', 'CA - Acceptance Criteria'),
            ('CA - PND Acceptance Criteria', 'CA - PND Acceptance Criteria'),
            ('Cl- Checklist', 'Cl- Checklist'),
            ('CM - Matrix Control', 'CM - Matrix Control'),
            ('CM - Model Control', 'CM - Model Control'),
            ('CPR - Control Weights and Relations', 'CPR - Control Weights and Relations'),
            ('POK course', 'POK course'),
            ('DI - Inspection Drawing', 'DI - Inspection Drawing'),
            ('DP - Drawing Painting', 'DP - Drawing Painting'),
            ('ED - Solid', 'ED - Solid'),
            ('EN - Assembly', 'EN - Assembly'),
            ('EN - Customer Assembly', 'EN - Customer Assembly'),
            ('FC - Foundry Client', 'FC - Foundry Client'),
            ('FM - Final Machining', 'FM - Final Machining'),
            ('Forging', 'Forging'),
            ('FP - POK Foundry', 'FP - POK Foundry'),
            ('MC - Customer Machining', 'MC - Customer Machining'),
            ('MF - Final Machining', 'MF - Final Machining'),
            ('MO - Model', 'MO - Model'),
            ('PDF- Solid', 'PDF- Solid'),
            ('PM - Manufacturing Plan', 'PM - Manufacturing Plan'),
            ('PM - Pre-machined', 'PM - Pre-machined'),
            ('Pre-form Plate', 'Pre-form Plate'),
            ('Pre-machined', 'Pre-machined'),
            ('QP - Quality Plan', 'QP - Quality Plan'),
            ('RC - Client Coating', 'RC - Client Coating'),
            ('RF - Fusion Report', 'RF - Fusion Report'),
            ('RT - Radiography', 'RT - Radiography'),
            ('YES - Over-imposition', 'YES - Over-imposition'),
            ('SO - Solid', 'SO - Solid'),
            ('SP - MT Heads', 'SP - MT Heads'),
            ('SP - MT Cables', 'SP - MT Cables'),
            ('SP - UT', 'SP - UT'),
            ('SV - Emptying System', 'SV - Emptying System'),
            ('SW - Solid', 'SW - Solid'),
            ('WTR- Wall Thickness Report', 'WTR- Wall Thickness Report'),
        ],
        string='Drawing type',
    )