# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MedicalAppointment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date: DF.Date | None
		doctor: DF.Link | None
		doctor_name: DF.Data | None
		durationminutes: DF.Int
		notes: DF.LongText | None
		patient_id: DF.Link | None
		patient_name: DF.Data | None
		reason: DF.LongText | None
		status: DF.Literal["Scheduled", "Completed", "Cancelled", "No-Show"]
		time: DF.Time | None
	# end: auto-generated types
	pass
