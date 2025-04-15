from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_accountcustomfield_response_200 import Postapi1AccountcustomfieldResponse200
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
        "url": "/api1/account/customfield",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1AccountcustomfieldResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1AccountcustomfieldResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1AccountcustomfieldResponse200]:
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
) -> Response[Postapi1AccountcustomfieldResponse200]:
    r"""Create a Custom Field

     This request allows you to create a new custom field within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a custom field with that name already exists, then the API endpoint will return with a response
    with the status for that custom field.
    If the custom field didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"title\": \"new2\",
        \"type\": \"string\",
        \"visible\": true,
        \"is_currency\": false,
        \"is_ddn\": true,
        \"is_required\": false,
        \"options\": [
            \"test\",
            \"test1\"
        ],
        \"field\": \"cf_string_7\"
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "title":"Claim Number", //custom field title/UI name, it's required parameter
                "object_type":"contact", //object type, it's requied paramter, (valid values: contact,
            job, workorder)
                "type": "dropdown", //custom field type, it's required paramter (valid values: date,
            double, long, string, boolean, dropdown)
                "is_required": true/false, //optional field (default = false)
                "is_currency": true/false, //optional field (default = false), only valid for
            field_type = double
                "options": [ "val1", "val2", "val3"] //requited field if field_type is dropdown (all
            possible options)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountcustomfieldResponse200]
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
) -> Optional[Postapi1AccountcustomfieldResponse200]:
    r"""Create a Custom Field

     This request allows you to create a new custom field within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a custom field with that name already exists, then the API endpoint will return with a response
    with the status for that custom field.
    If the custom field didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"title\": \"new2\",
        \"type\": \"string\",
        \"visible\": true,
        \"is_currency\": false,
        \"is_ddn\": true,
        \"is_required\": false,
        \"options\": [
            \"test\",
            \"test1\"
        ],
        \"field\": \"cf_string_7\"
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "title":"Claim Number", //custom field title/UI name, it's required parameter
                "object_type":"contact", //object type, it's requied paramter, (valid values: contact,
            job, workorder)
                "type": "dropdown", //custom field type, it's required paramter (valid values: date,
            double, long, string, boolean, dropdown)
                "is_required": true/false, //optional field (default = false)
                "is_currency": true/false, //optional field (default = false), only valid for
            field_type = double
                "options": [ "val1", "val2", "val3"] //requited field if field_type is dropdown (all
            possible options)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountcustomfieldResponse200
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
) -> Response[Postapi1AccountcustomfieldResponse200]:
    r"""Create a Custom Field

     This request allows you to create a new custom field within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a custom field with that name already exists, then the API endpoint will return with a response
    with the status for that custom field.
    If the custom field didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"title\": \"new2\",
        \"type\": \"string\",
        \"visible\": true,
        \"is_currency\": false,
        \"is_ddn\": true,
        \"is_required\": false,
        \"options\": [
            \"test\",
            \"test1\"
        ],
        \"field\": \"cf_string_7\"
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "title":"Claim Number", //custom field title/UI name, it's required parameter
                "object_type":"contact", //object type, it's requied paramter, (valid values: contact,
            job, workorder)
                "type": "dropdown", //custom field type, it's required paramter (valid values: date,
            double, long, string, boolean, dropdown)
                "is_required": true/false, //optional field (default = false)
                "is_currency": true/false, //optional field (default = false), only valid for
            field_type = double
                "options": [ "val1", "val2", "val3"] //requited field if field_type is dropdown (all
            possible options)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountcustomfieldResponse200]
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
) -> Optional[Postapi1AccountcustomfieldResponse200]:
    r"""Create a Custom Field

     This request allows you to create a new custom field within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If a custom field with that name already exists, then the API endpoint will return with a response
    with the status for that custom field.
    If the custom field didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"title\": \"new2\",
        \"type\": \"string\",
        \"visible\": true,
        \"is_currency\": false,
        \"is_ddn\": true,
        \"is_required\": false,
        \"options\": [
            \"test\",
            \"test1\"
        ],
        \"field\": \"cf_string_7\"
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "title":"Claim Number", //custom field title/UI name, it's required parameter
                "object_type":"contact", //object type, it's requied paramter, (valid values: contact,
            job, workorder)
                "type": "dropdown", //custom field type, it's required paramter (valid values: date,
            double, long, string, boolean, dropdown)
                "is_required": true/false, //optional field (default = false)
                "is_currency": true/false, //optional field (default = false), only valid for
            field_type = double
                "options": [ "val1", "val2", "val3"] //requited field if field_type is dropdown (all
            possible options)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountcustomfieldResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
