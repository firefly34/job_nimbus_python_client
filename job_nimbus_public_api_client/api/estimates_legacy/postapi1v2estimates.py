from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1v2_estimates_body import Postapi1V2EstimatesBody
from ...models.postapi_1v2_estimates_response_200 import Postapi1V2EstimatesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Postapi1V2EstimatesBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/v2/estimates",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1V2EstimatesResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1V2EstimatesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1V2EstimatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2EstimatesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1V2EstimatesResponse200]:
    """Create an Estimate

     This request allows you to create a new estimate within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2EstimatesBody):  Example: {'type': 'estimate', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_estimate': 1683781200, 'external_id': '993479',
            'number': '1047', 'is_active': True, 'status': 1, 'internal_note': 'Project Estimate',
            'related': [{'id': 'lyu27jrnumcrz2u89k3ydyr', 'type': 'job'}], 'items': [{'name':
            'Services', 'description': 'Test and Troy Coon / SIDING', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 15438.99, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name':
            'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type': 'material',
            'quantity': 1, 'price': 1303, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1V2EstimatesResponse200]
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
    body: Postapi1V2EstimatesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1V2EstimatesResponse200]:
    """Create an Estimate

     This request allows you to create a new estimate within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2EstimatesBody):  Example: {'type': 'estimate', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_estimate': 1683781200, 'external_id': '993479',
            'number': '1047', 'is_active': True, 'status': 1, 'internal_note': 'Project Estimate',
            'related': [{'id': 'lyu27jrnumcrz2u89k3ydyr', 'type': 'job'}], 'items': [{'name':
            'Services', 'description': 'Test and Troy Coon / SIDING', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 15438.99, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name':
            'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type': 'material',
            'quantity': 1, 'price': 1303, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1V2EstimatesResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1V2EstimatesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1V2EstimatesResponse200]:
    """Create an Estimate

     This request allows you to create a new estimate within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2EstimatesBody):  Example: {'type': 'estimate', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_estimate': 1683781200, 'external_id': '993479',
            'number': '1047', 'is_active': True, 'status': 1, 'internal_note': 'Project Estimate',
            'related': [{'id': 'lyu27jrnumcrz2u89k3ydyr', 'type': 'job'}], 'items': [{'name':
            'Services', 'description': 'Test and Troy Coon / SIDING', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 15438.99, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name':
            'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type': 'material',
            'quantity': 1, 'price': 1303, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1V2EstimatesResponse200]
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
    body: Postapi1V2EstimatesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1V2EstimatesResponse200]:
    """Create an Estimate

     This request allows you to create a new estimate within JobNimbus.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1V2EstimatesBody):  Example: {'type': 'estimate', 'date_created': 1683819562,
            'date_updated': 1684160281, 'date_estimate': 1683781200, 'external_id': '993479',
            'number': '1047', 'is_active': True, 'status': 1, 'internal_note': 'Project Estimate',
            'related': [{'id': 'lyu27jrnumcrz2u89k3ydyr', 'type': 'job'}], 'items': [{'name':
            'Services', 'description': 'Test and Troy Coon / SIDING', 'uom': 'Items', 'item_type':
            'material', 'quantity': 1, 'price': 15438.99, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name':
            'Services', 'description': 'Shake siding', 'uom': 'Items', 'item_type': 'material',
            'quantity': 1, 'price': 1303, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}, {'name': 'Services',
            'description': 'Remove Lights', 'uom': 'Items', 'item_type': 'material', 'quantity': 1,
            'price': -349.52, 'jnid': 'lyqi3qx3ee8hvnwh8g53wo9'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1V2EstimatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
