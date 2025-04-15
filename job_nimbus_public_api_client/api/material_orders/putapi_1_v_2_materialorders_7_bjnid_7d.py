from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.putapi_1v2_materialorders_7_bjnid_7d_body import Putapi1V2Materialorders7Bjnid7DBody
from ...models.putapi_1v2_materialorders_7_bjnid_7d_response_200 import Putapi1V2Materialorders7Bjnid7DResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Putapi1V2Materialorders7Bjnid7DBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api1/v2/materialorders/%7Bjnid%7D",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Putapi1V2Materialorders7Bjnid7DResponse200]:
    if response.status_code == 200:
        response_200 = Putapi1V2Materialorders7Bjnid7DResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Putapi1V2Materialorders7Bjnid7DResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Putapi1V2Materialorders7Bjnid7DBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Putapi1V2Materialorders7Bjnid7DResponse200]:
    """Delete a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Materialorders7Bjnid7DBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Putapi1V2Materialorders7Bjnid7DResponse200]
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
    body: Putapi1V2Materialorders7Bjnid7DBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Putapi1V2Materialorders7Bjnid7DResponse200]:
    """Delete a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Materialorders7Bjnid7DBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Putapi1V2Materialorders7Bjnid7DResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Putapi1V2Materialorders7Bjnid7DBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Putapi1V2Materialorders7Bjnid7DResponse200]:
    """Delete a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Materialorders7Bjnid7DBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Putapi1V2Materialorders7Bjnid7DResponse200]
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
    body: Putapi1V2Materialorders7Bjnid7DBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Putapi1V2Materialorders7Bjnid7DResponse200]:
    """Delete a MaterialOrder

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Materialorders7Bjnid7DBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Putapi1V2Materialorders7Bjnid7DResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
