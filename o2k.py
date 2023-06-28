# from openapi_parser import parse
import openapi_parser

specification = parse('swagger.yml')

urls = [x.url for x in specification.paths]

print(urls)