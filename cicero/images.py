import re


def expand_img_link(s, prefix):

    if "![" in s and "](" in s:
        if "http" not in s:
            p = re.compile(r"!\[(.*)\]\(")
            alt = p.findall(s)[0]
            p = re.compile(r'!\[.*\]\(([^")]+)')
            src = p.findall(s)[0]
            return "![{0}]({1}{2})\n".format(alt, prefix, src)

    if "<img" in s and 'src="' in s:
        if "http" not in s:
            p = re.compile(r'<img [^>]*src="([^"]+)')
            src = p.findall(s)[0]
            return s.replace(src, prefix + src)

    if "<source" in s and 'src="' in s:
        if "http" not in s:
            p = re.compile(r'<source [^>]*src="([^"]+)')
            src = p.findall(s)[0]
            return s.replace(src, prefix + src)

    if "background-image: url(" in s:
        if "http" not in s:
            p = re.compile(r'background-image: url\(([^")]+)')
            src = p.findall(s)[0]
            return s.replace(src, prefix + src)

    return s


def test_expand_img_link():
    assert (
        expand_img_link("![Raboof](img/pie.jpg)", "foo/")
        == "![Raboof](foo/img/pie.jpg)\n"
    )
    assert (
        expand_img_link("![Foo oof 123](img/pie.jpg)", "http://")
        == "![Foo oof 123](http://img/pie.jpg)\n"
    )
    assert expand_img_link("[Raboof](img/pie.jpg)", "foo/") == "[Raboof](img/pie.jpg)"
    assert expand_img_link("img src", "foo/") == "img src"
    assert (
        expand_img_link('<img src="img/phd_final.gif" style="width: 400px;"/>', "foo/")
        == '<img src="foo/img/phd_final.gif" style="width: 400px;"/>'
    )
    assert (
        expand_img_link('<source src="img/cat.mp4" type="video/mp4">', "foo/")
        == '<source src="foo/img/cat.mp4" type="video/mp4">'
    )
    assert (
        expand_img_link("background-image: url(foo.png)", "bar/")
        == "background-image: url(bar/foo.png)"
    )


def fix_images(s, prefix):
    return "\n".join([expand_img_link(line, prefix) for line in s.split("\n")])
