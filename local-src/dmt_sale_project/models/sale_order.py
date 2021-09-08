# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_id = fields.Many2one(
        'project.project',
        'Project',
        readonly=False,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain=[('allow_billable', '=', True)],
        help='Select a non billable project on which tasks can be created.',
    )

    @api.depends()
    def _compute_visible_project(self):
        """ User wants the project to be visible in all time.
        So we force this value independently from the parent's one """
        for order in self:
            order.visible_project = True
