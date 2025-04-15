from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1v2_invoices_response_200 import Getapi1V2InvoicesResponse200
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
        "url": "/api1/v2/invoices",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1V2InvoicesResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1V2InvoicesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1V2InvoicesResponse200]:
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
) -> Response[Getapi1V2InvoicesResponse200]:
    r"""Retrieve ALL Invoices

     This request allows you to retrieve all of the invoices within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"class_id\": null,
                \"class_name\": null,
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_due\": 1600000001,
                \"date_invoice\": 1600000002,
                \"date_paid_in_full\": 1600000003,
                \"date_status_change\": 1600000004,
                \"date_updated\": 1600000005,
                \"due\": 0,
                \"duplicate_from_id\": null,
                \"esigned\": false,
                \"external_id\": null,
                \"first_payment_date\": 1600000006,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"internal_note\": \"\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"description\": \"Sample Project / SAMPLE-ID / SERVICE\",
                        \"item_type\": \"material\",
                        \"jnid\": \"ITEM_ID_1\",
                        \"labor\": {
                            \"amount\": 0,
                            \"cost\": 0,
                            \"price\": 0,
                            \"tax_rate\": 0
                        },
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"quickbooksId\": \"1\",
                        \"tax_rate\": 0,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"INVOICE_ID_1\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"note\": \"\",
                \"number\": \"INV-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"payments\": [],
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
                \"supplier\": null,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"terms\": null,
                \"total\": 10000,
                \"total_paid\": 10000,
                \"type\": \"invoice\",
                \"version\": null
            }
        ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2InvoicesResponse200]
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
) -> Optional[Getapi1V2InvoicesResponse200]:
    r"""Retrieve ALL Invoices

     This request allows you to retrieve all of the invoices within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"class_id\": null,
                \"class_name\": null,
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_due\": 1600000001,
                \"date_invoice\": 1600000002,
                \"date_paid_in_full\": 1600000003,
                \"date_status_change\": 1600000004,
                \"date_updated\": 1600000005,
                \"due\": 0,
                \"duplicate_from_id\": null,
                \"esigned\": false,
                \"external_id\": null,
                \"first_payment_date\": 1600000006,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"internal_note\": \"\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"description\": \"Sample Project / SAMPLE-ID / SERVICE\",
                        \"item_type\": \"material\",
                        \"jnid\": \"ITEM_ID_1\",
                        \"labor\": {
                            \"amount\": 0,
                            \"cost\": 0,
                            \"price\": 0,
                            \"tax_rate\": 0
                        },
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"quickbooksId\": \"1\",
                        \"tax_rate\": 0,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"INVOICE_ID_1\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"note\": \"\",
                \"number\": \"INV-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"payments\": [],
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
                \"supplier\": null,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"terms\": null,
                \"total\": 10000,
                \"total_paid\": 10000,
                \"type\": \"invoice\",
                \"version\": null
            }
        ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2InvoicesResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1V2InvoicesResponse200]:
    r"""Retrieve ALL Invoices

     This request allows you to retrieve all of the invoices within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"class_id\": null,
                \"class_name\": null,
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_due\": 1600000001,
                \"date_invoice\": 1600000002,
                \"date_paid_in_full\": 1600000003,
                \"date_status_change\": 1600000004,
                \"date_updated\": 1600000005,
                \"due\": 0,
                \"duplicate_from_id\": null,
                \"esigned\": false,
                \"external_id\": null,
                \"first_payment_date\": 1600000006,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"internal_note\": \"\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"description\": \"Sample Project / SAMPLE-ID / SERVICE\",
                        \"item_type\": \"material\",
                        \"jnid\": \"ITEM_ID_1\",
                        \"labor\": {
                            \"amount\": 0,
                            \"cost\": 0,
                            \"price\": 0,
                            \"tax_rate\": 0
                        },
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"quickbooksId\": \"1\",
                        \"tax_rate\": 0,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"INVOICE_ID_1\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"note\": \"\",
                \"number\": \"INV-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"payments\": [],
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
                \"supplier\": null,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"terms\": null,
                \"total\": 10000,
                \"total_paid\": 10000,
                \"type\": \"invoice\",
                \"version\": null
            }
        ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2InvoicesResponse200]
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
) -> Optional[Getapi1V2InvoicesResponse200]:
    r"""Retrieve ALL Invoices

     This request allows you to retrieve all of the invoices within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Query Parameters:**

    - `from`: Starting index for pagination (e.g., 10)

    - `size`: Number of results to return (e.g., 5)


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"count\": 1000,
        \"results\": [
            {
                \"attachment_id\": \"attachmentjnid\",
                \"class_id\": null,
                \"class_name\": null,
                \"cost\": 10000,
                \"created_by\": \"system_qbo\",
                \"created_by_name\": \"QuickBooks\",
                \"customer\": \"customerjnid\",
                \"date_created\": 1600000000,
                \"date_due\": 1600000001,
                \"date_invoice\": 1600000002,
                \"date_paid_in_full\": 1600000003,
                \"date_status_change\": 1600000004,
                \"date_updated\": 1600000005,
                \"due\": 0,
                \"duplicate_from_id\": null,
                \"esigned\": false,
                \"external_id\": null,
                \"first_payment_date\": 1600000006,
                \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
                \"internal_note\": \"\",
                \"is_active\": true,
                \"is_archived\": true,
                \"items\": [
                    {
                        \"amount\": 10000,
                        \"cost\": 10000,
                        \"description\": \"Sample Project / SAMPLE-ID / SERVICE\",
                        \"item_type\": \"material\",
                        \"jnid\": \"ITEM_ID_1\",
                        \"labor\": {
                            \"amount\": 0,
                            \"cost\": 0,
                            \"price\": 0,
                            \"tax_rate\": 0
                        },
                        \"name\": \"Service\",
                        \"price\": 10000,
                        \"quantity\": 1,
                        \"quickbooksId\": \"1\",
                        \"tax_rate\": 0,
                        \"uom\": \"Items\"
                    }
                ],
                \"jnid\": \"INVOICE_ID_1\",
                \"location\": {
                    \"id\": 1
                },
                \"margin\": 0,
                \"note\": \"\",
                \"number\": \"INV-001\",
                \"owners\": [
                    {
                        \"id\": \"OWNER_ID_1\"
                    }
                ],
                \"payments\": [],
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
                \"supplier\": null,
                \"tax\": 0,
                \"template_id\": \"templatejnid\",
                \"terms\": null,
                \"total\": 10000,
                \"total_paid\": 10000,
                \"type\": \"invoice\",
                \"version\": null
            }
        ]
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2InvoicesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
