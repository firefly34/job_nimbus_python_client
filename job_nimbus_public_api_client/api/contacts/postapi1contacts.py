from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_contacts_body import Postapi1ContactsBody
from ...models.postapi_1_contacts_response_200 import Postapi1ContactsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Postapi1ContactsBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/contacts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1ContactsResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1ContactsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1ContactsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1ContactsBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1ContactsResponse200]:
    r"""Create a Contact

     This request allows you to create a new contact within JobNimbus.

    **Notes**:

    * First Name, Last Name, First & Last Name, Display_Name, or Company Name are required
    * record_type_name is required and should be a workflow name defined in the customers JobNimbus
    contact workflow settings
    * status_name is required and should be a status defined within the record_type_name workflow
    * source_name is optional but if provided should be set to one of the lead source names defined in
    the customer's settings
    * Also accepts most of the fields listed in the \"GET /contacts\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1ContactsBody):  Example: {'first_name': 'Sammy G', 'last_name': 'Kent',
            'record_type_name': 'Customer', 'status_name': 'Lead', 'geo': {'lon': -88.687277, 'lat':
            37.149574}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1ContactsResponse200]
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
    body: Postapi1ContactsBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1ContactsResponse200]:
    r"""Create a Contact

     This request allows you to create a new contact within JobNimbus.

    **Notes**:

    * First Name, Last Name, First & Last Name, Display_Name, or Company Name are required
    * record_type_name is required and should be a workflow name defined in the customers JobNimbus
    contact workflow settings
    * status_name is required and should be a status defined within the record_type_name workflow
    * source_name is optional but if provided should be set to one of the lead source names defined in
    the customer's settings
    * Also accepts most of the fields listed in the \"GET /contacts\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1ContactsBody):  Example: {'first_name': 'Sammy G', 'last_name': 'Kent',
            'record_type_name': 'Customer', 'status_name': 'Lead', 'geo': {'lon': -88.687277, 'lat':
            37.149574}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1ContactsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1ContactsBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1ContactsResponse200]:
    r"""Create a Contact

     This request allows you to create a new contact within JobNimbus.

    **Notes**:

    * First Name, Last Name, First & Last Name, Display_Name, or Company Name are required
    * record_type_name is required and should be a workflow name defined in the customers JobNimbus
    contact workflow settings
    * status_name is required and should be a status defined within the record_type_name workflow
    * source_name is optional but if provided should be set to one of the lead source names defined in
    the customer's settings
    * Also accepts most of the fields listed in the \"GET /contacts\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1ContactsBody):  Example: {'first_name': 'Sammy G', 'last_name': 'Kent',
            'record_type_name': 'Customer', 'status_name': 'Lead', 'geo': {'lon': -88.687277, 'lat':
            37.149574}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1ContactsResponse200]
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
    body: Postapi1ContactsBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1ContactsResponse200]:
    r"""Create a Contact

     This request allows you to create a new contact within JobNimbus.

    **Notes**:

    * First Name, Last Name, First & Last Name, Display_Name, or Company Name are required
    * record_type_name is required and should be a workflow name defined in the customers JobNimbus
    contact workflow settings
    * status_name is required and should be a status defined within the record_type_name workflow
    * source_name is optional but if provided should be set to one of the lead source names defined in
    the customer's settings
    * Also accepts most of the fields listed in the \"GET /contacts\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1ContactsBody):  Example: {'first_name': 'Sammy G', 'last_name': 'Kent',
            'record_type_name': 'Customer', 'status_name': 'Lead', 'geo': {'lon': -88.687277, 'lat':
            37.149574}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1ContactsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
