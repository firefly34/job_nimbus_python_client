from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1v2_invoices_body import Postapi1V2InvoicesBody
from ...models.postapi_1v2_invoices_response_200 import Postapi1V2InvoicesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Postapi1V2InvoicesBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/v2/invoices",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1V2InvoicesResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1V2InvoicesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1V2InvoicesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2InvoicesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1V2InvoicesResponse200]:
    """Create an Invoice

     This request allows you to create a new invoice within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2InvoicesBody):  Example: {'type': 'invoice', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_invoice': 1683781200, 'date_due': 1683781200,
            'external_id': '993479', 'number': '1047-795', 'is_active': True, 'status': 1,
            'internal_note': 'Project Invoice', 'related': [{'id': '{jobId}', 'type': 'job'}],
            'items': [{'name': 'Services', 'description': 'Test and Troy Coone / SIDING', 'uom':
            'Items', 'item_type': 'material', 'quantity': 1, 'price': 15438.99, 'jnid': '{itemId}'},
            {'name': 'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 1303, 'jnid': '{itemId}'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': '{itemId}'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1V2InvoicesResponse200]
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
    body: Postapi1V2InvoicesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1V2InvoicesResponse200]:
    """Create an Invoice

     This request allows you to create a new invoice within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2InvoicesBody):  Example: {'type': 'invoice', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_invoice': 1683781200, 'date_due': 1683781200,
            'external_id': '993479', 'number': '1047-795', 'is_active': True, 'status': 1,
            'internal_note': 'Project Invoice', 'related': [{'id': '{jobId}', 'type': 'job'}],
            'items': [{'name': 'Services', 'description': 'Test and Troy Coone / SIDING', 'uom':
            'Items', 'item_type': 'material', 'quantity': 1, 'price': 15438.99, 'jnid': '{itemId}'},
            {'name': 'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 1303, 'jnid': '{itemId}'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': '{itemId}'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1V2InvoicesResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2InvoicesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1V2InvoicesResponse200]:
    """Create an Invoice

     This request allows you to create a new invoice within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2InvoicesBody):  Example: {'type': 'invoice', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_invoice': 1683781200, 'date_due': 1683781200,
            'external_id': '993479', 'number': '1047-795', 'is_active': True, 'status': 1,
            'internal_note': 'Project Invoice', 'related': [{'id': '{jobId}', 'type': 'job'}],
            'items': [{'name': 'Services', 'description': 'Test and Troy Coone / SIDING', 'uom':
            'Items', 'item_type': 'material', 'quantity': 1, 'price': 15438.99, 'jnid': '{itemId}'},
            {'name': 'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 1303, 'jnid': '{itemId}'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': '{itemId}'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1V2InvoicesResponse200]
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
    body: Postapi1V2InvoicesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1V2InvoicesResponse200]:
    """Create an Invoice

     This request allows you to create a new invoice within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2InvoicesBody):  Example: {'type': 'invoice', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_invoice': 1683781200, 'date_due': 1683781200,
            'external_id': '993479', 'number': '1047-795', 'is_active': True, 'status': 1,
            'internal_note': 'Project Invoice', 'related': [{'id': '{jobId}', 'type': 'job'}],
            'items': [{'name': 'Services', 'description': 'Test and Troy Coone / SIDING', 'uom':
            'Items', 'item_type': 'material', 'quantity': 1, 'price': 15438.99, 'jnid': '{itemId}'},
            {'name': 'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 1303, 'jnid': '{itemId}'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': '{itemId}'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1V2InvoicesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
