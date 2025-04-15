from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postapi_1_files_body import Postapi1FilesBody
from ...models.postapi_1_files_response_200 import Postapi1FilesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Postapi1FilesBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api1/files",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Postapi1FilesResponse200]:
    if response.status_code == 200:
        response_200 = Postapi1FilesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Postapi1FilesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1FilesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1FilesResponse200]:
    r"""Create a File

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    *Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    Type:
    * 1=Document
    * 2=Photo
    * 3=Email Attachment
    * 4=naturalForms
    * 5=Invoice
    * 6=Eagleview
    * 7=Accurence
    * 8=Credit Memo

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    ```
    {
        \"count\": 165,
        \"files\": [
            {
                \"customer\": \"jagpt\",
                \"type\": \"attachment\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"is_active\": true,
                \"filename\": \"Screen Shot 2018-06-26 at 8.39.48 PM.png\",
                \"content_type\": \"image/png\",
                \"size\": 555204,
                \"jnid\": \"jsy16hg9ztze7cxx\",
                \"date_created\": 1551926855,
                \"date_updated\": 1551926859,
                \"is_private\": false,
                \"related\": [
                    {
                        \"id\": \"scpci\",
                        \"type\": \"contact\",
                        \"name\": \"Jimmy Rivera III\"
                    }
                ],
                \"primary\": {
                    \"id\": \"scpci\",
                    \"type\": \"contact\",
                    \"number\": \"1164\",
                    \"name\": \"Jimmy Rivera III\"
                },
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"sales_rep\": \"jagpu\",
                \"is_archived\": false,
                \"record_type\": 2,
                \"record_type_name\": \"Photo\"
            }
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesBody):  Example: {'data': 'VGhpcyBpcyBteSBuZXcgdGV4dCBkb2N1bWVudC4=',
            'is_private': False, 'related': ['hpzui'], 'type': 1, 'subtype': 'contact', 'filename':
            'myfilename.txt', 'description': 'The description of my file.', 'date': 1513367467,
            'persist': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1FilesResponse200]
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
    body: Postapi1FilesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1FilesResponse200]:
    r"""Create a File

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    *Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    Type:
    * 1=Document
    * 2=Photo
    * 3=Email Attachment
    * 4=naturalForms
    * 5=Invoice
    * 6=Eagleview
    * 7=Accurence
    * 8=Credit Memo

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    ```
    {
        \"count\": 165,
        \"files\": [
            {
                \"customer\": \"jagpt\",
                \"type\": \"attachment\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"is_active\": true,
                \"filename\": \"Screen Shot 2018-06-26 at 8.39.48 PM.png\",
                \"content_type\": \"image/png\",
                \"size\": 555204,
                \"jnid\": \"jsy16hg9ztze7cxx\",
                \"date_created\": 1551926855,
                \"date_updated\": 1551926859,
                \"is_private\": false,
                \"related\": [
                    {
                        \"id\": \"scpci\",
                        \"type\": \"contact\",
                        \"name\": \"Jimmy Rivera III\"
                    }
                ],
                \"primary\": {
                    \"id\": \"scpci\",
                    \"type\": \"contact\",
                    \"number\": \"1164\",
                    \"name\": \"Jimmy Rivera III\"
                },
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"sales_rep\": \"jagpu\",
                \"is_archived\": false,
                \"record_type\": 2,
                \"record_type_name\": \"Photo\"
            }
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesBody):  Example: {'data': 'VGhpcyBpcyBteSBuZXcgdGV4dCBkb2N1bWVudC4=',
            'is_private': False, 'related': ['hpzui'], 'type': 1, 'subtype': 'contact', 'filename':
            'myfilename.txt', 'description': 'The description of my file.', 'date': 1513367467,
            'persist': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1FilesResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Postapi1FilesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Postapi1FilesResponse200]:
    r"""Create a File

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    *Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    Type:
    * 1=Document
    * 2=Photo
    * 3=Email Attachment
    * 4=naturalForms
    * 5=Invoice
    * 6=Eagleview
    * 7=Accurence
    * 8=Credit Memo

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    ```
    {
        \"count\": 165,
        \"files\": [
            {
                \"customer\": \"jagpt\",
                \"type\": \"attachment\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"is_active\": true,
                \"filename\": \"Screen Shot 2018-06-26 at 8.39.48 PM.png\",
                \"content_type\": \"image/png\",
                \"size\": 555204,
                \"jnid\": \"jsy16hg9ztze7cxx\",
                \"date_created\": 1551926855,
                \"date_updated\": 1551926859,
                \"is_private\": false,
                \"related\": [
                    {
                        \"id\": \"scpci\",
                        \"type\": \"contact\",
                        \"name\": \"Jimmy Rivera III\"
                    }
                ],
                \"primary\": {
                    \"id\": \"scpci\",
                    \"type\": \"contact\",
                    \"number\": \"1164\",
                    \"name\": \"Jimmy Rivera III\"
                },
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"sales_rep\": \"jagpu\",
                \"is_archived\": false,
                \"record_type\": 2,
                \"record_type_name\": \"Photo\"
            }
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesBody):  Example: {'data': 'VGhpcyBpcyBteSBuZXcgdGV4dCBkb2N1bWVudC4=',
            'is_private': False, 'related': ['hpzui'], 'type': 1, 'subtype': 'contact', 'filename':
            'myfilename.txt', 'description': 'The description of my file.', 'date': 1513367467,
            'persist': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Postapi1FilesResponse200]
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
    body: Postapi1FilesBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Postapi1FilesResponse200]:
    r"""Create a File

     This request allows you to create a new File attachment within JobNimbus.

    **Notes**:

    *Data attribute should be base64 encoded, ie. btoa('This is my document text.')

    Type:
    * 1=Document
    * 2=Photo
    * 3=Email Attachment
    * 4=naturalForms
    * 5=Invoice
    * 6=Eagleview
    * 7=Accurence
    * 8=Credit Memo

    **Response Codes**:

    * HTTP Status 200 = success
    * Anything other status code = failure and will include an error message in the response

    **Response**:

    ```
    {
        \"count\": 165,
        \"files\": [
            {
                \"customer\": \"jagpt\",
                \"type\": \"attachment\",
                \"created_by\": \"jagpu\",
                \"created_by_name\": \"Josh Demo\",
                \"is_active\": true,
                \"filename\": \"Screen Shot 2018-06-26 at 8.39.48 PM.png\",
                \"content_type\": \"image/png\",
                \"size\": 555204,
                \"jnid\": \"jsy16hg9ztze7cxx\",
                \"date_created\": 1551926855,
                \"date_updated\": 1551926859,
                \"is_private\": false,
                \"related\": [
                    {
                        \"id\": \"scpci\",
                        \"type\": \"contact\",
                        \"name\": \"Jimmy Rivera III\"
                    }
                ],
                \"primary\": {
                    \"id\": \"scpci\",
                    \"type\": \"contact\",
                    \"number\": \"1164\",
                    \"name\": \"Jimmy Rivera III\"
                },
                \"owners\": [
                    {
                        \"id\": \"jagpu\"
                    }
                ],
                \"sales_rep\": \"jagpu\",
                \"is_archived\": false,
                \"record_type\": 2,
                \"record_type_name\": \"Photo\"
            }
        ]
    }
    ```

    Args:
        authorization (Union[Unset, str]):
        body (Postapi1FilesBody):  Example: {'data': 'VGhpcyBpcyBteSBuZXcgdGV4dCBkb2N1bWVudC4=',
            'is_private': False, 'related': ['hpzui'], 'type': 1, 'subtype': 'contact', 'filename':
            'myfilename.txt', 'description': 'The description of my file.', 'date': 1513367467,
            'persist': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Postapi1FilesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
