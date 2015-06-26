# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:10:58 2015

@author: pietro
"""
from __future__ import print_function
from pprint import pprint
# https://trac.osgeo.org/grass/browser/grass/trunk/lib/gis/parser_standard_options.c?format=txt


def parse_options(lines):
    def split_in_groups(lines):
        def count_par_diff(line):
            open_par = line.count('(')
            close_par = line.count(')')
            return open_par - close_par
        res = None
        diff = 0
        for line in lines:
            if line.startswith('case'):
                optname = line.split()[1][:-1]
                res = []
            elif line == 'break;':
                yield optname, res
            elif line.startswith('G_'):
                diff = count_par_diff(line)
            elif diff > 0:
                diff -= count_par_diff(line)
            else:
                res.append(line) if res is not None else None

    def split_opt_line(line):
        index = line.index('=')
        key = line[:index].strip()
        default = line[index + 1:].strip()
        if default.startswith('_('):
            default = default[2:]
        #print(line, '=>', key, ':', default)
        return key, default

    def parse_glines(glines):
        res = {}
        key = None
        for line in glines:
            if line.startswith('/*'):
                continue
            if line.startswith('Opt') and line.endswith(';'):
                key, default = [w.strip() for w in split_opt_line(line[5:])]
                res[key] = default
            elif line.startswith('Opt'):
                key, default = split_opt_line(line[5:])
                res[key] = [default, ]
            else:
                if key is not None:
                    if key not in res:
                        res[key] = []
                    start, end = 0, -1
                    if line.startswith('_('):
                        start = 2
                    if line.endswith(');'):
                        end = -3
                    elif line.endswith(';'):
                        end = -2
                    #print(line, '=>', key, ':', line[start:end])
                    res[key].append(line[start:end])
        #pprint(res)
        return res

    def clean_value(val):
        if isinstance(val, list):
            val = ' '.join(val)
        return val.replace('"', '').replace("\'", "'").strip().strip(';').strip().strip('_(').strip().strip(')').strip()


    # with open(optionfile, mode='r') as optfile:
    lines = [line.strip() for line in lines]
    result = []
    for optname, glines in split_in_groups(lines):
        if glines is not None:
            #import ipdb; ipdb.set_trace()
            res = parse_glines(glines)
            # clean description
            for key, val in res.items():
                res[key] = clean_value(val)
            result.append((optname, res))
    return result


class OptTable(object):
    """"""
    def __init__(self, list_of_dict):
        self.options = list_of_dict
        self.columns = sorted(set([key for _, d in self.options
                                   for key in d.keys()]))

    def _repr_html_(self):
        html = ["<table>"]
        # write headers
        html.append("<tr>")
        html.append("<td>{0}</td>".format('option'))
        for col in self.columns:
            html.append("<td>{0}</td>".format(col))
        html.append("</tr>")
        for optname, options in self.options:
            html.append("<tr>")
            html.append("<td>{0}</td>".format(optname))
            for col in self.columns:
                html.append("<td>{0}</td>".format(options.get(col, '')))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)


with open('parser_standard_options.txt', mode='r') as cfile:
    options = OptTable(parse_options(cfile.readlines()))

