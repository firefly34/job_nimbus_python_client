from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.putapi_1v2_estimates_3_cjnid_3e_body import Putapi1V2Estimates3Cjnid3EBody
from ...models.putapi_1v2_estimates_3_cjnid_3e_response_200 import Putapi1V2Estimates3Cjnid3EResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Putapi1V2Estimates3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api1/v2/estimates/%3Cjnid%3E",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Putapi1V2Estimates3Cjnid3EResponse200]:
    if response.status_code == 200:
        response_200 = Putapi1V2Estimates3Cjnid3EResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Putapi1V2Estimates3Cjnid3EResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Putapi1V2Estimates3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Putapi1V2Estimates3Cjnid3EResponse200]:
    r"""Delete an Estimate

     ### Delete an Existing Estimate

    This endpoint allows you to update an existing estimate within JobNimbus.

    #### Request Body

    - `is_active`: Indicates if the estimate is active or not


    #### Response

    The response of this request can be documented as a JSON schema. Here is a partial example of the
    response:

    ``` json
    {
      \"is_active\": false,
      \"type\": \"estimate\",
      \"date_created\": 1683819562,
      \"date_updated\": 1684160281,
      \"date_estimate\": 1683781200,
      \"external_id\": \"993479\",
      \"number\": \"1047\",
      \"status\": 1,
      \"internal_note\": \"Project Estimate\",
      \"related\": [
        {
          \"id\": \"lyu27jrnumcrz2u89k3ydyr\",
          \"type\": \"job\"
        }
      ],
      \"items\": [
        {
          \"name\": \"Services\",
          \"description\": \"Test and Troy Coon / SIDING\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 15438.99,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Shake siding\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 1303,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Remove Lights\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": -349.52,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        }
      ]
    }

     ```

    **Response JSON Schema:**

    ``` json
    {
        \"type\": \"object\",
        \"properties\": {
            \"type\": {\"type\": \"string\"},
            \"external_id\": {\"type\": [\"string\", \"null\"]},
            \"guid\": {\"type\": \"string\"},
            \"merged\": {\"type\": [\"string\", \"null\"]},
            \"class_id\": {\"type\": [\"string\", \"null\"]},
            \"class_name\": {\"type\": [\"string\", \"null\"]},
            \"supplier\": {\"type\": [\"string\", \"null\"]},
            \"recid\": {\"type\": \"integer\"},
            \"attachment_id\": {\"type\": \"string\"},
            \"customer\": {\"type\": \"string\"},
            \"created_by\": {\"type\": \"string\"},
            \"created_by_name\": {\"type\": \"string\"},
            \"date_created\": {\"type\": \"integer\"},
            \"date_updated\": {\"type\": \"integer\"},
            \"esigned\": {\"type\": \"boolean\"},
            \"is_active\": {\"type\": \"boolean\"},
            \"is_archived\": {\"type\": \"boolean\"},
            \"related\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"number\": {\"type\": \"string\"},
                        \"type\": {\"type\": \"string\"},
                        \"email\": {\"type\": [\"string\", \"null\"]},
                        \"subject\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"status\": {\"type\": \"integer\"},
            \"status_name\": {\"type\": \"string\"},
            \"number\": {\"type\": \"string\"},
            \"location\": {
                \"type\": \"object\",
                \"properties\": {
                    \"id\": {\"type\": \"integer\"}
                }
            },
            \"subtotal\": {\"type\": \"integer\"},
            \"margin\": {\"type\": \"integer\"},
            \"tax\": {\"type\": \"integer\"},
            \"total\": {\"type\": \"integer\"},
            \"cost\": {\"type\": \"integer\"},
            \"terms\": {\"type\": [\"string\", \"null\"]},
            \"note\": {\"type\": \"string\"},
            \"date_estimate\": {\"type\": \"integer\"},
            \"date_status_change\": {\"type\": \"integer\"},
            \"items\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                        \"showGroupTotal\": {\"type\": [\"string\", \"null\"]},
                        \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                        \"photos\": {\"type\": \"array\"},
                        \"jnid\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"uom\": {\"type\": \"string\"},
                        \"item_type\": {\"type\": \"string\"},
                        \"description\": {\"type\": \"string\"},
                        \"quantity\": {\"type\": \"integer\"},
                        \"price\": {\"type\": \"integer\"},
                        \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                        \"cost\": {\"type\": \"integer\"},
                        \"amount\": {\"type\": \"integer\"},
                        \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                        \"tax_name\": {\"type\": [\"string\", \"null\"]},
                        \"tax_rate\": {\"type\": \"integer\"},
                        \"labor\": {
                            \"type\": \"object\",
                            \"properties\": {
                                \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                                \"price\": {\"type\": \"integer\"},
                                \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                                \"cost\": {\"type\": \"integer\"},
                                \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                                \"amount\": {\"type\": \"integer\"},
                                \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                                \"tax_name\": {\"type\": [\"string\", \"null\"]},
                                \"tax_rate\": {\"type\": \"integer\"}
                            }
                        },
                        \"sku\": {\"type\": [\"string\", \"null\"]},
                        \"color\": {\"type\": [\"string\", \"null\"]},
                        \"category\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"sections\": {\"type\": \"array\"},
            \"owners\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"}
                    }
                }
            },
            \"sales_rep\": {\"type\": \"string\"},
            \"sales_rep_name\": {\"type\": \"string\"},
            \"jnid\": {\"type\": \"string\"},
            \"internal_note\": {\"type\": \"string\"},
            \"template_id\": {\"type\": \"string\"},
            \"version\": {\"type\": [\"string\", \"null\"]},
            \"duplicate_from_id\": {\"type\": [\"string\", \"null\"]}
        }
    }

     ```

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Estimates3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Putapi1V2Estimates3Cjnid3EResponse200]
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
    body: Putapi1V2Estimates3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Putapi1V2Estimates3Cjnid3EResponse200]:
    r"""Delete an Estimate

     ### Delete an Existing Estimate

    This endpoint allows you to update an existing estimate within JobNimbus.

    #### Request Body

    - `is_active`: Indicates if the estimate is active or not


    #### Response

    The response of this request can be documented as a JSON schema. Here is a partial example of the
    response:

    ``` json
    {
      \"is_active\": false,
      \"type\": \"estimate\",
      \"date_created\": 1683819562,
      \"date_updated\": 1684160281,
      \"date_estimate\": 1683781200,
      \"external_id\": \"993479\",
      \"number\": \"1047\",
      \"status\": 1,
      \"internal_note\": \"Project Estimate\",
      \"related\": [
        {
          \"id\": \"lyu27jrnumcrz2u89k3ydyr\",
          \"type\": \"job\"
        }
      ],
      \"items\": [
        {
          \"name\": \"Services\",
          \"description\": \"Test and Troy Coon / SIDING\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 15438.99,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Shake siding\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 1303,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Remove Lights\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": -349.52,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        }
      ]
    }

     ```

    **Response JSON Schema:**

    ``` json
    {
        \"type\": \"object\",
        \"properties\": {
            \"type\": {\"type\": \"string\"},
            \"external_id\": {\"type\": [\"string\", \"null\"]},
            \"guid\": {\"type\": \"string\"},
            \"merged\": {\"type\": [\"string\", \"null\"]},
            \"class_id\": {\"type\": [\"string\", \"null\"]},
            \"class_name\": {\"type\": [\"string\", \"null\"]},
            \"supplier\": {\"type\": [\"string\", \"null\"]},
            \"recid\": {\"type\": \"integer\"},
            \"attachment_id\": {\"type\": \"string\"},
            \"customer\": {\"type\": \"string\"},
            \"created_by\": {\"type\": \"string\"},
            \"created_by_name\": {\"type\": \"string\"},
            \"date_created\": {\"type\": \"integer\"},
            \"date_updated\": {\"type\": \"integer\"},
            \"esigned\": {\"type\": \"boolean\"},
            \"is_active\": {\"type\": \"boolean\"},
            \"is_archived\": {\"type\": \"boolean\"},
            \"related\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"number\": {\"type\": \"string\"},
                        \"type\": {\"type\": \"string\"},
                        \"email\": {\"type\": [\"string\", \"null\"]},
                        \"subject\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"status\": {\"type\": \"integer\"},
            \"status_name\": {\"type\": \"string\"},
            \"number\": {\"type\": \"string\"},
            \"location\": {
                \"type\": \"object\",
                \"properties\": {
                    \"id\": {\"type\": \"integer\"}
                }
            },
            \"subtotal\": {\"type\": \"integer\"},
            \"margin\": {\"type\": \"integer\"},
            \"tax\": {\"type\": \"integer\"},
            \"total\": {\"type\": \"integer\"},
            \"cost\": {\"type\": \"integer\"},
            \"terms\": {\"type\": [\"string\", \"null\"]},
            \"note\": {\"type\": \"string\"},
            \"date_estimate\": {\"type\": \"integer\"},
            \"date_status_change\": {\"type\": \"integer\"},
            \"items\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                        \"showGroupTotal\": {\"type\": [\"string\", \"null\"]},
                        \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                        \"photos\": {\"type\": \"array\"},
                        \"jnid\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"uom\": {\"type\": \"string\"},
                        \"item_type\": {\"type\": \"string\"},
                        \"description\": {\"type\": \"string\"},
                        \"quantity\": {\"type\": \"integer\"},
                        \"price\": {\"type\": \"integer\"},
                        \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                        \"cost\": {\"type\": \"integer\"},
                        \"amount\": {\"type\": \"integer\"},
                        \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                        \"tax_name\": {\"type\": [\"string\", \"null\"]},
                        \"tax_rate\": {\"type\": \"integer\"},
                        \"labor\": {
                            \"type\": \"object\",
                            \"properties\": {
                                \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                                \"price\": {\"type\": \"integer\"},
                                \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                                \"cost\": {\"type\": \"integer\"},
                                \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                                \"amount\": {\"type\": \"integer\"},
                                \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                                \"tax_name\": {\"type\": [\"string\", \"null\"]},
                                \"tax_rate\": {\"type\": \"integer\"}
                            }
                        },
                        \"sku\": {\"type\": [\"string\", \"null\"]},
                        \"color\": {\"type\": [\"string\", \"null\"]},
                        \"category\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"sections\": {\"type\": \"array\"},
            \"owners\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"}
                    }
                }
            },
            \"sales_rep\": {\"type\": \"string\"},
            \"sales_rep_name\": {\"type\": \"string\"},
            \"jnid\": {\"type\": \"string\"},
            \"internal_note\": {\"type\": \"string\"},
            \"template_id\": {\"type\": \"string\"},
            \"version\": {\"type\": [\"string\", \"null\"]},
            \"duplicate_from_id\": {\"type\": [\"string\", \"null\"]}
        }
    }

     ```

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Estimates3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Putapi1V2Estimates3Cjnid3EResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Putapi1V2Estimates3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Putapi1V2Estimates3Cjnid3EResponse200]:
    r"""Delete an Estimate

     ### Delete an Existing Estimate

    This endpoint allows you to update an existing estimate within JobNimbus.

    #### Request Body

    - `is_active`: Indicates if the estimate is active or not


    #### Response

    The response of this request can be documented as a JSON schema. Here is a partial example of the
    response:

    ``` json
    {
      \"is_active\": false,
      \"type\": \"estimate\",
      \"date_created\": 1683819562,
      \"date_updated\": 1684160281,
      \"date_estimate\": 1683781200,
      \"external_id\": \"993479\",
      \"number\": \"1047\",
      \"status\": 1,
      \"internal_note\": \"Project Estimate\",
      \"related\": [
        {
          \"id\": \"lyu27jrnumcrz2u89k3ydyr\",
          \"type\": \"job\"
        }
      ],
      \"items\": [
        {
          \"name\": \"Services\",
          \"description\": \"Test and Troy Coon / SIDING\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 15438.99,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Shake siding\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 1303,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Remove Lights\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": -349.52,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        }
      ]
    }

     ```

    **Response JSON Schema:**

    ``` json
    {
        \"type\": \"object\",
        \"properties\": {
            \"type\": {\"type\": \"string\"},
            \"external_id\": {\"type\": [\"string\", \"null\"]},
            \"guid\": {\"type\": \"string\"},
            \"merged\": {\"type\": [\"string\", \"null\"]},
            \"class_id\": {\"type\": [\"string\", \"null\"]},
            \"class_name\": {\"type\": [\"string\", \"null\"]},
            \"supplier\": {\"type\": [\"string\", \"null\"]},
            \"recid\": {\"type\": \"integer\"},
            \"attachment_id\": {\"type\": \"string\"},
            \"customer\": {\"type\": \"string\"},
            \"created_by\": {\"type\": \"string\"},
            \"created_by_name\": {\"type\": \"string\"},
            \"date_created\": {\"type\": \"integer\"},
            \"date_updated\": {\"type\": \"integer\"},
            \"esigned\": {\"type\": \"boolean\"},
            \"is_active\": {\"type\": \"boolean\"},
            \"is_archived\": {\"type\": \"boolean\"},
            \"related\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"number\": {\"type\": \"string\"},
                        \"type\": {\"type\": \"string\"},
                        \"email\": {\"type\": [\"string\", \"null\"]},
                        \"subject\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"status\": {\"type\": \"integer\"},
            \"status_name\": {\"type\": \"string\"},
            \"number\": {\"type\": \"string\"},
            \"location\": {
                \"type\": \"object\",
                \"properties\": {
                    \"id\": {\"type\": \"integer\"}
                }
            },
            \"subtotal\": {\"type\": \"integer\"},
            \"margin\": {\"type\": \"integer\"},
            \"tax\": {\"type\": \"integer\"},
            \"total\": {\"type\": \"integer\"},
            \"cost\": {\"type\": \"integer\"},
            \"terms\": {\"type\": [\"string\", \"null\"]},
            \"note\": {\"type\": \"string\"},
            \"date_estimate\": {\"type\": \"integer\"},
            \"date_status_change\": {\"type\": \"integer\"},
            \"items\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                        \"showGroupTotal\": {\"type\": [\"string\", \"null\"]},
                        \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                        \"photos\": {\"type\": \"array\"},
                        \"jnid\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"uom\": {\"type\": \"string\"},
                        \"item_type\": {\"type\": \"string\"},
                        \"description\": {\"type\": \"string\"},
                        \"quantity\": {\"type\": \"integer\"},
                        \"price\": {\"type\": \"integer\"},
                        \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                        \"cost\": {\"type\": \"integer\"},
                        \"amount\": {\"type\": \"integer\"},
                        \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                        \"tax_name\": {\"type\": [\"string\", \"null\"]},
                        \"tax_rate\": {\"type\": \"integer\"},
                        \"labor\": {
                            \"type\": \"object\",
                            \"properties\": {
                                \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                                \"price\": {\"type\": \"integer\"},
                                \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                                \"cost\": {\"type\": \"integer\"},
                                \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                                \"amount\": {\"type\": \"integer\"},
                                \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                                \"tax_name\": {\"type\": [\"string\", \"null\"]},
                                \"tax_rate\": {\"type\": \"integer\"}
                            }
                        },
                        \"sku\": {\"type\": [\"string\", \"null\"]},
                        \"color\": {\"type\": [\"string\", \"null\"]},
                        \"category\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"sections\": {\"type\": \"array\"},
            \"owners\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"}
                    }
                }
            },
            \"sales_rep\": {\"type\": \"string\"},
            \"sales_rep_name\": {\"type\": \"string\"},
            \"jnid\": {\"type\": \"string\"},
            \"internal_note\": {\"type\": \"string\"},
            \"template_id\": {\"type\": \"string\"},
            \"version\": {\"type\": [\"string\", \"null\"]},
            \"duplicate_from_id\": {\"type\": [\"string\", \"null\"]}
        }
    }

     ```

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Estimates3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Putapi1V2Estimates3Cjnid3EResponse200]
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
    body: Putapi1V2Estimates3Cjnid3EBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Putapi1V2Estimates3Cjnid3EResponse200]:
    r"""Delete an Estimate

     ### Delete an Existing Estimate

    This endpoint allows you to update an existing estimate within JobNimbus.

    #### Request Body

    - `is_active`: Indicates if the estimate is active or not


    #### Response

    The response of this request can be documented as a JSON schema. Here is a partial example of the
    response:

    ``` json
    {
      \"is_active\": false,
      \"type\": \"estimate\",
      \"date_created\": 1683819562,
      \"date_updated\": 1684160281,
      \"date_estimate\": 1683781200,
      \"external_id\": \"993479\",
      \"number\": \"1047\",
      \"status\": 1,
      \"internal_note\": \"Project Estimate\",
      \"related\": [
        {
          \"id\": \"lyu27jrnumcrz2u89k3ydyr\",
          \"type\": \"job\"
        }
      ],
      \"items\": [
        {
          \"name\": \"Services\",
          \"description\": \"Test and Troy Coon / SIDING\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 15438.99,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Shake siding\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": 1303,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        },
        {
          \"name\": \"Services\",
          \"description\": \"Remove Lights\",
          \"uom\": \"Items\",
          \"item_type\": \"material\",
          \"quantity\": 1,
          \"price\": -349.52,
          \"jnid\": \"lyqi3qx3ee8hvnwh8g53wo9\"
        }
      ]
    }

     ```

    **Response JSON Schema:**

    ``` json
    {
        \"type\": \"object\",
        \"properties\": {
            \"type\": {\"type\": \"string\"},
            \"external_id\": {\"type\": [\"string\", \"null\"]},
            \"guid\": {\"type\": \"string\"},
            \"merged\": {\"type\": [\"string\", \"null\"]},
            \"class_id\": {\"type\": [\"string\", \"null\"]},
            \"class_name\": {\"type\": [\"string\", \"null\"]},
            \"supplier\": {\"type\": [\"string\", \"null\"]},
            \"recid\": {\"type\": \"integer\"},
            \"attachment_id\": {\"type\": \"string\"},
            \"customer\": {\"type\": \"string\"},
            \"created_by\": {\"type\": \"string\"},
            \"created_by_name\": {\"type\": \"string\"},
            \"date_created\": {\"type\": \"integer\"},
            \"date_updated\": {\"type\": \"integer\"},
            \"esigned\": {\"type\": \"boolean\"},
            \"is_active\": {\"type\": \"boolean\"},
            \"is_archived\": {\"type\": \"boolean\"},
            \"related\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"number\": {\"type\": \"string\"},
                        \"type\": {\"type\": \"string\"},
                        \"email\": {\"type\": [\"string\", \"null\"]},
                        \"subject\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"status\": {\"type\": \"integer\"},
            \"status_name\": {\"type\": \"string\"},
            \"number\": {\"type\": \"string\"},
            \"location\": {
                \"type\": \"object\",
                \"properties\": {
                    \"id\": {\"type\": \"integer\"}
                }
            },
            \"subtotal\": {\"type\": \"integer\"},
            \"margin\": {\"type\": \"integer\"},
            \"tax\": {\"type\": \"integer\"},
            \"total\": {\"type\": \"integer\"},
            \"cost\": {\"type\": \"integer\"},
            \"terms\": {\"type\": [\"string\", \"null\"]},
            \"note\": {\"type\": \"string\"},
            \"date_estimate\": {\"type\": \"integer\"},
            \"date_status_change\": {\"type\": \"integer\"},
            \"items\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                        \"showGroupTotal\": {\"type\": [\"string\", \"null\"]},
                        \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                        \"photos\": {\"type\": \"array\"},
                        \"jnid\": {\"type\": \"string\"},
                        \"name\": {\"type\": \"string\"},
                        \"uom\": {\"type\": \"string\"},
                        \"item_type\": {\"type\": \"string\"},
                        \"description\": {\"type\": \"string\"},
                        \"quantity\": {\"type\": \"integer\"},
                        \"price\": {\"type\": \"integer\"},
                        \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                        \"cost\": {\"type\": \"integer\"},
                        \"amount\": {\"type\": \"integer\"},
                        \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                        \"tax_name\": {\"type\": [\"string\", \"null\"]},
                        \"tax_rate\": {\"type\": \"integer\"},
                        \"labor\": {
                            \"type\": \"object\",
                            \"properties\": {
                                \"quickbooksId\": {\"type\": [\"string\", \"null\"]},
                                \"price\": {\"type\": \"integer\"},
                                \"preSurchargePrice\": {\"type\": [\"string\", \"null\"]},
                                \"cost\": {\"type\": \"integer\"},
                                \"addMarkup\": {\"type\": [\"string\", \"null\"]},
                                \"amount\": {\"type\": \"integer\"},
                                \"tax_couch_id\": {\"type\": [\"string\", \"null\"]},
                                \"tax_name\": {\"type\": [\"string\", \"null\"]},
                                \"tax_rate\": {\"type\": \"integer\"}
                            }
                        },
                        \"sku\": {\"type\": [\"string\", \"null\"]},
                        \"color\": {\"type\": [\"string\", \"null\"]},
                        \"category\": {\"type\": [\"string\", \"null\"]}
                    }
                }
            },
            \"sections\": {\"type\": \"array\"},
            \"owners\": {
                \"type\": \"array\",
                \"items\": {
                    \"type\": \"object\",
                    \"properties\": {
                        \"id\": {\"type\": \"string\"}
                    }
                }
            },
            \"sales_rep\": {\"type\": \"string\"},
            \"sales_rep_name\": {\"type\": \"string\"},
            \"jnid\": {\"type\": \"string\"},
            \"internal_note\": {\"type\": \"string\"},
            \"template_id\": {\"type\": \"string\"},
            \"version\": {\"type\": [\"string\", \"null\"]},
            \"duplicate_from_id\": {\"type\": [\"string\", \"null\"]}
        }
    }

     ```

    **Response Codes**:

    - HTTP Status 200 = success

    - Anything other status code = failure and will include an error message in the response

    Args:
        authorization (Union[Unset, str]):
        body (Putapi1V2Estimates3Cjnid3EBody):  Example: {'is_active': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Putapi1V2Estimates3Cjnid3EResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
