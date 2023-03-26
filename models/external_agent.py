from odoo import fields, models

class ExternalAgent(models.Model):
	_name = "external.agent"
	_description = "External Agents"
	_order = "name"

	name = fields.Char('Agent Name', required=True, translate=True)
	age = fields.Integer('Age', required=True)
	min_sales = fields.Integer('Minimum of sales', default=5)
	apply_rappel = fields.Boolean('Apply rappel', default=False)
	salary = fields.Float('Salary', required=False)
	