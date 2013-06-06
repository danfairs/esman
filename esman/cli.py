from __future__ import absolute_import
import argparse
import pyes
import sys
from .dumprestore import dump_docs, restore_docs


def dump(conn, args):
    return dump_docs(sys.stdout, conn, args.index, args.doc_type,
                     encoding=args.encoding)


def restore(conn, args):
    return restore_docs(sys.stdin, conn, args.index, args.doc_type,
                        encoding=args.encoding)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--es', dest='es', help='ES URL',
                        default='http://localhost:9200/')
    subparsers = parser.add_subparsers()

    dump_parser = subparsers.add_parser('dump')
    dump_parser.add_argument('index', type=str)
    dump_parser.add_argument('doc_type', type=str)
    dump_parser.add_argument('--encoding', dest='encoding', default='utf8')
    dump_parser.set_defaults(func=dump)

    restore_parser = subparsers.add_parser('restore')
    restore_parser.add_argument('index', type=str)
    restore_parser.add_argument('doc_type', type=str)
    restore_parser.add_argument('--encoding', dest='encoding', default='utf8')
    restore_parser.set_defaults(func=restore)

    args = parser.parse_args()
    conn = pyes.ES(args.es)

    args.func(conn, args)
