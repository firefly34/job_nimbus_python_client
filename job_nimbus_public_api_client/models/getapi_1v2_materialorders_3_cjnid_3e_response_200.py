from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Getapi1V2Materialorders3Cjnid3EResponse200")


@_attrs_define
class Getapi1V2Materialorders3Cjnid3EResponse200:
    """
    Example:
        {'address': {'address_line1': 'P.O. Box 263, 900 Pharetra Ave', 'address_line2': '', 'city': 'East Lynn', 'geo':
            {'lat': 38.667221, 'lon': -94.229804}, 'state_text': 'MO', 'zip': '64743'}, 'attachment_id':
            'l461n85nqqwwy4s964ou5y9', 'class_id': None, 'class_name': None, 'created_by': 'l3ja7zg1oin4z1cavfqu9ou',
            'created_by_name': 'Michael Knowles', 'customer': 'l3ja7zfrzwgwfem9myim7h6', 'customer_note': None,
            'date_created': 1654720135, 'date_materialorder': 1654711200, 'date_status_change': 1654720135, 'date_updated':
            1654720135, 'duplicate_from_id': None, 'esigned': False, 'external_id': None, 'guid':
            'AFAF5AEA-853B-4A1A-8222-4B2B05934ABD', 'internal_note': None, 'is_active': True, 'is_archived': False, 'items':
            [{'category': 'C-012099', 'color': None, 'cost': 76.56, 'description': '', 'jnid': 'l461ku8xm3tjvhlrz8ft7t9',
            'name': 'Generic 1-1/4" Coil Roofing', 'photos': [], 'price': 95.7, 'quantity': 1, 'sku': '12099', 'uom':
            'CTN'}], 'jnid': 'l461n84tmut6nbv8du00ban', 'location': {'id': 1}, 'merged': None, 'number': '1001', 'owners':
            [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'recid': 1001, 'related': [{'id': 'l3w5owqszqj4i0cz5h9hta4', 'name':
            'Dorian Nash', 'number': '1507', 'type': 'contact'}], 'rules': [], 'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou',
            'sections': [], 'status': 0, 'status_name': 'Draft', 'supplier': {'branch': '300', 'customer_branch': '280381',
            'customer_job': 'SHOP', 'customer_job_name': 'SHOP ACCOUNT', 'delivery_time': None, 'logs': [], 'po': None,
            'status': 'Draft', 'type': 'Beacon Roofing Supply'}, 'template_id': 'l3ja810n16u1phh8vekq8sr-1',
            'total_line_item_cost': 76.56, 'total_line_item_price': 95.7, 'type': 'materialorder'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        getapi_1v2_materialorders_3_cjnid_3e_response_200 = cls()

        getapi_1v2_materialorders_3_cjnid_3e_response_200.additional_properties = d
        return getapi_1v2_materialorders_3_cjnid_3e_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
