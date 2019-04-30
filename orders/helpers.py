# -*- coding: utf-8 -*-
from django.conf import settings


def get_first_grouped_items(cls, params, from_idx=0, n=7):
    is_sqlite = settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3'
    if is_sqlite:
        query = 'SELECT GROUP_CONCAT(id, ",") AS id FROM {table} GROUP BY user_id, born ORDER BY born DESC'.format(
            table=cls._meta.db_table)
    else:
        query = 'SELECT array_agg(id) AS id FROM {table} GROUP BY user_id, born ORDER BY born DESC'.format(
            table=cls._meta.db_table)

    filters = params.get('filters', {})
    excludes = params.get('excludes', {})
    raw = cls.objects.filter(**filters).exclude(**excludes).raw(query)

    if is_sqlite:
        ids = [str(i.id) for i in raw]
        all_len = len(ids)
        ids = ids[from_idx:from_idx + n]
        pks = [pk for pk in ','.join(ids).split(',') if pk]
    else:
        ids = [o.id for o in raw]
        all_len = len(ids)
        ids = ids[from_idx:from_idx + n]
        pks = []
        for i in ids:
            pks.extend(i)

    return cls.objects.filter(id__in=pks), all_len

