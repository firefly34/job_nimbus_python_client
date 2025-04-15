from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1_tasks_response_200 import Getapi1TasksResponse200
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
        "url": "/api1/tasks",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1TasksResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1TasksResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1TasksResponse200]:
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
) -> Response[Getapi1TasksResponse200]:
    r"""Retrieve ALL Tasks

     This request allows you to retrieve all of the tasks within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:
    Example of a partial response:
    ```
    {
        \"count\": 117,
        \"results\": [
            {
                \"external_id\": null,
                \"recid\": 1145,
                \"number\": \"1145\",
                \"customer\": \"jagpt\",
                \"type\": \"task\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"date_created\": 1547742470,
                \"date_updated\": 1547742470,
                \"is_active\": true,
                \"is_archived\": false,
                \"primary\": null,
                \"actual_time\": 0,
                \"estimated_time\": 0,
                \"title\": \"Custom Task Type\",
                \"location\": {
                    \"id\": 1
                },
                \"description\": \"New custom task type\",
                \"record_type\": 6,
                \"record_type_name\": \"Custom Task Type\",
                \"priority\": 0,
                \"date_start\": 1547712000,
                \"date_sort\": null,
                \"date_end\": 0,
                \"is_completed\": false,
                \"hide_from_calendarview\": false,
                \"hide_from_tasklist\": false,
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"subcontractors\": [],
                \"related\": [
                    {
                        \"id\": \"ql1a9\",
                        \"name\": \"Martin ROBERTS\",
                        \"number\": \"1096\",
                        \"type\": \"contact\"
                    }
                ],
                \"jnid\": \"14yspl\",
                \"tags\": [],
                \"rules\": []
            },
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1TasksResponse200]
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
) -> Optional[Getapi1TasksResponse200]:
    r"""Retrieve ALL Tasks

     This request allows you to retrieve all of the tasks within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:
    Example of a partial response:
    ```
    {
        \"count\": 117,
        \"results\": [
            {
                \"external_id\": null,
                \"recid\": 1145,
                \"number\": \"1145\",
                \"customer\": \"jagpt\",
                \"type\": \"task\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"date_created\": 1547742470,
                \"date_updated\": 1547742470,
                \"is_active\": true,
                \"is_archived\": false,
                \"primary\": null,
                \"actual_time\": 0,
                \"estimated_time\": 0,
                \"title\": \"Custom Task Type\",
                \"location\": {
                    \"id\": 1
                },
                \"description\": \"New custom task type\",
                \"record_type\": 6,
                \"record_type_name\": \"Custom Task Type\",
                \"priority\": 0,
                \"date_start\": 1547712000,
                \"date_sort\": null,
                \"date_end\": 0,
                \"is_completed\": false,
                \"hide_from_calendarview\": false,
                \"hide_from_tasklist\": false,
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"subcontractors\": [],
                \"related\": [
                    {
                        \"id\": \"ql1a9\",
                        \"name\": \"Martin ROBERTS\",
                        \"number\": \"1096\",
                        \"type\": \"contact\"
                    }
                ],
                \"jnid\": \"14yspl\",
                \"tags\": [],
                \"rules\": []
            },
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1TasksResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1TasksResponse200]:
    r"""Retrieve ALL Tasks

     This request allows you to retrieve all of the tasks within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:
    Example of a partial response:
    ```
    {
        \"count\": 117,
        \"results\": [
            {
                \"external_id\": null,
                \"recid\": 1145,
                \"number\": \"1145\",
                \"customer\": \"jagpt\",
                \"type\": \"task\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"date_created\": 1547742470,
                \"date_updated\": 1547742470,
                \"is_active\": true,
                \"is_archived\": false,
                \"primary\": null,
                \"actual_time\": 0,
                \"estimated_time\": 0,
                \"title\": \"Custom Task Type\",
                \"location\": {
                    \"id\": 1
                },
                \"description\": \"New custom task type\",
                \"record_type\": 6,
                \"record_type_name\": \"Custom Task Type\",
                \"priority\": 0,
                \"date_start\": 1547712000,
                \"date_sort\": null,
                \"date_end\": 0,
                \"is_completed\": false,
                \"hide_from_calendarview\": false,
                \"hide_from_tasklist\": false,
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"subcontractors\": [],
                \"related\": [
                    {
                        \"id\": \"ql1a9\",
                        \"name\": \"Martin ROBERTS\",
                        \"number\": \"1096\",
                        \"type\": \"contact\"
                    }
                ],
                \"jnid\": \"14yspl\",
                \"tags\": [],
                \"rules\": []
            },
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1TasksResponse200]
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
) -> Optional[Getapi1TasksResponse200]:
    r"""Retrieve ALL Tasks

     This request allows you to retrieve all of the tasks within a JobNimbus account.

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:
    Example of a partial response:
    ```
    {
        \"count\": 117,
        \"results\": [
            {
                \"external_id\": null,
                \"recid\": 1145,
                \"number\": \"1145\",
                \"customer\": \"jagpt\",
                \"type\": \"task\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"date_created\": 1547742470,
                \"date_updated\": 1547742470,
                \"is_active\": true,
                \"is_archived\": false,
                \"primary\": null,
                \"actual_time\": 0,
                \"estimated_time\": 0,
                \"title\": \"Custom Task Type\",
                \"location\": {
                    \"id\": 1
                },
                \"description\": \"New custom task type\",
                \"record_type\": 6,
                \"record_type_name\": \"Custom Task Type\",
                \"priority\": 0,
                \"date_start\": 1547712000,
                \"date_sort\": null,
                \"date_end\": 0,
                \"is_completed\": false,
                \"hide_from_calendarview\": false,
                \"hide_from_tasklist\": false,
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"subcontractors\": [],
                \"related\": [
                    {
                        \"id\": \"ql1a9\",
                        \"name\": \"Martin ROBERTS\",
                        \"number\": \"1096\",
                        \"type\": \"contact\"
                    }
                ],
                \"jnid\": \"14yspl\",
                \"tags\": [],
                \"rules\": []
            },
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1TasksResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
