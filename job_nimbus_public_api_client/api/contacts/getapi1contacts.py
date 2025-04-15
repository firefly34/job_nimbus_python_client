from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1_contacts_response_200 import Getapi1ContactsResponse200
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
        "url": "/api1/contacts",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1ContactsResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1ContactsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1ContactsResponse200]:
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
) -> Response[Getapi1ContactsResponse200]:
    r"""Retrieve ALL Contacts

     This request allows you to retrieve all of the contacts within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    <hr />

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
      \"recid\": 1003,
      \"customer\": \"29a\",
      \"type\": \"contact\",
      \"created_by\": \"29b\",
      \"created_by_name\": \"Sam Burnet\",
      \"date_created\": 1459789425,
      \"date_updated\": 1460051077,
      \"owners\": [
        {
          \"id\": \"29b\"
        }
      ],
      \"location\": {
        \"id\": 1,
        \"parent_id\": null,
        \"name\": \"Developer Account\"
      },
      \"first_name\": \"Bruce\",
      \"last_name\": \"Wayne\",
      \"company\": \"Wayne Enterprises\",
      \"description\": \"Likes to wear costumes...\",
      \"email\": \"bruce@batman.com\",
      \"home_phone\": \"8882223333\",
      \"mobile_phone\": \"\",
      \"work_phone\": \"\",
      \"fax_number\": \"\",
      \"address_line1\": \"123 S. Bat Street\",
      \"address_line2\": null,
      \"city\": \"Heber City\",
      \"state_text\": \"UT\",
      \"country_name\": \"United States\",
      \"zip\": \"84032\",
      \"website\": \"www.batman.com\",
      \"record_type\": 1,
      \"record_type_name\": \"Customer\",
      \"status\": 2,
      \"status_name\": \"Inspection\",
      \"source\": 1,
      \"source_name\": \"Referral\",
      \"sales_rep\": \"1m1\",
      \"sales_rep_name\": \"Sam Burnet\",
      \"jnid\": \"1l7\",
      \"geo\": {
        \"lat\": 0,
        \"lon\": 0
      },
      ...
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1ContactsResponse200]
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
) -> Optional[Getapi1ContactsResponse200]:
    r"""Retrieve ALL Contacts

     This request allows you to retrieve all of the contacts within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    <hr />

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
      \"recid\": 1003,
      \"customer\": \"29a\",
      \"type\": \"contact\",
      \"created_by\": \"29b\",
      \"created_by_name\": \"Sam Burnet\",
      \"date_created\": 1459789425,
      \"date_updated\": 1460051077,
      \"owners\": [
        {
          \"id\": \"29b\"
        }
      ],
      \"location\": {
        \"id\": 1,
        \"parent_id\": null,
        \"name\": \"Developer Account\"
      },
      \"first_name\": \"Bruce\",
      \"last_name\": \"Wayne\",
      \"company\": \"Wayne Enterprises\",
      \"description\": \"Likes to wear costumes...\",
      \"email\": \"bruce@batman.com\",
      \"home_phone\": \"8882223333\",
      \"mobile_phone\": \"\",
      \"work_phone\": \"\",
      \"fax_number\": \"\",
      \"address_line1\": \"123 S. Bat Street\",
      \"address_line2\": null,
      \"city\": \"Heber City\",
      \"state_text\": \"UT\",
      \"country_name\": \"United States\",
      \"zip\": \"84032\",
      \"website\": \"www.batman.com\",
      \"record_type\": 1,
      \"record_type_name\": \"Customer\",
      \"status\": 2,
      \"status_name\": \"Inspection\",
      \"source\": 1,
      \"source_name\": \"Referral\",
      \"sales_rep\": \"1m1\",
      \"sales_rep_name\": \"Sam Burnet\",
      \"jnid\": \"1l7\",
      \"geo\": {
        \"lat\": 0,
        \"lon\": 0
      },
      ...
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1ContactsResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1ContactsResponse200]:
    r"""Retrieve ALL Contacts

     This request allows you to retrieve all of the contacts within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    <hr />

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
      \"recid\": 1003,
      \"customer\": \"29a\",
      \"type\": \"contact\",
      \"created_by\": \"29b\",
      \"created_by_name\": \"Sam Burnet\",
      \"date_created\": 1459789425,
      \"date_updated\": 1460051077,
      \"owners\": [
        {
          \"id\": \"29b\"
        }
      ],
      \"location\": {
        \"id\": 1,
        \"parent_id\": null,
        \"name\": \"Developer Account\"
      },
      \"first_name\": \"Bruce\",
      \"last_name\": \"Wayne\",
      \"company\": \"Wayne Enterprises\",
      \"description\": \"Likes to wear costumes...\",
      \"email\": \"bruce@batman.com\",
      \"home_phone\": \"8882223333\",
      \"mobile_phone\": \"\",
      \"work_phone\": \"\",
      \"fax_number\": \"\",
      \"address_line1\": \"123 S. Bat Street\",
      \"address_line2\": null,
      \"city\": \"Heber City\",
      \"state_text\": \"UT\",
      \"country_name\": \"United States\",
      \"zip\": \"84032\",
      \"website\": \"www.batman.com\",
      \"record_type\": 1,
      \"record_type_name\": \"Customer\",
      \"status\": 2,
      \"status_name\": \"Inspection\",
      \"source\": 1,
      \"source_name\": \"Referral\",
      \"sales_rep\": \"1m1\",
      \"sales_rep_name\": \"Sam Burnet\",
      \"jnid\": \"1l7\",
      \"geo\": {
        \"lat\": 0,
        \"lon\": 0
      },
      ...
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1ContactsResponse200]
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
) -> Optional[Getapi1ContactsResponse200]:
    r"""Retrieve ALL Contacts

     This request allows you to retrieve all of the contacts within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    <hr />

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
      \"recid\": 1003,
      \"customer\": \"29a\",
      \"type\": \"contact\",
      \"created_by\": \"29b\",
      \"created_by_name\": \"Sam Burnet\",
      \"date_created\": 1459789425,
      \"date_updated\": 1460051077,
      \"owners\": [
        {
          \"id\": \"29b\"
        }
      ],
      \"location\": {
        \"id\": 1,
        \"parent_id\": null,
        \"name\": \"Developer Account\"
      },
      \"first_name\": \"Bruce\",
      \"last_name\": \"Wayne\",
      \"company\": \"Wayne Enterprises\",
      \"description\": \"Likes to wear costumes...\",
      \"email\": \"bruce@batman.com\",
      \"home_phone\": \"8882223333\",
      \"mobile_phone\": \"\",
      \"work_phone\": \"\",
      \"fax_number\": \"\",
      \"address_line1\": \"123 S. Bat Street\",
      \"address_line2\": null,
      \"city\": \"Heber City\",
      \"state_text\": \"UT\",
      \"country_name\": \"United States\",
      \"zip\": \"84032\",
      \"website\": \"www.batman.com\",
      \"record_type\": 1,
      \"record_type_name\": \"Customer\",
      \"status\": 2,
      \"status_name\": \"Inspection\",
      \"source\": 1,
      \"source_name\": \"Referral\",
      \"sales_rep\": \"1m1\",
      \"sales_rep_name\": \"Sam Burnet\",
      \"jnid\": \"1l7\",
      \"geo\": {
        \"lat\": 0,
        \"lon\": 0
      },
      ...
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1ContactsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
