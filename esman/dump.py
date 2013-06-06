from __future__ import absolute_import
import json
from pyes.query import MatchAllQuery


def dump_docs(fp, conn, index_name, scroll='5m'):
    q = MatchAllQuery()
    for result in conn.search(q, scan=True, scroll=scroll):
        fp.write(json.dumps(result))
        fp.write('\n')
