#!/usr/bin/python3

import sys, xml.etree.ElementTree as ET

xml = sys.argv[1]
variant_en = sys.argv[2]
variant_ru = sys.argv[3]
variant_ua = sys.argv[4]
output = sys.argv[5]


tree = ET.parse(xml)
root = tree.getroot()
for item in root.findall("./layoutList/layout"): 
    if (item.findtext("./configItem/name") == "us") and item.findtext("./configItem/shortDescription") == "en" and item.findtext("./configItem/languageList/iso639Id") == "eng":
        parent = item.find("./variantList")
        for otheritem in parent.findall('./variant'):
            if otheritem.findtext('./configItem/name') == 'typo-birman-en':
                parent.remove(otheritem)
        if parent:
            tree_en = ET.parse(variant_en)
            root_en = tree_en.getroot()
            parent.insert(0, root_en)
    if (item.findtext("./configItem/name") == "ru") and item.findtext("./configItem/shortDescription") == "ru" and item.findtext("./configItem/languageList/iso639Id") == "rus":
        parent = item.find("./variantList")
        for otheritem in parent.findall('./variant'):
            if otheritem.findtext('./configItem/name') == 'typo-birman-ru':
                parent.remove(otheritem)        
        if parent:
            tree_ru = ET.parse(variant_ru)
            root_ru = tree_ru.getroot()
            parent.insert(0, root_ru)
    if (item.findtext("./configItem/name") == "ua") and item.findtext("./configItem/shortDescription") == "ua" and item.findtext("./configItem/languageList/iso639Id") == "ukr":
        parent = item.find("./variantList")
        for otheritem in parent.findall('./variant'):
            if otheritem.findtext('./configItem/name') == 'typo-birman-ua':
                parent.remove(otheritem)
        if parent:
            tree_ua = ET.parse(variant_ua)
            root_ua = tree_ua.getroot()
            parent.insert(0, root_ua)
tree.write(output)
