#!/usr/bin/python3
"""Module task_03_xml: Define Serializing and deserializing with XML"""



import xml.etree.cElementTree as ET


def serialize_to_xml(dictionary, filename):
    """create racine element"""
    boot = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(boot, key)
        child.text = str(value)
        
    tree = ET.ElementTree(boot)
    with open(filename, "wb") as xml_file:
        tree.write(xml_file)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    boot = tree.getroot()
    
    dictionary = {}
    
    for child in boot:
        dictionary[child.tag] = child.text
        
    return dictionary