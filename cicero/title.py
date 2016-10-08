def extract_title(markdown):
    for line in markdown.split('\n'):
        if '#' in line:
            index_first_non_whitespace = len(line) - len(line.lstrip())
            index_first_hash = line.index('#')
            first_alpha = list(filter(str.isalpha, str(line)))[0]
            index_first_alpha = line.index(first_alpha)
            if index_first_non_whitespace == index_first_hash:
                return line[index_first_alpha:]
    # we found nothing, we default to this
    return 'cicero.xyz'


def test_extract_title():
    markdown = '''name: inverse
    layout: true
    class: center, middle, inverse

    ---

    # Talking to C/C++/Fortran via CFFI

    ## Radovan Bast

    High Performance Computing Group,
    UiT The Arctic University of Norway

    Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
    Code examples: [OSI](http://opensource.org)-approved [MIT license](http://opensource.org/licenses/mit-license.html).

    ---'''
    assert extract_title(markdown) == 'Talking to C/C++/Fortran via CFFI'
