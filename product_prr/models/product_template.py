# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.AbstractModel):
    _inherit = 'product.template'

    mold_qty = fields.Float(
        size=20,
        string='Quantity per mold',
    )
    injection_qty = fields.Float(
        size=20,
        string='Amount per injection'
    )
    gross_weight = fields.Float(
        string="Gross weight",
        size=20,
    )
    casting_weight = fields.Float(
        string="Casting weight",
        size=20,
    )
    part_weight = fields.Float(
        string="Part weight",
        size=20,
    )
    pwm = fields.Float(
        string="PWM",
        size=20,
    )
    shipping_weight = fields.Float(
        string="Shipping weight",
        size=20,
    )
    mould_type = fields.Selection(
        [
            ("ceramic molding", "Ceramic molding"),
            ("sand molding", "Sand molding"),
            ("n/a", "N/A"),
        ],
        string="Mould type",
    )
    gross_yield = fields.Float(
        string="Gross yield",
        compute='_compute_get_gross_yield'
    )
    casting_yield = fields.Float(
        string="Casting yield",
        compute='_compute_get_casting_yield'
    )
    total_yield = fields.Float(
        string="Total yield",
        compute='_compute_get_total_yield'
    )
    welding_documents =fields.One2many(
        comodel_name='product.welding.specification.document',
        inverse_name='product_template_id',
        string='Welding documents files',
    )
    external_specification =fields.Many2one(
        'quality.specification',
        string='External Specification',
    )
    internal_specification =fields.Many2one(
        'quality.specification',
        string='Internal Specification',
    )
    drawing_files = fields.One2many(
        comodel_name='product.issues',
        inverse_name='product_template_id',
        string='Drawing files',
    )
    product_certifications = fields.One2many(
        comodel_name='product.cert',
        inverse_name='product_template_id',
        string='Product Certification',
    )
    product_mrp = fields.One2many(
        comodel_name='mrp.bom',
        inverse_name='product_tmpl_id',
        string='Product bom',
    )
    # alloy_id = fields.Many2one(
    #     'product.alloy',
    #     string='Alloy',
    # )

    @api.depends('casting_weight', 'gross_weight')
    def _compute_get_gross_yield(self):
        for product in self:
            product.gross_yield = (product.casting_weight / product.gross_weight)*100

    @api.depends('part_weight', 'gross_weight')
    def _compute_get_casting_yield(self):
        for product in self:
            product.casting_yield = (product.part_weight / product.gross_weight)*100

    @api.depends('part_weight', 'gross_weight')
    def _compute_get_total_yield(self):
        for product in self:
            product.total_yield = (product.part_weight / product.gross_weight)*100

    # @api.model
    # def get_prr_values(self):
    #     product_values = []
    #     for product in self:
    #         product_values.append({
    #             'name': product.name,
    #             'sequence': product.sequence,
    #             'type': product.type,
    #             'description': product.description,
    #             'image_field_name': product.image_1920,
    #             # 'currency_id': product.currency_id,
    #             # 'cost_currency_id': product.cost_currency_id,
    #         })
    #     return self.env.ref('product_prr.product_prr_report').report_action(self, data=product_values)
    #     # return {
    #     #     "report_data": product_values,
    #     # }
