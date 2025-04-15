from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Postapi1V2MaterialordersBody")


@_attrs_define
class Postapi1V2MaterialordersBody:
    """
    Example:
        {'customer_note': None, 'esigned': False, 'external_id': None, 'internal_note': None, 'is_active': True,
            'is_archived': False, 'items': [{'category': 'C-012099', 'color': None, 'cost': 76.56, 'description': '',
            'jnid': 'l461ku8xm3tjvhlrz8ft7t9', 'name': 'Generic 1-1/4" Coil Roofing', 'photos': [], 'price': 95.7,
            'quantity': 1, 'sku': '12099', 'uom': 'CTN'}], 'location': {'id': 1}, 'merged': None, 'owners': [{'id':
            'l3ja7zg1oin4z1cavfqu9ou'}], 'related': [{'id': 'l3w5owqszqj4i0cz5h9hta4', 'name': 'Dorian Nash', 'number':
            '1507', 'type': 'contact'}], 'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status': 0, 'status_name':
            'Draft', 'total_line_item_cost': 76.56, 'total_line_item_price': 95.7}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postapi_1v2_materialorders_body = cls()

        postapi_1v2_materialorders_body.additional_properties = d
        return postapi_1v2_materialorders_body

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
