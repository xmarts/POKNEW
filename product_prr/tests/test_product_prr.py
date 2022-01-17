# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged


@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(EstateTestCase, cls).setUpClass()
        cls.properties = cls.env['estate.property'].create([...])

    def test_creation_area(self):
        """Test that the total_area is computed like it should."""
        self.properties.living_area = 20
        self.assertRecordValues(self.properties, [
           {'name': ..., 'total_area': ...},
           {'name': ..., 'total_area': ...},
        ])