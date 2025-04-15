from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Postapi1V2WorkordersResponse200")


@_attrs_define
class Postapi1V2WorkordersResponse200:
    """
    Example:
        {'type': 'workorder', 'class_id': '', 'class_name': '', 'customer': 'l3ja7zfrzwgwfem9myim7h6', 'related':
            [{'id': 'lz8y1afzet1hfihuaxwzkx3', 'name': 'Alex Banzea', 'number': '1086', 'type': 'job', 'email': None,
            'subject': None}], 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'subcontractors': [], 'record_type': 24,
            'status': 366, 'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'location': {'id': 1}, 'is_active': True, 'esigned':
            False, 'is_archived': False, 'all_day': False, 'all_day_start_date': '', 'all_day_end_date': '', 'date_start':
            1722319200, 'date_end': 0, 'sections': [], 'items': [{'jnid': 'lgofp4nn5c9s0tc8ic0f7jw', 'description': '',
            'photos': [], 'name': 'App Discount', 'quantity': 1, 'price': 675, 'cost': 750, 'amount': 675, 'uom': 'Items',
            'item_type': 'material'}], 'total_line_item_cost': 750, 'total_line_item_price': 675, 'attachment_id':
            'lz8y2munwhpm7mvk58fvpm0', 'template_id': 'l3ja810fo9lla875ag0b3ia-1', 'guid':
            '6047AF5B-E3DF-4704-AB7D-FFB13B224527', 'recid': 1069, 'jnid': 'm3g4tv93s5hey11njgi55gt', 'created_by':
            'l3ja7zg1oin4z1cavfqu9ou', 'created_by_name': 'Jordan Herget', 'date_created': 1731517527, 'date_updated':
            1731517527, 'date_status_change': 1731517527, 'record_type_name': 'Brick', 'status_name': 'Assigned', 'number':
            '1069', 'parent_approved_estimate_total': 0, 'parent_approved_invoice_total': 0, 'parent_approved_invoice_due':
            0, 'parent_last_estimate': 0, 'parent_last_invoice': 0}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postapi_1v2_workorders_response_200 = cls()

        postapi_1v2_workorders_response_200.additional_properties = d
        return postapi_1v2_workorders_response_200

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
