# coding: utf-8

# flake8: noqa

"""
    Avaza API Documentation

    Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from avazacli.api.account_api import AccountApi
from avazacli.api.company_api import CompanyApi
from avazacli.api.contact_api import ContactApi
from avazacli.api.credit_note_api import CreditNoteApi
from avazacli.api.currency_api import CurrencyApi
from avazacli.api.estimate_api import EstimateApi
from avazacli.api.expense_api import ExpenseApi
from avazacli.api.inventory_api import InventoryApi
from avazacli.api.invoice_api import InvoiceApi
from avazacli.api.payment_api import PaymentApi
from avazacli.api.project_api import ProjectApi
from avazacli.api.project_timesheet_category_api import ProjectTimesheetCategoryApi
from avazacli.api.schedule_assignment_api import ScheduleAssignmentApi
from avazacli.api.schedule_series_api import ScheduleSeriesApi
from avazacli.api.section_api import SectionApi
from avazacli.api.task_api import TaskApi
from avazacli.api.tax_api import TaxApi
from avazacli.api.timesheet_api import TimesheetApi
from avazacli.api.timesheet_submission_api import TimesheetSubmissionApi
from avazacli.api.timesheet_timer_api import TimesheetTimerApi
from avazacli.api.user_profile_api import UserProfileApi
from avazacli.api.webhook_api import WebhookApi

# import ApiClient
from avazacli.api_client import ApiClient
from avazacli.configuration import Configuration
# import models into sdk package
from avazacli.models.account_details import AccountDetails
from avazacli.models.company import Company
from avazacli.models.company_contact import CompanyContact
from avazacli.models.company_list import CompanyList
from avazacli.models.contact_list import ContactList
from avazacli.models.create_subscription import CreateSubscription
from avazacli.models.credit_note import CreditNote
from avazacli.models.credit_note_allocation import CreditNoteAllocation
from avazacli.models.credit_note_line_item import CreditNoteLineItem
from avazacli.models.credit_note_list import CreditNoteList
from avazacli.models.currency import Currency
from avazacli.models.currency_list import CurrencyList
from avazacli.models.estimate_details import EstimateDetails
from avazacli.models.estimate_line_item_details import EstimateLineItemDetails
from avazacli.models.estimate_links import EstimateLinks
from avazacli.models.estimate_list import EstimateList
from avazacli.models.expense_details import ExpenseDetails
from avazacli.models.expense_list import ExpenseList
from avazacli.models.inventory_item import InventoryItem
from avazacli.models.inventory_list import InventoryList
from avazacli.models.invoice import Invoice
from avazacli.models.invoice_line_item import InvoiceLineItem
from avazacli.models.invoice_links import InvoiceLinks
from avazacli.models.invoice_list import InvoiceList
from avazacli.models.issuer_details import IssuerDetails
from avazacli.models.new_company import NewCompany
from avazacli.models.new_company_contact import NewCompanyContact
from avazacli.models.new_expense import NewExpense
from avazacli.models.new_invoice import NewInvoice
from avazacli.models.new_invoice_line_item import NewInvoiceLineItem
from avazacli.models.new_payment import NewPayment
from avazacli.models.new_payment_allocation import NewPaymentAllocation
from avazacli.models.new_project_model import NewProjectModel
from avazacli.models.new_section import NewSection
from avazacli.models.new_tag import NewTag
from avazacli.models.new_task import NewTask
from avazacli.models.new_timesheet import NewTimesheet
from avazacli.models.payment import Payment
from avazacli.models.payment_allocation import PaymentAllocation
from avazacli.models.payment_list import PaymentList
from avazacli.models.project_details import ProjectDetails
from avazacli.models.project_list import ProjectList
from avazacli.models.project_list_details import ProjectListDetails
from avazacli.models.project_member_details import ProjectMemberDetails
from avazacli.models.project_section_details import ProjectSectionDetails
from avazacli.models.project_tag_item import ProjectTagItem
from avazacli.models.project_timesheet_category_details import ProjectTimesheetCategoryDetails
from avazacli.models.project_timesheet_category_list import ProjectTimesheetCategoryList
from avazacli.models.recipient_details import RecipientDetails
from avazacli.models.role_details import RoleDetails
from avazacli.models.schedule_assignment_details import ScheduleAssignmentDetails
from avazacli.models.schedule_assignment_list import ScheduleAssignmentList
from avazacli.models.schedule_series_details import ScheduleSeriesDetails
from avazacli.models.schedule_series_list import ScheduleSeriesList
from avazacli.models.section_details import SectionDetails
from avazacli.models.section_list import SectionList
from avazacli.models.subscribe_result import SubscribeResult
from avazacli.models.tag_item import TagItem
from avazacli.models.task_details import TaskDetails
from avazacli.models.task_list import TaskList
from avazacli.models.tax_component import TaxComponent
from avazacli.models.tax_item import TaxItem
from avazacli.models.tax_list import TaxList
from avazacli.models.timesheet_details import TimesheetDetails
from avazacli.models.timesheet_list import TimesheetList
from avazacli.models.update_company import UpdateCompany
from avazacli.models.update_task import UpdateTask
from avazacli.models.update_timesheet_model import UpdateTimesheetModel
from avazacli.models.user_details import UserDetails
from avazacli.models.user_list import UserList
from avazacli.models.user_tag_details import UserTagDetails
from avazacli.models.webhook_details import WebhookDetails
from avazacli.models.webhook_list import WebhookList
