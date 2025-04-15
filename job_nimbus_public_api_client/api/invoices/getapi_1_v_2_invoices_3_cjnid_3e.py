from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1v2_invoices_3_cjnid_3e_response_200 import Getapi1V2Invoices3Cjnid3EResponse200
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
        "url": "/api1/v2/invoices/%3Cjnid%3E",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1V2Invoices3Cjnid3EResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1V2Invoices3Cjnid3EResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1V2Invoices3Cjnid3EResponse200]:
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
) -> Response[Getapi1V2Invoices3Cjnid3EResponse200]:
    r"""Retrieve an Invoice

     This request allows you to retrieve a single invoice within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"type\": \"invoice\",
        \"external_id\": null,
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
        \"merged\": null,
        \"class_id\": null,
        \"class_name\": null,
        \"supplier\": null,
        \"recid\": 1000,
        \"attachment_id\": \"ATTACHMENT_ID_123\",
        \"customer\": \"CUSTOMER_ID_123\",
        \"created_by\": \"system_qbo\",
        \"created_by_name\": \"QuickBooks\",
        \"date_created\": 1600000000,
        \"date_updated\": 1600000001,
        \"esigned\": false,
        \"is_active\": true,
        \"is_archived\": true,
        \"related\": [
            {
                \"id\": \"JOB_ID_123\",
                \"name\": \"John Doe / PROJECT-123\",
                \"number\": \"1000\",
                \"type\": \"job\",
                \"email\": null,
                \"subject\": null
            },
            {
                \"id\": \"CONTACT_ID_123\",
                \"name\": \"John Doe (CLIENT-123)\",
                \"number\": \"2000\",
                \"type\": \"contact\",
                \"email\": null,
                \"subject\": null
            }
        ],
        \"status\": 4,
        \"status_name\": \"Closed\",
        \"number\": \"INV-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"total_paid\": 10000,
        \"due\": 0,
        \"terms\": null,
        \"note\": \"\",
        \"date_due\": 1600000002,
        \"date_invoice\": 1600000003,
        \"date_status_change\": 1600000004,
        \"date_paid_in_full\": 1600000005,
        \"items\": [
            {
                \"quickbooksId\": \"1\",
                \"showGroupTotal\": null,
                \"addMarkup\": null,
                \"addMarkupIsExcluded\": null,
                \"photos\": [],
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"preSurchargePrice\": null,
                \"cost\": 10000,
                \"amount\": 10000,
                \"tax_couch_id\": null,
                \"tax_name\": null,
                \"tax_rate\": 0,
                \"labor\": {
                    \"quickbooksId\": null,
                    \"price\": 0,
                    \"preSurchargePrice\": null,
                    \"cost\": 0,
                    \"addMarkup\": null,
                    \"addMarkupIsExcluded\": null,
                    \"amount\": 0,
                    \"tax_couch_id\": null,
                    \"tax_name\": null,
                    \"tax_rate\": 0
                },
                \"sku\": null,
                \"color\": null,
                \"category\": null
            }
        ],
        \"sections\": [],
        \"payments\": [],
        \"owners\": [
            {
                \"id\": \"OWNER_ID_123\"
            }
        ],
        \"sales_rep\": \"SALES_REP_ID_123\",
        \"sales_rep_name\": \"Jane Smith\",
        \"jnid\": \"INVOICE_ID_123\",
        \"internal_note\": \"\",
        \"template_id\": \"TEMPLATE_ID_123\",
        \"first_payment_date\": 1600000006,
        \"version\": null,
        \"duplicate_from_id\": null
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2Invoices3Cjnid3EResponse200]
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
) -> Optional[Getapi1V2Invoices3Cjnid3EResponse200]:
    r"""Retrieve an Invoice

     This request allows you to retrieve a single invoice within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"type\": \"invoice\",
        \"external_id\": null,
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
        \"merged\": null,
        \"class_id\": null,
        \"class_name\": null,
        \"supplier\": null,
        \"recid\": 1000,
        \"attachment_id\": \"ATTACHMENT_ID_123\",
        \"customer\": \"CUSTOMER_ID_123\",
        \"created_by\": \"system_qbo\",
        \"created_by_name\": \"QuickBooks\",
        \"date_created\": 1600000000,
        \"date_updated\": 1600000001,
        \"esigned\": false,
        \"is_active\": true,
        \"is_archived\": true,
        \"related\": [
            {
                \"id\": \"JOB_ID_123\",
                \"name\": \"John Doe / PROJECT-123\",
                \"number\": \"1000\",
                \"type\": \"job\",
                \"email\": null,
                \"subject\": null
            },
            {
                \"id\": \"CONTACT_ID_123\",
                \"name\": \"John Doe (CLIENT-123)\",
                \"number\": \"2000\",
                \"type\": \"contact\",
                \"email\": null,
                \"subject\": null
            }
        ],
        \"status\": 4,
        \"status_name\": \"Closed\",
        \"number\": \"INV-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"total_paid\": 10000,
        \"due\": 0,
        \"terms\": null,
        \"note\": \"\",
        \"date_due\": 1600000002,
        \"date_invoice\": 1600000003,
        \"date_status_change\": 1600000004,
        \"date_paid_in_full\": 1600000005,
        \"items\": [
            {
                \"quickbooksId\": \"1\",
                \"showGroupTotal\": null,
                \"addMarkup\": null,
                \"addMarkupIsExcluded\": null,
                \"photos\": [],
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"preSurchargePrice\": null,
                \"cost\": 10000,
                \"amount\": 10000,
                \"tax_couch_id\": null,
                \"tax_name\": null,
                \"tax_rate\": 0,
                \"labor\": {
                    \"quickbooksId\": null,
                    \"price\": 0,
                    \"preSurchargePrice\": null,
                    \"cost\": 0,
                    \"addMarkup\": null,
                    \"addMarkupIsExcluded\": null,
                    \"amount\": 0,
                    \"tax_couch_id\": null,
                    \"tax_name\": null,
                    \"tax_rate\": 0
                },
                \"sku\": null,
                \"color\": null,
                \"category\": null
            }
        ],
        \"sections\": [],
        \"payments\": [],
        \"owners\": [
            {
                \"id\": \"OWNER_ID_123\"
            }
        ],
        \"sales_rep\": \"SALES_REP_ID_123\",
        \"sales_rep_name\": \"Jane Smith\",
        \"jnid\": \"INVOICE_ID_123\",
        \"internal_note\": \"\",
        \"template_id\": \"TEMPLATE_ID_123\",
        \"first_payment_date\": 1600000006,
        \"version\": null,
        \"duplicate_from_id\": null
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2Invoices3Cjnid3EResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1V2Invoices3Cjnid3EResponse200]:
    r"""Retrieve an Invoice

     This request allows you to retrieve a single invoice within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"type\": \"invoice\",
        \"external_id\": null,
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
        \"merged\": null,
        \"class_id\": null,
        \"class_name\": null,
        \"supplier\": null,
        \"recid\": 1000,
        \"attachment_id\": \"ATTACHMENT_ID_123\",
        \"customer\": \"CUSTOMER_ID_123\",
        \"created_by\": \"system_qbo\",
        \"created_by_name\": \"QuickBooks\",
        \"date_created\": 1600000000,
        \"date_updated\": 1600000001,
        \"esigned\": false,
        \"is_active\": true,
        \"is_archived\": true,
        \"related\": [
            {
                \"id\": \"JOB_ID_123\",
                \"name\": \"John Doe / PROJECT-123\",
                \"number\": \"1000\",
                \"type\": \"job\",
                \"email\": null,
                \"subject\": null
            },
            {
                \"id\": \"CONTACT_ID_123\",
                \"name\": \"John Doe (CLIENT-123)\",
                \"number\": \"2000\",
                \"type\": \"contact\",
                \"email\": null,
                \"subject\": null
            }
        ],
        \"status\": 4,
        \"status_name\": \"Closed\",
        \"number\": \"INV-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"total_paid\": 10000,
        \"due\": 0,
        \"terms\": null,
        \"note\": \"\",
        \"date_due\": 1600000002,
        \"date_invoice\": 1600000003,
        \"date_status_change\": 1600000004,
        \"date_paid_in_full\": 1600000005,
        \"items\": [
            {
                \"quickbooksId\": \"1\",
                \"showGroupTotal\": null,
                \"addMarkup\": null,
                \"addMarkupIsExcluded\": null,
                \"photos\": [],
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"preSurchargePrice\": null,
                \"cost\": 10000,
                \"amount\": 10000,
                \"tax_couch_id\": null,
                \"tax_name\": null,
                \"tax_rate\": 0,
                \"labor\": {
                    \"quickbooksId\": null,
                    \"price\": 0,
                    \"preSurchargePrice\": null,
                    \"cost\": 0,
                    \"addMarkup\": null,
                    \"addMarkupIsExcluded\": null,
                    \"amount\": 0,
                    \"tax_couch_id\": null,
                    \"tax_name\": null,
                    \"tax_rate\": 0
                },
                \"sku\": null,
                \"color\": null,
                \"category\": null
            }
        ],
        \"sections\": [],
        \"payments\": [],
        \"owners\": [
            {
                \"id\": \"OWNER_ID_123\"
            }
        ],
        \"sales_rep\": \"SALES_REP_ID_123\",
        \"sales_rep_name\": \"Jane Smith\",
        \"jnid\": \"INVOICE_ID_123\",
        \"internal_note\": \"\",
        \"template_id\": \"TEMPLATE_ID_123\",
        \"first_payment_date\": 1600000006,
        \"version\": null,
        \"duplicate_from_id\": null
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2Invoices3Cjnid3EResponse200]
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
) -> Optional[Getapi1V2Invoices3Cjnid3EResponse200]:
    r"""Retrieve an Invoice

     This request allows you to retrieve a single invoice within a JobNimbus account.

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Response**:

    Example of a partial response:

    ``` json
    {
        \"type\": \"invoice\",
        \"external_id\": null,
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
        \"merged\": null,
        \"class_id\": null,
        \"class_name\": null,
        \"supplier\": null,
        \"recid\": 1000,
        \"attachment_id\": \"ATTACHMENT_ID_123\",
        \"customer\": \"CUSTOMER_ID_123\",
        \"created_by\": \"system_qbo\",
        \"created_by_name\": \"QuickBooks\",
        \"date_created\": 1600000000,
        \"date_updated\": 1600000001,
        \"esigned\": false,
        \"is_active\": true,
        \"is_archived\": true,
        \"related\": [
            {
                \"id\": \"JOB_ID_123\",
                \"name\": \"John Doe / PROJECT-123\",
                \"number\": \"1000\",
                \"type\": \"job\",
                \"email\": null,
                \"subject\": null
            },
            {
                \"id\": \"CONTACT_ID_123\",
                \"name\": \"John Doe (CLIENT-123)\",
                \"number\": \"2000\",
                \"type\": \"contact\",
                \"email\": null,
                \"subject\": null
            }
        ],
        \"status\": 4,
        \"status_name\": \"Closed\",
        \"number\": \"INV-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"total_paid\": 10000,
        \"due\": 0,
        \"terms\": null,
        \"note\": \"\",
        \"date_due\": 1600000002,
        \"date_invoice\": 1600000003,
        \"date_status_change\": 1600000004,
        \"date_paid_in_full\": 1600000005,
        \"items\": [
            {
                \"quickbooksId\": \"1\",
                \"showGroupTotal\": null,
                \"addMarkup\": null,
                \"addMarkupIsExcluded\": null,
                \"photos\": [],
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"preSurchargePrice\": null,
                \"cost\": 10000,
                \"amount\": 10000,
                \"tax_couch_id\": null,
                \"tax_name\": null,
                \"tax_rate\": 0,
                \"labor\": {
                    \"quickbooksId\": null,
                    \"price\": 0,
                    \"preSurchargePrice\": null,
                    \"cost\": 0,
                    \"addMarkup\": null,
                    \"addMarkupIsExcluded\": null,
                    \"amount\": 0,
                    \"tax_couch_id\": null,
                    \"tax_name\": null,
                    \"tax_rate\": 0
                },
                \"sku\": null,
                \"color\": null,
                \"category\": null
            }
        ],
        \"sections\": [],
        \"payments\": [],
        \"owners\": [
            {
                \"id\": \"OWNER_ID_123\"
            }
        ],
        \"sales_rep\": \"SALES_REP_ID_123\",
        \"sales_rep_name\": \"Jane Smith\",
        \"jnid\": \"INVOICE_ID_123\",
        \"internal_note\": \"\",
        \"template_id\": \"TEMPLATE_ID_123\",
        \"first_payment_date\": 1600000006,
        \"version\": null,
        \"duplicate_from_id\": null
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2Invoices3Cjnid3EResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
