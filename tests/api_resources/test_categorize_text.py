# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from millionways import Millionways, AsyncMillionways
from tests.utils import assert_matches_type
from millionways.types import (
    CategorizeTextClassifyResponse,
    CategorizeTextClassifyByUserResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategorizeText:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify(self, client: Millionways) -> None:
        categorize_text = client.categorize_text.classify(
            api_key="apiKey",
        )
        assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_with_all_params(self, client: Millionways) -> None:
        categorize_text = client.categorize_text.classify(
            api_key="apiKey",
            language="en",
            text="I am feeling good today and I want to go outside and meet some people.",
        )
        assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify(self, client: Millionways) -> None:
        response = client.categorize_text.with_raw_response.classify(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        categorize_text = response.parse()
        assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify(self, client: Millionways) -> None:
        with client.categorize_text.with_streaming_response.classify(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            categorize_text = response.parse()
            assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_by_user(self, client: Millionways) -> None:
        categorize_text = client.categorize_text.classify_by_user(
            user_id="userId",
            api_key="apiKey",
        )
        assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_classify_by_user_with_all_params(self, client: Millionways) -> None:
        categorize_text = client.categorize_text.classify_by_user(
            user_id="userId",
            api_key="apiKey",
            language="en",
            text="I am feeling good today and I want to go outside and meet some people.",
        )
        assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_classify_by_user(self, client: Millionways) -> None:
        response = client.categorize_text.with_raw_response.classify_by_user(
            user_id="userId",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        categorize_text = response.parse()
        assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_classify_by_user(self, client: Millionways) -> None:
        with client.categorize_text.with_streaming_response.classify_by_user(
            user_id="userId",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            categorize_text = response.parse()
            assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_classify_by_user(self, client: Millionways) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.categorize_text.with_raw_response.classify_by_user(
                user_id="",
                api_key="apiKey",
            )


class TestAsyncCategorizeText:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify(self, async_client: AsyncMillionways) -> None:
        categorize_text = await async_client.categorize_text.classify(
            api_key="apiKey",
        )
        assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_with_all_params(self, async_client: AsyncMillionways) -> None:
        categorize_text = await async_client.categorize_text.classify(
            api_key="apiKey",
            language="en",
            text="I am feeling good today and I want to go outside and meet some people.",
        )
        assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncMillionways) -> None:
        response = await async_client.categorize_text.with_raw_response.classify(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        categorize_text = await response.parse()
        assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncMillionways) -> None:
        async with async_client.categorize_text.with_streaming_response.classify(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            categorize_text = await response.parse()
            assert_matches_type(CategorizeTextClassifyResponse, categorize_text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_by_user(self, async_client: AsyncMillionways) -> None:
        categorize_text = await async_client.categorize_text.classify_by_user(
            user_id="userId",
            api_key="apiKey",
        )
        assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_classify_by_user_with_all_params(self, async_client: AsyncMillionways) -> None:
        categorize_text = await async_client.categorize_text.classify_by_user(
            user_id="userId",
            api_key="apiKey",
            language="en",
            text="I am feeling good today and I want to go outside and meet some people.",
        )
        assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_classify_by_user(self, async_client: AsyncMillionways) -> None:
        response = await async_client.categorize_text.with_raw_response.classify_by_user(
            user_id="userId",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        categorize_text = await response.parse()
        assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_classify_by_user(self, async_client: AsyncMillionways) -> None:
        async with async_client.categorize_text.with_streaming_response.classify_by_user(
            user_id="userId",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            categorize_text = await response.parse()
            assert_matches_type(CategorizeTextClassifyByUserResponse, categorize_text, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_classify_by_user(self, async_client: AsyncMillionways) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.categorize_text.with_raw_response.classify_by_user(
                user_id="",
                api_key="apiKey",
            )
