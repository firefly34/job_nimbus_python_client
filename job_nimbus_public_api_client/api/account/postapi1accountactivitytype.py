from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_accountactivitytype_response_200 import Postapi1AccountactivitytypeResponse200
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
        "url": "/api1/account/activitytype",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1AccountactivitytypeResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1AccountactivitytypeResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1AccountactivitytypeResponse200]:
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
) -> Response[Postapi1AccountactivitytypeResponse200]:
    r"""Create an Activity Type

     This request allows you to create a new activity type within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If an activity type with that name already exists, then the API endpoint will return with a response
    with the status for that activity type.
    If the activity type didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"ActivityTypeId\": 1518,
        \"TypeName\": \"Note\",
        \"ShowInJobShare\": true,
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Task", //task type name, it's required parameter
                "IsActive": true/false, //optional field (default = true)
                "HideFromCalendarView": true/false, //optional field (default = false)
                "HideFromTaskList": true/false, //optional field (default = false)
                "DefaultName": "Task Name" //optional field (default value will be same as name)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountactivitytypeResponse200]
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
) -> Optional[Postapi1AccountactivitytypeResponse200]:
    r"""Create an Activity Type

     This request allows you to create a new activity type within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If an activity type with that name already exists, then the API endpoint will return with a response
    with the status for that activity type.
    If the activity type didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"ActivityTypeId\": 1518,
        \"TypeName\": \"Note\",
        \"ShowInJobShare\": true,
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Task", //task type name, it's required parameter
                "IsActive": true/false, //optional field (default = true)
                "HideFromCalendarView": true/false, //optional field (default = false)
                "HideFromTaskList": true/false, //optional field (default = false)
                "DefaultName": "Task Name" //optional field (default value will be same as name)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountactivitytypeResponse200
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
) -> Response[Postapi1AccountactivitytypeResponse200]:
    r"""Create an Activity Type

     This request allows you to create a new activity type within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If an activity type with that name already exists, then the API endpoint will return with a response
    with the status for that activity type.
    If the activity type didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"ActivityTypeId\": 1518,
        \"TypeName\": \"Note\",
        \"ShowInJobShare\": true,
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Task", //task type name, it's required parameter
                "IsActive": true/false, //optional field (default = true)
                "HideFromCalendarView": true/false, //optional field (default = false)
                "HideFromTaskList": true/false, //optional field (default = false)
                "DefaultName": "Task Name" //optional field (default value will be same as name)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1AccountactivitytypeResponse200]
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
) -> Optional[Postapi1AccountactivitytypeResponse200]:
    r"""Create an Activity Type

     This request allows you to create a new activity type within a Jobnimbus account. Note: The token
    used must have an access profile level with access to the account settings page.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    If an activity type with that name already exists, then the API endpoint will return with a response
    with the status for that activity type.
    If the activity type didn't exist, then the API endpoint will return a response similar to the
    example, below:

    ```
    {
        \"ActivityTypeId\": 1518,
        \"TypeName\": \"Note\",
        \"ShowInJobShare\": true,
        \"IsActive\": true
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
                "TypeName":"Task", //task type name, it's required parameter
                "IsActive": true/false, //optional field (default = true)
                "HideFromCalendarView": true/false, //optional field (default = false)
                "HideFromTaskList": true/false, //optional field (default = false)
                "DefaultName": "Task Name" //optional field (default value will be same as name)
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1AccountactivitytypeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
