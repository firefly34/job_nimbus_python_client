from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_filesfrom_url_body import Postapi1FilesfromUrlBody
from ...models.postapi_1_filesfrom_url_response_200 import Postapi1FilesfromUrlResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Postapi1FilesfromUrlBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/files/fromUrl",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1FilesfromUrlResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1FilesfromUrlResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1FilesfromUrlResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1FilesfromUrlBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1FilesfromUrlResponse200]:
    """Create a File from URL

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    * Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    * Type:
     * 1=Document
     * 2=Photo
     * 3=Email Attachment
     * 4=naturalForms
     * 5=Invoice
     * 6=Eagleview
     * 7=Accurence
     * 8=Credit Memo

    * related[] should be the jnid of the contact or job that this file should be attached to
    * type should be set to a valid file type as defined in the JobNimbus customer settings. Usually
    this can be set to 'Photo'
    * description should be set to a photo caption/description
    * name should be set to the file name. If not supplied, the file name will be extracted from the url
    * url should be set to the publicly accessable url of the image

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response
    * A json response body will include an 'id' field. This should probably be associated with the file
    in the remote database in case we decide to implement the ability to upload image revisions

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesfromUrlBody):  Example: {'related': ['3pd'], 'type': 'Photo',
            'description': 'This is the image description / caption', 'url':
            'https://s3.amazonaws.com/pubfilerepo/Tasks%20List.png'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1FilesfromUrlResponse200]
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
    body: Postapi1FilesfromUrlBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1FilesfromUrlResponse200]:
    """Create a File from URL

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    * Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    * Type:
     * 1=Document
     * 2=Photo
     * 3=Email Attachment
     * 4=naturalForms
     * 5=Invoice
     * 6=Eagleview
     * 7=Accurence
     * 8=Credit Memo

    * related[] should be the jnid of the contact or job that this file should be attached to
    * type should be set to a valid file type as defined in the JobNimbus customer settings. Usually
    this can be set to 'Photo'
    * description should be set to a photo caption/description
    * name should be set to the file name. If not supplied, the file name will be extracted from the url
    * url should be set to the publicly accessable url of the image

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response
    * A json response body will include an 'id' field. This should probably be associated with the file
    in the remote database in case we decide to implement the ability to upload image revisions

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesfromUrlBody):  Example: {'related': ['3pd'], 'type': 'Photo',
            'description': 'This is the image description / caption', 'url':
            'https://s3.amazonaws.com/pubfilerepo/Tasks%20List.png'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1FilesfromUrlResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1FilesfromUrlBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1FilesfromUrlResponse200]:
    """Create a File from URL

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    * Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    * Type:
     * 1=Document
     * 2=Photo
     * 3=Email Attachment
     * 4=naturalForms
     * 5=Invoice
     * 6=Eagleview
     * 7=Accurence
     * 8=Credit Memo

    * related[] should be the jnid of the contact or job that this file should be attached to
    * type should be set to a valid file type as defined in the JobNimbus customer settings. Usually
    this can be set to 'Photo'
    * description should be set to a photo caption/description
    * name should be set to the file name. If not supplied, the file name will be extracted from the url
    * url should be set to the publicly accessable url of the image

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response
    * A json response body will include an 'id' field. This should probably be associated with the file
    in the remote database in case we decide to implement the ability to upload image revisions

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesfromUrlBody):  Example: {'related': ['3pd'], 'type': 'Photo',
            'description': 'This is the image description / caption', 'url':
            'https://s3.amazonaws.com/pubfilerepo/Tasks%20List.png'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1FilesfromUrlResponse200]
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
    body: Postapi1FilesfromUrlBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1FilesfromUrlResponse200]:
    """Create a File from URL

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    * Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    * Type:
     * 1=Document
     * 2=Photo
     * 3=Email Attachment
     * 4=naturalForms
     * 5=Invoice
     * 6=Eagleview
     * 7=Accurence
     * 8=Credit Memo

    * related[] should be the jnid of the contact or job that this file should be attached to
    * type should be set to a valid file type as defined in the JobNimbus customer settings. Usually
    this can be set to 'Photo'
    * description should be set to a photo caption/description
    * name should be set to the file name. If not supplied, the file name will be extracted from the url
    * url should be set to the publicly accessable url of the image

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response
    * A json response body will include an 'id' field. This should probably be associated with the file
    in the remote database in case we decide to implement the ability to upload image revisions

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesfromUrlBody):  Example: {'related': ['3pd'], 'type': 'Photo',
            'description': 'This is the image description / caption', 'url':
            'https://s3.amazonaws.com/pubfilerepo/Tasks%20List.png'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1FilesfromUrlResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
