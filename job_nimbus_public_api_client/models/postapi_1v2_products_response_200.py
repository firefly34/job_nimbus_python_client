from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Postapi1V2ProductsResponse200")


@_attrs_define
class Postapi1V2ProductsResponse200:
    """
    Example:
        {'type': 'product', 'name': 'Test Material Labor Product', 'description': 'This is a test product',
            'location_id': 1, 'is_active': True, 'tax_exempt': False, 'item_type': 'labor+material', 'uoms': [{'uom': 'SQ
            YD', 'material': {'cost': 12, 'price': 15}, 'labor': {'cost': 0, 'price': 0}}, {'uom': 'Labor', 'material':
            {'cost': 200, 'price': 350}, 'labor': {'cost': 0, 'price': 0}}], 'customer': 'l3ja7zfrzwgwfem9myim7h6', 'jnid':
            'm3gwyq5zkgpkej3pc3cuylo', 'created_by': 'l3ja7zg1oin4z1cavfqu9ou', 'date_created': 1731564783, 'date_updated':
            1731564783}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postapi_1v2_products_response_200 = cls()

        postapi_1v2_products_response_200.additional_properties = d
        return postapi_1v2_products_response_200

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
