from django.urls import reverse_lazy

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = reverse_lazy(
#     "home:index")

# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = reverse_lazy(
#     "home:update-account"
# )

ACCOUNT_EMAIL_MAX_LENGTH = 40

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = ["none", "mandatory", "optional"][0]

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 900  # 15 minutes

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy("account_login")

ACCOUNT_PRESERVE_USERNAME_CASING = False

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_SIGNUP_REDIRECT_URL = reverse_lazy("books:book-list")

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_MIN_LENGTH = 5

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

ACCOUNT_FORMS = {
    'signup':'home.forms.SignupForm'
}

def ACCOUNT_USER_DISPLAY(user):
    """
    Override the default All auth display
    """
    return user.get_full_name() or user.email
