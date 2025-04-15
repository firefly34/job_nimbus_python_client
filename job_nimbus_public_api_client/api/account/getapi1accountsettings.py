from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1_accountsettings_response_200 import Getapi1AccountsettingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    field: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["field"] = field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api1/account/settings",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1AccountsettingsResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1AccountsettingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1AccountsettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    field: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1AccountsettingsResponse200]:
    r"""Retrieve Group Information

     This request allows you to retrieve the configuration of a JobNimbus account's settings.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    **Response**:

    - If a field is passed then the API will return a value in that field from the customer object.

    - If a field is null then see an example of the partial response below:


    ```
    [
     {
     \"name\": \"Sales\",
     \"managers\": [
      \"managerid1\",
       \"managerid2\",
      \"managerid3\"
     ],
     \"members\": [
      \"memberid1\",
      \"memberid2\",
      \"memberid3\"
     ]
    },
    ...
    ]

     ```

    Args:
        field (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1AccountsettingsResponse200]
    """

    kwargs = _get_kwargs(
        field=field,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    field: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Getapi1AccountsettingsResponse200]:
    r"""Retrieve Group Information

     This request allows you to retrieve the configuration of a JobNimbus account's settings.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    **Response**:

    - If a field is passed then the API will return a value in that field from the customer object.

    - If a field is null then see an example of the partial response below:


    ```
    [
     {
     \"name\": \"Sales\",
     \"managers\": [
      \"managerid1\",
       \"managerid2\",
      \"managerid3\"
     ],
     \"members\": [
      \"memberid1\",
      \"memberid2\",
      \"memberid3\"
     ]
    },
    ...
    ]

     ```

    Args:
        field (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1AccountsettingsResponse200
    """

    return sync_detailed(
        client=client,
        field=field,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    field: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1AccountsettingsResponse200]:
    r"""Retrieve Group Information

     This request allows you to retrieve the configuration of a JobNimbus account's settings.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    **Response**:

    - If a field is passed then the API will return a value in that field from the customer object.

    - If a field is null then see an example of the partial response below:


    ```
    [
     {
     \"name\": \"Sales\",
     \"managers\": [
      \"managerid1\",
       \"managerid2\",
      \"managerid3\"
     ],
     \"members\": [
      \"memberid1\",
      \"memberid2\",
      \"memberid3\"
     ]
    },
    ...
    ]

     ```

    Args:
        field (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1AccountsettingsResponse200]
    """

    kwargs = _get_kwargs(
        field=field,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    field: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Getapi1AccountsettingsResponse200]:
    r"""Retrieve Group Information

     This request allows you to retrieve the configuration of a JobNimbus account's settings.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    **Response**:

    - If a field is passed then the API will return a value in that field from the customer object.

    - If a field is null then see an example of the partial response below:


    ```
    [
     {
     \"name\": \"Sales\",
     \"managers\": [
      \"managerid1\",
       \"managerid2\",
      \"managerid3\"
     ],
     \"members\": [
      \"memberid1\",
      \"memberid2\",
      \"memberid3\"
     ]
    },
    ...
    ]

     ```

    Args:
        field (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1AccountsettingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            field=field,
            authorization=authorization,
        )
    ).parsed
