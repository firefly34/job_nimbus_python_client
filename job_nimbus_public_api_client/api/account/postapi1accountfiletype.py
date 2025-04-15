from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_accountfiletype_response_200 import Postapi1AccountfiletypeResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: str,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/account/filetype",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1AccountfiletypeResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1AccountfiletypeResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1AccountfiletypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1AccountfiletypeResponse200]:
    r"""Create a File Type

     This request allows you to create a new file type within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a file type with that name already exists, then the API endpoint will return with a response with
    the status for that file type.
    If the file type didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    {
        \"FileTypeId\": 895,
        \"TypeName\": \"Document\",
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Document", //file type name (attachment category name), it's required
            parameter
                "IsActive": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountfiletypeResponse200]
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
    body: str,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1AccountfiletypeResponse200]:
    r"""Create a File Type

     This request allows you to create a new file type within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a file type with that name already exists, then the API endpoint will return with a response with
    the status for that file type.
    If the file type didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    {
        \"FileTypeId\": 895,
        \"TypeName\": \"Document\",
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Document", //file type name (attachment category name), it's required
            parameter
                "IsActive": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountfiletypeResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1AccountfiletypeResponse200]:
    r"""Create a File Type

     This request allows you to create a new file type within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a file type with that name already exists, then the API endpoint will return with a response with
    the status for that file type.
    If the file type didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    {
        \"FileTypeId\": 895,
        \"TypeName\": \"Document\",
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Document", //file type name (attachment category name), it's required
            parameter
                "IsActive": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountfiletypeResponse200]
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
    body: str,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1AccountfiletypeResponse200]:
    r"""Create a File Type

     This request allows you to create a new file type within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a file type with that name already exists, then the API endpoint will return with a response with
    the status for that file type.
    If the file type didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    {
        \"FileTypeId\": 895,
        \"TypeName\": \"Document\",
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Document", //file type name (attachment category name), it's required
            parameter
                "IsActive": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountfiletypeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
