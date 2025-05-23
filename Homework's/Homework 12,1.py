import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        first = html.find("<")

        while first != -1:
            first = html.find("<")
            second = html.find(">")
            html = html.replace(html[first:second + 1], "")

        x = html.splitlines()
        new_html = ""

        for i in x:
            if i.strip():
                new_html += i + "\n"


    with codecs.open(result_file, "w", "utf-8") as result:
        result.write(new_html)


delete_html_tags("../draft.html")