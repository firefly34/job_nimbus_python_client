from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Putapi1V2Workorders7Bid7DResponse200")


@_attrs_define
class Putapi1V2Workorders7Bid7DResponse200:
    """
    Example:
        {'type': 'workorder', 'class_id': '', 'class_name': '', 'customer': 'l3ja7zfrzwgwfem9myim7h6', 'related':
            [{'id': 'lz8y1afzet1hfihuaxwzkx3', 'name': 'Alex Banzea', 'number': '1086', 'type': 'job', 'email': None,
            'subject': None}], 'created_by': 'l3ja7zg1oin4z1cavfqu9ou', 'created_by_name': 'Jordan Herget', 'date_created':
            1722375786, 'date_updated': 1731517148, 'date_status_change': 1722375786, 'recid': 1068, 'rules': [], 'number':
            '1068', 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'subcontractors': [], 'record_type': 24,
            'record_type_name': 'Brick', 'parent_last_estimate': 0, 'parent_approved_estimate_total': 0,
            'parent_approved_invoice_total': 0, 'parent_approved_invoice_due': 0, 'parent_last_invoice': 0, 'status': 366,
            'status_name': 'Assigned', 'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'location': {'id': 1}, 'is_active': False,
            'esigned': False, 'is_archived': False, 'all_day': False, 'all_day_start_date': '', 'all_day_end_date': '',
            'date_start': 1722319200, 'date_end': 0, 'guid': '2C96D8C6-9D57-4F62-86B8-CE700612E0E3', 'sections': [],
            'items': [{'jnid': 'lgofp4nn5c9s0tc8ic0f7jw', 'description': '', 'photos': [], 'name': 'App Discount',
            'quantity': 1, 'price': 675, 'cost': 750, 'amount': 675, 'uom': 'Items', 'item_type': 'material'}], 'jnid':
            'lz8y2mu4xjuz773scaqy1r5', 'total_line_item_cost': 750, 'total_line_item_price': 675, 'attachment_id':
            'lz8y2munwhpm7mvk58fvpm0', 'template_id': 'l3ja810fo9lla875ag0b3ia-1'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        putapi_1v2_workorders_7_bid_7d_response_200 = cls()

        putapi_1v2_workorders_7_bid_7d_response_200.additional_properties = d
        return putapi_1v2_workorders_7_bid_7d_response_200

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
