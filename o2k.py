from swagger_parser import SwaggerParser

def generate_karate_test_cases(swagger_file):
    parser = SwaggerParser(swagger_file)
    paths = parser.paths

    test_cases = []

    for path, path_item in paths.items():
        for method, operation in path_item.items():
            test_case = f"""
Scenario: Test {operation['operationId']}
    Given url {parser.host}{parser.base_path}{path}
    When method {method.upper()}
"""

            # Process request parameters
            parameters = operation.get('parameters', [])
            optional_parameters = [param for param in parameters if param.get('required') is False]
            mandatory_parameters = [param for param in parameters if param.get('required') is True]

            if optional_parameters:
                test_case += "    And request {} = <optional_value>\n".format(
                    ', '.join([param['name'] for param in optional_parameters])
                )

            if mandatory_parameters:
                test_case += "    And request {} = <mandatory_value>\n".format(
                    ', '.join([param['name'] for param in mandatory_parameters])
                )

            test_case += "    Then status {operation['responses'].keys()[0]}\n"

            test_cases.append(test_case)

    return '\n'.join(test_cases)


# Example usage
swagger_file = 'petstore_example/swagger.json'
karate_test_cases = generate_karate_test_cases(swagger_file)

print(karate_test_cases)
