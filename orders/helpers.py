# -*- coding: utf-8 -*-
from django.conf import settings


def get_first_grouped_items(cls, id__in, from_idx=0, n=7):
    is_sqlite = settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3'
    if is_sqlite:
        query = 'SELECT GROUP_CONCAT(id, ",") AS id FROM {table} GROUP BY user_id, born ORDER BY born DESC'.format(
            table=cls._meta.db_table)
    else:
        query = 'SELECT array_agg(id) AS id FROM {table} GROUP BY user_id, born ORDER BY born DESC'.format(
            table=cls._meta.db_table)

    raw_query = cls.objects.raw(query)

    if is_sqlite:
        rows = [str(o.id).split(',') for o in raw_query]
    else:
        rows = [o.id for o in raw_query]

    ids = []
    for row in rows:
        _ids = [int(idx) for idx in row if int(idx) in id__in]
        if len(_ids):
            ids.append(_ids)
    all_len = len(ids)
    ids = ids[from_idx:from_idx + n]
    pks = []
    for i in ids:
        pks.extend(i)

    return cls.objects.filter(id__in=pks).order_by('-born'), all_len
