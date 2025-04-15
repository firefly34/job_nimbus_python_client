from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.putapi_1v2_products_3_cjnid_3e_body import Putapi1V2Products3Cjnid3EBody
from ...models.putapi_1v2_products_3_cjnid_3e_response_200 import Putapi1V2Products3Cjnid3EResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Putapi1V2Products3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api1/v2/products/%3Cjnid%3E",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Putapi1V2Products3Cjnid3EResponse200]:
    if response.status_code == 200:
        response_200 = Putapi1V2Products3Cjnid3EResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Putapi1V2Products3Cjnid3EResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Putapi1V2Products3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Putapi1V2Products3Cjnid3EResponse200]:
    """Delete a Product

     This request allows you to update a specific product within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Additional Information:**

    - Only products with names less than 32 characters can be synced with QuickBooks. Even if the
    account is not linked with QuickBooks it's often good to keep product names within that range in
    case the account will be linked with Quickbooks later.

    - The `item_type` property in the JSON body should have the value of `material`, `labor`, or
    `labor+material`

    - `item_type` will always be `material` if labor and material is not enabled in the account. If
    labor and material is enabled in the account then the `item_type` will be `material` if there is
    only material cost/price, `labor` if there is only labor cost/price, and `labor+material` if there
    is both material cost/price **and** labor cost/price.

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Products3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Putapi1V2Products3Cjnid3EResponse200]
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
    body: Putapi1V2Products3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Putapi1V2Products3Cjnid3EResponse200]:
    """Delete a Product

     This request allows you to update a specific product within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Additional Information:**

    - Only products with names less than 32 characters can be synced with QuickBooks. Even if the
    account is not linked with QuickBooks it's often good to keep product names within that range in
    case the account will be linked with Quickbooks later.

    - The `item_type` property in the JSON body should have the value of `material`, `labor`, or
    `labor+material`

    - `item_type` will always be `material` if labor and material is not enabled in the account. If
    labor and material is enabled in the account then the `item_type` will be `material` if there is
    only material cost/price, `labor` if there is only labor cost/price, and `labor+material` if there
    is both material cost/price **and** labor cost/price.

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Products3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Putapi1V2Products3Cjnid3EResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Putapi1V2Products3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Putapi1V2Products3Cjnid3EResponse200]:
    """Delete a Product

     This request allows you to update a specific product within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Additional Information:**

    - Only products with names less than 32 characters can be synced with QuickBooks. Even if the
    account is not linked with QuickBooks it's often good to keep product names within that range in
    case the account will be linked with Quickbooks later.

    - The `item_type` property in the JSON body should have the value of `material`, `labor`, or
    `labor+material`

    - `item_type` will always be `material` if labor and material is not enabled in the account. If
    labor and material is enabled in the account then the `item_type` will be `material` if there is
    only material cost/price, `labor` if there is only labor cost/price, and `labor+material` if there
    is both material cost/price **and** labor cost/price.

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Products3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Putapi1V2Products3Cjnid3EResponse200]
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
    body: Putapi1V2Products3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Putapi1V2Products3Cjnid3EResponse200]:
    """Delete a Product

     This request allows you to update a specific product within a JobNimbus account.

    ---

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response


    ---

    **Additional Information:**

    - Only products with names less than 32 characters can be synced with QuickBooks. Even if the
    account is not linked with QuickBooks it's often good to keep product names within that range in
    case the account will be linked with Quickbooks later.

    - The `item_type` property in the JSON body should have the value of `material`, `labor`, or
    `labor+material`

    - `item_type` will always be `material` if labor and material is not enabled in the account. If
    labor and material is enabled in the account then the `item_type` will be `material` if there is
    only material cost/price, `labor` if there is only labor cost/price, and `labor+material` if there
    is both material cost/price **and** labor cost/price.

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Products3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Putapi1V2Products3Cjnid3EResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
