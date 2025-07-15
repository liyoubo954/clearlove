TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'lyb5201314',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                'echo': True
            }
        },
        'ddg_tenant_conn': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '172.16.105.132',
                'port': '3306',
                'user': 'ddg',
                'password': 'ddg.2021',
                'database': 'ddg_tenant',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                'echo': True
            }
        },
        'ecust_ddg_conn': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': '172.16.105.12',
                'port': '13366',
                'user': 'root',
                'password': '123456',
                'database': 'ecust_ddg',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb3',
                'echo': True
            }
        },
    },
    'apps': {
        'models': {
            'models': ['models', 'aerich.models'],
            'default_connection': 'default',
        },
        'ddg_models': {
            'models': ['ddg_models', 'daily_models'],
            'default_connection': 'ddg_tenant_conn',
        },
         'ecust_ddg_models': {
            'models': ['engineering_models','segment_models','project_stats_models','main_drive_models','risk_fault_models','shield_machine_models','shield_info_models','construction_progress_models','geology_data_models','disk_info_models','tunneling_instruction_models'],
            'default_connection': 'ecust_ddg_conn',
        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
