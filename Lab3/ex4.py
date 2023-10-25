def build_xml_element(tag, content, **dt):
    html = "<" + tag
    for x in dt.items():
        html += " " + x[0] + "=" + '"' + x[1] + '"'
    html += "> " + content + " </" + tag + ">"
    return html


print(build_xml_element("a", "Hello there", href ="http://python.org", _class ="my-link", id= "someid"))