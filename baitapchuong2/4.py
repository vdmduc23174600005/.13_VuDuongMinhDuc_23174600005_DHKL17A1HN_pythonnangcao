import xml.dom.minidom

def parse_xml():
    doc = xml.dom.minidom.parse("sample.xml")

    print(doc.toprettyxml())

parse_xml()