# backlog_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field**](DefaultApi.md#add_custom_field) | **POST** /api/v2/projects/{projectIdOrKey}/customFields | カスタム属性の追加
[**add_custom_field_list_item**](DefaultApi.md#add_custom_field_list_item) | **POST** /api/v2/projects/{projectIdOrKey}/customFields/{id}/items | 選択リストカスタム属性のリスト項目の追加
[**add_group**](DefaultApi.md#add_group) | **POST** /api/v2/groups | グループの追加
[**add_issue_comment**](DefaultApi.md#add_issue_comment) | **POST** /api/v2/issues/{issueIdOrKey}/comments | 課題コメントの追加
[**add_issue_comment_notification**](DefaultApi.md#add_issue_comment_notification) | **POST** /api/v2/issues/{issueIdOrKey}/comments/{commentId}/notifications | 課題コメントにお知らせを追加
[**add_issue_type**](DefaultApi.md#add_issue_type) | **POST** /api/v2/projects/{projectIdOrKey}/issueTypes | 種別の追加
[**add_project**](DefaultApi.md#add_project) | **POST** /api/v2/projects | プロジェクトの追加
[**add_project_administrator**](DefaultApi.md#add_project_administrator) | **POST** /api/v2/projects/{projectIdOrKey}/administrators | プロジェクト管理者の追加
[**add_project_category**](DefaultApi.md#add_project_category) | **POST** /api/v2/projects/{projectIdOrKey}/categories | カテゴリーの追加
[**add_project_group**](DefaultApi.md#add_project_group) | **POST** /api/v2/projects/{projectIdOrKey}/groups | プロジェクトグループの追加
[**add_project_status**](DefaultApi.md#add_project_status) | **POST** /api/v2/projects/{projectIdOrKey}/statuses | 状態の追加
[**add_project_team**](DefaultApi.md#add_project_team) | **POST** /api/v2/projects/{projectIdOrKey}/teams | プロジェクトチームの追加
[**add_project_user**](DefaultApi.md#add_project_user) | **POST** /api/v2/projects/{projectIdOrKey}/users | プロジェクトユーザーの追加
[**add_pull_request_comment**](DefaultApi.md#add_pull_request_comment) | **POST** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/comments | プルリクエストコメントの追加
[**add_recently_viewed_issue**](DefaultApi.md#add_recently_viewed_issue) | **POST** /api/v2/users/myself/recentlyViewedIssues | 自分が最近見た課題の追加
[**add_recently_viewed_wiki**](DefaultApi.md#add_recently_viewed_wiki) | **POST** /api/v2/users/myself/recentlyViewedWikis | 自分が最近見たWikiの追加
[**add_star**](DefaultApi.md#add_star) | **POST** /api/v2/stars | スターの追加
[**add_team**](DefaultApi.md#add_team) | **POST** /api/v2/teams | チームの追加
[**add_user**](DefaultApi.md#add_user) | **POST** /api/v2/users | ユーザーの追加
[**add_version**](DefaultApi.md#add_version) | **POST** /api/v2/projects/{projectIdOrKey}/versions | バージョン(マイルストーン)の追加
[**add_watching**](DefaultApi.md#add_watching) | **POST** /api/v2/watchings | ウォッチの追加
[**add_webhook**](DefaultApi.md#add_webhook) | **POST** /api/v2/projects/{projectIdOrKey}/webhooks | Webhookの追加
[**add_wiki_attachment**](DefaultApi.md#add_wiki_attachment) | **POST** /api/v2/wikis/{wikiId}/attachments | Wiki添付ファイルの追加
[**create_issue**](DefaultApi.md#create_issue) | **POST** /api/v2/issues | 課題の追加
[**create_pull_request**](DefaultApi.md#create_pull_request) | **POST** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests | プルリクエストの追加
[**create_wiki**](DefaultApi.md#create_wiki) | **POST** /api/v2/wikis | Wikiページの追加
[**delete_category**](DefaultApi.md#delete_category) | **DELETE** /api/v2/projects/{projectIdOrKey}/categories/{id} | カテゴリーの削除
[**delete_custom_field**](DefaultApi.md#delete_custom_field) | **DELETE** /api/v2/projects/{projectIdOrKey}/customFields/{id} | カスタム属性の削除
[**delete_custom_field_list_item**](DefaultApi.md#delete_custom_field_list_item) | **DELETE** /api/v2/projects/{projectIdOrKey}/customFields/{id}/items/{itemId} | 選択リストカスタム属性のリスト項目の削除
[**delete_group**](DefaultApi.md#delete_group) | **DELETE** /api/v2/groups/{groupId} | グループの削除
[**delete_issue**](DefaultApi.md#delete_issue) | **DELETE** /api/v2/issues/{issueIdOrKey} | 課題の削除
[**delete_issue_attachment**](DefaultApi.md#delete_issue_attachment) | **DELETE** /api/v2/issues/{issueIdOrKey}/attachments/{attachmentId} | 課題添付ファイルの削除
[**delete_issue_comment**](DefaultApi.md#delete_issue_comment) | **DELETE** /api/v2/issues/{issueIdOrKey}/comments/{commentId} | 課題コメントの削除
[**delete_issue_type**](DefaultApi.md#delete_issue_type) | **DELETE** /api/v2/projects/{projectIdOrKey}/issueTypes/{id} | 種別の削除
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /api/v2/projects/{projectIdOrKey} | プロジェクトの削除
[**delete_project_administrator**](DefaultApi.md#delete_project_administrator) | **DELETE** /api/v2/projects/{projectIdOrKey}/administrators | プロジェクト管理者の削除
[**delete_project_group**](DefaultApi.md#delete_project_group) | **DELETE** /api/v2/projects/{projectIdOrKey}/groups | プロジェクトグループの削除
[**delete_project_status**](DefaultApi.md#delete_project_status) | **DELETE** /api/v2/projects/{projectIdOrKey}/statuses/{id} | 状態の削除
[**delete_project_team**](DefaultApi.md#delete_project_team) | **DELETE** /api/v2/projects/{projectIdOrKey}/teams | プロジェクトチームの削除
[**delete_project_user**](DefaultApi.md#delete_project_user) | **DELETE** /api/v2/projects/{projectIdOrKey}/users | プロジェクトユーザーの削除
[**delete_pull_request_attachment**](DefaultApi.md#delete_pull_request_attachment) | **DELETE** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/attachments/{attachmentId} | プルリクエスト添付ファイルの削除
[**delete_team**](DefaultApi.md#delete_team) | **DELETE** /api/v2/teams/{teamId} | チームの削除
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /api/v2/users/{userId} | ユーザーの削除
[**delete_version**](DefaultApi.md#delete_version) | **DELETE** /api/v2/projects/{projectIdOrKey}/versions/{id} | バージョン(マイルストーン)の削除
[**delete_watching**](DefaultApi.md#delete_watching) | **DELETE** /api/v2/watchings/{watchingId} | ウォッチの削除
[**delete_webhook**](DefaultApi.md#delete_webhook) | **DELETE** /api/v2/projects/{projectIdOrKey}/webhooks/{webhookId} | Webhookの削除
[**delete_wiki**](DefaultApi.md#delete_wiki) | **DELETE** /api/v2/wikis/{wikiId} | Wikiページの削除
[**delete_wiki_attachment**](DefaultApi.md#delete_wiki_attachment) | **DELETE** /api/v2/wikis/{wikiId}/attachments/{attachmentId} | Wiki添付ファイルの削除
[**download_issue_attachment**](DefaultApi.md#download_issue_attachment) | **GET** /api/v2/issues/{issueIdOrKey}/attachments/{attachmentId} | 課題添付ファイルのダウンロード
[**download_pull_request_attachment**](DefaultApi.md#download_pull_request_attachment) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/attachments/{attachmentId} | プルリクエスト添付ファイルのダウンロード
[**download_shared_file**](DefaultApi.md#download_shared_file) | **GET** /api/v2/projects/{projectIdOrKey}/files/{sharedFileId} | 共有ファイルのダウンロード
[**download_wiki_attachment**](DefaultApi.md#download_wiki_attachment) | **GET** /api/v2/wikis/{wikiId}/attachments/{attachmentId} | Wiki添付ファイルのダウンロード
[**get_activity**](DefaultApi.md#get_activity) | **GET** /api/v2/activities/{activityId} | アクティビティの取得
[**get_custom_fields**](DefaultApi.md#get_custom_fields) | **GET** /api/v2/projects/{projectIdOrKey}/customFields | カスタム属性一覧の取得
[**get_git_repositories**](DefaultApi.md#get_git_repositories) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories | Gitリポジトリ一覧の取得
[**get_git_repository**](DefaultApi.md#get_git_repository) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName} | Gitリポジトリの取得
[**get_group**](DefaultApi.md#get_group) | **GET** /api/v2/groups/{groupId} | グループ情報の取得
[**get_group_icon**](DefaultApi.md#get_group_icon) | **GET** /api/v2/groups/{groupId}/icon | グループアイコンの取得
[**get_groups**](DefaultApi.md#get_groups) | **GET** /api/v2/groups | グループ一覧の取得
[**get_issue**](DefaultApi.md#get_issue) | **GET** /api/v2/issues/{issueIdOrKey} | 課題情報の取得
[**get_issue_attachments**](DefaultApi.md#get_issue_attachments) | **GET** /api/v2/issues/{issueIdOrKey}/attachments | 課題添付ファイル一覧の取得
[**get_issue_comment**](DefaultApi.md#get_issue_comment) | **GET** /api/v2/issues/{issueIdOrKey}/comments/{commentId} | 課題コメント情報の取得
[**get_issue_comment_notifications**](DefaultApi.md#get_issue_comment_notifications) | **GET** /api/v2/issues/{issueIdOrKey}/comments/{commentId}/notifications | 課題コメントのお知らせ一覧の取得
[**get_issue_comments**](DefaultApi.md#get_issue_comments) | **GET** /api/v2/issues/{issueIdOrKey}/comments | 課題コメントの取得
[**get_issue_comments_count**](DefaultApi.md#get_issue_comments_count) | **GET** /api/v2/issues/{issueIdOrKey}/comments/count | 課題コメント数の取得
[**get_issue_participants**](DefaultApi.md#get_issue_participants) | **GET** /api/v2/issues/{issueIdOrKey}/participants | 課題の参加者一覧の取得
[**get_issue_shared_files**](DefaultApi.md#get_issue_shared_files) | **GET** /api/v2/issues/{issueIdOrKey}/sharedFiles | 課題共有ファイル一覧の取得
[**get_issue_types**](DefaultApi.md#get_issue_types) | **GET** /api/v2/projects/{projectIdOrKey}/issueTypes | 種別一覧の取得
[**get_issues**](DefaultApi.md#get_issues) | **GET** /api/v2/issues | 課題一覧の取得
[**get_issues_count**](DefaultApi.md#get_issues_count) | **GET** /api/v2/issues/count | 課題数の取得
[**get_licence_info**](DefaultApi.md#get_licence_info) | **GET** /api/v2/space/licence | ライセンス情報の取得
[**get_my_recently_viewed_wikis**](DefaultApi.md#get_my_recently_viewed_wikis) | **GET** /api/v2/users/myself/recentlyViewedWikis | 自分が最近見たWiki一覧の取得
[**get_myself**](DefaultApi.md#get_myself) | **GET** /api/v2/users/myself | 認証ユーザー情報の取得
[**get_notifications**](DefaultApi.md#get_notifications) | **GET** /api/v2/notifications | お知らせ一覧の取得
[**get_notifications_count**](DefaultApi.md#get_notifications_count) | **GET** /api/v2/notifications/count | お知らせ数の取得
[**get_priorities**](DefaultApi.md#get_priorities) | **GET** /api/v2/priorities | 優先度一覧の取得
[**get_project**](DefaultApi.md#get_project) | **GET** /api/v2/projects/{projectIdOrKey} | プロジェクト情報の取得
[**get_project_activities**](DefaultApi.md#get_project_activities) | **GET** /api/v2/projects/{projectIdOrKey}/activities | プロジェクトの最近の活動の取得
[**get_project_administrators**](DefaultApi.md#get_project_administrators) | **GET** /api/v2/projects/{projectIdOrKey}/administrators | プロジェクト管理者一覧の取得
[**get_project_categories**](DefaultApi.md#get_project_categories) | **GET** /api/v2/projects/{projectIdOrKey}/categories | カテゴリー一覧の取得
[**get_project_disk_usage**](DefaultApi.md#get_project_disk_usage) | **GET** /api/v2/projects/{projectIdOrKey}/diskUsage | プロジェクトの容量使用状況の取得
[**get_project_files**](DefaultApi.md#get_project_files) | **GET** /api/v2/projects/{projectIdOrKey}/files/metadata/{path} | 共有ファイル一覧の取得
[**get_project_groups**](DefaultApi.md#get_project_groups) | **GET** /api/v2/projects/{projectIdOrKey}/groups | プロジェクトグループ一覧の取得
[**get_project_icon**](DefaultApi.md#get_project_icon) | **GET** /api/v2/projects/{projectIdOrKey}/image | プロジェクトアイコンの取得
[**get_project_statuses**](DefaultApi.md#get_project_statuses) | **GET** /api/v2/projects/{projectIdOrKey}/statuses | プロジェクトの状態一覧の取得
[**get_project_teams**](DefaultApi.md#get_project_teams) | **GET** /api/v2/projects/{projectIdOrKey}/teams | プロジェクトチーム一覧の取得
[**get_project_users**](DefaultApi.md#get_project_users) | **GET** /api/v2/projects/{projectIdOrKey}/users | プロジェクトユーザー一覧の取得
[**get_project_versions**](DefaultApi.md#get_project_versions) | **GET** /api/v2/projects/{projectIdOrKey}/versions | バージョン(マイルストーン)一覧の取得
[**get_projects**](DefaultApi.md#get_projects) | **GET** /api/v2/projects | プロジェクト一覧の取得
[**get_pull_request**](DefaultApi.md#get_pull_request) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number} | プルリクエストの取得
[**get_pull_request_attachments**](DefaultApi.md#get_pull_request_attachments) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/attachments | プルリクエスト添付ファイル一覧の取得
[**get_pull_request_comment_count**](DefaultApi.md#get_pull_request_comment_count) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/comments/count | プルリクエストコメント数の取得
[**get_pull_request_comments**](DefaultApi.md#get_pull_request_comments) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/comments | プルリクエストコメントの取得
[**get_pull_request_count**](DefaultApi.md#get_pull_request_count) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/count | プルリクエスト数の取得
[**get_pull_requests**](DefaultApi.md#get_pull_requests) | **GET** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests | プルリクエスト一覧の取得
[**get_rate_limit**](DefaultApi.md#get_rate_limit) | **GET** /api/v2/rateLimit | レート制限情報の取得
[**get_recently_viewed_issues**](DefaultApi.md#get_recently_viewed_issues) | **GET** /api/v2/users/myself/recentlyViewedIssues | 自分が最近見た課題一覧の取得
[**get_recently_viewed_projects**](DefaultApi.md#get_recently_viewed_projects) | **GET** /api/v2/users/myself/recentlyViewedProjects | 自分が最近見たプロジェクト一覧の取得
[**get_resolutions**](DefaultApi.md#get_resolutions) | **GET** /api/v2/resolutions | 完了理由一覧の取得
[**get_space**](DefaultApi.md#get_space) | **GET** /api/v2/space | スペース情報の取得
[**get_space_activities**](DefaultApi.md#get_space_activities) | **GET** /api/v2/space/activities | 最近の更新の取得
[**get_space_disk_usage**](DefaultApi.md#get_space_disk_usage) | **GET** /api/v2/space/diskUsage | スペースの容量使用状況の取得
[**get_space_image**](DefaultApi.md#get_space_image) | **GET** /api/v2/space/image | スペースアイコン画像の取得
[**get_space_notification**](DefaultApi.md#get_space_notification) | **GET** /api/v2/space/notification | スペースのお知らせの取得
[**get_statuses**](DefaultApi.md#get_statuses) | **GET** /api/v2/statuses | 状態一覧の取得
[**get_team**](DefaultApi.md#get_team) | **GET** /api/v2/teams/{teamId} | チーム情報の取得
[**get_team_icon**](DefaultApi.md#get_team_icon) | **GET** /api/v2/teams/{teamId}/icon | チームアイコンの取得
[**get_teams**](DefaultApi.md#get_teams) | **GET** /api/v2/teams | チーム一覧の取得
[**get_user**](DefaultApi.md#get_user) | **GET** /api/v2/users/{userId} | ユーザー情報の取得
[**get_user_activities**](DefaultApi.md#get_user_activities) | **GET** /api/v2/users/{userId}/activities | ユーザーの最近の活動の取得
[**get_user_icon**](DefaultApi.md#get_user_icon) | **GET** /api/v2/users/{userId}/icon | ユーザーアイコンの取得
[**get_user_stars**](DefaultApi.md#get_user_stars) | **GET** /api/v2/users/{userId}/stars | ユーザーの受け取ったスター一覧の取得
[**get_user_stars_count**](DefaultApi.md#get_user_stars_count) | **GET** /api/v2/users/{userId}/stars/count | ユーザーの受け取ったスターの数の取得
[**get_user_watchings**](DefaultApi.md#get_user_watchings) | **GET** /api/v2/users/{userId}/watchings | ウォッチ一覧の取得
[**get_users**](DefaultApi.md#get_users) | **GET** /api/v2/users | ユーザー一覧の取得
[**get_watching**](DefaultApi.md#get_watching) | **GET** /api/v2/watchings/{watchingId} | ウォッチ情報の取得
[**get_watching_count**](DefaultApi.md#get_watching_count) | **GET** /api/v2/users/{userId}/watchings/count | ウォッチ数の取得
[**get_webhook**](DefaultApi.md#get_webhook) | **GET** /api/v2/projects/{projectIdOrKey}/webhooks/{webhookId} | Webhookの取得
[**get_webhooks**](DefaultApi.md#get_webhooks) | **GET** /api/v2/projects/{projectIdOrKey}/webhooks | Webhook一覧の取得
[**get_wiki**](DefaultApi.md#get_wiki) | **GET** /api/v2/wikis/{wikiId} | Wikiページ情報の取得
[**get_wiki_attachments**](DefaultApi.md#get_wiki_attachments) | **GET** /api/v2/wikis/{wikiId}/attachments | Wiki添付ファイル一覧の取得
[**get_wiki_count**](DefaultApi.md#get_wiki_count) | **GET** /api/v2/wikis/count | Wikiページ数の取得
[**get_wiki_history**](DefaultApi.md#get_wiki_history) | **GET** /api/v2/wikis/{wikiId}/history | Wikiページ更新履歴一覧の取得
[**get_wiki_shared_files**](DefaultApi.md#get_wiki_shared_files) | **GET** /api/v2/wikis/{wikiId}/sharedFiles | Wiki共有ファイル一覧の取得
[**get_wiki_stars**](DefaultApi.md#get_wiki_stars) | **GET** /api/v2/wikis/{wikiId}/stars | Wikiページのスター一覧の取得
[**get_wiki_tags**](DefaultApi.md#get_wiki_tags) | **GET** /api/v2/wikis/tags | Wikiページタグ一覧の取得
[**get_wikis**](DefaultApi.md#get_wikis) | **GET** /api/v2/wikis | Wikiページ一覧の取得
[**link_shared_file_to_issue**](DefaultApi.md#link_shared_file_to_issue) | **POST** /api/v2/issues/{issueIdOrKey}/sharedFiles | 課題に共有ファイルをリンク
[**link_shared_files_to_wiki**](DefaultApi.md#link_shared_files_to_wiki) | **POST** /api/v2/wikis/{wikiId}/sharedFiles | Wikiに共有ファイルをリンク
[**mark_notification_as_read**](DefaultApi.md#mark_notification_as_read) | **POST** /api/v2/notifications/{id}/markAsRead | お知らせの既読化
[**mark_watching_as_read**](DefaultApi.md#mark_watching_as_read) | **POST** /api/v2/watchings/{watchingId}/markAsRead | ウォッチの既読化
[**post_attachment**](DefaultApi.md#post_attachment) | **POST** /api/v2/space/attachment | 添付ファイルの送信
[**reset_notification_count**](DefaultApi.md#reset_notification_count) | **POST** /api/v2/notifications/markAsRead | お知らせ数のリセット
[**unlink_issue_shared_file**](DefaultApi.md#unlink_issue_shared_file) | **DELETE** /api/v2/issues/{issueIdOrKey}/sharedFiles/{id} | 課題の共有ファイルのリンクを解除
[**unlink_wiki_shared_file**](DefaultApi.md#unlink_wiki_shared_file) | **DELETE** /api/v2/wikis/{wikiId}/sharedFiles/{id} | Wikiの共有ファイルのリンクを解除
[**update_category**](DefaultApi.md#update_category) | **PATCH** /api/v2/projects/{projectIdOrKey}/categories/{id} | カテゴリー情報の更新
[**update_custom_field**](DefaultApi.md#update_custom_field) | **PATCH** /api/v2/projects/{projectIdOrKey}/customFields/{id} | カスタム属性の更新
[**update_custom_field_list_item**](DefaultApi.md#update_custom_field_list_item) | **PATCH** /api/v2/projects/{projectIdOrKey}/customFields/{id}/items/{itemId} | 選択リストカスタム属性のリスト項目の更新
[**update_group**](DefaultApi.md#update_group) | **PATCH** /api/v2/groups/{groupId} | グループ情報の更新
[**update_issue**](DefaultApi.md#update_issue) | **PATCH** /api/v2/issues/{issueIdOrKey} | 課題情報の更新
[**update_issue_comment**](DefaultApi.md#update_issue_comment) | **PATCH** /api/v2/issues/{issueIdOrKey}/comments/{commentId} | 課題コメント情報の更新
[**update_issue_type**](DefaultApi.md#update_issue_type) | **PATCH** /api/v2/projects/{projectIdOrKey}/issueTypes/{id} | 種別情報の更新
[**update_project**](DefaultApi.md#update_project) | **PATCH** /api/v2/projects/{projectIdOrKey} | プロジェクト情報の更新
[**update_project_status**](DefaultApi.md#update_project_status) | **PATCH** /api/v2/projects/{projectIdOrKey}/statuses/{id} | 状態情報の更新
[**update_pull_request**](DefaultApi.md#update_pull_request) | **PATCH** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number} | プルリクエストの更新
[**update_pull_request_comment**](DefaultApi.md#update_pull_request_comment) | **PATCH** /api/v2/projects/{projectIdOrKey}/git/repositories/{repoIdOrName}/pullRequests/{number}/comments/{commentId} | プルリクエストコメント情報の更新
[**update_space_notification**](DefaultApi.md#update_space_notification) | **PUT** /api/v2/space/notification | スペースのお知らせの更新
[**update_status_display_order**](DefaultApi.md#update_status_display_order) | **PATCH** /api/v2/projects/{projectIdOrKey}/statuses/updateDisplayOrder | 状態の並び替え
[**update_team**](DefaultApi.md#update_team) | **PATCH** /api/v2/teams/{teamId} | チーム情報の更新
[**update_user**](DefaultApi.md#update_user) | **PATCH** /api/v2/users/{userId} | ユーザーの更新
[**update_version**](DefaultApi.md#update_version) | **PATCH** /api/v2/projects/{projectIdOrKey}/versions/{id} | バージョン(マイルストーン)情報の更新
[**update_watching**](DefaultApi.md#update_watching) | **PATCH** /api/v2/watchings/{watchingId} | ウォッチの更新
[**update_webhook**](DefaultApi.md#update_webhook) | **PATCH** /api/v2/projects/{projectIdOrKey}/webhooks/{webhookId} | Webhookの更新
[**update_wiki**](DefaultApi.md#update_wiki) | **PATCH** /api/v2/wikis/{wikiId} | Wikiページ情報の更新


# **add_custom_field**
> AddCustomField200Response add_custom_field(project_id_or_key, type_id, name, applicable_issue_types=applicable_issue_types, description=description, required=required, min=min, max=max, initial_value=initial_value, unit=unit, initial_value_type=initial_value_type, initial_date=initial_date, initial_shift=initial_shift, items=items, allow_input=allow_input, allow_add_item=allow_add_item)

カスタム属性の追加

プロジェクトに新しいカスタム属性を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_custom_field200_response import AddCustomField200Response
from backlog_client.models.add_custom_field_request_max import AddCustomFieldRequestMax
from backlog_client.models.add_custom_field_request_min import AddCustomFieldRequestMin
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    type_id = 56 # int | カスタム属性の形式1\\\\: 文字列2\\\\: 文章3\\\\: 数値4\\\\: 日付5\\\\: 単一リスト6\\\\: 複数リスト7\\\\: チェックボックス8\\\\: ラジオ
    name = 'name_example' # str | カスタム属性の名前
    applicable_issue_types = [56] # List[int] | カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 (optional)
    description = 'description_example' # str | カスタム属性の説明 (optional)
    required = True # bool | 必須な属性とする場合はtrue (optional)
    min = backlog_client.AddCustomFieldRequestMin() # AddCustomFieldRequestMin |  (optional)
    max = backlog_client.AddCustomFieldRequestMax() # AddCustomFieldRequestMax |  (optional)
    initial_value = 56 # int | 初期値（数値属性の場合） (optional)
    unit = 'unit_example' # str | 単位（数値属性の場合） (optional)
    initial_value_type = 56 # int | 1\\\\:当日 2\\\\: 当日 + initialShift 3\\\\:指定日（日付属性の場合） (optional)
    initial_date = 'initial_date_example' # str | 初期値 (yyyy-MM-dd)（日付属性の場合） (optional)
    initial_shift = 56 # int | 差分日数（日付属性の場合） (optional)
    items = ['items_example'] # List[str] | リスト項目（リスト属性の場合） (optional)
    allow_input = True # bool | その他直接入力を許可（リスト属性の場合） (optional)
    allow_add_item = True # bool | 項目の追加を許可（リスト属性の場合） (optional)

    try:
        # カスタム属性の追加
        api_response = api_instance.add_custom_field(project_id_or_key, type_id, name, applicable_issue_types=applicable_issue_types, description=description, required=required, min=min, max=max, initial_value=initial_value, unit=unit, initial_value_type=initial_value_type, initial_date=initial_date, initial_shift=initial_shift, items=items, allow_input=allow_input, allow_add_item=allow_add_item)
        print("The response of DefaultApi->add_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **type_id** | **int**| カスタム属性の形式1\\\\: 文字列2\\\\: 文章3\\\\: 数値4\\\\: 日付5\\\\: 単一リスト6\\\\: 複数リスト7\\\\: チェックボックス8\\\\: ラジオ | 
 **name** | **str**| カスタム属性の名前 | 
 **applicable_issue_types** | [**List[int]**](int.md)| カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 | [optional] 
 **description** | **str**| カスタム属性の説明 | [optional] 
 **required** | **bool**| 必須な属性とする場合はtrue | [optional] 
 **min** | [**AddCustomFieldRequestMin**](AddCustomFieldRequestMin.md)|  | [optional] 
 **max** | [**AddCustomFieldRequestMax**](AddCustomFieldRequestMax.md)|  | [optional] 
 **initial_value** | **int**| 初期値（数値属性の場合） | [optional] 
 **unit** | **str**| 単位（数値属性の場合） | [optional] 
 **initial_value_type** | **int**| 1\\\\:当日 2\\\\: 当日 + initialShift 3\\\\:指定日（日付属性の場合） | [optional] 
 **initial_date** | **str**| 初期値 (yyyy-MM-dd)（日付属性の場合） | [optional] 
 **initial_shift** | **int**| 差分日数（日付属性の場合） | [optional] 
 **items** | [**List[str]**](str.md)| リスト項目（リスト属性の場合） | [optional] 
 **allow_input** | **bool**| その他直接入力を許可（リスト属性の場合） | [optional] 
 **allow_add_item** | **bool**| 項目の追加を許可（リスト属性の場合） | [optional] 

### Return type

[**AddCustomField200Response**](AddCustomField200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_custom_field_list_item**
> AddCustomFieldListItem200Response add_custom_field_list_item(project_id_or_key, id, name)

選択リストカスタム属性のリスト項目の追加

選択リスト形式のカスタム属性のリスト項目を追加します。 「課題の追加/編集時に選択肢を追加できる」の設定が無効な場合は管理者権限のユーザーのみ呼び出せます。 指定されたカスタム属性が選択リスト形式でない場合はエラーになります。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_custom_field_list_item200_response import AddCustomFieldListItem200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カスタム属性のID
    name = 'name_example' # str | リスト項目の名前

    try:
        # 選択リストカスタム属性のリスト項目の追加
        api_response = api_instance.add_custom_field_list_item(project_id_or_key, id, name)
        print("The response of DefaultApi->add_custom_field_list_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_custom_field_list_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カスタム属性のID | 
 **name** | **str**| リスト項目の名前 | 

### Return type

[**AddCustomFieldListItem200Response**](AddCustomFieldListItem200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group**
> GetGroups200ResponseInner add_group(name, members=members)

グループの追加

2025年8月28日以降、順次利用できなくなります。 チームの追加をご利用ください。 グループを追加します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    name = 'name_example' # str | グループ名
    members = [56] # List[int] | グループに含めるユーザーID (optional)

    try:
        # グループの追加
        api_response = api_instance.add_group(name, members=members)
        print("The response of DefaultApi->add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| グループ名 | 
 **members** | [**List[int]**](int.md)| グループに含めるユーザーID | [optional] 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_issue_comment**
> AddIssueComment201Response add_issue_comment(issue_id_or_key, content, notified_user_id=notified_user_id, attachment_id=attachment_id)

課題コメントの追加

課題に新しいコメントを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_issue_comment201_response import AddIssueComment201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    content = 'content_example' # str | コメントの本文
    notified_user_id = [56] # List[int] | コメント登録の通知を受け取るユーザーID (optional)
    attachment_id = [56] # List[int] | 添付ファイルの送信APIが返すID (optional)

    try:
        # 課題コメントの追加
        api_response = api_instance.add_issue_comment(issue_id_or_key, content, notified_user_id=notified_user_id, attachment_id=attachment_id)
        print("The response of DefaultApi->add_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **content** | **str**| コメントの本文 | 
 **notified_user_id** | [**List[int]**](int.md)| コメント登録の通知を受け取るユーザーID | [optional] 
 **attachment_id** | [**List[int]**](int.md)| 添付ファイルの送信APIが返すID | [optional] 

### Return type

[**AddIssueComment201Response**](AddIssueComment201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功時のレスポンス |  * Location - https://xx.backlog.jp/user/eguchi <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_issue_comment_notification**
> AddIssueCommentNotification200Response add_issue_comment_notification(issue_id_or_key, comment_id, notified_user_id=notified_user_id)

課題コメントにお知らせを追加

コメントにお知らせを追加します 認証ユーザー自身が登録したコメントのみお知らせを追加することが出来ます。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_issue_comment_notification200_response import AddIssueCommentNotification200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    comment_id = 56 # int | コメントのID
    notified_user_id = [56] # List[int] | 課題の登録の通知を受け取るユーザーのID (optional)

    try:
        # 課題コメントにお知らせを追加
        api_response = api_instance.add_issue_comment_notification(issue_id_or_key, comment_id, notified_user_id=notified_user_id)
        print("The response of DefaultApi->add_issue_comment_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_issue_comment_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **comment_id** | **int**| コメントのID | 
 **notified_user_id** | [**List[int]**](int.md)| 課題の登録の通知を受け取るユーザーのID | [optional] 

### Return type

[**AddIssueCommentNotification200Response**](AddIssueCommentNotification200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_issue_type**
> GetIssueTypes200ResponseInner add_issue_type(project_id_or_key, name, color, template_summary=template_summary, template_description=template_description)

種別の追加

プロジェクトに種別を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_types200_response_inner import GetIssueTypes200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    name = 'name_example' # str | 種別の名前
    color = 'color_example' # str | 種別の背景色
    template_summary = 'template_summary_example' # str | 課題テンプレートの件名 (optional)
    template_description = 'template_description_example' # str | 課題テンプレートの詳細 (optional)

    try:
        # 種別の追加
        api_response = api_instance.add_issue_type(project_id_or_key, name, color, template_summary=template_summary, template_description=template_description)
        print("The response of DefaultApi->add_issue_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_issue_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **name** | **str**| 種別の名前 | 
 **color** | **str**| 種別の背景色 | 
 **template_summary** | **str**| 課題テンプレートの件名 | [optional] 
 **template_description** | **str**| 課題テンプレートの詳細 | [optional] 

### Return type

[**GetIssueTypes200ResponseInner**](GetIssueTypes200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project**
> AddProject201Response add_project(name, key, chart_enabled=chart_enabled, use_resolved_for_chart=use_resolved_for_chart, subtasking_enabled=subtasking_enabled, project_leader_can_edit_project_leader=project_leader_can_edit_project_leader, use_wiki=use_wiki, use_file_sharing=use_file_sharing, use_wiki_tree_view=use_wiki_tree_view, use_subversion=use_subversion, use_git=use_git, use_original_image_size_at_wiki=use_original_image_size_at_wiki, text_formatting_rule=text_formatting_rule, use_dev_attributes=use_dev_attributes)

プロジェクトの追加

新しいプロジェクトを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_project201_response import AddProject201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    name = 'name_example' # str | プロジェクト名
    key = 'key_example' # str | プロジェクトキー(半角英大文字と半角数字とアンダースコアが使用できます)
    chart_enabled = True # bool | チャートを使用するかどうか (optional)
    use_resolved_for_chart = True # bool | 「処理済み」以降を「完了」とみなすどうか (optional)
    subtasking_enabled = True # bool | 親子課題を使用するかどうか (optional)
    project_leader_can_edit_project_leader = True # bool | プロジェクト管理者も他のプロジェクト管理者を指定可能にする (optional)
    use_wiki = True # bool | Wikiを使用するかどうか (optional)
    use_file_sharing = True # bool | 共有ファイルを使用するかどうか (optional)
    use_wiki_tree_view = True # bool | Wikiツリー表示を有効にするかどうか (optional)
    use_subversion = True # bool | Subversionを使用するかどうか (optional)
    use_git = True # bool | Gitを使用するかどうか (optional)
    use_original_image_size_at_wiki = True # bool | Wikiの画像をオリジナルのサイズで表示するかどうか (optional)
    text_formatting_rule = 'text_formatting_rule_example' # str | テキスト整形のルール backlog または markdown (optional)
    use_dev_attributes = True # bool | 優先度、マイルストーン、発生バージョンを使用するかどうか (optional)

    try:
        # プロジェクトの追加
        api_response = api_instance.add_project(name, key, chart_enabled=chart_enabled, use_resolved_for_chart=use_resolved_for_chart, subtasking_enabled=subtasking_enabled, project_leader_can_edit_project_leader=project_leader_can_edit_project_leader, use_wiki=use_wiki, use_file_sharing=use_file_sharing, use_wiki_tree_view=use_wiki_tree_view, use_subversion=use_subversion, use_git=use_git, use_original_image_size_at_wiki=use_original_image_size_at_wiki, text_formatting_rule=text_formatting_rule, use_dev_attributes=use_dev_attributes)
        print("The response of DefaultApi->add_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| プロジェクト名 | 
 **key** | **str**| プロジェクトキー(半角英大文字と半角数字とアンダースコアが使用できます) | 
 **chart_enabled** | **bool**| チャートを使用するかどうか | [optional] 
 **use_resolved_for_chart** | **bool**| 「処理済み」以降を「完了」とみなすどうか | [optional] 
 **subtasking_enabled** | **bool**| 親子課題を使用するかどうか | [optional] 
 **project_leader_can_edit_project_leader** | **bool**| プロジェクト管理者も他のプロジェクト管理者を指定可能にする | [optional] 
 **use_wiki** | **bool**| Wikiを使用するかどうか | [optional] 
 **use_file_sharing** | **bool**| 共有ファイルを使用するかどうか | [optional] 
 **use_wiki_tree_view** | **bool**| Wikiツリー表示を有効にするかどうか | [optional] 
 **use_subversion** | **bool**| Subversionを使用するかどうか | [optional] 
 **use_git** | **bool**| Gitを使用するかどうか | [optional] 
 **use_original_image_size_at_wiki** | **bool**| Wikiの画像をオリジナルのサイズで表示するかどうか | [optional] 
 **text_formatting_rule** | **str**| テキスト整形のルール backlog または markdown | [optional] 
 **use_dev_attributes** | **bool**| 優先度、マイルストーン、発生バージョンを使用するかどうか | [optional] 

### Return type

[**AddProject201Response**](AddProject201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功時のレスポンス |  * Location - https://xx.backlog.jp/user/eguchi <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_administrator**
> GetIssueCommentNotifications200ResponseInnerUser add_project_administrator(project_id_or_key, user_id)

プロジェクト管理者の追加

プロジェクトユーザーにプロジェクト管理者権限を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    user_id = 56 # int | 追加するユーザーのID

    try:
        # プロジェクト管理者の追加
        api_response = api_instance.add_project_administrator(project_id_or_key, user_id)
        print("The response of DefaultApi->add_project_administrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_administrator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **user_id** | **int**| 追加するユーザーのID | 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_category**
> AddProjectCategory200Response add_project_category(project_id_or_key, name)

カテゴリーの追加

プロジェクトにカテゴリーを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_project_category200_response import AddProjectCategory200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    name = 'name_example' # str | カテゴリーの名前

    try:
        # カテゴリーの追加
        api_response = api_instance.add_project_category(project_id_or_key, name)
        print("The response of DefaultApi->add_project_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **name** | **str**| カテゴリーの名前 | 

### Return type

[**AddProjectCategory200Response**](AddProjectCategory200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_group**
> GetGroups200ResponseInner add_project_group(project_id_or_key, group_id)

プロジェクトグループの追加

2025年8月28日以降、順次利用できなくなります。（新しいタブで開く） プロジェクトチームの追加をご利用ください。 プロジェクトにグループを追加します。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    group_id = 56 # int | 追加するグループのID

    try:
        # プロジェクトグループの追加
        api_response = api_instance.add_project_group(project_id_or_key, group_id)
        print("The response of DefaultApi->add_project_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **group_id** | **int**| 追加するグループのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_status**
> GetIssues200ResponseInnerIssueType add_project_status(project_id_or_key, name, color)

状態の追加

プロジェクトに状態を追加します。 1プロジェクトにつき8個まで状態を追加できます。 標準の4つの状態と合わせると、合計12個の状態を設定できます。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_issue_type import GetIssues200ResponseInnerIssueType
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    name = 'name_example' # str | 状態の名前
    color = 'color_example' # str | 状態の背景色

    try:
        # 状態の追加
        api_response = api_instance.add_project_status(project_id_or_key, name, color)
        print("The response of DefaultApi->add_project_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **name** | **str**| 状態の名前 | 
 **color** | **str**| 状態の背景色 | 

### Return type

[**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_team**
> GetGroups200ResponseInner add_project_team(project_id_or_key, team_id)

プロジェクトチームの追加

プロジェクトにチームを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    team_id = 56 # int | 追加するチームのID

    try:
        # プロジェクトチームの追加
        api_response = api_instance.add_project_team(project_id_or_key, team_id)
        print("The response of DefaultApi->add_project_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **team_id** | **int**| 追加するチームのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_user**
> GetIssueCommentNotifications200ResponseInnerUser add_project_user(project_id_or_key, user_id)

プロジェクトユーザーの追加

プロジェクトにユーザーを追加します。  実行可能な権限: * 管理者 * プロジェクト管理者 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    user_id = 56 # int | 追加するユーザーのID

    try:
        # プロジェクトユーザーの追加
        api_response = api_instance.add_project_user(project_id_or_key, user_id)
        print("The response of DefaultApi->add_project_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_project_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **user_id** | **int**| 追加するユーザーのID | 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pull_request_comment**
> GetPullRequestComments200ResponseInner add_pull_request_comment(project_id_or_key, repo_id_or_name, number, content, attachment_id=attachment_id, notified_user_id=notified_user_id)

プルリクエストコメントの追加

プルリクエストにコメントを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_pull_request_comments200_response_inner import GetPullRequestComments200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号
    content = 'content_example' # str | コメントの本文
    attachment_id = [56] # List[int] | 添付ファイルの送信APIが返すID (optional)
    notified_user_id = [56] # List[int] | コメント登録の通知を受け取るユーザーID (optional)

    try:
        # プルリクエストコメントの追加
        api_response = api_instance.add_pull_request_comment(project_id_or_key, repo_id_or_name, number, content, attachment_id=attachment_id, notified_user_id=notified_user_id)
        print("The response of DefaultApi->add_pull_request_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_pull_request_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 
 **content** | **str**| コメントの本文 | 
 **attachment_id** | [**List[int]**](int.md)| 添付ファイルの送信APIが返すID | [optional] 
 **notified_user_id** | [**List[int]**](int.md)| コメント登録の通知を受け取るユーザーID | [optional] 

### Return type

[**GetPullRequestComments200ResponseInner**](GetPullRequestComments200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_recently_viewed_issue**
> AddRecentlyViewedIssue200Response add_recently_viewed_issue(issue_id_or_key)

自分が最近見た課題の追加

APIとの認証に使用しているユーザーが最近見た課題を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_issue200_response import AddRecentlyViewedIssue200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 自分が最近見た課題の追加
        api_response = api_instance.add_recently_viewed_issue(issue_id_or_key)
        print("The response of DefaultApi->add_recently_viewed_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_recently_viewed_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**AddRecentlyViewedIssue200Response**](AddRecentlyViewedIssue200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_recently_viewed_wiki**
> AddRecentlyViewedWiki200Response add_recently_viewed_wiki(wiki_id)

自分が最近見たWikiの追加

APIとの認証に使用しているユーザーが最近見たWikiを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response import AddRecentlyViewedWiki200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのId

    try:
        # 自分が最近見たWikiの追加
        api_response = api_instance.add_recently_viewed_wiki(wiki_id)
        print("The response of DefaultApi->add_recently_viewed_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_recently_viewed_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのId | 

### Return type

[**AddRecentlyViewedWiki200Response**](AddRecentlyViewedWiki200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_star**
> add_star(issue_id=issue_id, comment_id=comment_id, wiki_id=wiki_id, pull_request_id=pull_request_id, pull_request_comment_id=pull_request_comment_id)

スターの追加

課題、コメント、Wikiページにスターを一つ追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id = 56 # int | 課題のID (optional)
    comment_id = 56 # int | コメントのID (optional)
    wiki_id = 56 # int | WikiページのID (optional)
    pull_request_id = 56 # int | プルリクエストのID (optional)
    pull_request_comment_id = 56 # int | プルリクエストコメントのID (optional)

    try:
        # スターの追加
        api_instance.add_star(issue_id=issue_id, comment_id=comment_id, wiki_id=wiki_id, pull_request_id=pull_request_id, pull_request_comment_id=pull_request_comment_id)
    except Exception as e:
        print("Exception when calling DefaultApi->add_star: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **int**| 課題のID | [optional] 
 **comment_id** | **int**| コメントのID | [optional] 
 **wiki_id** | **int**| WikiページのID | [optional] 
 **pull_request_id** | **int**| プルリクエストのID | [optional] 
 **pull_request_comment_id** | **int**| プルリクエストコメントのID | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO_CONTENT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_team**
> GetGroups200ResponseInner add_team(name, members=members)

チームの追加

チームを追加します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    name = 'name_example' # str | グループ名
    members = [56] # List[int] | グループに含めるユーザーID (optional)

    try:
        # チームの追加
        api_response = api_instance.add_team(name, members=members)
        print("The response of DefaultApi->add_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| グループ名 | 
 **members** | [**List[int]**](int.md)| グループに含めるユーザーID | [optional] 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> GetIssueCommentNotifications200ResponseInnerUser add_user(user_id, password, name, mail_address, role_type)

ユーザーの追加

スペースに新しいユーザーを追加します。 プロジェクト管理者は管理者権限のユーザを追加することは出来ません。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 'user_id_example' # str | ユーザID
    password = 'password_example' # str | パスワード
    name = 'name_example' # str | ハンドルネーム
    mail_address = 'mail_address_example' # str | メールアドレス
    role_type = 56 # int | 管理者(1) 一般ユーザー(2) レポーター(3) ビューワー(4) ゲストレポーター(5) ゲストビューワー(6)

    try:
        # ユーザーの追加
        api_response = api_instance.add_user(user_id, password, name, mail_address, role_type)
        print("The response of DefaultApi->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ユーザID | 
 **password** | **str**| パスワード | 
 **name** | **str**| ハンドルネーム | 
 **mail_address** | **str**| メールアドレス | 
 **role_type** | **int**| 管理者(1) 一般ユーザー(2) レポーター(3) ビューワー(4) ゲストレポーター(5) ゲストビューワー(6) | 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功時のレスポンス |  * Location - https://xx.backlog.jp/user/eguchi <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_version**
> GetIssues200ResponseInnerMilestoneInner add_version(project_id_or_key, name, description=description, start_date=start_date, release_due_date=release_due_date)

バージョン(マイルストーン)の追加

プロジェクトにバージョン(マイルストーン)を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_milestone_inner import GetIssues200ResponseInnerMilestoneInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    name = 'name_example' # str | バージョンの名前
    description = 'description_example' # str | バージョンの説明 (optional)
    start_date = '2013-10-20' # date | バージョンの開始日 (yyyy-MM-dd) (optional)
    release_due_date = '2013-10-20' # date | バージョンのリリース予定日 (yyyy-MM-dd) (optional)

    try:
        # バージョン(マイルストーン)の追加
        api_response = api_instance.add_version(project_id_or_key, name, description=description, start_date=start_date, release_due_date=release_due_date)
        print("The response of DefaultApi->add_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **name** | **str**| バージョンの名前 | 
 **description** | **str**| バージョンの説明 | [optional] 
 **start_date** | **date**| バージョンの開始日 (yyyy-MM-dd) | [optional] 
 **release_due_date** | **date**| バージョンのリリース予定日 (yyyy-MM-dd) | [optional] 

### Return type

[**GetIssues200ResponseInnerMilestoneInner**](GetIssues200ResponseInnerMilestoneInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_watching**
> AddWatching201Response add_watching(issue_id_or_key, note=note)

ウォッチの追加

ウォッチを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_watching201_response import AddWatching201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    note = 'note_example' # str | メモ (optional)

    try:
        # ウォッチの追加
        api_response = api_instance.add_watching(issue_id_or_key, note=note)
        print("The response of DefaultApi->add_watching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_watching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **note** | **str**| メモ | [optional] 

### Return type

[**AddWatching201Response**](AddWatching201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_webhook**
> GetWebhooks200ResponseInner add_webhook(project_id_or_key, name=name, description=description, hook_url=hook_url, all_event=all_event, activity_type_ids=activity_type_ids)

Webhookの追加

Webhookを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_webhooks200_response_inner import GetWebhooks200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    name = 'name_example' # str | 名前 (optional)
    description = 'description_example' # str | 詳細 (optional)
    hook_url = 'hook_url_example' # str | hook URL (optional)
    all_event = True # bool | 全てのイベントを通知 (optional)
    activity_type_ids = [56] # List[int] | 通知するイベントのID (optional)

    try:
        # Webhookの追加
        api_response = api_instance.add_webhook(project_id_or_key, name=name, description=description, hook_url=hook_url, all_event=all_event, activity_type_ids=activity_type_ids)
        print("The response of DefaultApi->add_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **name** | **str**| 名前 | [optional] 
 **description** | **str**| 詳細 | [optional] 
 **hook_url** | **str**| hook URL | [optional] 
 **all_event** | **bool**| 全てのイベントを通知 | [optional] 
 **activity_type_ids** | [**List[int]**](int.md)| 通知するイベントのID | [optional] 

### Return type

[**GetWebhooks200ResponseInner**](GetWebhooks200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_wiki_attachment**
> List[AddWikiAttachment200ResponseInner] add_wiki_attachment(wiki_id, attachment_id=attachment_id)

Wiki添付ファイルの追加

Wikiに添付ファイルを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_wiki_attachment200_response_inner import AddWikiAttachment200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    attachment_id = [56] # List[int] | 添付ファイルの送信APIが返すID (optional)

    try:
        # Wiki添付ファイルの追加
        api_response = api_instance.add_wiki_attachment(wiki_id, attachment_id=attachment_id)
        print("The response of DefaultApi->add_wiki_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_wiki_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **attachment_id** | [**List[int]**](int.md)| 添付ファイルの送信APIが返すID | [optional] 

### Return type

[**List[AddWikiAttachment200ResponseInner]**](AddWikiAttachment200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_issue**
> CreateIssue201Response create_issue(project_id, summary, issue_type_id, priority_id, parent_issue_id=parent_issue_id, description=description, start_date=start_date, due_date=due_date, estimated_hours=estimated_hours, actual_hours=actual_hours, category_id=category_id, version_id=version_id, milestone_id=milestone_id, assignee_id=assignee_id, notified_user_id=notified_user_id, attachment_id=attachment_id, custom_field_id=custom_field_id, custom_field_id_other_value=custom_field_id_other_value)

課題の追加

新しい課題を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.create_issue201_response import CreateIssue201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id = 56 # int | 課題を登録するプロジェクトのID
    summary = 'summary_example' # str | 課題の件名
    issue_type_id = 56 # int | 課題の種別のID
    priority_id = 56 # int | 課題の優先度のID
    parent_issue_id = 56 # int | 課題の親課題のID (optional)
    description = 'description_example' # str | 課題の詳細 (optional)
    start_date = 'start_date_example' # str | 課題の開始日 (yyyy-MM-dd) (optional)
    due_date = 'due_date_example' # str | 課題の期限日 (yyyy-MM-dd) (optional)
    estimated_hours = 3.4 # float | 課題の予定時間 (optional)
    actual_hours = 3.4 # float | 課題の実績時間 (optional)
    category_id = [56] # List[int] | 課題のカテゴリーのID (optional)
    version_id = [56] # List[int] | 課題の発生バージョンのID (optional)
    milestone_id = [56] # List[int] | 課題のマイルストーンのID (optional)
    assignee_id = 56 # int | 課題の担当者のID (optional)
    notified_user_id = [56] # List[int] | 課題の登録の通知を受け取るユーザーのID (optional)
    attachment_id = [56] # List[int] | 添付ファイルの送信APIが返すID (optional)
    custom_field_id = 'custom_field_id_example' # str | カスタム属性の値 (optional)
    custom_field_id_other_value = 'custom_field_id_other_value_example' # str | リスト属性のその他入力の値 (optional)

    try:
        # 課題の追加
        api_response = api_instance.create_issue(project_id, summary, issue_type_id, priority_id, parent_issue_id=parent_issue_id, description=description, start_date=start_date, due_date=due_date, estimated_hours=estimated_hours, actual_hours=actual_hours, category_id=category_id, version_id=version_id, milestone_id=milestone_id, assignee_id=assignee_id, notified_user_id=notified_user_id, attachment_id=attachment_id, custom_field_id=custom_field_id, custom_field_id_other_value=custom_field_id_other_value)
        print("The response of DefaultApi->create_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| 課題を登録するプロジェクトのID | 
 **summary** | **str**| 課題の件名 | 
 **issue_type_id** | **int**| 課題の種別のID | 
 **priority_id** | **int**| 課題の優先度のID | 
 **parent_issue_id** | **int**| 課題の親課題のID | [optional] 
 **description** | **str**| 課題の詳細 | [optional] 
 **start_date** | **str**| 課題の開始日 (yyyy-MM-dd) | [optional] 
 **due_date** | **str**| 課題の期限日 (yyyy-MM-dd) | [optional] 
 **estimated_hours** | **float**| 課題の予定時間 | [optional] 
 **actual_hours** | **float**| 課題の実績時間 | [optional] 
 **category_id** | [**List[int]**](int.md)| 課題のカテゴリーのID | [optional] 
 **version_id** | [**List[int]**](int.md)| 課題の発生バージョンのID | [optional] 
 **milestone_id** | [**List[int]**](int.md)| 課題のマイルストーンのID | [optional] 
 **assignee_id** | **int**| 課題の担当者のID | [optional] 
 **notified_user_id** | [**List[int]**](int.md)| 課題の登録の通知を受け取るユーザーのID | [optional] 
 **attachment_id** | [**List[int]**](int.md)| 添付ファイルの送信APIが返すID | [optional] 
 **custom_field_id** | **str**| カスタム属性の値 | [optional] 
 **custom_field_id_other_value** | **str**| リスト属性のその他入力の値 | [optional] 

### Return type

[**CreateIssue201Response**](CreateIssue201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功時のレスポンス |  * Location - https://xx.backlog.jp/user/eguchi <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pull_request**
> CreatePullRequest200Response create_pull_request(project_id_or_key, repo_id_or_name, summary, description, base, branch, issue_id=issue_id, assignee_id=assignee_id, notified_user_id=notified_user_id, attachment_id=attachment_id)

プルリクエストの追加

プルリクエストを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.create_pull_request200_response import CreatePullRequest200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    summary = 'summary_example' # str | プルリクエストの件名
    description = 'description_example' # str | プルリクエストの詳細
    base = 'base_example' # str | マージ先のブランチ名
    branch = 'branch_example' # str | マージされるブランチ名
    issue_id = 56 # int | 関連課題のID (optional)
    assignee_id = 56 # int | プルリクエストの担当者のID (optional)
    notified_user_id = [56] # List[int] | プルリクエストの登録の通知を受け取るユーザーのID (optional)
    attachment_id = [56] # List[int] | 添付ファイルの送信APIが返すID (optional)

    try:
        # プルリクエストの追加
        api_response = api_instance.create_pull_request(project_id_or_key, repo_id_or_name, summary, description, base, branch, issue_id=issue_id, assignee_id=assignee_id, notified_user_id=notified_user_id, attachment_id=attachment_id)
        print("The response of DefaultApi->create_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **summary** | **str**| プルリクエストの件名 | 
 **description** | **str**| プルリクエストの詳細 | 
 **base** | **str**| マージ先のブランチ名 | 
 **branch** | **str**| マージされるブランチ名 | 
 **issue_id** | **int**| 関連課題のID | [optional] 
 **assignee_id** | **int**| プルリクエストの担当者のID | [optional] 
 **notified_user_id** | [**List[int]**](int.md)| プルリクエストの登録の通知を受け取るユーザーのID | [optional] 
 **attachment_id** | [**List[int]**](int.md)| 添付ファイルの送信APIが返すID | [optional] 

### Return type

[**CreatePullRequest200Response**](CreatePullRequest200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wiki**
> CreateWiki201Response create_wiki(project_id, name, content, mail_notify=mail_notify)

Wikiページの追加

WIkiの新しいページを追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.create_wiki201_response import CreateWiki201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id = 56 # int | プロジェクトのID
    name = 'name_example' # str | ページ名
    content = 'content_example' # str | ページの内容
    mail_notify = True # bool | ページの追加をメールで通知する場合はtrue (optional)

    try:
        # Wikiページの追加
        api_response = api_instance.create_wiki(project_id, name, content, mail_notify=mail_notify)
        print("The response of DefaultApi->create_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| プロジェクトのID | 
 **name** | **str**| ページ名 | 
 **content** | **str**| ページの内容 | 
 **mail_notify** | **bool**| ページの追加をメールで通知する場合はtrue | [optional] 

### Return type

[**CreateWiki201Response**](CreateWiki201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 成功時のレスポンス |  * Location - https://xx.backlog.jp/user/eguchi <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> DeleteCategory200Response delete_category(project_id_or_key, id)

カテゴリーの削除

カテゴリーを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.delete_category200_response import DeleteCategory200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カテゴリーのID

    try:
        # カテゴリーの削除
        api_response = api_instance.delete_category(project_id_or_key, id)
        print("The response of DefaultApi->delete_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カテゴリーのID | 

### Return type

[**DeleteCategory200Response**](DeleteCategory200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> AddCustomField200Response delete_custom_field(project_id_or_key, id)

カスタム属性の削除

カスタム属性を削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_custom_field200_response import AddCustomField200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カスタム属性のID

    try:
        # カスタム属性の削除
        api_response = api_instance.delete_custom_field(project_id_or_key, id)
        print("The response of DefaultApi->delete_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カスタム属性のID | 

### Return type

[**AddCustomField200Response**](AddCustomField200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field_list_item**
> AddCustomFieldListItem200Response delete_custom_field_list_item(project_id_or_key, id, item_id)

選択リストカスタム属性のリスト項目の削除

選択リスト形式のカスタム属性のリスト項目を削除します。 指定されたカスタム属性が選択リスト形式でない場合はエラーになります。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_custom_field_list_item200_response import AddCustomFieldListItem200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カスタム属性のID
    item_id = 56 # int | リスト項目のID

    try:
        # 選択リストカスタム属性のリスト項目の削除
        api_response = api_instance.delete_custom_field_list_item(project_id_or_key, id, item_id)
        print("The response of DefaultApi->delete_custom_field_list_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_custom_field_list_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カスタム属性のID | 
 **item_id** | **int**| リスト項目のID | 

### Return type

[**AddCustomFieldListItem200Response**](AddCustomFieldListItem200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> GetGroups200ResponseInner delete_group(group_id)

グループの削除

2025年8月28日以降、順次利用できなくなります。（新しいタブで開く） チームの削除 をご利用ください。 グループを削除します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    group_id = 56 # int | グループのID

    try:
        # グループの削除
        api_response = api_instance.delete_group(group_id)
        print("The response of DefaultApi->delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| グループのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue**
> AddRecentlyViewedIssue200Response delete_issue(issue_id_or_key)

課題の削除

課題を削除します。  実行可能な権限: - 管理者 - プロジェクト管理者 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_issue200_response import AddRecentlyViewedIssue200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 課題の削除
        api_response = api_instance.delete_issue(issue_id_or_key)
        print("The response of DefaultApi->delete_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**AddRecentlyViewedIssue200Response**](AddRecentlyViewedIssue200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue_attachment**
> AddRecentlyViewedWiki200ResponseAttachmentsInner delete_issue_attachment(issue_id_or_key, attachment_id)

課題添付ファイルの削除

課題の添付ファイルを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response_attachments_inner import AddRecentlyViewedWiki200ResponseAttachmentsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    attachment_id = 56 # int | 添付ファイルのID

    try:
        # 課題添付ファイルの削除
        api_response = api_instance.delete_issue_attachment(issue_id_or_key, attachment_id)
        print("The response of DefaultApi->delete_issue_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_issue_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **attachment_id** | **int**| 添付ファイルのID | 

### Return type

[**AddRecentlyViewedWiki200ResponseAttachmentsInner**](AddRecentlyViewedWiki200ResponseAttachmentsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue_comment**
> DeleteIssueComment200Response delete_issue_comment(issue_id_or_key, comment_id)

課題コメントの削除

課題コメントを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.delete_issue_comment200_response import DeleteIssueComment200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    comment_id = 56 # int | コメントのID

    try:
        # 課題コメントの削除
        api_response = api_instance.delete_issue_comment(issue_id_or_key, comment_id)
        print("The response of DefaultApi->delete_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **comment_id** | **int**| コメントのID | 

### Return type

[**DeleteIssueComment200Response**](DeleteIssueComment200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue_type**
> GetIssueTypes200ResponseInner delete_issue_type(project_id_or_key, id, substitute_issue_type_id)

種別の削除

プロジェクトから種別を削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_types200_response_inner import GetIssueTypes200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | 種別のID
    substitute_issue_type_id = 56 # int | 紐づく課題を付け替える先の種別のID

    try:
        # 種別の削除
        api_response = api_instance.delete_issue_type(project_id_or_key, id, substitute_issue_type_id)
        print("The response of DefaultApi->delete_issue_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_issue_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| 種別のID | 
 **substitute_issue_type_id** | **int**| 紐づく課題を付け替える先の種別のID | 

### Return type

[**GetIssueTypes200ResponseInner**](GetIssueTypes200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> DeleteProject200Response delete_project(project_id_or_key)

プロジェクトの削除

プロジェクトを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.delete_project200_response import DeleteProject200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクトの削除
        api_response = api_instance.delete_project(project_id_or_key)
        print("The response of DefaultApi->delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**DeleteProject200Response**](DeleteProject200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_administrator**
> GetIssueCommentNotifications200ResponseInnerUser delete_project_administrator(project_id_or_key, user_id)

プロジェクト管理者の削除

プロジェクトユーザーからプロジェクト管理者権限を削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    user_id = 56 # int | 削除するユーザーのID

    try:
        # プロジェクト管理者の削除
        api_response = api_instance.delete_project_administrator(project_id_or_key, user_id)
        print("The response of DefaultApi->delete_project_administrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project_administrator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **user_id** | **int**| 削除するユーザーのID | 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_group**
> GetGroups200ResponseInner delete_project_group(project_id_or_key, group_id)

プロジェクトグループの削除

2025年8月28日以降、順次利用できなくなります。 プロジェクトチームの削除をご利用ください。 プロジェクトからグループを削除します。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    group_id = 56 # int | 削除するグループのID

    try:
        # プロジェクトグループの削除
        api_response = api_instance.delete_project_group(project_id_or_key, group_id)
        print("The response of DefaultApi->delete_project_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **group_id** | **int**| 削除するグループのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_status**
> GetIssues200ResponseInnerIssueType delete_project_status(project_id_or_key, id, substitute_status_id)

状態の削除

プロジェクトから状態を削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_issue_type import GetIssues200ResponseInnerIssueType
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | 状態のID
    substitute_status_id = 56 # int | 紐づく課題を付け替える先の状態のID。削除対象の状態が設定されている課題がある場合、このパラメーターで指定した状態へ一括変更します。

    try:
        # 状態の削除
        api_response = api_instance.delete_project_status(project_id_or_key, id, substitute_status_id)
        print("The response of DefaultApi->delete_project_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| 状態のID | 
 **substitute_status_id** | **int**| 紐づく課題を付け替える先の状態のID。削除対象の状態が設定されている課題がある場合、このパラメーターで指定した状態へ一括変更します。 | 

### Return type

[**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_team**
> GetGroups200ResponseInner delete_project_team(project_id_or_key, team_id)

プロジェクトチームの削除

プロジェクトからチームを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    team_id = 56 # int | 削除するチームのID

    try:
        # プロジェクトチームの削除
        api_response = api_instance.delete_project_team(project_id_or_key, team_id)
        print("The response of DefaultApi->delete_project_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **team_id** | **int**| 削除するチームのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_user**
> GetIssueCommentNotifications200ResponseInnerUser delete_project_user(project_id_or_key, user_id)

プロジェクトユーザーの削除

プロジェクトからユーザーを削除します。  実行可能な権限: - 管理者 - プロジェクト管理者 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    user_id = 56 # int | 削除するユーザーのID

    try:
        # プロジェクトユーザーの削除
        api_response = api_instance.delete_project_user(project_id_or_key, user_id)
        print("The response of DefaultApi->delete_project_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **user_id** | **int**| 削除するユーザーのID | 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pull_request_attachment**
> AddRecentlyViewedWiki200ResponseAttachmentsInner delete_pull_request_attachment(project_id_or_key, repo_id_or_name, number, attachment_id)

プルリクエスト添付ファイルの削除

プルリクエストの添付ファイルを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response_attachments_inner import AddRecentlyViewedWiki200ResponseAttachmentsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号
    attachment_id = 56 # int | 添付ファイルのID

    try:
        # プルリクエスト添付ファイルの削除
        api_response = api_instance.delete_pull_request_attachment(project_id_or_key, repo_id_or_name, number, attachment_id)
        print("The response of DefaultApi->delete_pull_request_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_pull_request_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 
 **attachment_id** | **int**| 添付ファイルのID | 

### Return type

[**AddRecentlyViewedWiki200ResponseAttachmentsInner**](AddRecentlyViewedWiki200ResponseAttachmentsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> GetGroups200ResponseInner delete_team(team_id)

チームの削除

チームを削除します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    team_id = 56 # int | チームのID

    try:
        # チームの削除
        api_response = api_instance.delete_team(team_id)
        print("The response of DefaultApi->delete_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| チームのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> GetIssueCommentNotifications200ResponseInnerUser delete_user(user_id)

ユーザーの削除

ユーザーをスペースから削除します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | 削除するユーザーのID

    try:
        # ユーザーの削除
        api_response = api_instance.delete_user(user_id)
        print("The response of DefaultApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 削除するユーザーのID | 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> GetIssues200ResponseInnerMilestoneInner delete_version(project_id_or_key, id)

バージョン(マイルストーン)の削除

バージョン(マイルストーン)を削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_milestone_inner import GetIssues200ResponseInnerMilestoneInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | バージョンのID

    try:
        # バージョン(マイルストーン)の削除
        api_response = api_instance.delete_version(project_id_or_key, id)
        print("The response of DefaultApi->delete_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| バージョンのID | 

### Return type

[**GetIssues200ResponseInnerMilestoneInner**](GetIssues200ResponseInnerMilestoneInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_watching**
> DeleteWatching200Response delete_watching(watching_id)

ウォッチの削除

ウォッチを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.delete_watching200_response import DeleteWatching200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    watching_id = 56 # int | ウォッチのID

    try:
        # ウォッチの削除
        api_response = api_instance.delete_watching(watching_id)
        print("The response of DefaultApi->delete_watching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_watching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watching_id** | **int**| ウォッチのID | 

### Return type

[**DeleteWatching200Response**](DeleteWatching200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> GetWebhooks200ResponseInner delete_webhook(project_id_or_key, webhook_id)

Webhookの削除

Webhookを削除します。  実行可能な権限: - 管理者 - プロジェクト管理者 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_webhooks200_response_inner import GetWebhooks200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    webhook_id = 'webhook_id_example' # str | WebhookのID

    try:
        # Webhookの削除
        api_response = api_instance.delete_webhook(project_id_or_key, webhook_id)
        print("The response of DefaultApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **webhook_id** | **str**| WebhookのID | 

### Return type

[**GetWebhooks200ResponseInner**](GetWebhooks200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wiki**
> AddRecentlyViewedWiki200Response delete_wiki(wiki_id, mail_notify=mail_notify)

Wikiページの削除

WIkiページを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response import AddRecentlyViewedWiki200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    mail_notify = True # bool | ページの削除をメールで通知する場合はtrue (optional)

    try:
        # Wikiページの削除
        api_response = api_instance.delete_wiki(wiki_id, mail_notify=mail_notify)
        print("The response of DefaultApi->delete_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **mail_notify** | **bool**| ページの削除をメールで通知する場合はtrue | [optional] 

### Return type

[**AddRecentlyViewedWiki200Response**](AddRecentlyViewedWiki200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wiki_attachment**
> AddWikiAttachment200ResponseInner delete_wiki_attachment(wiki_id, attachment_id)

Wiki添付ファイルの削除

Wikiの添付ファイルを削除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_wiki_attachment200_response_inner import AddWikiAttachment200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    attachment_id = 56 # int | 添付ファイルのID

    try:
        # Wiki添付ファイルの削除
        api_response = api_instance.delete_wiki_attachment(wiki_id, attachment_id)
        print("The response of DefaultApi->delete_wiki_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_wiki_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **attachment_id** | **int**| 添付ファイルのID | 

### Return type

[**AddWikiAttachment200ResponseInner**](AddWikiAttachment200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_issue_attachment**
> bytearray download_issue_attachment(issue_id_or_key, attachment_id)

課題添付ファイルのダウンロード

課題の添付ファイルをダウンロードします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    attachment_id = 56 # int | 添付ファイルのID

    try:
        # 課題添付ファイルのダウンロード
        api_response = api_instance.download_issue_attachment(issue_id_or_key, attachment_id)
        print("The response of DefaultApi->download_issue_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_issue_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **attachment_id** | **int**| 添付ファイルのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_pull_request_attachment**
> bytearray download_pull_request_attachment(project_id_or_key, repo_id_or_name, number, attachment_id)

プルリクエスト添付ファイルのダウンロード

プルリクエストの添付ファイルをダウンロードします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号
    attachment_id = 56 # int | 添付ファイルのID

    try:
        # プルリクエスト添付ファイルのダウンロード
        api_response = api_instance.download_pull_request_attachment(project_id_or_key, repo_id_or_name, number, attachment_id)
        print("The response of DefaultApi->download_pull_request_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_pull_request_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 
 **attachment_id** | **int**| 添付ファイルのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_shared_file**
> bytearray download_shared_file(project_id_or_key, shared_file_id)

共有ファイルのダウンロード

共有ファイルを取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    shared_file_id = 56 # int | 共有ファイルのID

    try:
        # 共有ファイルのダウンロード
        api_response = api_instance.download_shared_file(project_id_or_key, shared_file_id)
        print("The response of DefaultApi->download_shared_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_shared_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **shared_file_id** | **int**| 共有ファイルのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_wiki_attachment**
> bytearray download_wiki_attachment(wiki_id, attachment_id)

Wiki添付ファイルのダウンロード

Wikiの添付ファイルをダウンロードします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    attachment_id = 56 # int | 添付ファイルのID

    try:
        # Wiki添付ファイルのダウンロード
        api_response = api_instance.download_wiki_attachment(wiki_id, attachment_id)
        print("The response of DefaultApi->download_wiki_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_wiki_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **attachment_id** | **int**| 添付ファイルのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> GetActivity200Response get_activity(activity_id)

アクティビティの取得

アクティビティの詳細を返します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_activity200_response import GetActivity200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    activity_id = 56 # int | アクティビティのID

    try:
        # アクティビティの取得
        api_response = api_instance.get_activity(activity_id)
        print("The response of DefaultApi->get_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| アクティビティのID | 

### Return type

[**GetActivity200Response**](GetActivity200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields**
> List[GetCustomFields200ResponseInner] get_custom_fields(project_id_or_key)

カスタム属性一覧の取得

プロジェクトに登録されているカスタム属性の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_custom_fields200_response_inner import GetCustomFields200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # カスタム属性一覧の取得
        api_response = api_instance.get_custom_fields(project_id_or_key)
        print("The response of DefaultApi->get_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetCustomFields200ResponseInner]**](GetCustomFields200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_repositories**
> List[GetGitRepository200Response] get_git_repositories(project_id_or_key)

Gitリポジトリ一覧の取得

Gitリポジトリの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_git_repository200_response import GetGitRepository200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # Gitリポジトリ一覧の取得
        api_response = api_instance.get_git_repositories(project_id_or_key)
        print("The response of DefaultApi->get_git_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_git_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetGitRepository200Response]**](GetGitRepository200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_repository**
> GetGitRepository200Response get_git_repository(project_id_or_key, repo_id_or_name)

Gitリポジトリの取得

Gitリポジトリを取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_git_repository200_response import GetGitRepository200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名

    try:
        # Gitリポジトリの取得
        api_response = api_instance.get_git_repository(project_id_or_key, repo_id_or_name)
        print("The response of DefaultApi->get_git_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_git_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 

### Return type

[**GetGitRepository200Response**](GetGitRepository200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GetGroups200ResponseInner get_group(group_id)

グループ情報の取得

2025年8月28日以降、順次利用できなくなります。（新しいタブで開く） チーム情報の取得をご利用ください。 グループの情報を取得します。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    group_id = 56 # int | グループのID

    try:
        # グループ情報の取得
        api_response = api_instance.get_group(group_id)
        print("The response of DefaultApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| グループのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_icon**
> bytearray get_group_icon(group_id)

グループアイコンの取得

2025年8月28日以降、順次利用できなくなります。 チームアイコンの取得をご利用ください。 グループのアイコン画像を取得します。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    group_id = 56 # int | グループのID

    try:
        # グループアイコンの取得
        api_response = api_instance.get_group_icon(group_id)
        print("The response of DefaultApi->get_group_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_group_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| グループのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> List[GetGroups200ResponseInner] get_groups(order=order, offset=offset, count=count)

グループ一覧の取得

2025年8月28日以降、順次利用できなくなります。（新しいタブで開く） チーム一覧の取得をご利用ください。 グループの一覧を取得します。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # グループ一覧の取得
        api_response = api_instance.get_groups(order=order, offset=offset, count=count)
        print("The response of DefaultApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**List[GetGroups200ResponseInner]**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue**
> AddRecentlyViewedIssue200Response get_issue(issue_id_or_key)

課題情報の取得

課題の情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_issue200_response import AddRecentlyViewedIssue200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 課題情報の取得
        api_response = api_instance.get_issue(issue_id_or_key)
        print("The response of DefaultApi->get_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**AddRecentlyViewedIssue200Response**](AddRecentlyViewedIssue200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_attachments**
> List[AddRecentlyViewedWiki200ResponseAttachmentsInner] get_issue_attachments(issue_id_or_key)

課題添付ファイル一覧の取得

課題の添付ファイルの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response_attachments_inner import AddRecentlyViewedWiki200ResponseAttachmentsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 課題添付ファイル一覧の取得
        api_response = api_instance.get_issue_attachments(issue_id_or_key)
        print("The response of DefaultApi->get_issue_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**List[AddRecentlyViewedWiki200ResponseAttachmentsInner]**](AddRecentlyViewedWiki200ResponseAttachmentsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_comment**
> GetIssueComments200ResponseInner get_issue_comment(issue_id_or_key, comment_id)

課題コメント情報の取得

課題コメントの詳細を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comments200_response_inner import GetIssueComments200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    comment_id = 56 # int | コメントのID

    try:
        # 課題コメント情報の取得
        api_response = api_instance.get_issue_comment(issue_id_or_key, comment_id)
        print("The response of DefaultApi->get_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **comment_id** | **int**| コメントのID | 

### Return type

[**GetIssueComments200ResponseInner**](GetIssueComments200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_comment_notifications**
> List[GetIssueCommentNotifications200ResponseInner] get_issue_comment_notifications(issue_id_or_key, comment_id)

課題コメントのお知らせ一覧の取得

課題コメントのお知らせ一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner import GetIssueCommentNotifications200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    comment_id = 56 # int | コメントのID

    try:
        # 課題コメントのお知らせ一覧の取得
        api_response = api_instance.get_issue_comment_notifications(issue_id_or_key, comment_id)
        print("The response of DefaultApi->get_issue_comment_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_comment_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **comment_id** | **int**| コメントのID | 

### Return type

[**List[GetIssueCommentNotifications200ResponseInner]**](GetIssueCommentNotifications200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_comments**
> List[GetIssueComments200ResponseInner] get_issue_comments(issue_id_or_key, min_id=min_id, max_id=max_id, count=count, order=order)

課題コメントの取得

課題に登録されているコメントの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comments200_response_inner import GetIssueComments200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # 課題コメントの取得
        api_response = api_instance.get_issue_comments(issue_id_or_key, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_issue_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetIssueComments200ResponseInner]**](GetIssueComments200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_comments_count**
> GetIssueCommentsCount200Response get_issue_comments_count(issue_id_or_key)

課題コメント数の取得

課題に登録されているコメントの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comments_count200_response import GetIssueCommentsCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 課題コメント数の取得
        api_response = api_instance.get_issue_comments_count(issue_id_or_key)
        print("The response of DefaultApi->get_issue_comments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_comments_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**GetIssueCommentsCount200Response**](GetIssueCommentsCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_participants**
> List[GetIssueCommentNotifications200ResponseInnerUser] get_issue_participants(issue_id_or_key)

課題の参加者一覧の取得

課題の参加者一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 課題の参加者一覧の取得
        api_response = api_instance.get_issue_participants(issue_id_or_key)
        print("The response of DefaultApi->get_issue_participants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_participants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**List[GetIssueCommentNotifications200ResponseInnerUser]**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_shared_files**
> List[GetRecentlyViewedIssues200ResponseIssueSharedFilesInner] get_issue_shared_files(issue_id_or_key)

課題共有ファイル一覧の取得

課題にリンクされた共有ファイルの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_shared_files_inner import GetRecentlyViewedIssues200ResponseIssueSharedFilesInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー

    try:
        # 課題共有ファイル一覧の取得
        api_response = api_instance.get_issue_shared_files(issue_id_or_key)
        print("The response of DefaultApi->get_issue_shared_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_shared_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 

### Return type

[**List[GetRecentlyViewedIssues200ResponseIssueSharedFilesInner]**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_types**
> List[GetIssueTypes200ResponseInner] get_issue_types(project_id_or_key)

種別一覧の取得

プロジェクトに登録されている種別の一覧を返します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_types200_response_inner import GetIssueTypes200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # 種別一覧の取得
        api_response = api_instance.get_issue_types(project_id_or_key)
        print("The response of DefaultApi->get_issue_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issue_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetIssueTypes200ResponseInner]**](GetIssueTypes200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issues**
> List[GetIssues200ResponseInner] get_issues(project_id=project_id, issue_type_id=issue_type_id, category_id=category_id, version_id=version_id, milestone_id=milestone_id, status_id=status_id, priority_id=priority_id, assignee_id=assignee_id, created_user_id=created_user_id, resolution_id=resolution_id, parent_child=parent_child, attachment=attachment, shared_file=shared_file, sort=sort, order=order, offset=offset, count=count, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, start_date_since=start_date_since, start_date_until=start_date_until, due_date_since=due_date_since, due_date_until=due_date_until, id=id, parent_issue_id=parent_issue_id, keyword=keyword, custom_field_id=custom_field_id, custom_field_id_min=custom_field_id_min, custom_field_id_max=custom_field_id_max, custom_field_id2=custom_field_id2)

課題一覧の取得

課題の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner import GetIssues200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id = [56] # List[int] | プロジェクトのID (optional)
    issue_type_id = [56] # List[int] | 種別のID (optional)
    category_id = [56] # List[int] | カテゴリーのID (optional)
    version_id = [56] # List[int] | 発生バージョンのID (optional)
    milestone_id = [56] # List[int] | マイルストーンのID (optional)
    status_id = [56] # List[int] | 状態のIDプロジェクト毎の状態一覧のAPI (optional)
    priority_id = [56] # List[int] | 優先度のID (optional)
    assignee_id = [56] # List[int] | 担当者のID (optional)
    created_user_id = [56] # List[int] | 登録者のID (optional)
    resolution_id = [56] # List[int] | 完了理由のID (optional)
    parent_child = 56 # int | 親子課題の条件0: すべて1: 子課題以外2: 子課題3: 親課題でも子課題でもない課題4: 親課題 (optional)
    attachment = True # bool | 添付ファイルを含む場合はtrue (optional)
    shared_file = True # bool | 共有ファイルを含む場合はtrue (optional)
    sort = 'sort_example' # str | 課題一覧のソートに使用する属性名\\\"issueType\\\"\\\"category\\\"\\\"version\\\"\\\"milestone\\\"\\\"summary\\\"\\\"status\\\"\\\"priority\\\"\\\"attachment\\\"\\\"sharedFile\\\"\\\"created\\\"\\\"createdUser\\\"\\\"updated\\\"\\\"updatedUser\\\"\\\"assignee\\\"\\\"startDate\\\"\\\"dueDate\\\"\\\"estimatedHours\\\"\\\"actualHours\\\"\\\"childIssue\\\"\\\"customField_${id}\\\" (optional)
    order = desc # str | ソート順 (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) (optional) (default to 20)
    created_since = '2013-10-20' # date | 登録日 (yyyy-MM-dd) (optional)
    created_until = '2013-10-20' # date | 登録日 (yyyy-MM-dd) (optional)
    updated_since = '2013-10-20' # date | 更新日 (yyyy-MM-dd) (optional)
    updated_until = '2013-10-20' # date | 更新日 (yyyy-MM-dd) (optional)
    start_date_since = '2013-10-20' # date | 開始日 (yyyy-MM-dd) (optional)
    start_date_until = '2013-10-20' # date | 開始日 (yyyy-MM-dd) (optional)
    due_date_since = '2013-10-20' # date | 期限日 (yyyy-MM-dd) (optional)
    due_date_until = '2013-10-20' # date | 期限日 (yyyy-MM-dd) (optional)
    id = [56] # List[int] | 課題のID (optional)
    parent_issue_id = [56] # List[int] | 親課題のID (optional)
    keyword = 'keyword_example' # str | 検索キーワード (optional)
    custom_field_id = 'custom_field_id_example' # str | カスタム属性（テキスト）の検索キーワード (optional)
    custom_field_id_min = 3.4 # float | カスタム属性（数値）の最小値 (optional)
    custom_field_id_max = 3.4 # float | カスタム属性（数値）の最大値 (optional)
    custom_field_id2 = [56] # List[int] | カスタム属性（リスト）の値のID (optional)

    try:
        # 課題一覧の取得
        api_response = api_instance.get_issues(project_id=project_id, issue_type_id=issue_type_id, category_id=category_id, version_id=version_id, milestone_id=milestone_id, status_id=status_id, priority_id=priority_id, assignee_id=assignee_id, created_user_id=created_user_id, resolution_id=resolution_id, parent_child=parent_child, attachment=attachment, shared_file=shared_file, sort=sort, order=order, offset=offset, count=count, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, start_date_since=start_date_since, start_date_until=start_date_until, due_date_since=due_date_since, due_date_until=due_date_until, id=id, parent_issue_id=parent_issue_id, keyword=keyword, custom_field_id=custom_field_id, custom_field_id_min=custom_field_id_min, custom_field_id_max=custom_field_id_max, custom_field_id2=custom_field_id2)
        print("The response of DefaultApi->get_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**List[int]**](int.md)| プロジェクトのID | [optional] 
 **issue_type_id** | [**List[int]**](int.md)| 種別のID | [optional] 
 **category_id** | [**List[int]**](int.md)| カテゴリーのID | [optional] 
 **version_id** | [**List[int]**](int.md)| 発生バージョンのID | [optional] 
 **milestone_id** | [**List[int]**](int.md)| マイルストーンのID | [optional] 
 **status_id** | [**List[int]**](int.md)| 状態のIDプロジェクト毎の状態一覧のAPI | [optional] 
 **priority_id** | [**List[int]**](int.md)| 優先度のID | [optional] 
 **assignee_id** | [**List[int]**](int.md)| 担当者のID | [optional] 
 **created_user_id** | [**List[int]**](int.md)| 登録者のID | [optional] 
 **resolution_id** | [**List[int]**](int.md)| 完了理由のID | [optional] 
 **parent_child** | **int**| 親子課題の条件0: すべて1: 子課題以外2: 子課題3: 親課題でも子課題でもない課題4: 親課題 | [optional] 
 **attachment** | **bool**| 添付ファイルを含む場合はtrue | [optional] 
 **shared_file** | **bool**| 共有ファイルを含む場合はtrue | [optional] 
 **sort** | **str**| 課題一覧のソートに使用する属性名\\\&quot;issueType\\\&quot;\\\&quot;category\\\&quot;\\\&quot;version\\\&quot;\\\&quot;milestone\\\&quot;\\\&quot;summary\\\&quot;\\\&quot;status\\\&quot;\\\&quot;priority\\\&quot;\\\&quot;attachment\\\&quot;\\\&quot;sharedFile\\\&quot;\\\&quot;created\\\&quot;\\\&quot;createdUser\\\&quot;\\\&quot;updated\\\&quot;\\\&quot;updatedUser\\\&quot;\\\&quot;assignee\\\&quot;\\\&quot;startDate\\\&quot;\\\&quot;dueDate\\\&quot;\\\&quot;estimatedHours\\\&quot;\\\&quot;actualHours\\\&quot;\\\&quot;childIssue\\\&quot;\\\&quot;customField_${id}\\\&quot; | [optional] 
 **order** | **str**| ソート順 | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) | [optional] [default to 20]
 **created_since** | **date**| 登録日 (yyyy-MM-dd) | [optional] 
 **created_until** | **date**| 登録日 (yyyy-MM-dd) | [optional] 
 **updated_since** | **date**| 更新日 (yyyy-MM-dd) | [optional] 
 **updated_until** | **date**| 更新日 (yyyy-MM-dd) | [optional] 
 **start_date_since** | **date**| 開始日 (yyyy-MM-dd) | [optional] 
 **start_date_until** | **date**| 開始日 (yyyy-MM-dd) | [optional] 
 **due_date_since** | **date**| 期限日 (yyyy-MM-dd) | [optional] 
 **due_date_until** | **date**| 期限日 (yyyy-MM-dd) | [optional] 
 **id** | [**List[int]**](int.md)| 課題のID | [optional] 
 **parent_issue_id** | [**List[int]**](int.md)| 親課題のID | [optional] 
 **keyword** | **str**| 検索キーワード | [optional] 
 **custom_field_id** | **str**| カスタム属性（テキスト）の検索キーワード | [optional] 
 **custom_field_id_min** | **float**| カスタム属性（数値）の最小値 | [optional] 
 **custom_field_id_max** | **float**| カスタム属性（数値）の最大値 | [optional] 
 **custom_field_id2** | [**List[int]**](int.md)| カスタム属性（リスト）の値のID | [optional] 

### Return type

[**List[GetIssues200ResponseInner]**](GetIssues200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issues_count**
> GetIssuesCount200Response get_issues_count(project_id=project_id, issue_type_id=issue_type_id, category_id=category_id, version_id=version_id, milestone_id=milestone_id, status_id=status_id, priority_id=priority_id, assignee_id=assignee_id, created_user_id=created_user_id, resolution_id=resolution_id, parent_child=parent_child, attachment=attachment, shared_file=shared_file, sort=sort, order=order, offset=offset, count=count, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, start_date_since=start_date_since, start_date_until=start_date_until, due_date_since=due_date_since, due_date_until=due_date_until, id=id, parent_issue_id=parent_issue_id, keyword=keyword, custom_field_id=custom_field_id, custom_field_id_min=custom_field_id_min, custom_field_id_max=custom_field_id_max, custom_field_id2=custom_field_id2)

課題数の取得

課題の数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues_count200_response import GetIssuesCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id = [56] # List[int] | プロジェクトのID (optional)
    issue_type_id = [56] # List[int] | 種別のID (optional)
    category_id = [56] # List[int] | カテゴリーのID (optional)
    version_id = [56] # List[int] | 発生バージョンのID (optional)
    milestone_id = [56] # List[int] | マイルストーンのID (optional)
    status_id = [56] # List[int] | 状態のID (optional)
    priority_id = [56] # List[int] | 優先度のID (optional)
    assignee_id = [56] # List[int] | 担当者のID (optional)
    created_user_id = [56] # List[int] | 登録者のID (optional)
    resolution_id = [56] # List[int] | 完了理由のID (optional)
    parent_child = 56 # int | 親子課題の条件0: すべて1: 子課題以外2: 子課題3: 親課題でも子課題でもない課題4: 親課題 (optional)
    attachment = True # bool | 添付ファイルを含む場合はtrue (optional)
    shared_file = True # bool | 共有ファイルを含む場合はtrue (optional)
    sort = 'sort_example' # str | 課題一覧のソートに使用する属性名\\\"issueType\\\"\\\"category\\\"\\\"version\\\"\\\"milestone\\\"\\\"summary\\\"\\\"status\\\"\\\"priority\\\"\\\"attachment\\\"\\\"sharedFile\\\"\\\"created\\\"\\\"createdUser\\\"\\\"updated\\\"\\\"updatedUser\\\"\\\"assignee\\\"\\\"startDate\\\"\\\"dueDate\\\"\\\"estimatedHours\\\"\\\"actualHours\\\"\\\"childIssue\\\"\\\"customField_${id}\\\" (optional)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    created_since = '2013-10-20' # date | 登録日 (yyyy-MM-dd) (optional)
    created_until = '2013-10-20' # date | 登録日 (yyyy-MM-dd) (optional)
    updated_since = '2013-10-20' # date | 更新日 (yyyy-MM-dd) (optional)
    updated_until = '2013-10-20' # date | 更新日 (yyyy-MM-dd) (optional)
    start_date_since = '2013-10-20' # date | 開始日 (yyyy-MM-dd) (optional)
    start_date_until = '2013-10-20' # date | 開始日 (yyyy-MM-dd) (optional)
    due_date_since = '2013-10-20' # date | 期限日 (yyyy-MM-dd) (optional)
    due_date_until = '2013-10-20' # date | 期限日 (yyyy-MM-dd) (optional)
    id = [56] # List[int] | 課題のID (optional)
    parent_issue_id = [56] # List[int] | 親課題のID (optional)
    keyword = 'keyword_example' # str | 検索キーワード (optional)
    custom_field_id = 'custom_field_id_example' # str | 検索キーワード (optional)
    custom_field_id_min = 3.4 # float | 最小値 (optional)
    custom_field_id_max = 3.4 # float | 最大値 (optional)
    custom_field_id2 = [56] # List[int] | 値のID (optional)

    try:
        # 課題数の取得
        api_response = api_instance.get_issues_count(project_id=project_id, issue_type_id=issue_type_id, category_id=category_id, version_id=version_id, milestone_id=milestone_id, status_id=status_id, priority_id=priority_id, assignee_id=assignee_id, created_user_id=created_user_id, resolution_id=resolution_id, parent_child=parent_child, attachment=attachment, shared_file=shared_file, sort=sort, order=order, offset=offset, count=count, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, start_date_since=start_date_since, start_date_until=start_date_until, due_date_since=due_date_since, due_date_until=due_date_until, id=id, parent_issue_id=parent_issue_id, keyword=keyword, custom_field_id=custom_field_id, custom_field_id_min=custom_field_id_min, custom_field_id_max=custom_field_id_max, custom_field_id2=custom_field_id2)
        print("The response of DefaultApi->get_issues_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_issues_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**List[int]**](int.md)| プロジェクトのID | [optional] 
 **issue_type_id** | [**List[int]**](int.md)| 種別のID | [optional] 
 **category_id** | [**List[int]**](int.md)| カテゴリーのID | [optional] 
 **version_id** | [**List[int]**](int.md)| 発生バージョンのID | [optional] 
 **milestone_id** | [**List[int]**](int.md)| マイルストーンのID | [optional] 
 **status_id** | [**List[int]**](int.md)| 状態のID | [optional] 
 **priority_id** | [**List[int]**](int.md)| 優先度のID | [optional] 
 **assignee_id** | [**List[int]**](int.md)| 担当者のID | [optional] 
 **created_user_id** | [**List[int]**](int.md)| 登録者のID | [optional] 
 **resolution_id** | [**List[int]**](int.md)| 完了理由のID | [optional] 
 **parent_child** | **int**| 親子課題の条件0: すべて1: 子課題以外2: 子課題3: 親課題でも子課題でもない課題4: 親課題 | [optional] 
 **attachment** | **bool**| 添付ファイルを含む場合はtrue | [optional] 
 **shared_file** | **bool**| 共有ファイルを含む場合はtrue | [optional] 
 **sort** | **str**| 課題一覧のソートに使用する属性名\\\&quot;issueType\\\&quot;\\\&quot;category\\\&quot;\\\&quot;version\\\&quot;\\\&quot;milestone\\\&quot;\\\&quot;summary\\\&quot;\\\&quot;status\\\&quot;\\\&quot;priority\\\&quot;\\\&quot;attachment\\\&quot;\\\&quot;sharedFile\\\&quot;\\\&quot;created\\\&quot;\\\&quot;createdUser\\\&quot;\\\&quot;updated\\\&quot;\\\&quot;updatedUser\\\&quot;\\\&quot;assignee\\\&quot;\\\&quot;startDate\\\&quot;\\\&quot;dueDate\\\&quot;\\\&quot;estimatedHours\\\&quot;\\\&quot;actualHours\\\&quot;\\\&quot;childIssue\\\&quot;\\\&quot;customField_${id}\\\&quot; | [optional] 
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **created_since** | **date**| 登録日 (yyyy-MM-dd) | [optional] 
 **created_until** | **date**| 登録日 (yyyy-MM-dd) | [optional] 
 **updated_since** | **date**| 更新日 (yyyy-MM-dd) | [optional] 
 **updated_until** | **date**| 更新日 (yyyy-MM-dd) | [optional] 
 **start_date_since** | **date**| 開始日 (yyyy-MM-dd) | [optional] 
 **start_date_until** | **date**| 開始日 (yyyy-MM-dd) | [optional] 
 **due_date_since** | **date**| 期限日 (yyyy-MM-dd) | [optional] 
 **due_date_until** | **date**| 期限日 (yyyy-MM-dd) | [optional] 
 **id** | [**List[int]**](int.md)| 課題のID | [optional] 
 **parent_issue_id** | [**List[int]**](int.md)| 親課題のID | [optional] 
 **keyword** | **str**| 検索キーワード | [optional] 
 **custom_field_id** | **str**| 検索キーワード | [optional] 
 **custom_field_id_min** | **float**| 最小値 | [optional] 
 **custom_field_id_max** | **float**| 最大値 | [optional] 
 **custom_field_id2** | [**List[int]**](int.md)| 値のID | [optional] 

### Return type

[**GetIssuesCount200Response**](GetIssuesCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licence_info**
> GetLicenceInfo200Response get_licence_info()

ライセンス情報の取得

ライセンスの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_licence_info200_response import GetLicenceInfo200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # ライセンス情報の取得
        api_response = api_instance.get_licence_info()
        print("The response of DefaultApi->get_licence_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_licence_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetLicenceInfo200Response**](GetLicenceInfo200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_recently_viewed_wikis**
> GetMyRecentlyViewedWikis200Response get_my_recently_viewed_wikis(order=order, offset=offset, count=count)

自分が最近見たWiki一覧の取得

APIとの認証に使用しているユーザーが最近見たWikiの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_my_recently_viewed_wikis200_response import GetMyRecentlyViewedWikis200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # 自分が最近見たWiki一覧の取得
        api_response = api_instance.get_my_recently_viewed_wikis(order=order, offset=offset, count=count)
        print("The response of DefaultApi->get_my_recently_viewed_wikis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_recently_viewed_wikis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**GetMyRecentlyViewedWikis200Response**](GetMyRecentlyViewedWikis200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_myself**
> GetIssueCommentNotifications200ResponseInnerUser get_myself()

認証ユーザー情報の取得

APIとの認証に使用しているユーザーの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # 認証ユーザー情報の取得
        api_response = api_instance.get_myself()
        print("The response of DefaultApi->get_myself:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_myself: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> List[GetNotifications200ResponseInner] get_notifications(min_id=min_id, max_id=max_id, count=count, order=order, sender_id=sender_id)

お知らせ一覧の取得

自分の受け取ったお知らせの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_notifications200_response_inner import GetNotifications200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    sender_id = 56 # int | 送信者ID (optional)

    try:
        # お知らせ一覧の取得
        api_response = api_instance.get_notifications(min_id=min_id, max_id=max_id, count=count, order=order, sender_id=sender_id)
        print("The response of DefaultApi->get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **sender_id** | **int**| 送信者ID | [optional] 

### Return type

[**List[GetNotifications200ResponseInner]**](GetNotifications200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_count**
> GetNotificationsCount200Response get_notifications_count(already_read=already_read, resource_already_read=resource_already_read)

お知らせ数の取得

自分の受け取ったお知らせの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_notifications_count200_response import GetNotificationsCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    already_read = True # bool |  (optional)
    resource_already_read = True # bool |  (optional)

    try:
        # お知らせ数の取得
        api_response = api_instance.get_notifications_count(already_read=already_read, resource_already_read=resource_already_read)
        print("The response of DefaultApi->get_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_notifications_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **already_read** | **bool**|  | [optional] 
 **resource_already_read** | **bool**|  | [optional] 

### Return type

[**GetNotificationsCount200Response**](GetNotificationsCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_priorities**
> List[GetPriorities200ResponseInner] get_priorities()

優先度一覧の取得

課題に設定できる優先度の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_priorities200_response_inner import GetPriorities200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # 優先度一覧の取得
        api_response = api_instance.get_priorities()
        print("The response of DefaultApi->get_priorities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_priorities: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetPriorities200ResponseInner]**](GetPriorities200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> AddProject201Response get_project(project_id_or_key)

プロジェクト情報の取得

プロジェクトの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_project201_response import AddProject201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクト情報の取得
        api_response = api_instance.get_project(project_id_or_key)
        print("The response of DefaultApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**AddProject201Response**](AddProject201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_activities**
> List[GetProjectActivities200ResponseInner] get_project_activities(project_id_or_key, activity_type_id=activity_type_id, min_id=min_id, max_id=max_id, count=count, order=order)

プロジェクトの最近の活動の取得

プロジェクト上の最近の活動の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_project_activities200_response_inner import GetProjectActivities200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    activity_type_id = [56] # List[int] | type(1-26) (optional)
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # プロジェクトの最近の活動の取得
        api_response = api_instance.get_project_activities(project_id_or_key, activity_type_id=activity_type_id, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_project_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **activity_type_id** | [**List[int]**](int.md)| type(1-26) | [optional] 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetProjectActivities200ResponseInner]**](GetProjectActivities200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_administrators**
> List[GetIssueCommentNotifications200ResponseInnerUser] get_project_administrators(project_id_or_key)

プロジェクト管理者一覧の取得

プロジェクト管理者に設定されているユーザーの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクト管理者一覧の取得
        api_response = api_instance.get_project_administrators(project_id_or_key)
        print("The response of DefaultApi->get_project_administrators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_administrators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetIssueCommentNotifications200ResponseInnerUser]**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_categories**
> List[GetProjectCategories200ResponseInner] get_project_categories(project_id_or_key)

カテゴリー一覧の取得

プロジェクトに登録されているカテゴリーの一覧を返します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_project_categories200_response_inner import GetProjectCategories200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # カテゴリー一覧の取得
        api_response = api_instance.get_project_categories(project_id_or_key)
        print("The response of DefaultApi->get_project_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetProjectCategories200ResponseInner]**](GetProjectCategories200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_disk_usage**
> GetProjectDiskUsage200Response get_project_disk_usage(project_id_or_key)

プロジェクトの容量使用状況の取得

プロジェクトの容量使用状況の情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_project_disk_usage200_response import GetProjectDiskUsage200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクトの容量使用状況の取得
        api_response = api_instance.get_project_disk_usage(project_id_or_key)
        print("The response of DefaultApi->get_project_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_disk_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**GetProjectDiskUsage200Response**](GetProjectDiskUsage200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_files**
> List[GetWikiSharedFiles200ResponseInner] get_project_files(project_id_or_key, path, order=order, offset=offset, count=count)

共有ファイル一覧の取得

共有ファイルの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_wiki_shared_files200_response_inner import GetWikiSharedFiles200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    path = 'path_example' # str | ディレクトリのパス
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 1000 # int | 取得上限(1-1000) 指定が無い場合は1000 (optional) (default to 1000)

    try:
        # 共有ファイル一覧の取得
        api_response = api_instance.get_project_files(project_id_or_key, path, order=order, offset=offset, count=count)
        print("The response of DefaultApi->get_project_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **path** | **str**| ディレクトリのパス | 
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-1000) 指定が無い場合は1000 | [optional] [default to 1000]

### Return type

[**List[GetWikiSharedFiles200ResponseInner]**](GetWikiSharedFiles200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_groups**
> List[GetGroups200ResponseInner] get_project_groups(project_id_or_key)

プロジェクトグループ一覧の取得

2025年8月28日以降、順次利用できなくなります。 プロジェクトチーム一覧の取得をご利用ください。 プロジェクトのグループの一覧を取得します。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクトグループ一覧の取得
        api_response = api_instance.get_project_groups(project_id_or_key)
        print("The response of DefaultApi->get_project_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetGroups200ResponseInner]**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_icon**
> bytearray get_project_icon(project_id_or_key)

プロジェクトアイコンの取得

プロジェクトのアイコン画像を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクトアイコンの取得
        api_response = api_instance.get_project_icon(project_id_or_key)
        print("The response of DefaultApi->get_project_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_statuses**
> List[GetProjectStatuses200ResponseInner] get_project_statuses(project_id_or_key)

プロジェクトの状態一覧の取得

プロジェクト固有の課題に設定できる状態一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_project_statuses200_response_inner import GetProjectStatuses200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | Project ID or Project Key

    try:
        # プロジェクトの状態一覧の取得
        api_response = api_instance.get_project_statuses(project_id_or_key)
        print("The response of DefaultApi->get_project_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| Project ID or Project Key | 

### Return type

[**List[GetProjectStatuses200ResponseInner]**](GetProjectStatuses200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_teams**
> List[GetGroups200ResponseInner] get_project_teams(project_id_or_key)

プロジェクトチーム一覧の取得

プロジェクトのチームの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # プロジェクトチーム一覧の取得
        api_response = api_instance.get_project_teams(project_id_or_key)
        print("The response of DefaultApi->get_project_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetGroups200ResponseInner]**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_users**
> List[GetIssueCommentNotifications200ResponseInnerUser] get_project_users(project_id_or_key, exclude_group_members=exclude_group_members)

プロジェクトユーザー一覧の取得

プロジェクトのユーザーの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    exclude_group_members = True # bool | グループを介してプロジェクトに参加しているメンバーを除く (optional)

    try:
        # プロジェクトユーザー一覧の取得
        api_response = api_instance.get_project_users(project_id_or_key, exclude_group_members=exclude_group_members)
        print("The response of DefaultApi->get_project_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **exclude_group_members** | **bool**| グループを介してプロジェクトに参加しているメンバーを除く | [optional] 

### Return type

[**List[GetIssueCommentNotifications200ResponseInnerUser]**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_versions**
> List[GetProjectVersions200ResponseInner] get_project_versions(project_id_or_key)

バージョン(マイルストーン)一覧の取得

プロジェクトに登録されているバージョン(マイルストーン)の一覧を返します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_project_versions200_response_inner import GetProjectVersions200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # バージョン(マイルストーン)一覧の取得
        api_response = api_instance.get_project_versions(project_id_or_key)
        print("The response of DefaultApi->get_project_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetProjectVersions200ResponseInner]**](GetProjectVersions200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> List[GetProjects200ResponseInner] get_projects(archived=archived, all=all)

プロジェクト一覧の取得

プロジェクトの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_projects200_response_inner import GetProjects200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    archived = True # bool | 省略された場合は全てのプロジェクト、falseの場合はアーカイブされていないプロジェクト、trueの場合はアーカイブされたプロジェクトを返します。 (optional)
    all = True # bool | ユーザが管理者権限の場合のみ有効なパラメータです。trueの場合はすべてのプロジェクト、falseの場合は参加しているプロジェクトのみを返します。初期値はfalse。 (optional)

    try:
        # プロジェクト一覧の取得
        api_response = api_instance.get_projects(archived=archived, all=all)
        print("The response of DefaultApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archived** | **bool**| 省略された場合は全てのプロジェクト、falseの場合はアーカイブされていないプロジェクト、trueの場合はアーカイブされたプロジェクトを返します。 | [optional] 
 **all** | **bool**| ユーザが管理者権限の場合のみ有効なパラメータです。trueの場合はすべてのプロジェクト、falseの場合は参加しているプロジェクトのみを返します。初期値はfalse。 | [optional] 

### Return type

[**List[GetProjects200ResponseInner]**](GetProjects200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request**
> GetPullRequest200Response get_pull_request(project_id_or_key, repo_id_or_name, number)

プルリクエストの取得

プルリクエストを取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_pull_request200_response import GetPullRequest200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号

    try:
        # プルリクエストの取得
        api_response = api_instance.get_pull_request(project_id_or_key, repo_id_or_name, number)
        print("The response of DefaultApi->get_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 

### Return type

[**GetPullRequest200Response**](GetPullRequest200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request_attachments**
> List[AddRecentlyViewedWiki200ResponseAttachmentsInner] get_pull_request_attachments(project_id_or_key, repo_id_or_name, number)

プルリクエスト添付ファイル一覧の取得

プルリクエストの添付ファイルの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response_attachments_inner import AddRecentlyViewedWiki200ResponseAttachmentsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号

    try:
        # プルリクエスト添付ファイル一覧の取得
        api_response = api_instance.get_pull_request_attachments(project_id_or_key, repo_id_or_name, number)
        print("The response of DefaultApi->get_pull_request_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pull_request_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 

### Return type

[**List[AddRecentlyViewedWiki200ResponseAttachmentsInner]**](AddRecentlyViewedWiki200ResponseAttachmentsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request_comment_count**
> GetIssueCommentsCount200Response get_pull_request_comment_count(project_id_or_key, repo_id_or_name, number)

プルリクエストコメント数の取得

プルリクエストに登録されているコメントの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comments_count200_response import GetIssueCommentsCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号

    try:
        # プルリクエストコメント数の取得
        api_response = api_instance.get_pull_request_comment_count(project_id_or_key, repo_id_or_name, number)
        print("The response of DefaultApi->get_pull_request_comment_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pull_request_comment_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 

### Return type

[**GetIssueCommentsCount200Response**](GetIssueCommentsCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request_comments**
> List[GetPullRequestComments200ResponseInner] get_pull_request_comments(project_id_or_key, repo_id_or_name, number, min_id=min_id, max_id=max_id, count=count, order=order)

プルリクエストコメントの取得

プルリクエストのコメントの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_pull_request_comments200_response_inner import GetPullRequestComments200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # プルリクエストコメントの取得
        api_response = api_instance.get_pull_request_comments(project_id_or_key, repo_id_or_name, number, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_pull_request_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pull_request_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetPullRequestComments200ResponseInner]**](GetPullRequestComments200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request_count**
> GetIssueCommentsCount200Response get_pull_request_count(project_id_or_key, repo_id_or_name, status_id=status_id, assignee_id=assignee_id, issue_id=issue_id, created_user_id=created_user_id, offset=offset, count=count)

プルリクエスト数の取得

プルリクエストの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comments_count200_response import GetIssueCommentsCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    status_id = [56] # List[int] | 状態のID (optional)
    assignee_id = [56] # List[int] | 担当者のID (optional)
    issue_id = [56] # List[int] | 関連課題のID (optional)
    created_user_id = [56] # List[int] | 登録者のID (optional)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # プルリクエスト数の取得
        api_response = api_instance.get_pull_request_count(project_id_or_key, repo_id_or_name, status_id=status_id, assignee_id=assignee_id, issue_id=issue_id, created_user_id=created_user_id, offset=offset, count=count)
        print("The response of DefaultApi->get_pull_request_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pull_request_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **status_id** | [**List[int]**](int.md)| 状態のID | [optional] 
 **assignee_id** | [**List[int]**](int.md)| 担当者のID | [optional] 
 **issue_id** | [**List[int]**](int.md)| 関連課題のID | [optional] 
 **created_user_id** | [**List[int]**](int.md)| 登録者のID | [optional] 
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**GetIssueCommentsCount200Response**](GetIssueCommentsCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_requests**
> List[GetPullRequests200ResponseInner] get_pull_requests(project_id_or_key, repo_id_or_name, status_id=status_id, assignee_id=assignee_id, issue_id=issue_id, created_user_id=created_user_id, offset=offset, count=count)

プルリクエスト一覧の取得

プルリクエストの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_pull_requests200_response_inner import GetPullRequests200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    status_id = [56] # List[int] | 状態のID (optional)
    assignee_id = [56] # List[int] | 担当者のID (optional)
    issue_id = [56] # List[int] | 関連課題のID (optional)
    created_user_id = [56] # List[int] | 登録者のID (optional)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # プルリクエスト一覧の取得
        api_response = api_instance.get_pull_requests(project_id_or_key, repo_id_or_name, status_id=status_id, assignee_id=assignee_id, issue_id=issue_id, created_user_id=created_user_id, offset=offset, count=count)
        print("The response of DefaultApi->get_pull_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_pull_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **status_id** | [**List[int]**](int.md)| 状態のID | [optional] 
 **assignee_id** | [**List[int]**](int.md)| 担当者のID | [optional] 
 **issue_id** | [**List[int]**](int.md)| 関連課題のID | [optional] 
 **created_user_id** | [**List[int]**](int.md)| 登録者のID | [optional] 
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**List[GetPullRequests200ResponseInner]**](GetPullRequests200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_limit**
> GetRateLimit200Response get_rate_limit()

レート制限情報の取得

使用中のAPIキーに対応するユーザーに対して、現在設定されているレート制限に関する情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_rate_limit200_response import GetRateLimit200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # レート制限情報の取得
        api_response = api_instance.get_rate_limit()
        print("The response of DefaultApi->get_rate_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_rate_limit: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRateLimit200Response**](GetRateLimit200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recently_viewed_issues**
> GetRecentlyViewedIssues200Response get_recently_viewed_issues(order=order, offset=offset, count=count)

自分が最近見た課題一覧の取得

APIとの認証に使用しているユーザーが最近見た課題の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response import GetRecentlyViewedIssues200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # 自分が最近見た課題一覧の取得
        api_response = api_instance.get_recently_viewed_issues(order=order, offset=offset, count=count)
        print("The response of DefaultApi->get_recently_viewed_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_recently_viewed_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**GetRecentlyViewedIssues200Response**](GetRecentlyViewedIssues200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recently_viewed_projects**
> GetRecentlyViewedProjects200Response get_recently_viewed_projects(order=order, offset=offset, count=count)

自分が最近見たプロジェクト一覧の取得

APIとの認証に使用しているユーザーが最近見たプロジェクトの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_projects200_response import GetRecentlyViewedProjects200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # 自分が最近見たプロジェクト一覧の取得
        api_response = api_instance.get_recently_viewed_projects(order=order, offset=offset, count=count)
        print("The response of DefaultApi->get_recently_viewed_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_recently_viewed_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**GetRecentlyViewedProjects200Response**](GetRecentlyViewedProjects200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resolutions**
> List[GetPriorities200ResponseInner] get_resolutions()

完了理由一覧の取得

課題に設定できる完了理由の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_priorities200_response_inner import GetPriorities200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # 完了理由一覧の取得
        api_response = api_instance.get_resolutions()
        print("The response of DefaultApi->get_resolutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_resolutions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetPriorities200ResponseInner]**](GetPriorities200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space**
> GetSpace200Response get_space()

スペース情報の取得

スペースの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_space200_response import GetSpace200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # スペース情報の取得
        api_response = api_instance.get_space()
        print("The response of DefaultApi->get_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_space: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSpace200Response**](GetSpace200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_activities**
> List[GetSpaceActivities200ResponseInner] get_space_activities(activity_type_id=activity_type_id, min_id=min_id, max_id=max_id, count=count, order=order)

最近の更新の取得

スペース上で行われた最近の更新の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_space_activities200_response_inner import GetSpaceActivities200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    activity_type_id = [56] # List[int] | type(1-26) (optional)
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # 最近の更新の取得
        api_response = api_instance.get_space_activities(activity_type_id=activity_type_id, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_space_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_space_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_type_id** | [**List[int]**](int.md)| type(1-26) | [optional] 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetSpaceActivities200ResponseInner]**](GetSpaceActivities200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_disk_usage**
> GetSpaceDiskUsage200Response get_space_disk_usage()

スペースの容量使用状況の取得

スペースの容量使用状況の情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_space_disk_usage200_response import GetSpaceDiskUsage200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # スペースの容量使用状況の取得
        api_response = api_instance.get_space_disk_usage()
        print("The response of DefaultApi->get_space_disk_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_space_disk_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSpaceDiskUsage200Response**](GetSpaceDiskUsage200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_image**
> bytearray get_space_image()

スペースアイコン画像の取得

スペースのアイコン画像を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # スペースアイコン画像の取得
        api_response = api_instance.get_space_image()
        print("The response of DefaultApi->get_space_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_space_image: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_space_notification**
> GetSpaceNotification200Response get_space_notification()

スペースのお知らせの取得

スペースのお知らせの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_space_notification200_response import GetSpaceNotification200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # スペースのお知らせの取得
        api_response = api_instance.get_space_notification()
        print("The response of DefaultApi->get_space_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_space_notification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSpaceNotification200Response**](GetSpaceNotification200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statuses**
> List[GetStatuses200ResponseInner] get_statuses()

状態一覧の取得

2025年8月28日以降、順次利用できなくなります。（新しいタブで開く）  プロジェクトの状態一覧の取得をご利用ください。  課題に設定できる状態の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_statuses200_response_inner import GetStatuses200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # 状態一覧の取得
        api_response = api_instance.get_statuses()
        print("The response of DefaultApi->get_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetStatuses200ResponseInner]**](GetStatuses200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> GetGroups200ResponseInner get_team(team_id)

チーム情報の取得

チームの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    team_id = 56 # int | チームのID

    try:
        # チーム情報の取得
        api_response = api_instance.get_team(team_id)
        print("The response of DefaultApi->get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| チームのID | 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_icon**
> bytearray get_team_icon(team_id)

チームアイコンの取得

チームアイコン画像を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    team_id = 56 # int | チームのID

    try:
        # チームアイコンの取得
        api_response = api_instance.get_team_icon(team_id)
        print("The response of DefaultApi->get_team_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_team_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| チームのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> List[GetGroups200ResponseInner] get_teams(order=order, offset=offset, count=count)

チーム一覧の取得

チームの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    offset = 56 # int |  (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)

    try:
        # チーム一覧の取得
        api_response = api_instance.get_teams(order=order, offset=offset, count=count)
        print("The response of DefaultApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **offset** | **int**|  | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]

### Return type

[**List[GetGroups200ResponseInner]**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUsers200ResponseInner get_user(user_id)

ユーザー情報の取得

ユーザー情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_users200_response_inner import GetUsers200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID

    try:
        # ユーザー情報の取得
        api_response = api_instance.get_user(user_id)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 

### Return type

[**GetUsers200ResponseInner**](GetUsers200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_activities**
> List[GetUserActivities200ResponseInner] get_user_activities(user_id, activity_type_id=activity_type_id, min_id=min_id, max_id=max_id, count=count, order=order)

ユーザーの最近の活動の取得

ユーザーの最近の活動の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_user_activities200_response_inner import GetUserActivities200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID
    activity_type_id = [56] # List[int] | type(1-17) (optional)
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # ユーザーの最近の活動の取得
        api_response = api_instance.get_user_activities(user_id, activity_type_id=activity_type_id, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_user_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 
 **activity_type_id** | [**List[int]**](int.md)| type(1-17) | [optional] 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetUserActivities200ResponseInner]**](GetUserActivities200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_icon**
> bytearray get_user_icon(user_id)

ユーザーアイコンの取得

ユーザーのアイコン画像を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID

    try:
        # ユーザーアイコンの取得
        api_response = api_instance.get_user_icon(user_id)
        print("The response of DefaultApi->get_user_icon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_icon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 

### Return type

**bytearray**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Content-Type -  <br>  * Content-Disposition -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_stars**
> List[GetRecentlyViewedIssues200ResponseIssueStarsInner] get_user_stars(user_id, min_id=min_id, max_id=max_id, count=count, order=order)

ユーザーの受け取ったスター一覧の取得

ユーザーの受け取ったスターの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_stars_inner import GetRecentlyViewedIssues200ResponseIssueStarsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # ユーザーの受け取ったスター一覧の取得
        api_response = api_instance.get_user_stars(user_id, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_user_stars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_stars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetRecentlyViewedIssues200ResponseIssueStarsInner]**](GetRecentlyViewedIssues200ResponseIssueStarsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_stars_count**
> GetUserStarsCount200Response get_user_stars_count(user_id, since=since, until=until)

ユーザーの受け取ったスターの数の取得

ユーザーの受け取ったスターの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_user_stars_count200_response import GetUserStarsCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID
    since = '2013-10-20' # date | 指定した日付以降のスターをカウント (yyyy-MM-dd) (optional)
    until = '2013-10-20' # date | 指定した日付以前のスターをカウント (yyyy-MM-dd) (optional)

    try:
        # ユーザーの受け取ったスターの数の取得
        api_response = api_instance.get_user_stars_count(user_id, since=since, until=until)
        print("The response of DefaultApi->get_user_stars_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_stars_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 
 **since** | **date**| 指定した日付以降のスターをカウント (yyyy-MM-dd) | [optional] 
 **until** | **date**| 指定した日付以前のスターをカウント (yyyy-MM-dd) | [optional] 

### Return type

[**GetUserStarsCount200Response**](GetUserStarsCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_watchings**
> List[GetUserWatchings200ResponseInner] get_user_watchings(user_id, order=order, sort=sort, count=count, offset=offset, resource_already_read=resource_already_read, issue_id=issue_id)

ウォッチ一覧の取得

ウォッチの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_user_watchings200_response_inner import GetUserWatchings200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)
    sort = issueUpdated # str | ウォッチ一覧のソートに使用する属性名\\\"created\\\"\\\"updated\\\"\\\"issueUpdated\\\"指定が無い場合は\\\"issueUpdated\\\" (optional) (default to issueUpdated)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    offset = 56 # int |  (optional)
    resource_already_read = True # bool | ウォッチしている課題の詳細を既読かどうか。trueの場合は既読のウォッチ、falseの場合は未読のウォッチ、指定しない場合は両方のウォッチを返します。指定が無い場合は両方 (optional)
    issue_id = [56] # List[int] | 課題のID (optional)

    try:
        # ウォッチ一覧の取得
        api_response = api_instance.get_user_watchings(user_id, order=order, sort=sort, count=count, offset=offset, resource_already_read=resource_already_read, issue_id=issue_id)
        print("The response of DefaultApi->get_user_watchings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_watchings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]
 **sort** | **str**| ウォッチ一覧のソートに使用する属性名\\\&quot;created\\\&quot;\\\&quot;updated\\\&quot;\\\&quot;issueUpdated\\\&quot;指定が無い場合は\\\&quot;issueUpdated\\\&quot; | [optional] [default to issueUpdated]
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **offset** | **int**|  | [optional] 
 **resource_already_read** | **bool**| ウォッチしている課題の詳細を既読かどうか。trueの場合は既読のウォッチ、falseの場合は未読のウォッチ、指定しない場合は両方のウォッチを返します。指定が無い場合は両方 | [optional] 
 **issue_id** | [**List[int]**](int.md)| 課題のID | [optional] 

### Return type

[**List[GetUserWatchings200ResponseInner]**](GetUserWatchings200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> List[GetUsers200ResponseInner] get_users()

ユーザー一覧の取得

スペースのユーザーの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_users200_response_inner import GetUsers200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # ユーザー一覧の取得
        api_response = api_instance.get_users()
        print("The response of DefaultApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GetUsers200ResponseInner]**](GetUsers200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watching**
> GetWatching200Response get_watching(watching_id)

ウォッチ情報の取得

ウォッチの情報を追加します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_watching200_response import GetWatching200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    watching_id = 56 # int | ウォッチのID

    try:
        # ウォッチ情報の取得
        api_response = api_instance.get_watching(watching_id)
        print("The response of DefaultApi->get_watching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_watching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watching_id** | **int**| ウォッチのID | 

### Return type

[**GetWatching200Response**](GetWatching200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watching_count**
> GetNotificationsCount200Response get_watching_count(user_id, resource_already_read=resource_already_read, already_read=already_read)

ウォッチ数の取得

ウォッチの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_notifications_count200_response import GetNotificationsCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | ユーザーのID
    resource_already_read = True # bool | 既読かどうか。trueの場合は既読のウォッチ、falseの場合は未読のウォッチ、指定しない場合は両方のウォッチを返します。指定が無い場合は両方 (optional)
    already_read = True # bool | ウォッチメニューの一覧表示後に更新されたウォッチの件数を返します。trueの場合はウォッチメニューを表示した後に更新されていない(既読状態の)件数を返します。falseの場合はウォッチメニューを表示した後に更新された(未読状態の)ウォッチの件数を返します。指定が無い場合は両方を合わせた件数を返します。resourceAlreadyReadが指定してある場合、alreadyReadは使用されません。 (optional)

    try:
        # ウォッチ数の取得
        api_response = api_instance.get_watching_count(user_id, resource_already_read=resource_already_read, already_read=already_read)
        print("The response of DefaultApi->get_watching_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_watching_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ユーザーのID | 
 **resource_already_read** | **bool**| 既読かどうか。trueの場合は既読のウォッチ、falseの場合は未読のウォッチ、指定しない場合は両方のウォッチを返します。指定が無い場合は両方 | [optional] 
 **already_read** | **bool**| ウォッチメニューの一覧表示後に更新されたウォッチの件数を返します。trueの場合はウォッチメニューを表示した後に更新されていない(既読状態の)件数を返します。falseの場合はウォッチメニューを表示した後に更新された(未読状態の)ウォッチの件数を返します。指定が無い場合は両方を合わせた件数を返します。resourceAlreadyReadが指定してある場合、alreadyReadは使用されません。 | [optional] 

### Return type

[**GetNotificationsCount200Response**](GetNotificationsCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> GetWebhooks200ResponseInner get_webhook(project_id_or_key, webhook_id)

Webhookの取得

Webhookの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_webhooks200_response_inner import GetWebhooks200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    webhook_id = 'webhook_id_example' # str | WebhookのID

    try:
        # Webhookの取得
        api_response = api_instance.get_webhook(project_id_or_key, webhook_id)
        print("The response of DefaultApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **webhook_id** | **str**| WebhookのID | 

### Return type

[**GetWebhooks200ResponseInner**](GetWebhooks200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> List[GetWebhooks200ResponseInner] get_webhooks(project_id_or_key)

Webhook一覧の取得

Webhookの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_webhooks200_response_inner import GetWebhooks200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # Webhook一覧の取得
        api_response = api_instance.get_webhooks(project_id_or_key)
        print("The response of DefaultApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetWebhooks200ResponseInner]**](GetWebhooks200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki**
> AddRecentlyViewedWiki200Response get_wiki(wiki_id)

Wikiページ情報の取得

Wikiページの情報を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response import AddRecentlyViewedWiki200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID

    try:
        # Wikiページ情報の取得
        api_response = api_instance.get_wiki(wiki_id)
        print("The response of DefaultApi->get_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 

### Return type

[**AddRecentlyViewedWiki200Response**](AddRecentlyViewedWiki200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_attachments**
> List[GetIssues200ResponseInnerAttachmentsInner] get_wiki_attachments(wiki_id)

Wiki添付ファイル一覧の取得

Wikiの添付ファイルの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_attachments_inner import GetIssues200ResponseInnerAttachmentsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID

    try:
        # Wiki添付ファイル一覧の取得
        api_response = api_instance.get_wiki_attachments(wiki_id)
        print("The response of DefaultApi->get_wiki_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 

### Return type

[**List[GetIssues200ResponseInnerAttachmentsInner]**](GetIssues200ResponseInnerAttachmentsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_count**
> GetWikiCount200Response get_wiki_count(project_id_or_key=project_id_or_key)

Wikiページ数の取得

Wikiページの数を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_wiki_count200_response import GetWikiCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー (optional)

    try:
        # Wikiページ数の取得
        api_response = api_instance.get_wiki_count(project_id_or_key=project_id_or_key)
        print("The response of DefaultApi->get_wiki_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | [optional] 

### Return type

[**GetWikiCount200Response**](GetWikiCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_history**
> List[GetWikiHistory200ResponseInner] get_wiki_history(wiki_id, min_id=min_id, max_id=max_id, count=count, order=order)

Wikiページ更新履歴一覧の取得

Wikiページの更新履歴の一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_wiki_history200_response_inner import GetWikiHistory200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    min_id = 56 # int | 最小ID (optional)
    max_id = 56 # int | 最大ID (optional)
    count = 20 # int | 取得上限(1-100) 指定が無い場合は20 (optional) (default to 20)
    order = desc # str | \\\"asc\\\"または\\\"desc\\\" 指定が無い場合は\\\"desc\\\" (optional) (default to desc)

    try:
        # Wikiページ更新履歴一覧の取得
        api_response = api_instance.get_wiki_history(wiki_id, min_id=min_id, max_id=max_id, count=count, order=order)
        print("The response of DefaultApi->get_wiki_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **min_id** | **int**| 最小ID | [optional] 
 **max_id** | **int**| 最大ID | [optional] 
 **count** | **int**| 取得上限(1-100) 指定が無い場合は20 | [optional] [default to 20]
 **order** | **str**| \\\&quot;asc\\\&quot;または\\\&quot;desc\\\&quot; 指定が無い場合は\\\&quot;desc\\\&quot; | [optional] [default to desc]

### Return type

[**List[GetWikiHistory200ResponseInner]**](GetWikiHistory200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_shared_files**
> List[GetWikiSharedFiles200ResponseInner] get_wiki_shared_files(wiki_id)

Wiki共有ファイル一覧の取得

Wikiの共有ファイルの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_wiki_shared_files200_response_inner import GetWikiSharedFiles200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID

    try:
        # Wiki共有ファイル一覧の取得
        api_response = api_instance.get_wiki_shared_files(wiki_id)
        print("The response of DefaultApi->get_wiki_shared_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki_shared_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 

### Return type

[**List[GetWikiSharedFiles200ResponseInner]**](GetWikiSharedFiles200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_stars**
> List[GetRecentlyViewedIssues200ResponseIssueStarsInner] get_wiki_stars(wiki_id)

Wikiページのスター一覧の取得

Wikiページが受け取ったスターの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_stars_inner import GetRecentlyViewedIssues200ResponseIssueStarsInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID

    try:
        # Wikiページのスター一覧の取得
        api_response = api_instance.get_wiki_stars(wiki_id)
        print("The response of DefaultApi->get_wiki_stars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki_stars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 

### Return type

[**List[GetRecentlyViewedIssues200ResponseIssueStarsInner]**](GetRecentlyViewedIssues200ResponseIssueStarsInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wiki_tags**
> List[GetIssues200ResponseInnerPriority] get_wiki_tags(project_id_or_key)

Wikiページタグ一覧の取得

プロジェクト内のWikiページで使用されているタグの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_priority import GetIssues200ResponseInnerPriority
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー

    try:
        # Wikiページタグ一覧の取得
        api_response = api_instance.get_wiki_tags(project_id_or_key)
        print("The response of DefaultApi->get_wiki_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wiki_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 

### Return type

[**List[GetIssues200ResponseInnerPriority]**](GetIssues200ResponseInnerPriority.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wikis**
> List[GetMyRecentlyViewedWikis200ResponsePage] get_wikis(project_id_or_key=project_id_or_key, keyword=keyword)

Wikiページ一覧の取得

Wikiページの一覧を取得します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_my_recently_viewed_wikis200_response_page import GetMyRecentlyViewedWikis200ResponsePage
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー (optional)
    keyword = 'keyword_example' # str | 検索キーワード (optional)

    try:
        # Wikiページ一覧の取得
        api_response = api_instance.get_wikis(project_id_or_key=project_id_or_key, keyword=keyword)
        print("The response of DefaultApi->get_wikis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_wikis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | [optional] 
 **keyword** | **str**| 検索キーワード | [optional] 

### Return type

[**List[GetMyRecentlyViewedWikis200ResponsePage]**](GetMyRecentlyViewedWikis200ResponsePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_shared_file_to_issue**
> List[GetRecentlyViewedIssues200ResponseIssueSharedFilesInner] link_shared_file_to_issue(issue_id_or_key, file_id)

課題に共有ファイルをリンク

課題に共有ファイルをリンクします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_shared_files_inner import GetRecentlyViewedIssues200ResponseIssueSharedFilesInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    file_id = 56 # int | 共有ファイルのID

    try:
        # 課題に共有ファイルをリンク
        api_response = api_instance.link_shared_file_to_issue(issue_id_or_key, file_id)
        print("The response of DefaultApi->link_shared_file_to_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->link_shared_file_to_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **file_id** | **int**| 共有ファイルのID | 

### Return type

[**List[GetRecentlyViewedIssues200ResponseIssueSharedFilesInner]**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_shared_files_to_wiki**
> GetRecentlyViewedIssues200ResponseIssueSharedFilesInner link_shared_files_to_wiki(wiki_id, file_id)

Wikiに共有ファイルをリンク

Wikiに共有ファイルをリンクします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_shared_files_inner import GetRecentlyViewedIssues200ResponseIssueSharedFilesInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    file_id = 56 # int | 共有ファイルのID

    try:
        # Wikiに共有ファイルをリンク
        api_response = api_instance.link_shared_files_to_wiki(wiki_id, file_id)
        print("The response of DefaultApi->link_shared_files_to_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->link_shared_files_to_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **file_id** | **int**| 共有ファイルのID | 

### Return type

[**GetRecentlyViewedIssues200ResponseIssueSharedFilesInner**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notification_as_read**
> mark_notification_as_read(id)

お知らせの既読化

お知らせを既読にします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    id = 56 # int | お知らせのID

    try:
        # お知らせの既読化
        api_instance.mark_notification_as_read(id)
    except Exception as e:
        print("Exception when calling DefaultApi->mark_notification_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| お知らせのID | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO_CONTENT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_watching_as_read**
> mark_watching_as_read(watching_id)

ウォッチの既読化

ウォッチを既読にします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    watching_id = 56 # int | ウォッチのID

    try:
        # ウォッチの既読化
        api_instance.mark_watching_as_read(watching_id)
    except Exception as e:
        print("Exception when calling DefaultApi->mark_watching_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watching_id** | **int**| ウォッチのID | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO_CONTENT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachment**
> PostAttachment200Response post_attachment(file=file)

添付ファイルの送信

課題、コメントまたはWikiに添付するファイルを送信し、添付ファイルに発行されたIDを取得します。  送信されたファイルは添付された後に削除されます。また添付されなかった場合は1時間後に削除されます。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.post_attachment200_response import PostAttachment200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    file = None # bytearray | アップロードするファイル (optional)

    try:
        # 添付ファイルの送信
        api_response = api_instance.post_attachment(file=file)
        print("The response of DefaultApi->post_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| アップロードするファイル | [optional] 

### Return type

[**PostAttachment200Response**](PostAttachment200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_notification_count**
> ResetNotificationCount200Response reset_notification_count()

お知らせ数のリセット

自分の受け取ったお知らせの未読数をリセットします。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.reset_notification_count200_response import ResetNotificationCount200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # お知らせ数のリセット
        api_response = api_instance.reset_notification_count()
        print("The response of DefaultApi->reset_notification_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->reset_notification_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResetNotificationCount200Response**](ResetNotificationCount200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_issue_shared_file**
> GetRecentlyViewedIssues200ResponseIssueSharedFilesInner unlink_issue_shared_file(issue_id_or_key, id)

課題の共有ファイルのリンクを解除

課題にリンクされた共有ファイルのリンクを解除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_shared_files_inner import GetRecentlyViewedIssues200ResponseIssueSharedFilesInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    id = 56 # int | 共有ファイルのID

    try:
        # 課題の共有ファイルのリンクを解除
        api_response = api_instance.unlink_issue_shared_file(issue_id_or_key, id)
        print("The response of DefaultApi->unlink_issue_shared_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->unlink_issue_shared_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **id** | **int**| 共有ファイルのID | 

### Return type

[**GetRecentlyViewedIssues200ResponseIssueSharedFilesInner**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_wiki_shared_file**
> GetRecentlyViewedIssues200ResponseIssueSharedFilesInner unlink_wiki_shared_file(wiki_id, id)

Wikiの共有ファイルのリンクを解除

Wikiにリンクされた共有ファイルのリンクを解除します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_recently_viewed_issues200_response_issue_shared_files_inner import GetRecentlyViewedIssues200ResponseIssueSharedFilesInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    id = 56 # int | 共有ファイルのID

    try:
        # Wikiの共有ファイルのリンクを解除
        api_response = api_instance.unlink_wiki_shared_file(wiki_id, id)
        print("The response of DefaultApi->unlink_wiki_shared_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->unlink_wiki_shared_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **id** | **int**| 共有ファイルのID | 

### Return type

[**GetRecentlyViewedIssues200ResponseIssueSharedFilesInner**](GetRecentlyViewedIssues200ResponseIssueSharedFilesInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> AddProjectCategory200Response update_category(project_id_or_key, id, name=name)

カテゴリー情報の更新

カテゴリーの情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_project_category200_response import AddProjectCategory200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カテゴリーのID
    name = 'name_example' # str | カテゴリーの名前 (optional)

    try:
        # カテゴリー情報の更新
        api_response = api_instance.update_category(project_id_or_key, id, name=name)
        print("The response of DefaultApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カテゴリーのID | 
 **name** | **str**| カテゴリーの名前 | [optional] 

### Return type

[**AddProjectCategory200Response**](AddProjectCategory200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> AddCustomField200Response update_custom_field(project_id_or_key, id, name=name, applicable_issue_types=applicable_issue_types, description=description, required=required, min=min, max=max, initial_value=initial_value, unit=unit, initial_value_type=initial_value_type, initial_date=initial_date, initial_shift=initial_shift, items=items, allow_input=allow_input, allow_add_item=allow_add_item)

カスタム属性の更新

カスタム属性を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_custom_field200_response import AddCustomField200Response
from backlog_client.models.add_custom_field_request_max import AddCustomFieldRequestMax
from backlog_client.models.add_custom_field_request_min import AddCustomFieldRequestMin
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カスタム属性のID
    name = 'name_example' # str | カスタム属性の名前 (optional)
    applicable_issue_types = [56] # List[int] | カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 (optional)
    description = 'description_example' # str | カスタム属性の説明 (optional)
    required = True # bool | 必須な属性とする場合はtrue (optional)
    min = backlog_client.AddCustomFieldRequestMin() # AddCustomFieldRequestMin |  (optional)
    max = backlog_client.AddCustomFieldRequestMax() # AddCustomFieldRequestMax |  (optional)
    initial_value = 56 # int | 初期値（数値属性） (optional)
    unit = 'unit_example' # str | 単位（数値属性） (optional)
    initial_value_type = 56 # int | 1:当日 2: 当日 + initialShift 3:指定日（日付属性） (optional)
    initial_date = 'initial_date_example' # str | 初期値 (yyyy-MM-dd)（日付属性） (optional)
    initial_shift = 56 # int | 差分日数（日付属性） (optional)
    items = ['items_example'] # List[str] | リスト項目（リスト属性） (optional)
    allow_input = True # bool | その他直接入力を許可（リスト属性） (optional)
    allow_add_item = True # bool | 項目の追加を許可（リスト属性） (optional)

    try:
        # カスタム属性の更新
        api_response = api_instance.update_custom_field(project_id_or_key, id, name=name, applicable_issue_types=applicable_issue_types, description=description, required=required, min=min, max=max, initial_value=initial_value, unit=unit, initial_value_type=initial_value_type, initial_date=initial_date, initial_shift=initial_shift, items=items, allow_input=allow_input, allow_add_item=allow_add_item)
        print("The response of DefaultApi->update_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カスタム属性のID | 
 **name** | **str**| カスタム属性の名前 | [optional] 
 **applicable_issue_types** | [**List[int]**](int.md)| カスタム属性を有効にする種別ID空の場合、すべての課題種別で有効 | [optional] 
 **description** | **str**| カスタム属性の説明 | [optional] 
 **required** | **bool**| 必須な属性とする場合はtrue | [optional] 
 **min** | [**AddCustomFieldRequestMin**](AddCustomFieldRequestMin.md)|  | [optional] 
 **max** | [**AddCustomFieldRequestMax**](AddCustomFieldRequestMax.md)|  | [optional] 
 **initial_value** | **int**| 初期値（数値属性） | [optional] 
 **unit** | **str**| 単位（数値属性） | [optional] 
 **initial_value_type** | **int**| 1:当日 2: 当日 + initialShift 3:指定日（日付属性） | [optional] 
 **initial_date** | **str**| 初期値 (yyyy-MM-dd)（日付属性） | [optional] 
 **initial_shift** | **int**| 差分日数（日付属性） | [optional] 
 **items** | [**List[str]**](str.md)| リスト項目（リスト属性） | [optional] 
 **allow_input** | **bool**| その他直接入力を許可（リスト属性） | [optional] 
 **allow_add_item** | **bool**| 項目の追加を許可（リスト属性） | [optional] 

### Return type

[**AddCustomField200Response**](AddCustomField200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_list_item**
> AddCustomFieldListItem200Response update_custom_field_list_item(project_id_or_key, id, item_id, name=name)

選択リストカスタム属性のリスト項目の更新

選択リスト形式のカスタム属性のリスト項目を更新します。 指定されたカスタム属性が選択リスト形式でない場合はエラーになります。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_custom_field_list_item200_response import AddCustomFieldListItem200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | カスタム属性のID
    item_id = 56 # int | リスト項目のID
    name = 'name_example' # str | リスト項目の名前 (optional)

    try:
        # 選択リストカスタム属性のリスト項目の更新
        api_response = api_instance.update_custom_field_list_item(project_id_or_key, id, item_id, name=name)
        print("The response of DefaultApi->update_custom_field_list_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_custom_field_list_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| カスタム属性のID | 
 **item_id** | **int**| リスト項目のID | 
 **name** | **str**| リスト項目の名前 | [optional] 

### Return type

[**AddCustomFieldListItem200Response**](AddCustomFieldListItem200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> GetGroups200ResponseInner update_group(group_id, name=name, members=members)

グループ情報の更新

2025年8月28日以降、順次利用できなくなります。（新しいタブで開く） チーム情報の更新をご利用ください。 グループの情報を更新します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    group_id = 56 # int | グループのID
    name = 'name_example' # str | グループ名 (optional)
    members = [56] # List[int] | グループに含めるユーザーID (optional)

    try:
        # グループ情報の更新
        api_response = api_instance.update_group(group_id, name=name, members=members)
        print("The response of DefaultApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| グループのID | 
 **name** | **str**| グループ名 | [optional] 
 **members** | [**List[int]**](int.md)| グループに含めるユーザーID | [optional] 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_issue**
> UpdateIssue200Response update_issue(issue_id_or_key, summary=summary, parent_issue_id=parent_issue_id, description=description, status_id=status_id, resolution_id=resolution_id, start_date=start_date, due_date=due_date, estimated_hours=estimated_hours, actual_hours=actual_hours, issue_type_id=issue_type_id, category_id=category_id, version_id=version_id, milestone_id=milestone_id, priority_id=priority_id, assignee_id=assignee_id, notified_user_id=notified_user_id, attachment_id=attachment_id, comment=comment)

課題情報の更新

課題の情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.update_issue200_response import UpdateIssue200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    summary = 'summary_example' # str | 課題の件名 (optional)
    parent_issue_id = 56 # int | 課題の親課題のID (optional)
    description = 'description_example' # str | 課題の詳細 (optional)
    status_id = 56 # int | 状態のID (optional)
    resolution_id = 56 # int | 完了理由のID (optional)
    start_date = 'start_date_example' # str | 課題の開始日 (yyyy-MM-dd) (optional)
    due_date = 'due_date_example' # str | 課題の期限日 (yyyy-MM-dd) (optional)
    estimated_hours = 3.4 # float | 課題の予定時間 (optional)
    actual_hours = 3.4 # float | 課題の実績時間 (optional)
    issue_type_id = 56 # int | 課題の種別のID (optional)
    category_id = [56] # List[int] | カテゴリーのID (optional)
    version_id = [56] # List[int] | 発生バージョンのID (optional)
    milestone_id = [56] # List[int] | マイルストーンのID (optional)
    priority_id = 56 # int | 課題の優先度のID (optional)
    assignee_id = 56 # int | 課題の担当者のID (optional)
    notified_user_id = [56] # List[int] | 課題の登録の通知を受け取るユーザーのID (optional)
    attachment_id = [56] # List[int] | 添付ファイルの送信APIが返すID (optional)
    comment = 'comment_example' # str | コメント (optional)

    try:
        # 課題情報の更新
        api_response = api_instance.update_issue(issue_id_or_key, summary=summary, parent_issue_id=parent_issue_id, description=description, status_id=status_id, resolution_id=resolution_id, start_date=start_date, due_date=due_date, estimated_hours=estimated_hours, actual_hours=actual_hours, issue_type_id=issue_type_id, category_id=category_id, version_id=version_id, milestone_id=milestone_id, priority_id=priority_id, assignee_id=assignee_id, notified_user_id=notified_user_id, attachment_id=attachment_id, comment=comment)
        print("The response of DefaultApi->update_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **summary** | **str**| 課題の件名 | [optional] 
 **parent_issue_id** | **int**| 課題の親課題のID | [optional] 
 **description** | **str**| 課題の詳細 | [optional] 
 **status_id** | **int**| 状態のID | [optional] 
 **resolution_id** | **int**| 完了理由のID | [optional] 
 **start_date** | **str**| 課題の開始日 (yyyy-MM-dd) | [optional] 
 **due_date** | **str**| 課題の期限日 (yyyy-MM-dd) | [optional] 
 **estimated_hours** | **float**| 課題の予定時間 | [optional] 
 **actual_hours** | **float**| 課題の実績時間 | [optional] 
 **issue_type_id** | **int**| 課題の種別のID | [optional] 
 **category_id** | [**List[int]**](int.md)| カテゴリーのID | [optional] 
 **version_id** | [**List[int]**](int.md)| 発生バージョンのID | [optional] 
 **milestone_id** | [**List[int]**](int.md)| マイルストーンのID | [optional] 
 **priority_id** | **int**| 課題の優先度のID | [optional] 
 **assignee_id** | **int**| 課題の担当者のID | [optional] 
 **notified_user_id** | [**List[int]**](int.md)| 課題の登録の通知を受け取るユーザーのID | [optional] 
 **attachment_id** | [**List[int]**](int.md)| 添付ファイルの送信APIが返すID | [optional] 
 **comment** | **str**| コメント | [optional] 

### Return type

[**UpdateIssue200Response**](UpdateIssue200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_issue_comment**
> GetIssueComments200ResponseInner update_issue_comment(issue_id_or_key, comment_id, content=content)

課題コメント情報の更新

課題コメントの情報を更新します。 認証ユーザー自身が登録したコメントのみ更新することが出来ます。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comments200_response_inner import GetIssueComments200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    issue_id_or_key = 'issue_id_or_key_example' # str | 課題のID または 課題キー
    comment_id = 56 # int | コメントのID
    content = 'content_example' # str | コメントの本文 (optional)

    try:
        # 課題コメント情報の更新
        api_response = api_instance.update_issue_comment(issue_id_or_key, comment_id, content=content)
        print("The response of DefaultApi->update_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id_or_key** | **str**| 課題のID または 課題キー | 
 **comment_id** | **int**| コメントのID | 
 **content** | **str**| コメントの本文 | [optional] 

### Return type

[**GetIssueComments200ResponseInner**](GetIssueComments200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_issue_type**
> GetIssueTypes200ResponseInner update_issue_type(project_id_or_key, id, name=name, color=color, template_summary=template_summary, template_description=template_description)

種別情報の更新

種別の情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_types200_response_inner import GetIssueTypes200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | 種別のID
    name = 'name_example' # str | 種別の名前 (optional)
    color = 'color_example' # str | 種別の背景色 (optional)
    template_summary = 'template_summary_example' # str | 課題テンプレートの件名 (optional)
    template_description = 'template_description_example' # str | 課題テンプレートの詳細 (optional)

    try:
        # 種別情報の更新
        api_response = api_instance.update_issue_type(project_id_or_key, id, name=name, color=color, template_summary=template_summary, template_description=template_description)
        print("The response of DefaultApi->update_issue_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_issue_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| 種別のID | 
 **name** | **str**| 種別の名前 | [optional] 
 **color** | **str**| 種別の背景色 | [optional] 
 **template_summary** | **str**| 課題テンプレートの件名 | [optional] 
 **template_description** | **str**| 課題テンプレートの詳細 | [optional] 

### Return type

[**GetIssueTypes200ResponseInner**](GetIssueTypes200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> AddProject201Response update_project(project_id_or_key, name=name, key=key, chart_enabled=chart_enabled, use_resolved_for_chart=use_resolved_for_chart, subtasking_enabled=subtasking_enabled, project_leader_can_edit_project_leader=project_leader_can_edit_project_leader, use_wiki=use_wiki, use_file_sharing=use_file_sharing, use_wiki_tree_view=use_wiki_tree_view, use_subversion=use_subversion, use_git=use_git, use_original_image_size_at_wiki=use_original_image_size_at_wiki, text_formatting_rule=text_formatting_rule, archived=archived, use_dev_attributes=use_dev_attributes)

プロジェクト情報の更新

プロジェクトの情報を更新します。  実行可能な権限: - 管理者 - プロジェクト管理者 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_project201_response import AddProject201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    name = 'name_example' # str | プロジェクト名 (optional)
    key = 'key_example' # str | プロジェクトキー (optional)
    chart_enabled = True # bool | チャートを使用するかどうか (optional)
    use_resolved_for_chart = True # bool | 「処理済み」以降を「完了」とみなすどうか (optional)
    subtasking_enabled = True # bool | 親子課題を使用するかどうか (optional)
    project_leader_can_edit_project_leader = True # bool | プロジェクト管理者も他のプロジェクト管理者を指定可能にする (optional)
    use_wiki = True # bool | Wikiを使用するかどうか (optional)
    use_file_sharing = True # bool | 共有ファイルを使用するかどうか (optional)
    use_wiki_tree_view = True # bool | Wikiツリー表示を有効にするかどうか (optional)
    use_subversion = True # bool | Subversionを使用するかどうか (optional)
    use_git = True # bool | Gitを使用するかどうか (optional)
    use_original_image_size_at_wiki = True # bool | Wikiの画像をオリジナルのサイズで表示するかどうか (optional)
    text_formatting_rule = 'text_formatting_rule_example' # str | テキスト整形のルール backlog または markdown (optional)
    archived = True # bool | プロジェクトの一覧に表示するかどうか (optional)
    use_dev_attributes = True # bool | 優先度、マイルストーン、発生バージョンを使用するかどうか (optional)

    try:
        # プロジェクト情報の更新
        api_response = api_instance.update_project(project_id_or_key, name=name, key=key, chart_enabled=chart_enabled, use_resolved_for_chart=use_resolved_for_chart, subtasking_enabled=subtasking_enabled, project_leader_can_edit_project_leader=project_leader_can_edit_project_leader, use_wiki=use_wiki, use_file_sharing=use_file_sharing, use_wiki_tree_view=use_wiki_tree_view, use_subversion=use_subversion, use_git=use_git, use_original_image_size_at_wiki=use_original_image_size_at_wiki, text_formatting_rule=text_formatting_rule, archived=archived, use_dev_attributes=use_dev_attributes)
        print("The response of DefaultApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **name** | **str**| プロジェクト名 | [optional] 
 **key** | **str**| プロジェクトキー | [optional] 
 **chart_enabled** | **bool**| チャートを使用するかどうか | [optional] 
 **use_resolved_for_chart** | **bool**| 「処理済み」以降を「完了」とみなすどうか | [optional] 
 **subtasking_enabled** | **bool**| 親子課題を使用するかどうか | [optional] 
 **project_leader_can_edit_project_leader** | **bool**| プロジェクト管理者も他のプロジェクト管理者を指定可能にする | [optional] 
 **use_wiki** | **bool**| Wikiを使用するかどうか | [optional] 
 **use_file_sharing** | **bool**| 共有ファイルを使用するかどうか | [optional] 
 **use_wiki_tree_view** | **bool**| Wikiツリー表示を有効にするかどうか | [optional] 
 **use_subversion** | **bool**| Subversionを使用するかどうか | [optional] 
 **use_git** | **bool**| Gitを使用するかどうか | [optional] 
 **use_original_image_size_at_wiki** | **bool**| Wikiの画像をオリジナルのサイズで表示するかどうか | [optional] 
 **text_formatting_rule** | **str**| テキスト整形のルール backlog または markdown | [optional] 
 **archived** | **bool**| プロジェクトの一覧に表示するかどうか | [optional] 
 **use_dev_attributes** | **bool**| 優先度、マイルストーン、発生バージョンを使用するかどうか | [optional] 

### Return type

[**AddProject201Response**](AddProject201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_status**
> GetIssues200ResponseInnerIssueType update_project_status(project_id_or_key, id, name=name, color=color)

状態情報の更新

追加した状態の情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_issue_type import GetIssues200ResponseInnerIssueType
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | 状態のID
    name = 'name_example' # str | 状態の名前 (optional)
    color = 'color_example' # str | 状態の背景色 (optional)

    try:
        # 状態情報の更新
        api_response = api_instance.update_project_status(project_id_or_key, id, name=name, color=color)
        print("The response of DefaultApi->update_project_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| 状態のID | 
 **name** | **str**| 状態の名前 | [optional] 
 **color** | **str**| 状態の背景色 | [optional] 

### Return type

[**GetIssues200ResponseInnerIssueType**](GetIssues200ResponseInnerIssueType.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pull_request**
> UpdatePullRequest200Response update_pull_request(project_id_or_key, repo_id_or_name, number, summary=summary, description=description, issue_id=issue_id, assignee_id=assignee_id, notified_user_id=notified_user_id, comment=comment)

プルリクエストの更新

プルリクエストを更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.update_pull_request200_response import UpdatePullRequest200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号
    summary = 'summary_example' # str | プルリクエストの件名 (optional)
    description = 'description_example' # str | プルリクエストの詳細 (optional)
    issue_id = 56 # int | 関連課題のID (optional)
    assignee_id = 56 # int | プルリクエストの担当者のID (optional)
    notified_user_id = [56] # List[int] | プルリクエストの登録の通知を受け取るユーザーのID (optional)
    comment = 'comment_example' # str | コメント (optional)

    try:
        # プルリクエストの更新
        api_response = api_instance.update_pull_request(project_id_or_key, repo_id_or_name, number, summary=summary, description=description, issue_id=issue_id, assignee_id=assignee_id, notified_user_id=notified_user_id, comment=comment)
        print("The response of DefaultApi->update_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 
 **summary** | **str**| プルリクエストの件名 | [optional] 
 **description** | **str**| プルリクエストの詳細 | [optional] 
 **issue_id** | **int**| 関連課題のID | [optional] 
 **assignee_id** | **int**| プルリクエストの担当者のID | [optional] 
 **notified_user_id** | [**List[int]**](int.md)| プルリクエストの登録の通知を受け取るユーザーのID | [optional] 
 **comment** | **str**| コメント | [optional] 

### Return type

[**UpdatePullRequest200Response**](UpdatePullRequest200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pull_request_comment**
> GetPullRequestComments200ResponseInner update_pull_request_comment(project_id_or_key, repo_id_or_name, number, comment_id, content=content)

プルリクエストコメント情報の更新

プルリクエストコメントの情報を更新します。 認証ユーザー自身が登録したコメントのみ更新することが出来ます。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_pull_request_comments200_response_inner import GetPullRequestComments200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    repo_id_or_name = 'repo_id_or_name_example' # str | リポジトリのID または リポジトリ名
    number = 56 # int | プルリクエストの番号
    comment_id = 56 # int | コメントのID
    content = 'content_example' # str | コメントの本文 (optional)

    try:
        # プルリクエストコメント情報の更新
        api_response = api_instance.update_pull_request_comment(project_id_or_key, repo_id_or_name, number, comment_id, content=content)
        print("The response of DefaultApi->update_pull_request_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_pull_request_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **repo_id_or_name** | **str**| リポジトリのID または リポジトリ名 | 
 **number** | **int**| プルリクエストの番号 | 
 **comment_id** | **int**| コメントのID | 
 **content** | **str**| コメントの本文 | [optional] 

### Return type

[**GetPullRequestComments200ResponseInner**](GetPullRequestComments200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_space_notification**
> GetSpaceNotification200Response update_space_notification()

スペースのお知らせの更新

スペースのお知らせの情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_space_notification200_response import GetSpaceNotification200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)

    try:
        # スペースのお知らせの更新
        api_response = api_instance.update_space_notification()
        print("The response of DefaultApi->update_space_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_space_notification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSpaceNotification200Response**](GetSpaceNotification200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_display_order**
> List[GetProjectStatuses200ResponseInner] update_status_display_order(project_id_or_key, status_id=status_id)

状態の並び替え

状態の表示順を変更します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_project_statuses200_response_inner import GetProjectStatuses200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    status_id = [56] # List[int] | 表示順に並べた、状態のIDのリスト。そのプロジェクトで使える全ての状態を渡してください。表示順には以下の制限があります未対応は先頭にあること完了は末尾にあること処理中は処理済みよりも前にあること (optional)

    try:
        # 状態の並び替え
        api_response = api_instance.update_status_display_order(project_id_or_key, status_id=status_id)
        print("The response of DefaultApi->update_status_display_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_status_display_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **status_id** | [**List[int]**](int.md)| 表示順に並べた、状態のIDのリスト。そのプロジェクトで使える全ての状態を渡してください。表示順には以下の制限があります未対応は先頭にあること完了は末尾にあること処理中は処理済みよりも前にあること | [optional] 

### Return type

[**List[GetProjectStatuses200ResponseInner]**](GetProjectStatuses200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> GetGroups200ResponseInner update_team(team_id, name=name, members=members)

チーム情報の更新

チームの情報を更新します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_groups200_response_inner import GetGroups200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    team_id = 56 # int | チームのID
    name = 'name_example' # str | チーム名 (optional)
    members = [56] # List[int] | チームに含めるユーザーID (optional)

    try:
        # チーム情報の更新
        api_response = api_instance.update_team(team_id, name=name, members=members)
        print("The response of DefaultApi->update_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| チームのID | 
 **name** | **str**| チーム名 | [optional] 
 **members** | [**List[int]**](int.md)| チームに含めるユーザーID | [optional] 

### Return type

[**GetGroups200ResponseInner**](GetGroups200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> GetIssueCommentNotifications200ResponseInnerUser update_user(user_id, password=password, name=name, mail_address=mail_address, role_type=role_type)

ユーザーの更新

ユーザーの情報を更新します。 新プランのスペースではこのAPIを利用できません。 

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issue_comment_notifications200_response_inner_user import GetIssueCommentNotifications200ResponseInnerUser
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    user_id = 56 # int | 更新するユーザーのID
    password = 'password_example' # str | パスワード (optional)
    name = 'name_example' # str | ハンドルネーム (optional)
    mail_address = 'mail_address_example' # str | メールアドレス (optional)
    role_type = 56 # int | 管理者(1) 一般ユーザー(2) レポーター(3) ビューワー(4) ゲストレポーター(5) ゲストビューワー(6) (optional)

    try:
        # ユーザーの更新
        api_response = api_instance.update_user(user_id, password=password, name=name, mail_address=mail_address, role_type=role_type)
        print("The response of DefaultApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| 更新するユーザーのID | 
 **password** | **str**| パスワード | [optional] 
 **name** | **str**| ハンドルネーム | [optional] 
 **mail_address** | **str**| メールアドレス | [optional] 
 **role_type** | **int**| 管理者(1) 一般ユーザー(2) レポーター(3) ビューワー(4) ゲストレポーター(5) ゲストビューワー(6) | [optional] 

### Return type

[**GetIssueCommentNotifications200ResponseInnerUser**](GetIssueCommentNotifications200ResponseInnerUser.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  * Location - https://xx.backlog.jp/user/eguchi <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> GetIssues200ResponseInnerMilestoneInner update_version(project_id_or_key, id, name, description=description, start_date=start_date, release_due_date=release_due_date, archived=archived)

バージョン(マイルストーン)情報の更新

バージョン(マイルストーン)の情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_issues200_response_inner_milestone_inner import GetIssues200ResponseInnerMilestoneInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    id = 56 # int | バージョンのID
    name = 'name_example' # str | バージョンの名前
    description = 'description_example' # str | バージョンの説明 (optional)
    start_date = 'start_date_example' # str | バージョンの開始日 (yyyy-MM-dd) (optional)
    release_due_date = 'release_due_date_example' # str | バージョンのリリース予定日 (yyyy-MM-dd) (optional)
    archived = True # bool | プロジェクトホームに表示しない場合はtrue (optional)

    try:
        # バージョン(マイルストーン)情報の更新
        api_response = api_instance.update_version(project_id_or_key, id, name, description=description, start_date=start_date, release_due_date=release_due_date, archived=archived)
        print("The response of DefaultApi->update_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **id** | **int**| バージョンのID | 
 **name** | **str**| バージョンの名前 | 
 **description** | **str**| バージョンの説明 | [optional] 
 **start_date** | **str**| バージョンの開始日 (yyyy-MM-dd) | [optional] 
 **release_due_date** | **str**| バージョンのリリース予定日 (yyyy-MM-dd) | [optional] 
 **archived** | **bool**| プロジェクトホームに表示しない場合はtrue | [optional] 

### Return type

[**GetIssues200ResponseInnerMilestoneInner**](GetIssues200ResponseInnerMilestoneInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_watching**
> AddWatching201Response update_watching(watching_id, note=note)

ウォッチの更新

ウォッチを更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_watching201_response import AddWatching201Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    watching_id = 56 # int | ウォッチのID
    note = 'note_example' # str | メモ (optional)

    try:
        # ウォッチの更新
        api_response = api_instance.update_watching(watching_id, note=note)
        print("The response of DefaultApi->update_watching:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_watching: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watching_id** | **int**| ウォッチのID | 
 **note** | **str**| メモ | [optional] 

### Return type

[**AddWatching201Response**](AddWatching201Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> GetWebhooks200ResponseInner update_webhook(project_id_or_key, webhook_id, name=name, description=description, hook_url=hook_url, all_event=all_event, activity_type_ids=activity_type_ids)

Webhookの更新

Webhookの情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.get_webhooks200_response_inner import GetWebhooks200ResponseInner
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    project_id_or_key = 'project_id_or_key_example' # str | プロジェクトのID または プロジェクトキー
    webhook_id = 'webhook_id_example' # str | WebhookのID
    name = 'name_example' # str | 名前 (optional)
    description = 'description_example' # str | 詳細 (optional)
    hook_url = 'hook_url_example' # str | hook URL (optional)
    all_event = True # bool | 全てのイベントを通知 (optional)
    activity_type_ids = [56] # List[int] | 通知するイベントのID (optional)

    try:
        # Webhookの更新
        api_response = api_instance.update_webhook(project_id_or_key, webhook_id, name=name, description=description, hook_url=hook_url, all_event=all_event, activity_type_ids=activity_type_ids)
        print("The response of DefaultApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id_or_key** | **str**| プロジェクトのID または プロジェクトキー | 
 **webhook_id** | **str**| WebhookのID | 
 **name** | **str**| 名前 | [optional] 
 **description** | **str**| 詳細 | [optional] 
 **hook_url** | **str**| hook URL | [optional] 
 **all_event** | **bool**| 全てのイベントを通知 | [optional] 
 **activity_type_ids** | [**List[int]**](int.md)| 通知するイベントのID | [optional] 

### Return type

[**GetWebhooks200ResponseInner**](GetWebhooks200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wiki**
> AddRecentlyViewedWiki200Response update_wiki(wiki_id, name=name, content=content, mail_notify=mail_notify)

Wikiページ情報の更新

Wikiページの情報を更新します。

### Example

* Api Key Authentication (apiKey):

```python
import backlog_client
from backlog_client.models.add_recently_viewed_wiki200_response import AddRecentlyViewedWiki200Response
from backlog_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = backlog_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with backlog_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = backlog_client.DefaultApi(api_client)
    wiki_id = 56 # int | WikiページのID
    name = 'name_example' # str | ページ名 (optional)
    content = 'content_example' # str | ページの内容 (optional)
    mail_notify = True # bool | ページの更新をメールで通知する場合はtrue (optional)

    try:
        # Wikiページ情報の更新
        api_response = api_instance.update_wiki(wiki_id, name=name, content=content, mail_notify=mail_notify)
        print("The response of DefaultApi->update_wiki:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_wiki: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_id** | **int**| WikiページのID | 
 **name** | **str**| ページ名 | [optional] 
 **content** | **str**| ページの内容 | [optional] 
 **mail_notify** | **bool**| ページの更新をメールで通知する場合はtrue | [optional] 

### Return type

[**AddRecentlyViewedWiki200Response**](AddRecentlyViewedWiki200Response.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功時のレスポンス |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

