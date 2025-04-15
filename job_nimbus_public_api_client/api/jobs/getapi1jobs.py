from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1_jobs_response_200 import Getapi1JobsResponse200
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
        "url": "/api1/jobs",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1JobsResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1JobsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1JobsResponse200]:
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
) -> Response[Getapi1JobsResponse200]:
    r"""Retrieve ALL Jobs

     This request allows you to retrieve all of the jobs within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---


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

    **Response**:

    Example of a partial response:

    ```
    {
        \"count\": 117,
        \"results\": [
        {
     \"recid\": 1001,
     \"customer\": \"3oz\",
     \"type\": \"job\",
     \"created_by\": \"3p0\",
     \"created_by_name\": \"Bot Barton\",
     \"date_created\": 1472567571,
     \"date_updated\": 1472567572,
     \"location\": {
      \"id\": 1,
      \"parent_id\": null
     },
     \"owners\": [
      {
       \"id\": \"3p0\"
      }
     ],
     \"is_active\": true,
     \"name\": \"Test job\",
     \"number\": \"1001\",
     \"record_type\": 5,
     \"record_type_name\": \"Residential\",
     \"status\": 19,
     \"status_name\": \"Lead\",
     \"description\": null,
     \"sales_rep\": \"3p0\",
     \"sales_rep_name\": \"Bob Barton\",
     \"address_line1\": \"100 N 52 E\",
     \"address_line2\": \"\",
     \"city\": \"American Fork\",
     \"state_text\": \"UT\",
     \"country_name\": \"United States\",
     \"zip\": \"84003\",
     \"jnid\": \"3pg\",
     \"geo\": {
      \"lat\": 40.387368,
      \"lon\": -111.789513
     },
     ...
    ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1JobsResponse200]
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
) -> Optional[Getapi1JobsResponse200]:
    r"""Retrieve ALL Jobs

     This request allows you to retrieve all of the jobs within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---


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

    **Response**:

    Example of a partial response:

    ```
    {
        \"count\": 117,
        \"results\": [
        {
     \"recid\": 1001,
     \"customer\": \"3oz\",
     \"type\": \"job\",
     \"created_by\": \"3p0\",
     \"created_by_name\": \"Bot Barton\",
     \"date_created\": 1472567571,
     \"date_updated\": 1472567572,
     \"location\": {
      \"id\": 1,
      \"parent_id\": null
     },
     \"owners\": [
      {
       \"id\": \"3p0\"
      }
     ],
     \"is_active\": true,
     \"name\": \"Test job\",
     \"number\": \"1001\",
     \"record_type\": 5,
     \"record_type_name\": \"Residential\",
     \"status\": 19,
     \"status_name\": \"Lead\",
     \"description\": null,
     \"sales_rep\": \"3p0\",
     \"sales_rep_name\": \"Bob Barton\",
     \"address_line1\": \"100 N 52 E\",
     \"address_line2\": \"\",
     \"city\": \"American Fork\",
     \"state_text\": \"UT\",
     \"country_name\": \"United States\",
     \"zip\": \"84003\",
     \"jnid\": \"3pg\",
     \"geo\": {
      \"lat\": 40.387368,
      \"lon\": -111.789513
     },
     ...
    ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1JobsResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1JobsResponse200]:
    r"""Retrieve ALL Jobs

     This request allows you to retrieve all of the jobs within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---


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

    **Response**:

    Example of a partial response:

    ```
    {
        \"count\": 117,
        \"results\": [
        {
     \"recid\": 1001,
     \"customer\": \"3oz\",
     \"type\": \"job\",
     \"created_by\": \"3p0\",
     \"created_by_name\": \"Bot Barton\",
     \"date_created\": 1472567571,
     \"date_updated\": 1472567572,
     \"location\": {
      \"id\": 1,
      \"parent_id\": null
     },
     \"owners\": [
      {
       \"id\": \"3p0\"
      }
     ],
     \"is_active\": true,
     \"name\": \"Test job\",
     \"number\": \"1001\",
     \"record_type\": 5,
     \"record_type_name\": \"Residential\",
     \"status\": 19,
     \"status_name\": \"Lead\",
     \"description\": null,
     \"sales_rep\": \"3p0\",
     \"sales_rep_name\": \"Bob Barton\",
     \"address_line1\": \"100 N 52 E\",
     \"address_line2\": \"\",
     \"city\": \"American Fork\",
     \"state_text\": \"UT\",
     \"country_name\": \"United States\",
     \"zip\": \"84003\",
     \"jnid\": \"3pg\",
     \"geo\": {
      \"lat\": 40.387368,
      \"lon\": -111.789513
     },
     ...
    ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1JobsResponse200]
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
) -> Optional[Getapi1JobsResponse200]:
    r"""Retrieve ALL Jobs

     This request allows you to retrieve all of the jobs within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---


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

    **Response**:

    Example of a partial response:

    ```
    {
        \"count\": 117,
        \"results\": [
        {
     \"recid\": 1001,
     \"customer\": \"3oz\",
     \"type\": \"job\",
     \"created_by\": \"3p0\",
     \"created_by_name\": \"Bot Barton\",
     \"date_created\": 1472567571,
     \"date_updated\": 1472567572,
     \"location\": {
      \"id\": 1,
      \"parent_id\": null
     },
     \"owners\": [
      {
       \"id\": \"3p0\"
      }
     ],
     \"is_active\": true,
     \"name\": \"Test job\",
     \"number\": \"1001\",
     \"record_type\": 5,
     \"record_type_name\": \"Residential\",
     \"status\": 19,
     \"status_name\": \"Lead\",
     \"description\": null,
     \"sales_rep\": \"3p0\",
     \"sales_rep_name\": \"Bob Barton\",
     \"address_line1\": \"100 N 52 E\",
     \"address_line2\": \"\",
     \"city\": \"American Fork\",
     \"state_text\": \"UT\",
     \"country_name\": \"United States\",
     \"zip\": \"84003\",
     \"jnid\": \"3pg\",
     \"geo\": {
      \"lat\": 40.387368,
      \"lon\": -111.789513
     },
     ...
    ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1JobsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
