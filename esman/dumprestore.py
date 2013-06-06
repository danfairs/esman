from __future__ import absolute_import
import json
from pyes.query import MatchAllQuery


def dump_docs(fp, conn, index_name, doc_type, scroll='5m', encoding='utf8'):
    q = MatchAllQuery()
    for result in conn.search(q, indices=[index_name], doc_types=[doc_type],
                              scan=True, scroll=scroll):
        fp.write(json.dumps(result, encoding=encoding))
        fp.write('\n')


def restore_docs(fp, conn, index_name, doc_type, encoding='utf8'):
    for line in fp:
        doc = json.loads(line, encoding=encoding)
        conn.index(line.strip().decode(encoding), index_name, doc_type,
                   bulk=True, id=doc['_id'])
    conn.force_bulk()
