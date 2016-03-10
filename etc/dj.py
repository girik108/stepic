CONFIG = {
    # 'mode': 'wsgi',
    'working_dir': '/home/box/web/ask/ask/',
    'python': '/usr/bin/python3',
    'args': (
        '--bind=127.0.0.1:8000',
        '--workers=4',
        '--timeout=60',
        'wsgi:application',
    ),
}
