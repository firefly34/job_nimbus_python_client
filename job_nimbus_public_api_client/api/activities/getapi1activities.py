from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1_activities_response_200 import Getapi1ActivitiesResponse200
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
        "url": "/api1/activities",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1ActivitiesResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1ActivitiesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1ActivitiesResponse200]:
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
) -> Response[Getapi1ActivitiesResponse200]:
    r"""Retrieve ALL Activities

     This request allows you to retrieve all of the activities within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Request Parameters**

    Request parameters should be passed in the query string

    size - number of elements to return (default: 1000)

    from - zero based starting point to be used for pagination (default: 0)

    sort_field - which field to sort by (default: date_created)

    sort_direction = which direction to sort the results (default: 'desc')

    fields - limit which fields to include in response (default: all fields will be included)

    filter - URL encoded JSON filter object i.e.:

    ```

    {
        \"must\": [
            {
                \"range\": {
                    \"date_created\": {
                        \"gte\": 1459749600,
                        \"lte\": 1459835940
                    }
                }
            }
        ]
    }
    ```

    <hr />

    **Response**:

    Example of a partial response:
    ```
    {
      \"count\": 10,
      \"activity\": [
      {
        \"type\": \"activity\",
        \"customer\": \"7z76o\",
        \"location\": {
            \"id\": 1
        },
        \"primary\": {
            \"new_status\": 13,
            \"id\": \"he2d2\",
            \"name\": \"Clark Kent\",
            \"type\": \"contact\",
            \"number\": \"1017\"
        },
        \"is_active\": true,
        \"note\": \"Contact Created\",
        \"is_status_change\": true,
        \"record_type_name\": \"Contact Created\",
        \"owners\": [],
        \"related\": [
            {
                \"id\": \"he2d2\",
                \"type\": \"contact\",
                \"name\": \"Clark Kent\",
                \"number\": \"1017\"
            }
        ],
        \"jnid\": \"he2d3\",
        \"created_by\": \"neo\",
        \"created_by_name\": \"Thomas Anderson\",
        \"date_created\": 1512763337,
        \"date_updated\": 1512763337,
        \"is_archived\": false,
        \"is_editable\": false
      },
      ...
    ]
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1ActivitiesResponse200]
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
) -> Optional[Getapi1ActivitiesResponse200]:
    r"""Retrieve ALL Activities

     This request allows you to retrieve all of the activities within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Request Parameters**

    Request parameters should be passed in the query string

    size - number of elements to return (default: 1000)

    from - zero based starting point to be used for pagination (default: 0)

    sort_field - which field to sort by (default: date_created)

    sort_direction = which direction to sort the results (default: 'desc')

    fields - limit which fields to include in response (default: all fields will be included)

    filter - URL encoded JSON filter object i.e.:

    ```

    {
        \"must\": [
            {
                \"range\": {
                    \"date_created\": {
                        \"gte\": 1459749600,
                        \"lte\": 1459835940
                    }
                }
            }
        ]
    }
    ```

    <hr />

    **Response**:

    Example of a partial response:
    ```
    {
      \"count\": 10,
      \"activity\": [
      {
        \"type\": \"activity\",
        \"customer\": \"7z76o\",
        \"location\": {
            \"id\": 1
        },
        \"primary\": {
            \"new_status\": 13,
            \"id\": \"he2d2\",
            \"name\": \"Clark Kent\",
            \"type\": \"contact\",
            \"number\": \"1017\"
        },
        \"is_active\": true,
        \"note\": \"Contact Created\",
        \"is_status_change\": true,
        \"record_type_name\": \"Contact Created\",
        \"owners\": [],
        \"related\": [
            {
                \"id\": \"he2d2\",
                \"type\": \"contact\",
                \"name\": \"Clark Kent\",
                \"number\": \"1017\"
            }
        ],
        \"jnid\": \"he2d3\",
        \"created_by\": \"neo\",
        \"created_by_name\": \"Thomas Anderson\",
        \"date_created\": 1512763337,
        \"date_updated\": 1512763337,
        \"is_archived\": false,
        \"is_editable\": false
      },
      ...
    ]
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1ActivitiesResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1ActivitiesResponse200]:
    r"""Retrieve ALL Activities

     This request allows you to retrieve all of the activities within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Request Parameters**

    Request parameters should be passed in the query string

    size - number of elements to return (default: 1000)

    from - zero based starting point to be used for pagination (default: 0)

    sort_field - which field to sort by (default: date_created)

    sort_direction = which direction to sort the results (default: 'desc')

    fields - limit which fields to include in response (default: all fields will be included)

    filter - URL encoded JSON filter object i.e.:

    ```

    {
        \"must\": [
            {
                \"range\": {
                    \"date_created\": {
                        \"gte\": 1459749600,
                        \"lte\": 1459835940
                    }
                }
            }
        ]
    }
    ```

    <hr />

    **Response**:

    Example of a partial response:
    ```
    {
      \"count\": 10,
      \"activity\": [
      {
        \"type\": \"activity\",
        \"customer\": \"7z76o\",
        \"location\": {
            \"id\": 1
        },
        \"primary\": {
            \"new_status\": 13,
            \"id\": \"he2d2\",
            \"name\": \"Clark Kent\",
            \"type\": \"contact\",
            \"number\": \"1017\"
        },
        \"is_active\": true,
        \"note\": \"Contact Created\",
        \"is_status_change\": true,
        \"record_type_name\": \"Contact Created\",
        \"owners\": [],
        \"related\": [
            {
                \"id\": \"he2d2\",
                \"type\": \"contact\",
                \"name\": \"Clark Kent\",
                \"number\": \"1017\"
            }
        ],
        \"jnid\": \"he2d3\",
        \"created_by\": \"neo\",
        \"created_by_name\": \"Thomas Anderson\",
        \"date_created\": 1512763337,
        \"date_updated\": 1512763337,
        \"is_archived\": false,
        \"is_editable\": false
      },
      ...
    ]
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1ActivitiesResponse200]
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
) -> Optional[Getapi1ActivitiesResponse200]:
    r"""Retrieve ALL Activities

     This request allows you to retrieve all of the activities within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Request Parameters**

    Request parameters should be passed in the query string

    size - number of elements to return (default: 1000)

    from - zero based starting point to be used for pagination (default: 0)

    sort_field - which field to sort by (default: date_created)

    sort_direction = which direction to sort the results (default: 'desc')

    fields - limit which fields to include in response (default: all fields will be included)

    filter - URL encoded JSON filter object i.e.:

    ```

    {
        \"must\": [
            {
                \"range\": {
                    \"date_created\": {
                        \"gte\": 1459749600,
                        \"lte\": 1459835940
                    }
                }
            }
        ]
    }
    ```

    <hr />

    **Response**:

    Example of a partial response:
    ```
    {
      \"count\": 10,
      \"activity\": [
      {
        \"type\": \"activity\",
        \"customer\": \"7z76o\",
        \"location\": {
            \"id\": 1
        },
        \"primary\": {
            \"new_status\": 13,
            \"id\": \"he2d2\",
            \"name\": \"Clark Kent\",
            \"type\": \"contact\",
            \"number\": \"1017\"
        },
        \"is_active\": true,
        \"note\": \"Contact Created\",
        \"is_status_change\": true,
        \"record_type_name\": \"Contact Created\",
        \"owners\": [],
        \"related\": [
            {
                \"id\": \"he2d2\",
                \"type\": \"contact\",
                \"name\": \"Clark Kent\",
                \"number\": \"1017\"
            }
        ],
        \"jnid\": \"he2d3\",
        \"created_by\": \"neo\",
        \"created_by_name\": \"Thomas Anderson\",
        \"date_created\": 1512763337,
        \"date_updated\": 1512763337,
        \"is_archived\": false,
        \"is_editable\": false
      },
      ...
    ]
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1ActivitiesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
