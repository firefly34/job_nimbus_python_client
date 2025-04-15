from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Postapi1V2InvoicesBody")


@_attrs_define
class Postapi1V2InvoicesBody:
    """
    Example:
        {'type': 'invoice', 'date_created': 1683819562, 'date_updated': 1684160281, 'date_invoice': 1683781200,
            'date_due': 1683781200, 'external_id': '993479', 'number': '1047-795', 'is_active': True, 'status': 1,
            'internal_note': 'Project Invoice', 'related': [{'id': '{jobId}', 'type': 'job'}], 'items': [{'name':
            'Services', 'description': 'Test and Troy Coone / SIDING', 'uom': 'Items', 'item_type': 'material', 'quantity':
            1, 'price': 15438.99, 'jnid': '{itemId}'}, {'name': 'Services', 'description': 'Shake siding', 'uom': 'Items',
            'item_type': 'material', 'quantity': 1, 'price': 1303, 'jnid': '{itemId}'}, {'name': 'Services', 'description':
            'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1, 'price': -349.52, 'jnid': '{itemId}'}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postapi_1v2_invoices_body = cls()

        postapi_1v2_invoices_body.additional_properties = d
        return postapi_1v2_invoices_body

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
