# coding: utf-8

"""
    Backlog API

    Backlog REST API specification

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from backlog_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_add_custom_field(self) -> None:
        """Test case for add_custom_field

        カスタム属性の追加
        """
        pass

    def test_add_custom_field_list_item(self) -> None:
        """Test case for add_custom_field_list_item

        選択リストカスタム属性のリスト項目の追加
        """
        pass

    def test_add_group(self) -> None:
        """Test case for add_group

        グループの追加
        """
        pass

    def test_add_issue_comment(self) -> None:
        """Test case for add_issue_comment

        課題コメントの追加
        """
        pass

    def test_add_issue_comment_notification(self) -> None:
        """Test case for add_issue_comment_notification

        課題コメントにお知らせを追加
        """
        pass

    def test_add_issue_type(self) -> None:
        """Test case for add_issue_type

        種別の追加
        """
        pass

    def test_add_project(self) -> None:
        """Test case for add_project

        プロジェクトの追加
        """
        pass

    def test_add_project_administrator(self) -> None:
        """Test case for add_project_administrator

        プロジェクト管理者の追加
        """
        pass

    def test_add_project_category(self) -> None:
        """Test case for add_project_category

        カテゴリーの追加
        """
        pass

    def test_add_project_group(self) -> None:
        """Test case for add_project_group

        プロジェクトグループの追加
        """
        pass

    def test_add_project_status(self) -> None:
        """Test case for add_project_status

        状態の追加
        """
        pass

    def test_add_project_team(self) -> None:
        """Test case for add_project_team

        プロジェクトチームの追加
        """
        pass

    def test_add_project_user(self) -> None:
        """Test case for add_project_user

        プロジェクトユーザーの追加
        """
        pass

    def test_add_pull_request_comment(self) -> None:
        """Test case for add_pull_request_comment

        プルリクエストコメントの追加
        """
        pass

    def test_add_recently_viewed_issue(self) -> None:
        """Test case for add_recently_viewed_issue

        自分が最近見た課題の追加
        """
        pass

    def test_add_recently_viewed_wiki(self) -> None:
        """Test case for add_recently_viewed_wiki

        自分が最近見たWikiの追加
        """
        pass

    def test_add_star(self) -> None:
        """Test case for add_star

        スターの追加
        """
        pass

    def test_add_team(self) -> None:
        """Test case for add_team

        チームの追加
        """
        pass

    def test_add_user(self) -> None:
        """Test case for add_user

        ユーザーの追加
        """
        pass

    def test_add_version(self) -> None:
        """Test case for add_version

        バージョン(マイルストーン)の追加
        """
        pass

    def test_add_watching(self) -> None:
        """Test case for add_watching

        ウォッチの追加
        """
        pass

    def test_add_webhook(self) -> None:
        """Test case for add_webhook

        Webhookの追加
        """
        pass

    def test_add_wiki_attachment(self) -> None:
        """Test case for add_wiki_attachment

        Wiki添付ファイルの追加
        """
        pass

    def test_create_issue(self) -> None:
        """Test case for create_issue

        課題の追加
        """
        pass

    def test_create_pull_request(self) -> None:
        """Test case for create_pull_request

        プルリクエストの追加
        """
        pass

    def test_create_wiki(self) -> None:
        """Test case for create_wiki

        Wikiページの追加
        """
        pass

    def test_delete_category(self) -> None:
        """Test case for delete_category

        カテゴリーの削除
        """
        pass

    def test_delete_custom_field(self) -> None:
        """Test case for delete_custom_field

        カスタム属性の削除
        """
        pass

    def test_delete_custom_field_list_item(self) -> None:
        """Test case for delete_custom_field_list_item

        選択リストカスタム属性のリスト項目の削除
        """
        pass

    def test_delete_group(self) -> None:
        """Test case for delete_group

        グループの削除
        """
        pass

    def test_delete_issue(self) -> None:
        """Test case for delete_issue

        課題の削除
        """
        pass

    def test_delete_issue_attachment(self) -> None:
        """Test case for delete_issue_attachment

        課題添付ファイルの削除
        """
        pass

    def test_delete_issue_comment(self) -> None:
        """Test case for delete_issue_comment

        課題コメントの削除
        """
        pass

    def test_delete_issue_type(self) -> None:
        """Test case for delete_issue_type

        種別の削除
        """
        pass

    def test_delete_project(self) -> None:
        """Test case for delete_project

        プロジェクトの削除
        """
        pass

    def test_delete_project_administrator(self) -> None:
        """Test case for delete_project_administrator

        プロジェクト管理者の削除
        """
        pass

    def test_delete_project_group(self) -> None:
        """Test case for delete_project_group

        プロジェクトグループの削除
        """
        pass

    def test_delete_project_status(self) -> None:
        """Test case for delete_project_status

        状態の削除
        """
        pass

    def test_delete_project_team(self) -> None:
        """Test case for delete_project_team

        プロジェクトチームの削除
        """
        pass

    def test_delete_project_user(self) -> None:
        """Test case for delete_project_user

        プロジェクトユーザーの削除
        """
        pass

    def test_delete_pull_request_attachment(self) -> None:
        """Test case for delete_pull_request_attachment

        プルリクエスト添付ファイルの削除
        """
        pass

    def test_delete_team(self) -> None:
        """Test case for delete_team

        チームの削除
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        ユーザーの削除
        """
        pass

    def test_delete_version(self) -> None:
        """Test case for delete_version

        バージョン(マイルストーン)の削除
        """
        pass

    def test_delete_watching(self) -> None:
        """Test case for delete_watching

        ウォッチの削除
        """
        pass

    def test_delete_webhook(self) -> None:
        """Test case for delete_webhook

        Webhookの削除
        """
        pass

    def test_delete_wiki(self) -> None:
        """Test case for delete_wiki

        Wikiページの削除
        """
        pass

    def test_delete_wiki_attachment(self) -> None:
        """Test case for delete_wiki_attachment

        Wiki添付ファイルの削除
        """
        pass

    def test_download_issue_attachment(self) -> None:
        """Test case for download_issue_attachment

        課題添付ファイルのダウンロード
        """
        pass

    def test_download_pull_request_attachment(self) -> None:
        """Test case for download_pull_request_attachment

        プルリクエスト添付ファイルのダウンロード
        """
        pass

    def test_download_shared_file(self) -> None:
        """Test case for download_shared_file

        共有ファイルのダウンロード
        """
        pass

    def test_download_wiki_attachment(self) -> None:
        """Test case for download_wiki_attachment

        Wiki添付ファイルのダウンロード
        """
        pass

    def test_get_activity(self) -> None:
        """Test case for get_activity

        アクティビティの取得
        """
        pass

    def test_get_custom_fields(self) -> None:
        """Test case for get_custom_fields

        カスタム属性一覧の取得
        """
        pass

    def test_get_git_repositories(self) -> None:
        """Test case for get_git_repositories

        Gitリポジトリ一覧の取得
        """
        pass

    def test_get_git_repository(self) -> None:
        """Test case for get_git_repository

        Gitリポジトリの取得
        """
        pass

    def test_get_group(self) -> None:
        """Test case for get_group

        グループ情報の取得
        """
        pass

    def test_get_group_icon(self) -> None:
        """Test case for get_group_icon

        グループアイコンの取得
        """
        pass

    def test_get_groups(self) -> None:
        """Test case for get_groups

        グループ一覧の取得
        """
        pass

    def test_get_issue(self) -> None:
        """Test case for get_issue

        課題情報の取得
        """
        pass

    def test_get_issue_attachments(self) -> None:
        """Test case for get_issue_attachments

        課題添付ファイル一覧の取得
        """
        pass

    def test_get_issue_comment(self) -> None:
        """Test case for get_issue_comment

        課題コメント情報の取得
        """
        pass

    def test_get_issue_comment_notifications(self) -> None:
        """Test case for get_issue_comment_notifications

        課題コメントのお知らせ一覧の取得
        """
        pass

    def test_get_issue_comments(self) -> None:
        """Test case for get_issue_comments

        課題コメントの取得
        """
        pass

    def test_get_issue_comments_count(self) -> None:
        """Test case for get_issue_comments_count

        課題コメント数の取得
        """
        pass

    def test_get_issue_participants(self) -> None:
        """Test case for get_issue_participants

        課題の参加者一覧の取得
        """
        pass

    def test_get_issue_shared_files(self) -> None:
        """Test case for get_issue_shared_files

        課題共有ファイル一覧の取得
        """
        pass

    def test_get_issue_types(self) -> None:
        """Test case for get_issue_types

        種別一覧の取得
        """
        pass

    def test_get_issues(self) -> None:
        """Test case for get_issues

        課題一覧の取得
        """
        pass

    def test_get_issues_count(self) -> None:
        """Test case for get_issues_count

        課題数の取得
        """
        pass

    def test_get_licence_info(self) -> None:
        """Test case for get_licence_info

        ライセンス情報の取得
        """
        pass

    def test_get_my_recently_viewed_wikis(self) -> None:
        """Test case for get_my_recently_viewed_wikis

        自分が最近見たWiki一覧の取得
        """
        pass

    def test_get_myself(self) -> None:
        """Test case for get_myself

        認証ユーザー情報の取得
        """
        pass

    def test_get_notifications(self) -> None:
        """Test case for get_notifications

        お知らせ一覧の取得
        """
        pass

    def test_get_notifications_count(self) -> None:
        """Test case for get_notifications_count

        お知らせ数の取得
        """
        pass

    def test_get_priorities(self) -> None:
        """Test case for get_priorities

        優先度一覧の取得
        """
        pass

    def test_get_project(self) -> None:
        """Test case for get_project

        プロジェクト情報の取得
        """
        pass

    def test_get_project_activities(self) -> None:
        """Test case for get_project_activities

        プロジェクトの最近の活動の取得
        """
        pass

    def test_get_project_administrators(self) -> None:
        """Test case for get_project_administrators

        プロジェクト管理者一覧の取得
        """
        pass

    def test_get_project_categories(self) -> None:
        """Test case for get_project_categories

        カテゴリー一覧の取得
        """
        pass

    def test_get_project_disk_usage(self) -> None:
        """Test case for get_project_disk_usage

        プロジェクトの容量使用状況の取得
        """
        pass

    def test_get_project_files(self) -> None:
        """Test case for get_project_files

        共有ファイル一覧の取得
        """
        pass

    def test_get_project_groups(self) -> None:
        """Test case for get_project_groups

        プロジェクトグループ一覧の取得
        """
        pass

    def test_get_project_icon(self) -> None:
        """Test case for get_project_icon

        プロジェクトアイコンの取得
        """
        pass

    def test_get_project_statuses(self) -> None:
        """Test case for get_project_statuses

        プロジェクトの状態一覧の取得
        """
        pass

    def test_get_project_teams(self) -> None:
        """Test case for get_project_teams

        プロジェクトチーム一覧の取得
        """
        pass

    def test_get_project_users(self) -> None:
        """Test case for get_project_users

        プロジェクトユーザー一覧の取得
        """
        pass

    def test_get_project_versions(self) -> None:
        """Test case for get_project_versions

        バージョン(マイルストーン)一覧の取得
        """
        pass

    def test_get_project_webhooks(self) -> None:
        """Test case for get_project_webhooks

        Webhook一覧の取得
        """
        pass

    def test_get_projects(self) -> None:
        """Test case for get_projects

        プロジェクト一覧の取得
        """
        pass

    def test_get_pull_request(self) -> None:
        """Test case for get_pull_request

        プルリクエストの取得
        """
        pass

    def test_get_pull_request_attachments(self) -> None:
        """Test case for get_pull_request_attachments

        プルリクエスト添付ファイル一覧の取得
        """
        pass

    def test_get_pull_request_comment_count(self) -> None:
        """Test case for get_pull_request_comment_count

        プルリクエストコメント数の取得
        """
        pass

    def test_get_pull_request_comments(self) -> None:
        """Test case for get_pull_request_comments

        プルリクエストコメントの取得
        """
        pass

    def test_get_pull_requests(self) -> None:
        """Test case for get_pull_requests

        プルリクエスト一覧の取得
        """
        pass

    def test_get_pull_requests_count(self) -> None:
        """Test case for get_pull_requests_count

        プルリクエスト数の取得
        """
        pass

    def test_get_rate_limit(self) -> None:
        """Test case for get_rate_limit

        レート制限情報の取得
        """
        pass

    def test_get_recently_viewed_issues(self) -> None:
        """Test case for get_recently_viewed_issues

        自分が最近見た課題一覧の取得
        """
        pass

    def test_get_recently_viewed_projects(self) -> None:
        """Test case for get_recently_viewed_projects

        自分が最近見たプロジェクト一覧の取得
        """
        pass

    def test_get_resolutions(self) -> None:
        """Test case for get_resolutions

        完了理由一覧の取得
        """
        pass

    def test_get_space(self) -> None:
        """Test case for get_space

        スペース情報の取得
        """
        pass

    def test_get_space_activities(self) -> None:
        """Test case for get_space_activities

        最近の更新の取得
        """
        pass

    def test_get_space_disk_usage(self) -> None:
        """Test case for get_space_disk_usage

        スペースの容量使用状況の取得
        """
        pass

    def test_get_space_image(self) -> None:
        """Test case for get_space_image

        スペースアイコン画像の取得
        """
        pass

    def test_get_space_notification(self) -> None:
        """Test case for get_space_notification

        スペースのお知らせの取得
        """
        pass

    def test_get_statuses(self) -> None:
        """Test case for get_statuses

        状態一覧の取得
        """
        pass

    def test_get_team(self) -> None:
        """Test case for get_team

        チーム情報の取得
        """
        pass

    def test_get_team_icon(self) -> None:
        """Test case for get_team_icon

        チームアイコンの取得
        """
        pass

    def test_get_teams(self) -> None:
        """Test case for get_teams

        チーム一覧の取得
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        ユーザー情報の取得
        """
        pass

    def test_get_user_activities(self) -> None:
        """Test case for get_user_activities

        ユーザーの最近の活動の取得
        """
        pass

    def test_get_user_icon(self) -> None:
        """Test case for get_user_icon

        ユーザーアイコンの取得
        """
        pass

    def test_get_user_stars(self) -> None:
        """Test case for get_user_stars

        ユーザーの受け取ったスター一覧の取得
        """
        pass

    def test_get_user_stars_count(self) -> None:
        """Test case for get_user_stars_count

        ユーザーの受け取ったスターの数の取得
        """
        pass

    def test_get_user_watchings(self) -> None:
        """Test case for get_user_watchings

        ウォッチ一覧の取得
        """
        pass

    def test_get_users(self) -> None:
        """Test case for get_users

        ユーザー一覧の取得
        """
        pass

    def test_get_watching(self) -> None:
        """Test case for get_watching

        ウォッチ情報の取得
        """
        pass

    def test_get_watching_count(self) -> None:
        """Test case for get_watching_count

        ウォッチ数の取得
        """
        pass

    def test_get_webhook(self) -> None:
        """Test case for get_webhook

        Webhookの取得
        """
        pass

    def test_get_wiki(self) -> None:
        """Test case for get_wiki

        Wikiページ情報の取得
        """
        pass

    def test_get_wiki_attachments(self) -> None:
        """Test case for get_wiki_attachments

        Wiki添付ファイル一覧の取得
        """
        pass

    def test_get_wiki_count(self) -> None:
        """Test case for get_wiki_count

        Wikiページ数の取得
        """
        pass

    def test_get_wiki_history(self) -> None:
        """Test case for get_wiki_history

        Wikiページ更新履歴一覧の取得
        """
        pass

    def test_get_wiki_shared_files(self) -> None:
        """Test case for get_wiki_shared_files

        Wiki共有ファイル一覧の取得
        """
        pass

    def test_get_wiki_stars(self) -> None:
        """Test case for get_wiki_stars

        Wikiページのスター一覧の取得
        """
        pass

    def test_get_wiki_tags(self) -> None:
        """Test case for get_wiki_tags

        Wikiページタグ一覧の取得
        """
        pass

    def test_get_wikis(self) -> None:
        """Test case for get_wikis

        Wikiページ一覧の取得
        """
        pass

    def test_link_shared_file_to_wiki(self) -> None:
        """Test case for link_shared_file_to_wiki

        Wikiに共有ファイルをリンク
        """
        pass

    def test_link_shared_files_to_issue(self) -> None:
        """Test case for link_shared_files_to_issue

        課題に共有ファイルをリンク
        """
        pass

    def test_mark_notification_as_read(self) -> None:
        """Test case for mark_notification_as_read

        お知らせの既読化
        """
        pass

    def test_mark_watching_as_read(self) -> None:
        """Test case for mark_watching_as_read

        ウォッチの既読化
        """
        pass

    def test_post_attachment(self) -> None:
        """Test case for post_attachment

        添付ファイルの送信
        """
        pass

    def test_reset_notification_count(self) -> None:
        """Test case for reset_notification_count

        お知らせ数のリセット
        """
        pass

    def test_unlink_issue_shared_file(self) -> None:
        """Test case for unlink_issue_shared_file

        課題の共有ファイルのリンクを解除
        """
        pass

    def test_unlink_wiki_shared_file(self) -> None:
        """Test case for unlink_wiki_shared_file

        Wikiの共有ファイルのリンクを解除
        """
        pass

    def test_update_category(self) -> None:
        """Test case for update_category

        カテゴリー情報の更新
        """
        pass

    def test_update_custom_field(self) -> None:
        """Test case for update_custom_field

        カスタム属性の更新
        """
        pass

    def test_update_custom_field_list_item(self) -> None:
        """Test case for update_custom_field_list_item

        選択リストカスタム属性のリスト項目の更新
        """
        pass

    def test_update_group(self) -> None:
        """Test case for update_group

        グループ情報の更新
        """
        pass

    def test_update_issue(self) -> None:
        """Test case for update_issue

        課題情報の更新
        """
        pass

    def test_update_issue_comment(self) -> None:
        """Test case for update_issue_comment

        課題コメント情報の更新
        """
        pass

    def test_update_issue_type(self) -> None:
        """Test case for update_issue_type

        種別情報の更新
        """
        pass

    def test_update_project(self) -> None:
        """Test case for update_project

        プロジェクト情報の更新
        """
        pass

    def test_update_project_status(self) -> None:
        """Test case for update_project_status

        状態情報の更新
        """
        pass

    def test_update_pull_request(self) -> None:
        """Test case for update_pull_request

        プルリクエストの更新
        """
        pass

    def test_update_pull_request_comment(self) -> None:
        """Test case for update_pull_request_comment

        プルリクエストコメント情報の更新
        """
        pass

    def test_update_space_notification(self) -> None:
        """Test case for update_space_notification

        スペースのお知らせの更新
        """
        pass

    def test_update_status_display_order(self) -> None:
        """Test case for update_status_display_order

        状態の並び替え
        """
        pass

    def test_update_team(self) -> None:
        """Test case for update_team

        チーム情報の更新
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        ユーザーの更新
        """
        pass

    def test_update_version(self) -> None:
        """Test case for update_version

        バージョン(マイルストーン)情報の更新
        """
        pass

    def test_update_watching(self) -> None:
        """Test case for update_watching

        ウォッチの更新
        """
        pass

    def test_update_webhook(self) -> None:
        """Test case for update_webhook

        Webhookの更新
        """
        pass

    def test_update_wiki(self) -> None:
        """Test case for update_wiki

        Wikiページ情報の更新
        """
        pass


if __name__ == '__main__':
    unittest.main()