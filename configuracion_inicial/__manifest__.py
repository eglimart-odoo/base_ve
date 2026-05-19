{
    'name': 'Setup Venezuela SUMITIC',
    'version': '1.0',
    'summary': 'Configuración inicial de idioma y módulos para Venezuela',
    'depends': [
        'base',
        'sale_management',
        'stock',
        'account',
        'purchase',
        'contacts',
        'l10n_ve', # Esto instala el Plan de Cuentas de Venezuela
    ],
    'installable': True,
    'application': True,
}
