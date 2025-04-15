from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1v2_estimates_response_200 import Getapi1V2EstimatesResponse200
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
        "url": "/api1/v2/estimates",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1V2EstimatesResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1V2EstimatesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1V2EstimatesResponse200]:
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
) -> Response[Getapi1V2EstimatesResponse200]:
    r"""Retrieve ALL Estimates

     ### Retrieve Estimates

    This endpoint allows you to retrieve all estimates within a JobNimbus account.

    ---

    **Request Parameters:**

    - `from` (optional): Starting index for pagination (e.g., 10)

    - `size` (optional): Number of results to return (e.g., 5)


    ---

    **Response:**

    The response will contain an array of estimates with the following fields:

    - `attachment_id`: ID of the attachment

    - `cost`: Total cost of the estimate

    - `created_by`: ID of the user who created the estimate

    - `created_by_name`: Name of the user who created the estimate

    - `customer`: ID of the customer associated with the estimate

    - `date_created`: Timestamp of the creation date

    - `date_estimate`: Timestamp of the estimate date

    - `date_sign_requested`: Timestamp of the sign request date

    - `date_signed`: Timestamp of the sign date

    - `date_status_change`: Timestamp of the status change date

    - `date_updated`: Timestamp of the last update

    - `esigned`: Boolean indicating if the estimate is e-signed

    - `guid`: Unique identifier of the estimate

    - `is_active`: Boolean indicating if the estimate is active

    - `is_archived`: Boolean indicating if the estimate is archived

    - `items`: Array of items within the estimate, each containing amount, cost, item type, name, price,
    quantity, and unit of measure

    - `jnid`: ID of the estimate

    - `location`: Object containing the ID of the location

    - `margin`: Margin of the estimate

    - `number`: Estimate number

    - `owners`: Array of owners, each containing the ID

    - `recid`: Record ID

    - `related`: Array of related entities, each containing ID, name, number, and type

    - `sales_rep`: ID of the sales representative

    - `sales_rep_name`: Name of the sales representative

    - `sections`: Array of sections

    - `signature_status`: Status of the signature

    - `source`: Source of the estimate

    - `status`: Status code of the estimate

    - `status_name`: Name of the status

    - `subtotal`: Subtotal of the estimate

    - `tax`: Tax amount

    - `template_id`: ID of the template used for the estimate

    - `total`: Total amount of the estimate

    - `type`: always 'estimate'


    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_estimate\": 1600000000,
                \"date_sign_requested\": 1600000000,
                \"date_signed\": 1600000000,
                \"date_status_change\": 1600000000,
                \"date_updated\": 1600000000,
                \"esigned\": false,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"item_type\": \"material\",
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"Estimate_ID\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"number\": \"EST-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"recid\": 1000,
                \"related\": [
                    {
                        \"id\": \"JOB_ID_1\",
                        \"name\": \"Sample Project / SAMPLE-ID\",
                        \"number\": \"1000\",
                        \"type\": \"job\"
                    },
                    {
                        \"id\": \"CONTACT_ID_1\",
                        \"name\": \"John Doe (SAMPLE-ID)\",
                        \"number\": \"1001\",
                        \"type\": \"contact\"
                    }
                ],
                \"sales_rep\": \"salesrepjnid\",
                \"sales_rep_name\": \"Jane Smith\",
                \"sections\": [],
                \"status\": 4,
                \"status_name\": \"Closed\",
                \"subtotal\": 10000,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"total\": 10000,
                \"type\": \"estimate\"
            }
        ]
    }

     ```

    **Response Codes**:

    - HTTP Status 200: Success

    - Any other status code: Failure with an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2EstimatesResponse200]
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
) -> Optional[Getapi1V2EstimatesResponse200]:
    r"""Retrieve ALL Estimates

     ### Retrieve Estimates

    This endpoint allows you to retrieve all estimates within a JobNimbus account.

    ---

    **Request Parameters:**

    - `from` (optional): Starting index for pagination (e.g., 10)

    - `size` (optional): Number of results to return (e.g., 5)


    ---

    **Response:**

    The response will contain an array of estimates with the following fields:

    - `attachment_id`: ID of the attachment

    - `cost`: Total cost of the estimate

    - `created_by`: ID of the user who created the estimate

    - `created_by_name`: Name of the user who created the estimate

    - `customer`: ID of the customer associated with the estimate

    - `date_created`: Timestamp of the creation date

    - `date_estimate`: Timestamp of the estimate date

    - `date_sign_requested`: Timestamp of the sign request date

    - `date_signed`: Timestamp of the sign date

    - `date_status_change`: Timestamp of the status change date

    - `date_updated`: Timestamp of the last update

    - `esigned`: Boolean indicating if the estimate is e-signed

    - `guid`: Unique identifier of the estimate

    - `is_active`: Boolean indicating if the estimate is active

    - `is_archived`: Boolean indicating if the estimate is archived

    - `items`: Array of items within the estimate, each containing amount, cost, item type, name, price,
    quantity, and unit of measure

    - `jnid`: ID of the estimate

    - `location`: Object containing the ID of the location

    - `margin`: Margin of the estimate

    - `number`: Estimate number

    - `owners`: Array of owners, each containing the ID

    - `recid`: Record ID

    - `related`: Array of related entities, each containing ID, name, number, and type

    - `sales_rep`: ID of the sales representative

    - `sales_rep_name`: Name of the sales representative

    - `sections`: Array of sections

    - `signature_status`: Status of the signature

    - `source`: Source of the estimate

    - `status`: Status code of the estimate

    - `status_name`: Name of the status

    - `subtotal`: Subtotal of the estimate

    - `tax`: Tax amount

    - `template_id`: ID of the template used for the estimate

    - `total`: Total amount of the estimate

    - `type`: always 'estimate'


    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_estimate\": 1600000000,
                \"date_sign_requested\": 1600000000,
                \"date_signed\": 1600000000,
                \"date_status_change\": 1600000000,
                \"date_updated\": 1600000000,
                \"esigned\": false,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"item_type\": \"material\",
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"Estimate_ID\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"number\": \"EST-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"recid\": 1000,
                \"related\": [
                    {
                        \"id\": \"JOB_ID_1\",
                        \"name\": \"Sample Project / SAMPLE-ID\",
                        \"number\": \"1000\",
                        \"type\": \"job\"
                    },
                    {
                        \"id\": \"CONTACT_ID_1\",
                        \"name\": \"John Doe (SAMPLE-ID)\",
                        \"number\": \"1001\",
                        \"type\": \"contact\"
                    }
                ],
                \"sales_rep\": \"salesrepjnid\",
                \"sales_rep_name\": \"Jane Smith\",
                \"sections\": [],
                \"status\": 4,
                \"status_name\": \"Closed\",
                \"subtotal\": 10000,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"total\": 10000,
                \"type\": \"estimate\"
            }
        ]
    }

     ```

    **Response Codes**:

    - HTTP Status 200: Success

    - Any other status code: Failure with an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2EstimatesResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1V2EstimatesResponse200]:
    r"""Retrieve ALL Estimates

     ### Retrieve Estimates

    This endpoint allows you to retrieve all estimates within a JobNimbus account.

    ---

    **Request Parameters:**

    - `from` (optional): Starting index for pagination (e.g., 10)

    - `size` (optional): Number of results to return (e.g., 5)


    ---

    **Response:**

    The response will contain an array of estimates with the following fields:

    - `attachment_id`: ID of the attachment

    - `cost`: Total cost of the estimate

    - `created_by`: ID of the user who created the estimate

    - `created_by_name`: Name of the user who created the estimate

    - `customer`: ID of the customer associated with the estimate

    - `date_created`: Timestamp of the creation date

    - `date_estimate`: Timestamp of the estimate date

    - `date_sign_requested`: Timestamp of the sign request date

    - `date_signed`: Timestamp of the sign date

    - `date_status_change`: Timestamp of the status change date

    - `date_updated`: Timestamp of the last update

    - `esigned`: Boolean indicating if the estimate is e-signed

    - `guid`: Unique identifier of the estimate

    - `is_active`: Boolean indicating if the estimate is active

    - `is_archived`: Boolean indicating if the estimate is archived

    - `items`: Array of items within the estimate, each containing amount, cost, item type, name, price,
    quantity, and unit of measure

    - `jnid`: ID of the estimate

    - `location`: Object containing the ID of the location

    - `margin`: Margin of the estimate

    - `number`: Estimate number

    - `owners`: Array of owners, each containing the ID

    - `recid`: Record ID

    - `related`: Array of related entities, each containing ID, name, number, and type

    - `sales_rep`: ID of the sales representative

    - `sales_rep_name`: Name of the sales representative

    - `sections`: Array of sections

    - `signature_status`: Status of the signature

    - `source`: Source of the estimate

    - `status`: Status code of the estimate

    - `status_name`: Name of the status

    - `subtotal`: Subtotal of the estimate

    - `tax`: Tax amount

    - `template_id`: ID of the template used for the estimate

    - `total`: Total amount of the estimate

    - `type`: always 'estimate'


    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_estimate\": 1600000000,
                \"date_sign_requested\": 1600000000,
                \"date_signed\": 1600000000,
                \"date_status_change\": 1600000000,
                \"date_updated\": 1600000000,
                \"esigned\": false,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"item_type\": \"material\",
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"Estimate_ID\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"number\": \"EST-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"recid\": 1000,
                \"related\": [
                    {
                        \"id\": \"JOB_ID_1\",
                        \"name\": \"Sample Project / SAMPLE-ID\",
                        \"number\": \"1000\",
                        \"type\": \"job\"
                    },
                    {
                        \"id\": \"CONTACT_ID_1\",
                        \"name\": \"John Doe (SAMPLE-ID)\",
                        \"number\": \"1001\",
                        \"type\": \"contact\"
                    }
                ],
                \"sales_rep\": \"salesrepjnid\",
                \"sales_rep_name\": \"Jane Smith\",
                \"sections\": [],
                \"status\": 4,
                \"status_name\": \"Closed\",
                \"subtotal\": 10000,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"total\": 10000,
                \"type\": \"estimate\"
            }
        ]
    }

     ```

    **Response Codes**:

    - HTTP Status 200: Success

    - Any other status code: Failure with an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2EstimatesResponse200]
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
) -> Optional[Getapi1V2EstimatesResponse200]:
    r"""Retrieve ALL Estimates

     ### Retrieve Estimates

    This endpoint allows you to retrieve all estimates within a JobNimbus account.

    ---

    **Request Parameters:**

    - `from` (optional): Starting index for pagination (e.g., 10)

    - `size` (optional): Number of results to return (e.g., 5)


    ---

    **Response:**

    The response will contain an array of estimates with the following fields:

    - `attachment_id`: ID of the attachment

    - `cost`: Total cost of the estimate

    - `created_by`: ID of the user who created the estimate

    - `created_by_name`: Name of the user who created the estimate

    - `customer`: ID of the customer associated with the estimate

    - `date_created`: Timestamp of the creation date

    - `date_estimate`: Timestamp of the estimate date

    - `date_sign_requested`: Timestamp of the sign request date

    - `date_signed`: Timestamp of the sign date

    - `date_status_change`: Timestamp of the status change date

    - `date_updated`: Timestamp of the last update

    - `esigned`: Boolean indicating if the estimate is e-signed

    - `guid`: Unique identifier of the estimate

    - `is_active`: Boolean indicating if the estimate is active

    - `is_archived`: Boolean indicating if the estimate is archived

    - `items`: Array of items within the estimate, each containing amount, cost, item type, name, price,
    quantity, and unit of measure

    - `jnid`: ID of the estimate

    - `location`: Object containing the ID of the location

    - `margin`: Margin of the estimate

    - `number`: Estimate number

    - `owners`: Array of owners, each containing the ID

    - `recid`: Record ID

    - `related`: Array of related entities, each containing ID, name, number, and type

    - `sales_rep`: ID of the sales representative

    - `sales_rep_name`: Name of the sales representative

    - `sections`: Array of sections

    - `signature_status`: Status of the signature

    - `source`: Source of the estimate

    - `status`: Status code of the estimate

    - `status_name`: Name of the status

    - `subtotal`: Subtotal of the estimate

    - `tax`: Tax amount

    - `template_id`: ID of the template used for the estimate

    - `total`: Total amount of the estimate

    - `type`: always 'estimate'


    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_estimate\": 1600000000,
                \"date_sign_requested\": 1600000000,
                \"date_signed\": 1600000000,
                \"date_status_change\": 1600000000,
                \"date_updated\": 1600000000,
                \"esigned\": false,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"item_type\": \"material\",
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"Estimate_ID\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"number\": \"EST-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"recid\": 1000,
                \"related\": [
                    {
                        \"id\": \"JOB_ID_1\",
                        \"name\": \"Sample Project / SAMPLE-ID\",
                        \"number\": \"1000\",
                        \"type\": \"job\"
                    },
                    {
                        \"id\": \"CONTACT_ID_1\",
                        \"name\": \"John Doe (SAMPLE-ID)\",
                        \"number\": \"1001\",
                        \"type\": \"contact\"
                    }
                ],
                \"sales_rep\": \"salesrepjnid\",
                \"sales_rep_name\": \"Jane Smith\",
                \"sections\": [],
                \"status\": 4,
                \"status_name\": \"Closed\",
                \"subtotal\": 10000,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"total\": 10000,
                \"type\": \"estimate\"
            }
        ]
    }

     ```

    **Response Codes**:

    - HTTP Status 200: Success

    - Any other status code: Failure with an error message in the response

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2EstimatesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
