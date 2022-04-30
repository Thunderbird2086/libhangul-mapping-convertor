# -*- coding: utf-8 -*-
'''libhangul mapping convertor
'''

import argparse
import os
import pathlib
import sys
import xml.etree.ElementTree as ET
import yaml


def get_args():
    """parsing arguments
    """
    parser = argparse.ArgumentParser(
            "Keyboard mapping convertor for libhangul")
    parser.add_argument('--config', '-c',
                        # type=argparse.FileType('r'),
                        default='config.yaml',
                        help="mapping confiiguration")
    parser.add_argument('--in_path' , '-i',
                        type=pathlib.Path,
                        default='./',
                        help="path for input files")
    parser.add_argument('--out_path', '-o',
                        type=pathlib.Path,
                        default='./',
                        help="path for output files")


    return parser.parse_args()


def _expand_eliments(eliments):
    eliments = list(eliments)
    eliments.extend([elem.upper() for elem in eliments])
    
    return eliments


def _update_mapping(mapping):
    keys = _expand_eliments(mapping.keys())
    values = _expand_eliments(mapping.values())

    return dict(zip([hex(ord(k)) for k in keys],
                    [hex(ord(v)) for v in values]))


_CONVERTED = 'converted'

def convert(name, mapping, targets, in_path, out_path):
    """convert mappings"""
    mapping = _update_mapping(mapping)

    for xml_file in targets:
        in_file = os.path.join(in_path, xml_file)
        tree = ET.parse(in_file)

        root = tree.getroot()
        if _CONVERTED in root.keys():
            print("'{}' is already converted for '{}'".format(
                  in_file, root.get(_CONVERTED)))
            continue

        root.set(_CONVERTED, name)

        for item in root.iter('item'):
            key = item.attrib['key']
            if key in mapping.keys():
                item.attrib['key'] = mapping[key]

        tree.write(os.path.join(out_path, xml_file), encoding='utf-8',
                   xml_declaration=True)
            

def main(name, conversions, in_path, out_path):
    for conv in conversions:
        convert(name, conv['mapping'], conv['targets'], in_path, out_path)


if __name__ == '__main__':
    ARGS = get_args()

    with open(ARGS.config) as yml:
        config = yaml.safe_load(yml)

    main(config['name'], config['conversions'], ARGS.in_path, ARGS.out_path)
