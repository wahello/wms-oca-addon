# Copyright 2020 Camptocamp
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _action_launch_stock_rule(self, previous_product_uom_qty=False):
        result = super()._action_launch_stock_rule(
            previous_product_uom_qty=previous_product_uom_qty
        )
        # As the user who confirms the order might not have access right to assign
        # a release channel, we use sudo here, to avoid errors
        pickings = self.move_ids.picking_id.sudo()
        # ensure we assign a channel on any picking OUT generated for the sale,
        # if moves are assigned to an existing transfer, we recompute the
        # channel
        pickings._delay_assign_release_channel()
        return result
