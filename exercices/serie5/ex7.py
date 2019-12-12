#!/usr/bin/python

def parse_query_string(url: str) -> dict:
    url_parameters = url[url.index("?")+1:]
    url_parameters = url_parameters.split("&")
    parameters_dict = {}
    for elmt in url_parameters:
        key, value = elmt.split("=")
        parameters_dict[key] = value
    return parameters_dict


url = input("Entrez un URL : ")
print(parse_query_string(url))
