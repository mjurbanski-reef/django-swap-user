from django.conf import settings as django_settings
from django.utils.module_loading import import_string


#
# Mostly inspired by `rest_framework.settings`
#

IMPORT_SETTINGS = [
    "OTP_SENDER_CLASS",
    "GET_OTP_SERVICE_CLASS",
    "CHECK_OTP_SERVICE_CLASS",
]
DEFAULT_SETTINGS = {
    "OTP_SENDER_CLASS": "swap_user.otp_senders.StdOutOTPSender",
    "GET_OTP_SERVICE_CLASS": "swap_user.services.GetOTPService",
    "CHECK_OTP_SERVICE_CLASS": "swap_user.services.CheckOTPService",
    "OTP_PATTERN": "user:otp:{user_id}",
    "OTP_TIMEOUT": 60,
    "OTP_ALPHABET": "0123456789",
    "OTP_LENGTH": 5,
}
NAMESPACE = "SWAP_USER"

# Add default values and create working mapping
MAPPING = {
    "A": "PHONENUMBER_DB_FORMAT",
    "B": "PHONENUMBER_DEFAULT_REGION",
    "C": "PHONENUMBER_DEFAULT_FORMAT",
}


class SwapUserSettings:
    """
    Settings object mostly inspired from `rest_framework.settings`.
    """

    def make_import(self, item, path):
        val = import_string(path)
        setattr(self, item, val)

        return val

    def __getattr__(self, item):
        try:
            namespaced_settings = getattr(django_settings, NAMESPACE)
            value = namespaced_settings[item]
        except (AttributeError, KeyError):
            value = DEFAULT_SETTINGS[item]

        if item in IMPORT_SETTINGS:
            value = self.make_import(item, value)

        return value


swap_user_settings = SwapUserSettings()
