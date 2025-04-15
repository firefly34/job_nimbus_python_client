from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Getapi1V2Workorders3Cjnid3EResponse200")


@_attrs_define
class Getapi1V2Workorders3Cjnid3EResponse200:
    """
    Example:
        {'type': 'workorder', 'merged': None, 'class_id': '', 'external_id': None, 'class_name': '', 'customer':
            'l3ja7zfrzwgwfem9myim7h6', 'supplier': None, 'related': [{'id': 'lz8y1afzet1hfihuaxwzkx3', 'name': 'Alex
            Banzea', 'number': '1086', 'type': 'job', 'email': None, 'subject': None}], 'created_by':
            'l3ja7zg1oin4z1cavfqu9ou', 'created_by_name': 'Jordan Herget', 'date_created': 1722375786, 'date_updated':
            1726786488, 'date_status_change': 1722375786, 'recid': 1068, 'rules': [], 'number': '1068', 'owners': [{'id':
            'l3ja7zg1oin4z1cavfqu9ou'}], 'subcontractors': [], 'record_type': 24, 'record_type_name': 'Brick',
            'parent_last_estimate': 0, 'parent_approved_estimate_total': 0, 'parent_approved_invoice_total': 0,
            'parent_approved_invoice_due': 0, 'parent_last_invoice': 0, 'parent_fax_number': None, 'parent_home_phone':
            None, 'parent_mobile_phone': None, 'parent_work_phone': None, 'status': 366, 'status_name': 'Assigned',
            'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'location': {'id': 1}, 'is_active': True, 'esigned': False,
            'is_archived': False, 'all_day': False, 'all_day_start_date': '', 'all_day_end_date': '', 'date_start':
            1722319200, 'date_end': 0, 'internal_note': None, 'customer_note': None, 'cf_string_1': None, 'cf_string_2':
            None, 'cf_string_3': None, 'cf_string_4': None, 'cf_string_5': None, 'cf_string_6': None, 'cf_string_7': None,
            'cf_string_8': None, 'cf_string_9': None, 'cf_string_10': None, 'cf_string_11': None, 'cf_string_12': None,
            'cf_string_13': None, 'cf_string_14': None, 'cf_string_15': None, 'cf_string_16': None, 'cf_string_17': None,
            'cf_string_18': None, 'cf_string_19': None, 'cf_string_20': None, 'cf_string_21': None, 'cf_string_22': None,
            'cf_string_23': None, 'cf_string_24': None, 'cf_string_25': None, 'cf_string_26': None, 'cf_string_27': None,
            'cf_string_28': None, 'cf_string_29': None, 'cf_string_30': None, 'cf_string_31': None, 'cf_string_32': None,
            'cf_string_33': None, 'cf_string_34': None, 'guid': '2C96D8C6-9D57-4F62-86B8-CE700612E0E3', 'cf_string_35':
            None, 'cf_string_36': None, 'cf_string_37': None, 'cf_string_38': None, 'cf_string_39': None, 'cf_string_40':
            None, 'cf_string_41': None, 'cf_string_42': None, 'cf_string_43': None, 'cf_string_44': None, 'cf_string_45':
            None, 'cf_string_46': None, 'cf_string_47': None, 'cf_string_48': None, 'cf_string_49': None, 'cf_string_50':
            None, 'cf_string_51': None, 'cf_string_52': None, 'cf_string_53': None, 'cf_string_54': None, 'cf_string_55':
            None, 'cf_string_56': None, 'cf_string_57': None, 'cf_string_58': None, 'cf_string_59': None, 'cf_string_60':
            None, 'cf_string_61': None, 'cf_string_62': None, 'cf_string_63': None, 'cf_string_64': None, 'cf_string_65':
            None, 'cf_string_66': None, 'cf_string_67': None, 'cf_string_68': None, 'cf_string_69': None, 'cf_string_70':
            None, 'cf_string_71': None, 'cf_string_72': None, 'cf_string_73': None, 'cf_string_74': None, 'cf_string_75':
            None, 'cf_string_76': None, 'cf_string_77': None, 'cf_string_78': None, 'cf_string_79': None, 'cf_string_80':
            None, 'cf_string_81': None, 'cf_string_82': None, 'cf_string_83': None, 'cf_string_84': None, 'cf_string_85':
            None, 'cf_string_86': None, 'cf_string_87': None, 'cf_string_88': None, 'cf_string_89': None, 'cf_string_90':
            None, 'cf_string_91': None, 'cf_string_92': None, 'cf_string_93': None, 'cf_string_94': None, 'cf_string_95':
            None, 'cf_string_96': None, 'cf_string_97': None, 'cf_string_98': None, 'cf_string_99': None, 'cf_string_100':
            None, 'cf_date_1': None, 'cf_date_2': None, 'cf_date_3': None, 'cf_date_4': None, 'cf_date_5': None,
            'cf_date_6': None, 'cf_date_7': None, 'cf_date_8': None, 'cf_date_9': None, 'cf_date_10': None, 'cf_date_11':
            None, 'cf_date_12': None, 'cf_date_13': None, 'cf_date_14': None, 'cf_date_15': None, 'cf_date_16': None,
            'cf_date_17': None, 'cf_date_18': None, 'cf_date_19': None, 'cf_date_20': None, 'cf_date_21': None,
            'cf_date_22': None, 'cf_date_23': None, 'cf_date_24': None, 'cf_date_25': None, 'cf_date_26': None,
            'cf_date_27': None, 'cf_date_28': None, 'cf_date_29': None, 'cf_date_30': None, 'cf_date_31': None,
            'cf_date_32': None, 'cf_date_33': None, 'cf_date_34': None, 'cf_date_35': None, 'cf_date_36': None,
            'cf_date_37': None, 'cf_date_38': None, 'cf_date_39': None, 'cf_date_40': None, 'cf_date_41': None,
            'cf_date_42': None, 'cf_date_43': None, 'cf_date_44': None, 'cf_date_45': None, 'cf_date_46': None,
            'cf_date_47': None, 'cf_date_48': None, 'cf_date_49': None, 'cf_date_50': None, 'cf_long_1': None, 'cf_long_2':
            None, 'cf_long_3': None, 'cf_long_4': None, 'cf_long_5': None, 'cf_long_6': None, 'cf_long_7': None,
            'cf_long_8': None, 'cf_long_9': None, 'cf_long_10': None, 'cf_long_11': None, 'cf_long_12': None, 'cf_long_13':
            None, 'cf_long_14': None, 'cf_long_15': None, 'cf_long_16': None, 'cf_long_17': None, 'cf_long_18': None,
            'cf_long_19': None, 'cf_long_20': None, 'cf_long_21': None, 'cf_long_22': None, 'cf_long_23': None,
            'cf_long_24': None, 'cf_long_25': None, 'cf_long_26': None, 'cf_long_27': None, 'cf_long_28': None,
            'cf_long_29': None, 'cf_long_30': None, 'cf_long_31': None, 'cf_long_32': None, 'cf_long_33': None,
            'cf_long_34': None, 'cf_long_35': None, 'cf_long_36': None, 'cf_long_37': None, 'cf_long_38': None,
            'cf_long_39': None, 'cf_long_40': None, 'cf_long_41': None, 'cf_long_42': None, 'cf_long_43': None,
            'cf_long_44': None, 'cf_long_45': None, 'cf_long_46': None, 'cf_long_47': None, 'cf_long_48': None,
            'cf_long_49': None, 'cf_long_50': None, 'cf_double_1': None, 'cf_double_2': None, 'cf_double_3': None,
            'cf_double_4': None, 'cf_double_5': None, 'cf_double_6': None, 'cf_double_7': None, 'cf_double_8': None,
            'cf_double_9': None, 'cf_double_10': None, 'cf_double_11': None, 'cf_double_12': None, 'cf_double_13': None,
            'cf_double_14': None, 'cf_double_15': None, 'cf_double_16': None, 'cf_double_17': None, 'cf_double_18': None,
            'cf_double_19': None, 'cf_double_20': None, 'cf_double_21': None, 'cf_double_22': None, 'cf_double_23': None,
            'cf_double_24': None, 'cf_double_25': None, 'cf_double_26': None, 'cf_double_27': None, 'cf_double_28': None,
            'cf_double_29': None, 'cf_double_30': None, 'cf_double_31': None, 'cf_double_32': None, 'cf_double_33': None,
            'cf_double_34': None, 'cf_double_35': None, 'cf_double_36': None, 'cf_double_37': None, 'cf_double_38': None,
            'cf_double_39': None, 'cf_double_40': None, 'cf_double_41': None, 'cf_double_42': None, 'cf_double_43': None,
            'cf_double_44': None, 'cf_double_45': None, 'cf_double_46': None, 'cf_double_47': None, 'cf_double_48': None,
            'cf_double_49': None, 'cf_double_50': None, 'cf_boolean_1': None, 'cf_boolean_2': None, 'cf_boolean_3': None,
            'cf_boolean_4': None, 'cf_boolean_5': None, 'cf_boolean_6': None, 'cf_boolean_7': None, 'cf_boolean_8': None,
            'cf_boolean_9': None, 'cf_boolean_10': None, 'cf_boolean_11': None, 'cf_boolean_12': None, 'cf_boolean_13':
            None, 'cf_boolean_14': None, 'cf_boolean_15': None, 'cf_boolean_16': None, 'cf_boolean_17': None,
            'cf_boolean_18': None, 'cf_boolean_19': None, 'cf_boolean_20': None, 'cf_boolean_21': None, 'cf_boolean_22':
            None, 'cf_boolean_23': None, 'cf_boolean_24': None, 'cf_boolean_25': None, 'cf_boolean_26': None,
            'cf_boolean_27': None, 'cf_boolean_28': None, 'cf_boolean_29': None, 'cf_boolean_30': None, 'cf_boolean_31':
            None, 'cf_boolean_32': None, 'cf_boolean_33': None, 'cf_boolean_34': None, 'cf_boolean_35': None,
            'cf_boolean_36': None, 'cf_boolean_37': None, 'cf_boolean_38': None, 'cf_boolean_39': None, 'cf_boolean_40':
            None, 'cf_boolean_41': None, 'cf_boolean_42': None, 'cf_boolean_43': None, 'cf_boolean_44': None,
            'cf_boolean_45': None, 'cf_boolean_46': None, 'cf_boolean_47': None, 'cf_boolean_48': None, 'cf_boolean_49':
            None, 'cf_boolean_50': None, 'sections': [], 'items': [{'jnid': 'lgofp4nn5c9s0tc8ic0f7jw', 'description': '',
            'photos': [], 'name': 'App Discount', 'quantity': 1, 'price': 675, 'cost': 750, 'amount': 675, 'uom': 'Items',
            'color': None, 'item_type': 'material', 'labor': None, 'sku': None, 'category': None}], 'jnid':
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
        getapi_1v2_workorders_3_cjnid_3e_response_200 = cls()

        getapi_1v2_workorders_3_cjnid_3e_response_200.additional_properties = d
        return getapi_1v2_workorders_3_cjnid_3e_response_200

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
