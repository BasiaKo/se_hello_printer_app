import json
import lxml.etree
import lxml.builder

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result = format_to_xml(msg, imie)
    return result


def format_to_json(msg, imie):
    slownik={"imie":imie, "msg":msg}
    wynik=json.dumps(slownik)
    return wynik


def format_to_xml(msg, imie):
    E=lxml.builder.ElementMaker()
    root=E.greeting
    imieN=E.imie(imie)
    msgN=E.msg(msg)

    doc=root(imieN, msgN)
    wynik=lxml.etree.tostring(doc, pretty_print=True)
    return wynik


def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
