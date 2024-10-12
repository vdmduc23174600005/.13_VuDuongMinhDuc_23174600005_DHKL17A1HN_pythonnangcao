import xml.dom.minidom

def parse_and_print_elements():
    doc = xml.dom.minidom.parse("sample.xml")

    staff_elements = doc.getElementsByTagName("staff")

    for staff in staff_elements:
        name = staff.getElementsByTagName("name")[0].childNodes[0].data
        print(f"Staff Name: {name}")

parse_and_print_elements()