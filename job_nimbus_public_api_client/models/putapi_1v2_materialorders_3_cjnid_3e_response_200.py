from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Putapi1V2Materialorders3Cjnid3EResponse200")


@_attrs_define
class Putapi1V2Materialorders3Cjnid3EResponse200:
    """
    Example:
        {'type': 'materialorder', 'address': {'address_line1': 'P.O. Box 263, 900 Pharetra Ave', 'address_line2': '',
            'city': 'East Lynn', 'state_text': 'MO', 'zip': '64743'}, 'attachment_id': 'l461n85nqqwwy4s964ou5y9', 'esigned':
            False, 'is_active': True, 'is_archived': False, 'items': [{'category': 'C-012099', 'cost': 76.56, 'description':
            '', 'jnid': 'l461ku8xm3tjvhlrz8ft7t9', 'name': 'Generic 1-1/4" Coil Roofing', 'photos': [], 'price': 95.7,
            'quantity': 1, 'sku': '12099', 'uom': 'CTN', 'item_type': 'material', 'amount': 95.7}], 'location': {'id': 1},
            'related': [{'id': 'l3w5owqszqj4i0cz5h9hta4', 'name': 'Dorian Nash', 'number': '1507', 'type': 'contact'}],
            'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status': 1, 'supplier': {'branch': '300',
            'customer_branch': '280381', 'customer_job': 'SHOP', 'customer_job_name': 'SHOP ACCOUNT', 'logs': [], 'status':
            'Draft', 'type': 'Beacon Roofing Supply'}, 'template_id': 'l3ja810n16u1phh8vekq8sr-1', 'total_line_item_cost':
            76.56, 'total_line_item_price': 95.7, 'customer': 'l3ja7zfrzwgwfem9myim7h6', 'owners': [{'id':
            'l3ja7zg1oin4z1cavfqu9ou'}], 'guid': 'B61A2A96-21F0-4631-B13B-AED91A5EE914', 'recid': 1005, 'jnid':
            'm3tbge36pj6k1opkpz4luzc', 'created_by': 'l3ja7zg1oin4z1cavfqu9ou', 'created_by_name': 'Jordan Herget',
            'date_created': 1732314716, 'date_updated': 1732314787, 'date_status_change': 1732314716, 'number': '1005',
            'status_name': 'Draft', 'date_materialorder': 1732314716}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        putapi_1v2_materialorders_3_cjnid_3e_response_200 = cls()

        putapi_1v2_materialorders_3_cjnid_3e_response_200.additional_properties = d
        return putapi_1v2_materialorders_3_cjnid_3e_response_200

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
