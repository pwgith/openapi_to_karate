# from openapi_parser import parse

# specification = parse('petstore.yaml')

# for path in specification.paths:
#     supported_methods = ','.join([x.method.value for x in path.operations])

#     print(f"Operation: {path.url}, methods: {supported_methods}")

from pprint import pprint
from prance import ResolvingParser
# parser = ResolvingParser('petstore.yaml')
parser = ResolvingParser('petstore.yaml')
parser.specification  # contains fully resolved specs as a dict
# pprint(parser.specification["paths"])
class Items:
    def __init__(self, items_data):
        self.required = items_data.get("required", None)
        self.type = items_data.get("type", None)
        self.xml = items_data.get("xml", None)
        if self.xml is not None:
            self.xml = XML(self.xml)
        properties_data = items_data.get("properties", None)
        self.properties = []
        if properties_data is not None:
            for property_name, property_data in properties_data.items():
                self.properties.append(Property(property_name, property_data))
        if "required" in items_data:
            del items_data["required"]
        if "type" in items_data:
            del items_data["type"]
        if "xml" in items_data:
            del items_data["xml"]
        if "properties" in items_data:
            del items_data["properties"]

        self.left_overs = items_data



    def dump(self):
        print("                Items:")
        print("                  Required: ", self.required)
        print("                  Type: ", self.type)
        if len(self.left_overs) > 0:
            print("                  Hmmm:", self.left_overs)
        if self.xml is not None:
            self.xml.dump()
        if self.properties is not None:
            for property in self.properties:
                property.dump()


class XML:
    def __init__(self, xml_data):
        self.name = xml_data.get("name", "No Name")
        self.wrapped = xml_data.get("wrapped", "No Wrapped")

        if "wrapped" in xml_data:
            del xml_data["wrapped"]
        if "name" in xml_data:
            del xml_data["name"]
        self.extra = xml_data


    def dump(self):
        print("            XML:")
        print("              Name: ", self.name)
        print("              Wrapped: ", self.wrapped)
        if len(self.extra) > 0:
            print("              Hmmm: ", self.extra)

class Property:
    def __init__(self, property_name, property_data) -> None:
        self.required = False
        self.property_name = property_name
        self.type = property_data.get("type", "No Type")
        self.format = property_data.get("format", "No Format")
        self.example = property_data.get("example", "No Example")
        self.description = property_data.get("description", "No Description")
        self.enum = property_data.get("enum", [])
        self.xml = property_data.get("xml", None)
        self.items = property_data.get("items", None)
        properties_data = property_data.get("properties", None)
        self.properties = None
        if properties_data is not None:
            self.properties = []
            for sub_property_name, sub_property_data in properties_data.items():
                self.properties.append(Property(sub_property_name, sub_property_data))
        if self.items is not None:
            self.items = Items(self.items)
        if self.xml is not None:
            self.xml = XML(self.xml)
        if "type" in property_data:
            del property_data["type"]
        if "format" in property_data:
            del property_data["format"]
        if "example" in property_data:
            del property_data["example"]
        if "description" in property_data:
            del property_data["description"]
        if "enum" in property_data:
            del property_data["enum"]
        if "xml" in property_data:
            del property_data["xml"]
        if "items" in property_data:
            del property_data["items"]
        if "properties" in property_data:
            del property_data["properties"]
        self.left_overs = property_data

    def set_required(self, required_list):
        if self.property_name in required_list:
            self.required = True


    def dump(self):
        print("             Property:")
        print("               Name:", self.property_name)
        print("               Type:", self.type)
        print("               Format:", self.format)
        print("               Example:", self.example)
        print("               Description:", self.description)
        print("               Enum:", self.enum)
        print("               Required:", self.required)
        if len(self.left_overs.keys()) > 0:
            print("               Hmmm:", self.left_overs)
        if self.xml is not None:
            self.xml.dump()
        if self.items is not None:
            self.items.dump()
        if self.properties is not None:
            for property in self.properties:
                property.dump()

class JsonSchema:
    def __init__(self, json_schema_data):
        self.required = json_schema_data.get("required", None)
        self.type = json_schema_data.get("type", None)
        self.xml = json_schema_data.get("xml", None)
        if self.xml is not None:
            self.xml = XML(self.xml)
        properties_data = json_schema_data.get("properties", None)
        self.properties = []
        if properties_data is not None:
            for property_name, property_data in properties_data.items():
                self.properties.append(Property(property_name, property_data))
        if self.required is not None:
            for property in self.properties:
                property.set_required(self.required)
    


    def dump(self):
        print("          JSON Schema:")
        print("          Required: ", self.required)
        print("          type: ", self.type)
        if self.xml is not None:
            self.xml.dump()
        if self.properties is not None:
            for property in self.properties:
                property.dump()

class RequestBody:
    def __init__(self, request_body_data):
        # print(request_body_data.keys())
        self.description = request_body_data.get("description", "No Description")
        self.content = request_body_data.get("content", None)
        self.required = request_body_data.get("required", None)
        self.json_schema = self.content.get("application/json", None)
        if self.json_schema is not None:
            self.json_schema = self.json_schema.get("schema", None)
            if self.json_schema is not None:
                self.json_schema = JsonSchema(self.json_schema) 

        if "description" in request_body_data:
            del request_body_data["description"]
        if "content" in request_body_data:
            del request_body_data["content"]
        if "required" in request_body_data:
            del request_body_data["required"]
        if "application/json" in request_body_data:
            del request_body_data["application/json"]
        if "xml" in request_body_data:
            del request_body_data["xml"]
        self.extras = None
        if len(request_body_data.keys()) > 0:
            self.extras = request_body_data

    def dump(self):
        print("     Body: ")
        print("       Description: ", self.description)
        print("       Required: ", self.required)
        if self.json_schema is not None:
            self.json_schema.dump()
        if self.extras is not None:
            print("       Hmmm: ", self.extras)

class Schema:
    def __init__(self, schema_data):
        self.default = schema_data.get("default", "No Default")
        self.enum = schema_data.get("enum", None)
        self.type = schema_data.get("type", "No Type")
        self.format = schema_data.get("format", "No Format")
        self.items = schema_data.get("items", "No Items")

        if "default" in schema_data:
            del schema_data["default"]
        if "enum" in schema_data:
            del schema_data["enum"]
        if "type" in schema_data:
            del schema_data["type"]
        if "format" in schema_data:
            del schema_data["format"]
        if "items" in schema_data:
            del schema_data["items"]
        self.extras = schema_data

    def dump(self):
        print("        Schema")
        print("         Default: ", self.default)
        print("         Enum: ", self.enum)
        print("         Type: ", self.type)
        if len(self.extras) > 0:
            print("         Hmmm: ", self.extras)


class Parameter:
    def __init__(self, parameter_data):
        self.name = parameter_data.get("name", "No Name")
        self.description = parameter_data.get("name", "No Description")
        self.explode = parameter_data.get("explode", "No Explode")
        self.parameter_in = parameter_data.get("in", "No In")
        self.required = parameter_data.get("required", "No Required")
        self.schema = parameter_data.get("schema", None)
        if self.schema is not None:
            self.schema = Schema(self.schema)

        if "name" in parameter_data:
            del parameter_data["name"]
        if "description" in parameter_data:
            del parameter_data["description"]
        if "explode" in parameter_data:
            del parameter_data["explode"]
        if "in" in parameter_data:
            del parameter_data["in"]
        if "required" in parameter_data:
            del parameter_data["required"]
        if "schema" in parameter_data:
            del parameter_data["schema"]
        self.extras = parameter_data

    def dump(self):
        print("     Parameter")
        print("      Name: ", self.name)
        print("      Description: ", self.description)
        print("      Explode: ", self.explode)
        print("      In: ", self.parameter_in)
        print("      Required: ", self.required)
        if self.schema is not None:
            self.schema.dump()
        if len(self.extras) > 0:
            print("      Hmmm: ", self.extras)


class Method:
    def __init__(self, method_name, method_data):
        self.method_name = method_name
        self.tags = method_data.get("tags", "No Tags")
        self.summary = method_data.get("summary", "No Summary")
        self.description = method_data.get("description", "No Description")
        self.operation_id = method_data.get("operationId", "No Operation Id")
        self.request_body = method_data.get("requestBody", None)
        if self.request_body is not None:
            self.request_body = RequestBody(self.request_body)
        self.responses = method_data.get("responses", None)
        self.security = method_data.get("security", None)
        parameter_data = method_data.get("parameters", None)
        self.paramaters = []
        if parameter_data is not None:
            for parameter in parameter_data:
                self.paramaters.append(Parameter(parameter))

        self.method_data = method_data

        if "tags" in method_data:
            del method_data["tags"]
        if "summary" in method_data:
            del method_data["summary"]
        if "description" in method_data:
            del method_data["description"]
        if "operationId" in method_data:
            del method_data["operationId"]
        if "requestBody" in method_data:
            del method_data["requestBody"]
        if "responses" in method_data:
            del method_data["responses"]
        if "security" in method_data:
            del method_data["security"]
        if "parameters" in method_data:
            del method_data["parameters"]
        self.extras = method_data



    def dump(self):
        print("   Method: " + self.method_name)
        print("    Tags: ", self.tags)
        print("    Summary: " + self.summary)
        print("    Description: " + self.description)
        print("    Operation Id: " + self.operation_id)
        if self.request_body is not None:
            self.request_body.dump() 
        for parameter in self.paramaters:
            parameter.dump()
        if len(self.extras) > 0 :
            print("    Hmmm: ")
            pprint(self.extras)


class Path:
    def __init__(self, path_name, path_data):
        self.path_name = path_name
        self.methods = []
        for method_name, method_data in path_data.items():
            self.methods.append(Method(method_name, method_data))

    def dump(self):
        print(self.path_name)
        for method in self.methods:
            method.dump()


paths = []
for path, path_value in parser.specification["paths"].items():
    paths.append(Path(path, path_value))
for p in paths:
    p.dump()  
