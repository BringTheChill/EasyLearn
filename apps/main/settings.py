import dj_database_url
import os
from os.path import join, normpath

APP_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(APP_DIR)
INSTALL_DIR = os.path.dirname(BASE_DIR)

STATIC_ROOT = join(INSTALL_DIR, 'www', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = join(INSTALL_DIR, 'www', 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'

CMS_TEMPLATES = (
    ('index.html', 'Homepage'),
    # ('page-right-sidebar.html', 'Right sidebar'),
    # ('contact.html', 'Contact'),
    # ('services.html', 'Servicii'),
)

CKEDITOR_SETTINGS = {
    'language': 'en',
    'toolbar': 'CMS',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Link', 'Unlink'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Link', 'Unlink'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'skin': 'moono-lisa',
    'toolbarCanCollapse': False,
    'entities': False,
    'entities_latin': False,
}

SITE_ID = 1

LANGUAGES = [
    ('en-us', 'English'),
]

STATICFILES_DIRS = (
    normpath(join(BASE_DIR, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    # 'djangocms_admin_style',
    'django.contrib.sites',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'constance',
    'captcha',
    'watson',
    'star_ratings',
    'students',
    # 'teachers',
    # 'djangocms_text_ckeditor',
    # 'djangocms_blog',
    # 'djangocms_link',
    # 'djangocms_file',
    # 'djangocms_picture',
    # 'djangocms_video',
    # 'djangocms_style',
    # 'taggit',
    # 'taggit_autosuggest',
    # 'cms',
    # 'menus',
    # 'treebeard',
    # 'sekizai',
    'easy_thumbnails',
    'filer',
    'mptt',
    'crispy_forms',
    'courses',
    'users',
]

# STAR_RATINGS_STAR_HEIGHT = 20

RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')

CACHE_URL = os.environ.get('CACHE_URL', "redis://localhost:6379/0")
CACHE_BACKEND = "django_redis.cache.RedisCache"
CACHE_PREFIX = 'easylearn'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_REDIS_CONNECTION = os.environ.get('CONSTANCE_REDIS_CONNECTION', CACHE_URL)
CONSTANCE_REDIS_PREFIX = 'constance:{}:'.format(CACHE_PREFIX)

CONSTANCE_CONFIG = {
    'ADRESA': ('Str.General Magheru, nr.33', 'Adresa de contact'),
    'TELEFON': ('0757657863', 'Telefon de contact'),
    'EMAIL': ('vflorinrobert@easylearn.ro', 'Email de contact'),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your_email@example.com')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 465)
EMAIL_SUBJECT_PREFIX = '[%s] ' % 'EASYLEARN'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = not EMAIL_USE_TLS
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SECURITY_EMAIL_SENDER = 'vflorinrobert@gmail.com'

AUTH_USER_MODEL = 'users.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    # 'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'watson.middleware.SearchContextMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'constance.context_processors.config',
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                'django.template.context_processors.csrf',
                'django.template.context_processors.request',
                "django.contrib.messages.context_processors.messages",
                # 'sekizai.context_processors.sekizai',
                # 'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
THUMBNAIL_DEBUG = DEBUG
FILER_SUBJECT_LOCATION_IMAGE_DEBUG = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

if DEBUG:
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
    INSTALLED_APPS += (
        'debug_toolbar',
        # 'debug_panel',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # 'debug_panel.middleware.DebugPanelMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
        'RESULTS_CACHE_SIZE': 200,
    }
    # Added cachalot panel
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        # 'haystack_panel.panel.HaystackDebugPanel',
        # 'cachalot.panels.CachalotPanel',
    ]

    # You may disable CMS caching
    # CMS_PAGE_CACHE = False
    # CMS_PLACEHOLDER_CACHE = False
    # CMS_PLUGIN_CACHE = False

    INTERNAL_IPS = ('127.0.0.1',)
    # for memcached
    # CACHES['debug-panel'] = {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': '127.0.0.1:11211',
    #     'KEY_PREFIX': 'prodeo',
    # }
