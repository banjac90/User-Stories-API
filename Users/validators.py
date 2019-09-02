import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
#password validators
class NumberValidator(object):
	def validate(self, password, user=None):
		if not re.findall('\d', password):
			raise ValidationError(_("The password must contain at least 1 digit"), code='password_no_number',)

	def get_help_text(self):
		return _("The password must contain at least 1 digit")


class UpercaseValidator(object):
	def validate(self, password, user=None):
		if not re.findall('[A-Z]', password):
			raise ValidationError(_("The password must contain at least 1 uppercase letter"), code='password_no_upper',)

	def get_help_text(self):
		return _("The password must contain at least 1 upercase letter")


class SymbolValidator(object):
	def validate(self, password, user=None):
		if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
			raise ValidationError(_("The password must contain at least 1 symbol"), code='password_no_symbol',)

	def get_help_text(self):
		return _("The password must contain at least 1 symbol")
