from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1v2_materialorders_body import Postapi1V2MaterialordersBody
from ...models.postapi_1v2_materialorders_response_200 import Postapi1V2MaterialordersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Postapi1V2MaterialordersBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/v2/materialorders",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1V2MaterialordersResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1V2MaterialordersResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1V2MaterialordersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2MaterialordersBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1V2MaterialordersResponse200]:
    """Create a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2MaterialordersBody):  Example: {'customer_note': None, 'esigned': False,
            'external_id': None, 'internal_note': None, 'is_active': True, 'is_archived': False,
            'items': [{'category': 'C-012099', 'color': None, 'cost': 76.56, 'description': '',
            'jnid': 'l461ku8xm3tjvhlrz8ft7t9', 'name': 'Generic 1-1/4" Coil Roofing', 'photos': [],
            'price': 95.7, 'quantity': 1, 'sku': '12099', 'uom': 'CTN'}], 'location': {'id': 1},
            'merged': None, 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'related': [{'id':
            'l3w5owqszqj4i0cz5h9hta4', 'name': 'Dorian Nash', 'number': '1507', 'type': 'contact'}],
            'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status': 0, 'status_name':
            'Draft', 'total_line_item_cost': 76.56, 'total_line_item_price': 95.7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1V2MaterialordersResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2MaterialordersBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1V2MaterialordersResponse200]:
    """Create a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2MaterialordersBody):  Example: {'customer_note': None, 'esigned': False,
            'external_id': None, 'internal_note': None, 'is_active': True, 'is_archived': False,
            'items': [{'category': 'C-012099', 'color': None, 'cost': 76.56, 'description': '',
            'jnid': 'l461ku8xm3tjvhlrz8ft7t9', 'name': 'Generic 1-1/4" Coil Roofing', 'photos': [],
            'price': 95.7, 'quantity': 1, 'sku': '12099', 'uom': 'CTN'}], 'location': {'id': 1},
            'merged': None, 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'related': [{'id':
            'l3w5owqszqj4i0cz5h9hta4', 'name': 'Dorian Nash', 'number': '1507', 'type': 'contact'}],
            'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status': 0, 'status_name':
            'Draft', 'total_line_item_cost': 76.56, 'total_line_item_price': 95.7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1V2MaterialordersResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2MaterialordersBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1V2MaterialordersResponse200]:
    """Create a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2MaterialordersBody):  Example: {'customer_note': None, 'esigned': False,
            'external_id': None, 'internal_note': None, 'is_active': True, 'is_archived': False,
            'items': [{'category': 'C-012099', 'color': None, 'cost': 76.56, 'description': '',
            'jnid': 'l461ku8xm3tjvhlrz8ft7t9', 'name': 'Generic 1-1/4" Coil Roofing', 'photos': [],
            'price': 95.7, 'quantity': 1, 'sku': '12099', 'uom': 'CTN'}], 'location': {'id': 1},
            'merged': None, 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'related': [{'id':
            'l3w5owqszqj4i0cz5h9hta4', 'name': 'Dorian Nash', 'number': '1507', 'type': 'contact'}],
            'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status': 0, 'status_name':
            'Draft', 'total_line_item_cost': 76.56, 'total_line_item_price': 95.7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1V2MaterialordersResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2MaterialordersBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1V2MaterialordersResponse200]:
    """Create a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2MaterialordersBody):  Example: {'customer_note': None, 'esigned': False,
            'external_id': None, 'internal_note': None, 'is_active': True, 'is_archived': False,
            'items': [{'category': 'C-012099', 'color': None, 'cost': 76.56, 'description': '',
            'jnid': 'l461ku8xm3tjvhlrz8ft7t9', 'name': 'Generic 1-1/4" Coil Roofing', 'photos': [],
            'price': 95.7, 'quantity': 1, 'sku': '12099', 'uom': 'CTN'}], 'location': {'id': 1},
            'merged': None, 'owners': [{'id': 'l3ja7zg1oin4z1cavfqu9ou'}], 'related': [{'id':
            'l3w5owqszqj4i0cz5h9hta4', 'name': 'Dorian Nash', 'number': '1507', 'type': 'contact'}],
            'sales_rep': 'l3ja7zg1oin4z1cavfqu9ou', 'sections': [], 'status': 0, 'status_name':
            'Draft', 'total_line_item_cost': 76.56, 'total_line_item_price': 95.7}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1V2MaterialordersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
