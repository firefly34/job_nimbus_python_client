from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1v2_workorders_response_200 import Getapi1V2WorkordersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api1/v2/workorders",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1V2WorkordersResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1V2WorkordersResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1V2WorkordersResponse200]:
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
) -> Response[Getapi1V2WorkordersResponse200]:
    """Retrieve ALL WorkOrders

     This request allows you to retrieve all of the work orders within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Additional details:**

    - `size` equals 1,000 by default if not included in the request.

    - The maximum value for `size` is 10,000.

    - The `count` property in the response body refers to the number of work orders in the account, not
    the number of work orders returned in the request.

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2WorkordersResponse200]
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
) -> Optional[Getapi1V2WorkordersResponse200]:
    """Retrieve ALL WorkOrders

     This request allows you to retrieve all of the work orders within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Additional details:**

    - `size` equals 1,000 by default if not included in the request.

    - The maximum value for `size` is 10,000.

    - The `count` property in the response body refers to the number of work orders in the account, not
    the number of work orders returned in the request.

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2WorkordersResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1V2WorkordersResponse200]:
    """Retrieve ALL WorkOrders

     This request allows you to retrieve all of the work orders within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Additional details:**

    - `size` equals 1,000 by default if not included in the request.

    - The maximum value for `size` is 10,000.

    - The `count` property in the response body refers to the number of work orders in the account, not
    the number of work orders returned in the request.

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2WorkordersResponse200]
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
) -> Optional[Getapi1V2WorkordersResponse200]:
    """Retrieve ALL WorkOrders

     This request allows you to retrieve all of the work orders within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Additional details:**

    - `size` equals 1,000 by default if not included in the request.

    - The maximum value for `size` is 10,000.

    - The `count` property in the response body refers to the number of work orders in the account, not
    the number of work orders returned in the request.

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2WorkordersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
