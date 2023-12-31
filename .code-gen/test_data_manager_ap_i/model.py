from .utils import datetime_decoder
from .utils import discriminator_decoder
from dataclasses import dataclass
from dataclasses import field
from dataclasses_json.api import DataClassJsonMixin
from dataclasses_json.api import dataclass_json
from dataclasses_json.cfg import LetterCase
from dataclasses_json.cfg import config
from datetime import date
from datetime import datetime
from datetime import time
from enum import Enum
from typing import *

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FullTestDataItem(DataClassJsonMixin):
    """
    Required Properties:
     - test_data_type
     - test_data_status
     - test_data_purpose
     - test_data_index
     - test_data_id
    
    Generated by Python OpenAPI Parser
    """
    
    test_data_type: str = Option.empty
    test_data_status: str = Option.empty
    test_data_purpose: str = Option.empty
    test_data_index: float = Option.empty
    test_data_id: str = Option.empty

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TestDataRequest(DataClassJsonMixin):
    """
    Required Properties:
     - request_id
     - request_status
     - test_data_items
    
    Generated by Python OpenAPI Parser
    """
    
    request_id: str = Option.empty
    request_status: str = Option.empty
    test_data_items: List[FullTestDataItem] = Option.empty

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RequestTestDataItem(DataClassJsonMixin):
    """
    Required Properties:
     - test_data_type
     - test_data_purpose
    
    Generated by Python OpenAPI Parser
    """
    
    test_data_type: str = Option.empty
    test_data_purpose: str = Option.empty

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class UnprovisionedTestDataItem(DataClassJsonMixin):
    """
    Required Properties:
     - request_id
     - request_index
     - test_data_type
     - test_data_purpose
    
    Generated by Python OpenAPI Parser
    """
    
    request_id: str = Option.empty
    request_index: str = Option.empty
    test_data_type: str = Option.empty
    test_data_purpose: str = Option.empty

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class NewTestDataItem(DataClassJsonMixin):
    """
    Required Properties:
     - test_data_id
    
    Generated by Python OpenAPI Parser
    """
    
    test_data_id: str = Option.empty

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ProvisionedTestDataItem(DataClassJsonMixin):
    """
    Required Properties:
     - test_data_id
    
    Generated by Python OpenAPI Parser
    """
    
    test_data_id: str = Option.empty
    test_data_details: Optional[dict] = Option.empty

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Error(DataClassJsonMixin):
    """
    Required Properties:
     - code
     - message
    
    Generated by Python OpenAPI Parser
    """
    
    code: int = Option.empty
    message: str = Option.empty


__all__ = \
[
    'Error',
    'FullTestDataItem',
    'NewTestDataItem',
    'ProvisionedTestDataItem',
    'RequestTestDataItem',
    'TestDataRequest',
    'UnprovisionedTestDataItem',
]
