# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


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

@frappe.whitelist(allow_guest=True)
def get_user_details(id_token, password):
    try:
        from firebase_admin import auth
        import firebase_admin
        from firebase_admin import credentials
        from frappe.auth import LoginManager
        if not firebase_admin._apps:
            cred = credentials.Certificate("/Users/user/w-saas/frappe-bench/sites/firebase_service_account.json")
            firebase_admin.initialize_app(cred)
        # 1. Verify Firebase Token
        decoded_token = auth.verify_id_token(id_token)
        email = decoded_token.get('email')

        if not email:
            frappe.throw(_("No email in Firebase token"))

        # 2. Lookup User
        user = frappe.get_value("User", {"email": email})
        if not user:
            frappe.throw(_("No matching user found in Frappe for this email"))


        # 3. Validate password
        login_manager = LoginManager()
        login_manager.authenticate(user=user, pwd=password)
        login_manager.post_login()
        sid = frappe.local.session.sid
        # frappe.set_user(user)

        return {
            "message": "Login successful",
            "sid": sid,
            "user": frappe.session.user
        }

    except Exception as e:
        frappe.log_error(str(e), "Double Login Failed")
        frappe.throw(_("Authentication failed: ") + str(e))
