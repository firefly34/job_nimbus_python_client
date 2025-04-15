from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_accountlocation_response_200 import Postapi1AccountlocationResponse200
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
        "url": "/api1/account/location",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1AccountlocationResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1AccountlocationResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1AccountlocationResponse200]:
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
) -> Response[Postapi1AccountlocationResponse200]:
    r"""Create a Location

     This request allows you to create a new location within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a location  with that name already exists, then the API endpoint will return with a response with
    the status for that location.
    If the location didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    Eg1:
    {
        \"id\": 4,
        \"name\": \"Location Name\",
        \"is_active\": true,
        \"address_line1\": \"address1\",
        \"address_line2\": \"address2\",
        \"code\": \"HH\",
        \"city\": \"American Fork\",
        \"zip\": \"84004\",
        \"phone\": \"999-999-9999\"
    }
    Eg2:
    {
        \"id\": 1,
        \"name\": \"HungryHead\",
        \"code\": \"HH\",
        \"address_line1\": \"102, sapetrshi apt\",
        \"address_line2\": \"sagrampura\",
        \"city\": \"Surat\",
        \"state_text\": \"Gujarat\",
        \"country_name\": \"India\",
        \"zip\": \"392002\",
        \"phone\": \"9033204250\",
        \"logo_id\": \"j5m9a0agbjnt3xvv\",
        \"header_color\": \"#c1cfd8\",
        \"is_active\": true,
        \"calendar\": {
            \"weekends\": true,
            \"start_day\": 0,
            \"business_hours\": {
                \"start\": 1502649000,
                \"end\": 1502734500
            }
        }
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "name":"Location Name", //Location name, it's required parameter
                "address_line1": "address1", //optional field
                "address_line2": "address2", //optional field
                "code": "HH", //optional field
                "city": "American Fork", //optional field
                "zip": "84004", //optional field
                "phone": "999-999-9999", //optional field
                "is_active": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountlocationResponse200]
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
) -> Optional[Postapi1AccountlocationResponse200]:
    r"""Create a Location

     This request allows you to create a new location within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a location  with that name already exists, then the API endpoint will return with a response with
    the status for that location.
    If the location didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    Eg1:
    {
        \"id\": 4,
        \"name\": \"Location Name\",
        \"is_active\": true,
        \"address_line1\": \"address1\",
        \"address_line2\": \"address2\",
        \"code\": \"HH\",
        \"city\": \"American Fork\",
        \"zip\": \"84004\",
        \"phone\": \"999-999-9999\"
    }
    Eg2:
    {
        \"id\": 1,
        \"name\": \"HungryHead\",
        \"code\": \"HH\",
        \"address_line1\": \"102, sapetrshi apt\",
        \"address_line2\": \"sagrampura\",
        \"city\": \"Surat\",
        \"state_text\": \"Gujarat\",
        \"country_name\": \"India\",
        \"zip\": \"392002\",
        \"phone\": \"9033204250\",
        \"logo_id\": \"j5m9a0agbjnt3xvv\",
        \"header_color\": \"#c1cfd8\",
        \"is_active\": true,
        \"calendar\": {
            \"weekends\": true,
            \"start_day\": 0,
            \"business_hours\": {
                \"start\": 1502649000,
                \"end\": 1502734500
            }
        }
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "name":"Location Name", //Location name, it's required parameter
                "address_line1": "address1", //optional field
                "address_line2": "address2", //optional field
                "code": "HH", //optional field
                "city": "American Fork", //optional field
                "zip": "84004", //optional field
                "phone": "999-999-9999", //optional field
                "is_active": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountlocationResponse200
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
) -> Response[Postapi1AccountlocationResponse200]:
    r"""Create a Location

     This request allows you to create a new location within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a location  with that name already exists, then the API endpoint will return with a response with
    the status for that location.
    If the location didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    Eg1:
    {
        \"id\": 4,
        \"name\": \"Location Name\",
        \"is_active\": true,
        \"address_line1\": \"address1\",
        \"address_line2\": \"address2\",
        \"code\": \"HH\",
        \"city\": \"American Fork\",
        \"zip\": \"84004\",
        \"phone\": \"999-999-9999\"
    }
    Eg2:
    {
        \"id\": 1,
        \"name\": \"HungryHead\",
        \"code\": \"HH\",
        \"address_line1\": \"102, sapetrshi apt\",
        \"address_line2\": \"sagrampura\",
        \"city\": \"Surat\",
        \"state_text\": \"Gujarat\",
        \"country_name\": \"India\",
        \"zip\": \"392002\",
        \"phone\": \"9033204250\",
        \"logo_id\": \"j5m9a0agbjnt3xvv\",
        \"header_color\": \"#c1cfd8\",
        \"is_active\": true,
        \"calendar\": {
            \"weekends\": true,
            \"start_day\": 0,
            \"business_hours\": {
                \"start\": 1502649000,
                \"end\": 1502734500
            }
        }
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "name":"Location Name", //Location name, it's required parameter
                "address_line1": "address1", //optional field
                "address_line2": "address2", //optional field
                "code": "HH", //optional field
                "city": "American Fork", //optional field
                "zip": "84004", //optional field
                "phone": "999-999-9999", //optional field
                "is_active": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountlocationResponse200]
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
) -> Optional[Postapi1AccountlocationResponse200]:
    r"""Create a Location

     This request allows you to create a new location within a Jobnimbus account. Note: The token used
    must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a location  with that name already exists, then the API endpoint will return with a response with
    the status for that location.
    If the location didn't exist, then the API endpoint will return a response similar to the example,
    below:

    ```
    Eg1:
    {
        \"id\": 4,
        \"name\": \"Location Name\",
        \"is_active\": true,
        \"address_line1\": \"address1\",
        \"address_line2\": \"address2\",
        \"code\": \"HH\",
        \"city\": \"American Fork\",
        \"zip\": \"84004\",
        \"phone\": \"999-999-9999\"
    }
    Eg2:
    {
        \"id\": 1,
        \"name\": \"HungryHead\",
        \"code\": \"HH\",
        \"address_line1\": \"102, sapetrshi apt\",
        \"address_line2\": \"sagrampura\",
        \"city\": \"Surat\",
        \"state_text\": \"Gujarat\",
        \"country_name\": \"India\",
        \"zip\": \"392002\",
        \"phone\": \"9033204250\",
        \"logo_id\": \"j5m9a0agbjnt3xvv\",
        \"header_color\": \"#c1cfd8\",
        \"is_active\": true,
        \"calendar\": {
            \"weekends\": true,
            \"start_day\": 0,
            \"business_hours\": {
                \"start\": 1502649000,
                \"end\": 1502734500
            }
        }
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "name":"Location Name", //Location name, it's required parameter
                "address_line1": "address1", //optional field
                "address_line2": "address2", //optional field
                "code": "HH", //optional field
                "city": "American Fork", //optional field
                "zip": "84004", //optional field
                "phone": "999-999-9999", //optional field
                "is_active": true/false, //optional field (default = true)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountlocationResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
