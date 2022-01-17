from odoo import models, fields, api

class ProductCert(models.Model):
    _name = 'product.cert'
    _description = 'Product certification'

    name = fields.Char(
        string='Certification',
        size=50,
    )
    type = fields.Char(
        string='Product Type',
        size=50,
    )
    specification =fields.Many2one(
        'quality.specification',
        string='Specification',
    )
    sample_size = fields.Char(
        string='Sample size',
        size=50,
    )
    scan_plan = fields.Char(
        string='Scan plan',
        size=50,
    )
    draw_area = fields.Char(
        string='Draw area',
        size=50,
    )
    certification_type = fields.Char(
        string='Certification type',
        size=50,
    )
    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product'
    )
    certifications_files = fields.Many2many(
        'ir.attachment',
        string="Attachment",
        help='You can attach the copy of your Letter'
    )