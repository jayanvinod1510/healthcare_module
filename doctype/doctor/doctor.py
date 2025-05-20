# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Doctor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.healthcare_management.doctype.doctor_available_days.doctor_available_days import DoctorAvailableDays
		from frappe.types import DF

		additional_info: DF.LongText | None
		available_days: DF.TableMultiSelect[DoctorAvailableDays]
		available_hours: DF.Int
		doctor_name: DF.Data | None
		email: DF.Data | None
		is_active: DF.Check
		mobile_number: DF.Data | None
		qualification: DF.Data | None
		specialization: DF.Literal["Cardiologist", "Dentist"]
	# end: auto-generated types
	pass

@frappe.whitelist()
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:49430'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type, X-Requested-With'
    return response

# after_request = [add_cors_headers]

@frappe.whitelist(allow_guest=True)
def custom_login(usr, pwd):
    from frappe.auth import LoginManager
    try:
        # Authenticate using Frappe's LoginManager
        login_manager = LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()

        # Get the session ID (sid) from Frappe's session
        sid = frappe.local.session.sid

        # Return the session ID and user information
        return {
            "message": "Login successful",
            "sid": sid,
            "user": frappe.session.user
        }

    except frappe.AuthenticationError:
        frappe.clear_messages()
        return {
            "message": "Login failed",
            "error": "Invalid username or password"
        }
