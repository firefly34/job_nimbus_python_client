from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Getapi1V2WorkordersResponse200")


@_attrs_define
class Getapi1V2WorkordersResponse200:
    """
    Example:
        {'count': 54, 'results': [{'all_day': False, 'all_day_end_date': '', 'all_day_start_date': '', 'attachment_id':
            'lz8y2munwhpm7mvk58fvpm0', 'class_id': '', 'class_name': '', 'created_by': 'l3ja7zg1oin4z1cavfqu9ou',
            'created_by_name': 'Jordan Herget', 'customer': 'l3ja7zfrzwgwfem9myim7h6', 'customer_note': None,
            'date_created': 1722375786, 'date_end': 0, 'date_start': 1722319200, 'date_status_change': 1722375786,
            'date_updated': 1726786488, 'esigned': False, 'external_id': None, 'guid':
            '2C96D8C6-9D57-4F62-86B8-CE700612E0E3', 'internal_note': None, 'is_active': True, 'is_archived': False, 'items':
            [{'amount': 675, 'category': None, 'color': None, 'cost': 750, 'description': '', 'item_type': 'material',
            'jnid': 'lgofp4nn5c9s0tc8ic0f7jw', 'labor': None, 'name': 'App Discount', 'photos': [], 'price': 675,
            'quantity': 1, 'sku': None, 'uom': 'Items'}], 'jnid': 'lz8y2mu4xjuz773scaqy1r5', 'location': {'id': 1},
            'merged': None, 'number': '1068', 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}],
            'parent_approved_estimate_total': 0, 'parent_approved_invoice_due': 0, 'parent_approved_invoice_total': 0,
            'parent_fax_number': None, 'parent_home_phone': None, 'parent_last_estimate': 0, 'parent_last_invoice': 0,
            'parent_mobile_phone': None, 'parent_work_phone': None, 'recid': 1068, 'record_type': 24, 'record_type_name':
            'Brick', 'related': [{'email': None, 'id': 'lz8y1afzet1hfihuaxwzkx3', 'name': 'Alex Banzea', 'number': '1086',
            'subject': None, 'type': 'job'}], 'rules': [], 'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status':
            366, 'status_name': 'Assigned', 'subcontractors': [], 'supplier': None, 'template_id':
            'l3ja810fo9lla875ag0b3ia-1', 'total_line_item_cost': 750, 'total_line_item_price': 675, 'type': 'workorder'}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        getapi_1v2_workorders_response_200 = cls()

        getapi_1v2_workorders_response_200.additional_properties = d
        return getapi_1v2_workorders_response_200

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
