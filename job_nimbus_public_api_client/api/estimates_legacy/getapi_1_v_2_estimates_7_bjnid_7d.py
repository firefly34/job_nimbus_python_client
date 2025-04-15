from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.getapi_1v2_estimates_7_bjnid_7d_response_200 import Getapi1V2Estimates7Bjnid7DResponse200
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
        "url": "/api1/v2/estimates/%7Bjnid%7D",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Getapi1V2Estimates7Bjnid7DResponse200]:
    if response.status_code == 200:
        response_200 = Getapi1V2Estimates7Bjnid7DResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Getapi1V2Estimates7Bjnid7DResponse200]:
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
) -> Response[Getapi1V2Estimates7Bjnid7DResponse200]:
    r"""Retrieve an Estimate

     ### Retrieve Estimate

    This endpoint allows you to retrieve a single estimate within a JobNimbus account by providing the
    `estimateID` in the URL.

    #### Request Body

    This is a GET request and does not require a request body.

    #### Response Body

    The response will contain the details of the retrieved estimate, including the `type`, `guid`,
    `source`, `recid`, `attachment_id`, `customer`, `created_by`, `created_by_name`,
    `date_sign_requested`, `date_signed`, `date_created`, `date_updated`, `is_active`,
    `signature_status`, `related` (with id, name, number, type, email, and subject), `owners` (with id),
    `sales_rep`, `status`, `status_name`, `number`, `cost`, `margin`, `subtotal`, `tax`, `total`,
    `location` (with id), `date_estimate`, `date_status_change`, `items` (with jnid, name, description,
    quantity, cost, price, uom, sku, category, item_type, and amount), `sections` (with index, name,
    group, and showGroupTotal), `jnid`, `template_id`, `is_archived`, `esigned`, and `sales_rep_name`.

    Example of a partial response:

    ``` json
    {
        \"type\": \"estimate\",
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
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
        \"number\": \"EST-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"terms\": null,
        \"note\": \"\",
        \"date_estimate\": 1600000003,
        \"date_status_change\": 1600000004,
        \"items\": [
            {
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"cost\": 10000,
                \"amount\": 10000
            }
        ],
        \"sections\": [],
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
        \"first_payment_date\": 1600000006
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2Estimates7Bjnid7DResponse200]
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
) -> Optional[Getapi1V2Estimates7Bjnid7DResponse200]:
    r"""Retrieve an Estimate

     ### Retrieve Estimate

    This endpoint allows you to retrieve a single estimate within a JobNimbus account by providing the
    `estimateID` in the URL.

    #### Request Body

    This is a GET request and does not require a request body.

    #### Response Body

    The response will contain the details of the retrieved estimate, including the `type`, `guid`,
    `source`, `recid`, `attachment_id`, `customer`, `created_by`, `created_by_name`,
    `date_sign_requested`, `date_signed`, `date_created`, `date_updated`, `is_active`,
    `signature_status`, `related` (with id, name, number, type, email, and subject), `owners` (with id),
    `sales_rep`, `status`, `status_name`, `number`, `cost`, `margin`, `subtotal`, `tax`, `total`,
    `location` (with id), `date_estimate`, `date_status_change`, `items` (with jnid, name, description,
    quantity, cost, price, uom, sku, category, item_type, and amount), `sections` (with index, name,
    group, and showGroupTotal), `jnid`, `template_id`, `is_archived`, `esigned`, and `sales_rep_name`.

    Example of a partial response:

    ``` json
    {
        \"type\": \"estimate\",
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
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
        \"number\": \"EST-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"terms\": null,
        \"note\": \"\",
        \"date_estimate\": 1600000003,
        \"date_status_change\": 1600000004,
        \"items\": [
            {
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"cost\": 10000,
                \"amount\": 10000
            }
        ],
        \"sections\": [],
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
        \"first_payment_date\": 1600000006
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2Estimates7Bjnid7DResponse200
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Getapi1V2Estimates7Bjnid7DResponse200]:
    r"""Retrieve an Estimate

     ### Retrieve Estimate

    This endpoint allows you to retrieve a single estimate within a JobNimbus account by providing the
    `estimateID` in the URL.

    #### Request Body

    This is a GET request and does not require a request body.

    #### Response Body

    The response will contain the details of the retrieved estimate, including the `type`, `guid`,
    `source`, `recid`, `attachment_id`, `customer`, `created_by`, `created_by_name`,
    `date_sign_requested`, `date_signed`, `date_created`, `date_updated`, `is_active`,
    `signature_status`, `related` (with id, name, number, type, email, and subject), `owners` (with id),
    `sales_rep`, `status`, `status_name`, `number`, `cost`, `margin`, `subtotal`, `tax`, `total`,
    `location` (with id), `date_estimate`, `date_status_change`, `items` (with jnid, name, description,
    quantity, cost, price, uom, sku, category, item_type, and amount), `sections` (with index, name,
    group, and showGroupTotal), `jnid`, `template_id`, `is_archived`, `esigned`, and `sales_rep_name`.

    Example of a partial response:

    ``` json
    {
        \"type\": \"estimate\",
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
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
        \"number\": \"EST-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"terms\": null,
        \"note\": \"\",
        \"date_estimate\": 1600000003,
        \"date_status_change\": 1600000004,
        \"items\": [
            {
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"cost\": 10000,
                \"amount\": 10000
            }
        ],
        \"sections\": [],
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
        \"first_payment_date\": 1600000006
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Getapi1V2Estimates7Bjnid7DResponse200]
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
) -> Optional[Getapi1V2Estimates7Bjnid7DResponse200]:
    r"""Retrieve an Estimate

     ### Retrieve Estimate

    This endpoint allows you to retrieve a single estimate within a JobNimbus account by providing the
    `estimateID` in the URL.

    #### Request Body

    This is a GET request and does not require a request body.

    #### Response Body

    The response will contain the details of the retrieved estimate, including the `type`, `guid`,
    `source`, `recid`, `attachment_id`, `customer`, `created_by`, `created_by_name`,
    `date_sign_requested`, `date_signed`, `date_created`, `date_updated`, `is_active`,
    `signature_status`, `related` (with id, name, number, type, email, and subject), `owners` (with id),
    `sales_rep`, `status`, `status_name`, `number`, `cost`, `margin`, `subtotal`, `tax`, `total`,
    `location` (with id), `date_estimate`, `date_status_change`, `items` (with jnid, name, description,
    quantity, cost, price, uom, sku, category, item_type, and amount), `sections` (with index, name,
    group, and showGroupTotal), `jnid`, `template_id`, `is_archived`, `esigned`, and `sales_rep_name`.

    Example of a partial response:

    ``` json
    {
        \"type\": \"estimate\",
        \"guid\": \"12345678-ABCD-1234-EFGH-1234567890AB\",
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
        \"number\": \"EST-001\",
        \"location\": {
            \"id\": 1
        },
        \"subtotal\": 10000,
        \"margin\": 0,
        \"tax\": 0,
        \"total\": 10000,
        \"cost\": 10000,
        \"terms\": null,
        \"note\": \"\",
        \"date_estimate\": 1600000003,
        \"date_status_change\": 1600000004,
        \"items\": [
            {
                \"jnid\": \"ITEM_ID_123\",
                \"name\": \"Service\",
                \"uom\": \"Items\",
                \"item_type\": \"material\",
                \"description\": \"John Doe / PROJECT-123 / SERVICE\",
                \"quantity\": 1,
                \"price\": 10000,
                \"cost\": 10000,
                \"amount\": 10000
            }
        ],
        \"sections\": [],
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
        \"first_payment_date\": 1600000006
    }

     ```

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Getapi1V2Estimates7Bjnid7DResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
