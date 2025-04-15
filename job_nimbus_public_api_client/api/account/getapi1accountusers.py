from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1_accountusers_response_200 import Getapi1AccountusersResponse200
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
        "url": "/api1/account/users",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1AccountusersResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1AccountusersResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1AccountusersResponse200]:
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
) -> Response[Getapi1AccountusersResponse200]:
    r"""Retrieve Users or Team Members

     This request allows you to retrieve a list of an account's JobNimbus users.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    Example of a partial response:

    ```
    {
        \"users\": [
            {
                \"first_name\": \"fname\",
                \"last_name\": \"lname\",
                \"image_url\": \"\",
                \"id\": \"abcdid\", // this is user's contact jnid
                \"calendar_color\": \"#2ECC71\",
                \"email\": \"abc@jobnimbus.com\",
                \"is_active\": true // whether user is active or disabled
            },....
       \"date_updated\": 1519413931 // last time when this document updated (user added, updated,
    modified)
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1AccountusersResponse200]
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
) -> Optional[Getapi1AccountusersResponse200]:
    r"""Retrieve Users or Team Members

     This request allows you to retrieve a list of an account's JobNimbus users.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    Example of a partial response:

    ```
    {
        \"users\": [
            {
                \"first_name\": \"fname\",
                \"last_name\": \"lname\",
                \"image_url\": \"\",
                \"id\": \"abcdid\", // this is user's contact jnid
                \"calendar_color\": \"#2ECC71\",
                \"email\": \"abc@jobnimbus.com\",
                \"is_active\": true // whether user is active or disabled
            },....
       \"date_updated\": 1519413931 // last time when this document updated (user added, updated,
    modified)
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1AccountusersResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1AccountusersResponse200]:
    r"""Retrieve Users or Team Members

     This request allows you to retrieve a list of an account's JobNimbus users.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    Example of a partial response:

    ```
    {
        \"users\": [
            {
                \"first_name\": \"fname\",
                \"last_name\": \"lname\",
                \"image_url\": \"\",
                \"id\": \"abcdid\", // this is user's contact jnid
                \"calendar_color\": \"#2ECC71\",
                \"email\": \"abc@jobnimbus.com\",
                \"is_active\": true // whether user is active or disabled
            },....
       \"date_updated\": 1519413931 // last time when this document updated (user added, updated,
    modified)
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1AccountusersResponse200]
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
) -> Optional[Getapi1AccountusersResponse200]:
    r"""Retrieve Users or Team Members

     This request allows you to retrieve a list of an account's JobNimbus users.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    Example of a partial response:

    ```
    {
        \"users\": [
            {
                \"first_name\": \"fname\",
                \"last_name\": \"lname\",
                \"image_url\": \"\",
                \"id\": \"abcdid\", // this is user's contact jnid
                \"calendar_color\": \"#2ECC71\",
                \"email\": \"abc@jobnimbus.com\",
                \"is_active\": true // whether user is active or disabled
            },....
       \"date_updated\": 1519413931 // last time when this document updated (user added, updated,
    modified)
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1AccountusersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
