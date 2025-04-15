from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_activities_response_200 import Postapi1ActivitiesResponse200
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
        "url": "/api1/activities",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1ActivitiesResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1ActivitiesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1ActivitiesResponse200]:
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
) -> Response[Postapi1ActivitiesResponse200]:
    r"""Create an Activity

     This request allows you to create a new Activity within JobNimbus.

    **Notes**:

    * note, record_type_name and primary.id should be included.
    * Also accepts most of the fields listed in the \"GET /activities\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
              "note": "My new note",
              "date_created": 1513108061,
              "record_type_name": "Note",
               "primary": {
                "id": "i97"
              },
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1ActivitiesResponse200]
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
) -> Optional[Postapi1ActivitiesResponse200]:
    r"""Create an Activity

     This request allows you to create a new Activity within JobNimbus.

    **Notes**:

    * note, record_type_name and primary.id should be included.
    * Also accepts most of the fields listed in the \"GET /activities\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
              "note": "My new note",
              "date_created": 1513108061,
              "record_type_name": "Note",
               "primary": {
                "id": "i97"
              },
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1ActivitiesResponse200
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
) -> Response[Postapi1ActivitiesResponse200]:
    r"""Create an Activity

     This request allows you to create a new Activity within JobNimbus.

    **Notes**:

    * note, record_type_name and primary.id should be included.
    * Also accepts most of the fields listed in the \"GET /activities\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
              "note": "My new note",
              "date_created": 1513108061,
              "record_type_name": "Note",
               "primary": {
                "id": "i97"
              },
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1ActivitiesResponse200]
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
) -> Optional[Postapi1ActivitiesResponse200]:
    r"""Create an Activity

     This request allows you to create a new Activity within JobNimbus.

    **Notes**:

    * note, record_type_name and primary.id should be included.
    * Also accepts most of the fields listed in the \"GET /activities\" response

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (str):  Example: {
              "note": "My new note",
              "date_created": 1513108061,
              "record_type_name": "Note",
               "primary": {
                "id": "i97"
              },
            }.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1ActivitiesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
