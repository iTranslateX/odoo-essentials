from odoo import api, fields, models, exceptions


class Checkout(models.Model):
    _name = "library.checkout"
    _description = "Checkout Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    member_id = fields.Many2one(
        "library.member",
        required=True,
    )
    user_id = fields.Many2one(
        "res.users",
        "Librarian",
        default=lambda s: s.env.user,
    )
    request_date = fields.Date(
        default=lambda s: fields.Date.today(),
        compute="_compute_request_date_onchange",
        store=True,
        readonly=False,
    )
    line_ids = fields.One2many(
        'library.checkout.line',
        'checkout_id',
        string="Borrowed Books",
    )

    @api.model
    def _default_stage_id(self):
        Stage = self.env["library.checkout.stage"]
        return Stage.search([("state", "=", "new")], limit=1)
    stage_id = fields.Many2one(
        "library.checkout.stage",
        default=_default_stage_id,
        group_expand="_group_expand_stage_id")
    state = fields.Selection(related="stage_id.state")
    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(readonly=True)

    @api.depends("member_id")
    def _compute_request_date_onchange(self):
        today_date = fields.Date.today()
        if self.request_date != today_date:
            self.request_date = today_date
            return {
                "warning": {
                    "title": "Changed Request Date",
                    "message": "Request date changed to today!",
                }
            }

    # @api.onchange("member_id")
    # def onchange_member_id(self):
    #     today_date = fields.Date.today()
    #     if self.request_date != today_date:
    #         self.request_date = today_date
    #         return {
    #             "warning": {
    #                 "title": "Changed Request Date",
    #                 "message": "Request date changed to today!",
    #             }
    #         }

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    @api.model
    def create(self, vals):
        # 创建前执行的代码，应使用vals字典
        new_record = super().create(vals)
        # 创建后执行的代码，应使用new_record
        if new_record.stage_id.state in ('open', 'close'):
            raise exceptions.UserError("State not allowed for new checkouts.")
        return  new_record

    def write(self, vals):
        # 写入之前的代码，self为老值
        if "stage_id" in vals:
            Stage = self.env["library.checkout.stage"]
            old_state = self.stage_id.state
            new_state = Stage.browse(vals["stage_id"]).state
            if new_state != old_state and new_state == "open":
                vals["checkout_date"] = fields.Date.today()
            if new_state != old_state and new_state == "done":
                vals["close_date"] = fields.Date.today()
        # old_state = self.stage_id.state
        super().write(vals)
        # 写入之后的代码，可使用更新后的self
        # new_state = self.stage_id.state
        # if not self.env.context.get("_checkout_write"):
        #     if new_state != old_state and new_state == "open":
        #         self.with_context(_checkout_write=True).write(
        #             {"checkout_date": fields.Date.today()})
        #     if new_state != old_state and new_state == "done":
        #         self.with_context(_checkout_write=True).write(
        #             {"close_date": fields.Date.today()})
        return True

