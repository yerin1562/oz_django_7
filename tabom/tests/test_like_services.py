from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_services import do_like


class TestLikeServices(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given: 테스트 재료 준비
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When: 실제 테스트 대상(함수, api 등)울 살행
        like = do_like(user.id, article.id)

        # Then: 대상 호출 결과 검증
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user.id)
        self.assertEqual(article.id, like.article.id)
