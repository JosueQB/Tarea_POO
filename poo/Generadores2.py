# """
# def devuelveLenguajes(*lenguajes):
#     for leng in lenguajes:
#         yield leng
# """

def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng

