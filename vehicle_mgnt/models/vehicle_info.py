# -*- coding: utf-8 -*-

from flectra import api, fields, models

class VehicalData(models.Model):
    _name = "vehical.data"



    @api.multi
    @api.depends('customer_line')
    def _calculate_customers(self):
        for cust in self:
            print ("-----total customers-----", cust.customer_line)
            cust.total_buyers = len(cust.customer_line)

    name = fields.Char(string="Vehicle Name", size=30 , required=True)

    chasis_no = fields.Integer(string="CHASIS CODE",help="CHASIS_NO")
    is_availabe = fields.Boolean(string="vehicle available")
    vehical_img = fields.Binary(string="iamge",help="vehical image",)
    price = fields.Integer(string="Vehicle Price", size=10)
    assemble_on = fields.Date(string="vehicle assemble")
    model = fields.Integer(string="year model")
    type = fields.Selection([('bike', 'Bike'),
                             ('car', 'Car'),
                             ('bus', 'bus'),
                             ('truck', 'Truck'), ], string="Vehicle Type")

    warranty = fields.Selection([('one','1 Year'),
                                 ('two','2 year'),
                                 ('five','5 Year'),
                                 ('no','No Warranty'),],default="no", string="warranty")


    feul_type = fields.Selection([('petrol','Petrol'),
                                  ('diesel','Diesel'),
                                  ('both','Both'),],string="Fuel Type")
    customer_line = fields.One2many("customer.data","vehical_id", string="Aggrement with", readonly=True)

    feature_ids = fields.Many2many("feature.data", "vehical_feature_rel",
                                   "vehical_id", "feature_id", string="Feature")
    aggrement_date = fields.Date(string="First agreement date")

    total_buyers = fields.Integer(string="Total Buyers", compute=_calculate_customers, store=True)

    state = fields.Selection([
        ('confirm', 'Confirm'),
        ('pending', 'Pending')
    ], string='Status',  required=True, track_visibility='always', copy=False)

    def state_pending(self):
        self.state="pending"

    def state_confirm(self):
        self.state="confirm"