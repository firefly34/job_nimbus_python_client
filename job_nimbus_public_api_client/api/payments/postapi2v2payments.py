from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_2v2_payments_response_200 import Postapi2V2PaymentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api2/v2/payments",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi2V2PaymentsResponse200]:
    if response.status_code == 200:
        response_200 = Postapi2V2PaymentsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi2V2PaymentsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi2V2PaymentsResponse200]:
    """Create a Payment

     This request allows you to create a payment within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - HTTP Status 500 = failure (most likely missing a required field)

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi2V2PaymentsResponse200]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi2V2PaymentsResponse200]:
    """Create a Payment

     This request allows you to create a payment within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - HTTP Status 500 = failure (most likely missing a required field)

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi2V2PaymentsResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi2V2PaymentsResponse200]:
    """Create a Payment

     This request allows you to create a payment within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - HTTP Status 500 = failure (most likely missing a required field)

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi2V2PaymentsResponse200]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi2V2PaymentsResponse200]:
    """Create a Payment

     This request allows you to create a payment within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - HTTP Status 500 = failure (most likely missing a required field)

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi2V2PaymentsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
