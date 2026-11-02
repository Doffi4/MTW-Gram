# Инвентарь экранов из исходников

Всего: **441** контроллеров в 76 пакетах. Сгенерировано `recon/tools/screens_inventory.py`. `title` — ключ локализации заголовка (значения в `Telegram-Mac/en.lproj/Localizable.strings`).


## AboutFeatureUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AboutFeatureModalController` | func->InputDataModalController | aboutCocoonTitle | COCOON |  | `packages/AboutFeatureUI/Sources/AboutFeatureUI/AboutFeatureModalController.swift:410` |

## AddTonBalanceUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AddTonBalanceController` | func->InputDataModalController | fragmentTonAddFundsTitle | Add funds |  | `packages/AddTonBalanceUI/Sources/AddTonBalanceUI/AddTonBalanceController.swift:55` |

## AffiliateUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `Affiliate_LinkPreview` | func->InputDataModalController | affiliateProgramToastLinkCopiedTitle | Link copied to clipboard |  | `packages/AffiliateUI/Sources/AffiliateUI/Affiliate_LinkPreview.swift:367` |
| `Affiliate_PeerController` | func->InputDataController | affiliateProgramsExistingPrograms | Existing Affiliate Programs |  | `packages/AffiliateUI/Sources/AffiliateUI/Affiliate_PeerController.swift:500` |
| `Affiliate_ProgramPreview` | func->InputDataModalController |  |  |  | `packages/AffiliateUI/Sources/AffiliateUI/Affiliate_ProgramPreview.swift:362` |
| `Affiliate_StartController` | func->InputDataController | affiliateSetupToastTerminatedTitle | Affiliate Program Ended |  | `packages/AffiliateUI/Sources/AffiliateUI/Affiliate_StartController.swift:171` |

## AlertsUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ModalAlertController` | func->InputDataModalController |  |  |  | `packages/AlertsUI/Sources/AlertsUI/ModalAlertController.swift:902` |

## AudioPlayerUI (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AudioPlayerUIPlaceholderInstantVideoPIP` | class:ViewController |  |  |  | `packages/AudioPlayerUI/Sources/AudioPlayerUI/AudioPlayerUIHooks.swift:80` |
| `PlayerListController` | class:ModalViewController |  |  |  | `packages/AudioPlayerUI/Sources/AudioPlayerUI/PlayerListController.swift:830` |

## AuthUI (14)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AuthController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/AuthController.swift:252` |
| `AuthPlaceholderUpdateTabController` | class:ViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/AuthUIHooks.swift:59` |
| `Auth_AwaitingResetController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_AwaitingReset.swift:218` |
| `Auth_CodeEntryController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_CodeEntry.swift:394` |
| `Auth_EmailController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_Email.swift:198` |
| `Auth_EmailSetupController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_EmailSetup.swift:239` |
| `Auth_Loading` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_Loading.swift:35` |
| `Auth_PasswordEntryController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_PasswordEntry.swift:320` |
| `Auth_PhoneNumberController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_PhoneNumber.swift:293` |
| `Auth_SignupController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_Signup.swift:354` |
| `Auth_TokenController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_Token.swift:284` |
| `Auth_WordController` | class:GenericViewController |  |  |  | `packages/AuthUI/Sources/AuthUI/Auth_Word.swift:476` |
| `LoginWidgetConfirmationController` | func->InputDataModalController |  |  |  | `packages/AuthUI/Sources/AuthUI/LoginWidgetConfirmation.swift:792` |
| `TermsModalController` | class:ModalViewController | termsOfServiceAccept | Agree & Continue |  | `packages/AuthUI/Sources/AuthUI/TermsModalController.swift:59` |

## AvatarEditorUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AvatarConstructorController` | class:ModalViewController | customAvatarTitleEmoji | Emoji |  | `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:962` |
| `EditImageModalController` | class:ModalViewController |  |  |  | `packages/AvatarEditorUI/Sources/AvatarEditorUI/EditImageModalController.swift:754` |
| `VideoAvatarModalController` | class:ModalViewController |  |  |  | `packages/AvatarEditorUI/Sources/AvatarEditorUI/VideoAvatarModalController.swift:305` |

## BoostUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `BoostChannelModalController` | func->InputDataModalController |  |  |  | `packages/BoostUI/Sources/BoostUI/BoostChannelModalController.swift:1040` |
| `BoostReassignController` | func->InputDataModalController | boostReassignTitle | Reassign Boosts |  | `packages/BoostUI/Sources/BoostUI/BoostReassignController.swift:187` |
| `GiftLinkModalController` | func->InputDataModalController | giftLinkTitle | Gift Link |  | `packages/BoostUI/Sources/BoostUI/GiftLinkModalController.swift:226` |
| `GiveawayModalController` | func->InputDataModalController | giveawayStarChooseRandomly | Choose Randomly |  | `packages/BoostUI/Sources/BoostUI/GiveawayModalController.swift:782` |

## BusinessUI (11)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `BusinessAddQuickReply` | func->InputDataModalController | businessQuickReplyAddInfo | Add a shortcut for your quick reply. |  | `packages/BusinessUI/Sources/BusinessUI/BusinessQuickReplyController.swift:695` |
| `BusinessChatbotController` | func->InputDataController | businessChatBotManageMessages | Manage Messages |  | `packages/BusinessUI/Sources/BusinessUI/BusinessChatbotController.swift:663` |
| `BusinessHoursController` | func->InputDataController | businessHoursTitle | Business Hours |  | `packages/BusinessUI/Sources/BusinessUI/BusinessHoursController.swift:420` |
| `BusinessIntroController` | func->InputDataController | businessIntroTitle | Start Page |  | `packages/BusinessUI/Sources/BusinessUI/BusinessIntroController.swift:267` |
| `BusinessLinkRenameController` | func->InputDataModalController | businessLinksNameTitle | Link Name |  | `packages/BusinessUI/Sources/BusinessUI/BusinessLinksController.swift:483` |
| `BusinessLinksController` | func->InputDataController | businessLinksTitle | Links to Chat |  | `packages/BusinessUI/Sources/BusinessUI/BusinessLinksController.swift:319` |
| `BusinessLocationController` | func->InputDataController | businessLocationTitle | Location |  | `packages/BusinessUI/Sources/BusinessUI/BusinessLocationController.swift:253` |
| `BusinessMessageController` | func->InputDataController | businessScheduleStart | Schedule Start |  | `packages/BusinessUI/Sources/BusinessUI/BusinessMessageController.swift:659` |
| `BusinessQuickReplyController` | func->InputDataController | businessQuickReplyTitle | Quick Replies |  | `packages/BusinessUI/Sources/BusinessUI/BusinessQuickReplyController.swift:550` |
| `BusinessTimezonesController` | func->InputDataModalController | businessHoursTimezone | Timezone |  | `packages/BusinessUI/Sources/BusinessUI/BusinessTimezonesController.swift:87` |
| `BusinessdayHoursController` | func->InputDataController |  |  |  | `packages/BusinessUI/Sources/BusinessUI/BusinessHoursController.swift:626` |

## CalendarUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `CalendarController` | class:GenericViewController |  |  |  | `packages/CalendarUI/Sources/CalendarUI/CalendarController.swift:17` |
| `CalendarMonthController` | class:GenericViewController |  |  |  | `packages/CalendarUI/Sources/CalendarUI/CalendarMonthController.swift:337` |
| `CalendarNavigation` | class:NavigationViewController |  |  |  | `packages/CalendarUI/Sources/CalendarUI/CalendarController.swift:11` |
| `ChatCalendarController` | func->ViewController |  |  |  | `packages/CalendarUI/Sources/CalendarUI/ChatCalendarController.swift:111` |

## CallsUI (10)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `CallFeedbackController` | func->ModalViewController | callFeedbackTitle | Call Feedback |  | `packages/CallsUI/Sources/CallsUI/CallFeedbackController.swift:180` |
| `CallRatingModalViewController` | class:ModalViewController | callRatingModalNotNow | Not Now |  | `packages/CallsUI/Sources/CallsUI/CallRatingModalViewController.swift:95` |
| `CallSettingsController` | func->InputDataController | callSettingsTitle | Call Settings |  | `packages/CallsUI/Sources/CallsUI/CallSettingsController.swift:153` |
| `CallSettingsModalController` | func->InputDataModalController |  |  |  | `packages/CallsUI/Sources/CallsUI/CallSettingsModalController.swift:22` |
| `DesktopCaptureListUI` | class:GenericViewController |  |  |  | `packages/CallsUI/Sources/CallsUI/DesktopCaptureListUI.swift:130` |
| `GroupCallDisplayAsController` | func->InputDataModalController | displayMeAsNewTitle | New Video Chat |  | `packages/CallsUI/Sources/CallsUI/GroupCallDisplayAsController.swift:252` |
| `GroupCallInviteLinkController` | func->InputDataModalController | modalCopyLink | Copy Link |  | `packages/CallsUI/Sources/CallsUI/GroupCallInviteLinkController.swift:437` |
| `JoinGroupCallController` | func->InputDataModalController | groupCallJoinTitle | Join Group Call |  | `packages/CallsUI/Sources/CallsUI/JoinGroupCallController.swift:244` |
| `JoinVoiceChatAlertController` | func->InputDataModalController | chatVoiceChatJoinLinkTitle | Video Chat |  | `packages/CallsUI/Sources/CallsUI/JoinVoiceChatAlertController.swift:51` |
| `RecentCallsViewController` | class:TelegramGenericViewController |  |  |  | `packages/CallsUI/Sources/CallsUI/RecentCallsViewController.swift:357` |

## ChangePhoneNumberUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PhoneNumberCodeConfirmController` | class:GenericViewController |  |  |  | `packages/ChangePhoneNumberUI/Sources/ChangePhoneNumberUI/PhoneNumberConfirmCodeController.swift:124` |
| `PhoneNumberConfirmController` | class:GenericViewController |  |  |  | `packages/ChangePhoneNumberUI/Sources/ChangePhoneNumberUI/PhoneNumberConfirmController.swift:87` |
| `PhoneNumberIntroController` | class:GenericViewController |  |  |  | `packages/ChangePhoneNumberUI/Sources/ChangePhoneNumberUI/PhoneNumberIntroController.swift:84` |

## ChannelAdminUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChannelAdminsViewController` | class:EditableViewController | adminsAddAdmin | Add Admin |  | `packages/ChannelAdminUI/Sources/ChannelAdminUI/ChannelAdminsViewController.swift:410` |
| `ChannelBotAdminController` | func->InputDataModalController | channelAddBotTitle | Add Bot |  | `packages/ChannelAdminUI/Sources/ChannelAdminUI/ChannelBotAdminController.swift:388` |
| `ChannelEventFilterModalController` | func->InputDataModalController | channelAdminsRecentActions | Recent Actions |  | `packages/ChannelAdminUI/Sources/ChannelAdminUI/ChannelEventFilterModalController.swift:457` |
| `ChannelEventLogController` | class:TelegramGenericViewController |  |  |  | `packages/ChannelAdminUI/Sources/ChannelAdminUI/ChannelEventLogController.swift:384` |

## ChannelSettingsUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `DiscussionSetModalController` | class:ModalViewController | discussionSetModalOK | Link Group |  | `packages/ChannelSettingsUI/Sources/ChannelSettingsUI/DiscussionSetModalController.swift:75` |
| `GroupStickerSetController` | class:TableViewController |  |  |  | `packages/ChannelSettingsUI/Sources/ChannelSettingsUI/GroupStickerSetController.swift:278` |
| `ReactionsSettingsController` | func->InputDataController | reactionSettingsQuickTitle | Quick Reaction |  | `packages/ChannelSettingsUI/Sources/ChannelSettingsUI/ReactionsSettingsController.swift:164` |
| `SuggestPostController` | func->InputDataController | channelMessagesTitle | Direct Messages |  | `packages/ChannelSettingsUI/Sources/ChannelSettingsUI/SuggestPostController.swift:101` |

## ChatExportUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChatExportController` | func->InputDataModalController |  |  |  | `packages/ChatExportUI/Sources/ChatExportUI/ChatExportController.swift:685` |
| `FullExportController` | func->InputDataModalController |  |  |  | `packages/ChatExportUI/Sources/ChatExportUI/ChatExportController.swift:1484` |
| `chatExportProgressModal` | func->InputDataModalController |  |  |  | `packages/ChatExportUI/Sources/ChatExportUI/ChatExportController.swift:423` |
| `fullExportProgressModal` | func->InputDataModalController |  |  |  | `packages/ChatExportUI/Sources/ChatExportUI/ChatExportController.swift:1212` |

## ChatListUI (10)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AddContactModalController` | func->InputDataModalController | contactsAddContact | Add Contact |  | `packages/ChatListUI/Sources/ChatListUI/AddContactModalController.swift:121` |
| `ChatListController` | class:PeersListController | newSessionReviewAcceptTitle | New Login Allowed |  | `packages/ChatListUI/Sources/ChatListUI/ChatListController.swift:701` |
| `ChatPreviewModalController` | class:ModalController |  |  |  | `packages/ChatListUI/Sources/ChatListUI/ChatListRowItem.swift:2700` |
| `CommunityListController` | class:PeersListController | communityListDefaultTitle | Community |  | `packages/ChatListUI/Sources/ChatListUI/CommunityListController.swift:262` |
| `ContactsController` | class:PeersListController |  |  |  | `packages/ChatListUI/Sources/ChatListUI/ContactsController.swift:304` |
| `PeersListController` | class:TelegramGenericViewController | chatForwardActionHeader | Forward Messages |  | `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:2236` |
| `SavedPeersController` | func->InputDataController |  |  |  | `packages/ChatListUI/Sources/ChatListUI/SavedPeersController.swift:137` |
| `SearchController` | class:GenericViewController |  |  |  | `packages/ChatListUI/Sources/ChatListUI/SearchController.swift:812` |
| `SearchTabsController` | class:GenericViewController |  |  |  | `packages/ChatListUI/Sources/ChatListUI/SearchTabsController.swift:43` |
| `searchSiblingController` | func->ViewController |  |  |  | `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3172` |

## ChatUI (32)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChatAdditionController` | class:ChatController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatAdditionController.swift:11` |
| `ChatController` | class:TelegramGenericViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatController.swift:2440` |
| `ChatScheduleController` | class:ChatController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatScheduleController.swift:13` |
| `ChatSwitchInlineController` | class:ChatController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatSwitchInlineController.swift:16` |
| `ChatThemeSelectorController` | class:TelegramGenericViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatThemeSelectorController.swift:382` |
| `DeclineSuggestPostModalController` | func->InputDataModalController | declineSuggestPostTitle | Reject Suggested Post |  | `packages/ChatUI/Sources/ChatUI/DeclineSuggestPostModalController.swift:65` |
| `DeleteGroupMessagesController` | func->InputDataModalController | supergroupDeleteRestrictionProceed | Done |  | `packages/ChatUI/Sources/ChatUI/DeleteGroupMessagesController.swift:591` |
| `DiceRollController` | func->InputDataModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/DiceRollController.swift:1188` |
| `EditPostSuggestionController` | func->InputDataModalController | editPostSuggestionDateTitle | Select Date |  | `packages/ChatUI/Sources/ChatUI/EditPostSuggestionController.swift:601` |
| `FactCheckController` | func->InputDataModalController | factCheckTitle | Fact Check |  | `packages/ChatUI/Sources/ChatUI/FactCheckController.swift:58` |
| `InputContextViewController` | class:GenericViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:334` |
| `InstantVideoPIP` | class:GenericViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:53` |
| `NewContactController` | func->InputDataModalController | newContactTitle | New Contact |  | `packages/ChatUI/Sources/ChatUI/NewContactController.swift:92` |
| `RichEditorModalController` | class:InputDataModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/RichTextEditorWindowController.swift:2521` |
| `RichTextAiComposeController` | func->InputDataModalController | richTextAiComposeTitle | Create with AI |  | `packages/ChatUI/Sources/ChatUI/RichTextAiComposeController.swift:164` |
| `RichTextEditorController` | func->InputDataModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/RichTextEditorWindowController.swift:293` |
| `RichTextLatexModalController` | func->InputDataModalController | richTextEditorFormula | Formula |  | `packages/ChatUI/Sources/ChatUI/RichTextEditorWindowController.swift:2140` |
| `SingleTimeMediaViewer` | class:ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:433` |
| `VCardModalController` | func->InputDataModalController | modalOK | OK |  | `packages/ChatUI/Sources/ChatUI/VCardModalController.swift:143` |
| `Wrap` | class:ModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3229` |
| `chatDateSelector` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatNavigationHooks.swift:361` |
| `composerEditorController` | func->InputDataModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/RichTextEditorWindowController.swift:164` |
| `makeChannelParticipantControllerObserved` | func->InputDataModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatHistoryUIHooks.swift:265` |
| `makeEmojiPickerObserved` | func->ViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatInputUIHooks.swift:106` |
| `makeForwardMessagesShareModalObserved` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatUIHooks.swift:58` |
| `makePeerMediaControllerObserved` | func->ViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatUIHooks.swift:87` |
| `makeRichTranslateModalObserved` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatInputUIHooks.swift:91` |
| `makeShareMessagesModalObserved` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatHistoryUIHooks.swift:241` |
| `makeStickerPackPreviewObserved` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatMediaUIHooks.swift:26` |
| `makeTranslateModalObserved` | func->InputDataModalController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatHistoryUIHooks.swift:284` |
| `makeTranslateModalObserved` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatInputUIHooks.swift:75` |
| `makeWalletSendControllerObserved` | func->ModalViewController |  |  |  | `packages/ChatUI/Sources/ChatUI/ChatInputUIHooks.swift:44` |

## CommunityUI (9)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `CommunitiesController` | func->InputDataController | communitiesNewCommunity | New Community |  | `packages/CommunityUI/Sources/CommunityUI/CommunitiesController.swift:101` |
| `CommunityAddController` | func->InputDataModalController | communityAddTitle | Add Chat |  | `packages/CommunityUI/Sources/CommunityUI/CommunityAddController.swift:89` |
| `CommunityAdminController` | func->InputDataModalController | communityAdminAddAdmin | Add Admin |  | `packages/CommunityUI/Sources/CommunityUI/CommunityAdminController.swift:100` |
| `CommunityAdminsController` | func->InputDataController | communityAdminsTitle | Administrators |  | `packages/CommunityUI/Sources/CommunityUI/CommunityAdminsController.swift:112` |
| `CommunityCreateController` | func->InputDataModalController | communitiesNewCommunity | New Community |  | `packages/CommunityUI/Sources/CommunityUI/CommunitiesController.swift:227` |
| `CommunityEditController` | func->InputDataController | communityEditTitle | Edit Community |  | `packages/CommunityUI/Sources/CommunityUI/CommunityEditController.swift:251` |
| `CommunityPrivateChatController` | func->InputDataModalController | communityGroup | Group |  | `packages/CommunityUI/Sources/CommunityUI/CommunityModals.swift:105` |
| `CommunityRequestsController` | func->InputDataModalController | communityRequestsPendingRequests | Pending Requests |  | `packages/CommunityUI/Sources/CommunityUI/CommunityRequestsController.swift:139` |
| `CommunityViewController` | func->InputDataModalController | communityViewTitle | Community |  | `packages/CommunityUI/Sources/CommunityUI/CommunityViewController.swift:529` |

## ComposeUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ComposePlaceholderChannelVisibilityController` | class:ViewController |  |  |  | `packages/ComposeUI/Sources/ComposeUI/ComposeUIHooks.swift:56` |
| `CreateBotModalController` | func->InputDataModalController | createBotCreate | Create |  | `packages/ComposeUI/Sources/ComposeUI/CreateBotModalController.swift:346` |
| `CreateChannelController` | func->InputDataController | channelNewChannel | New Channel |  | `packages/ComposeUI/Sources/ComposeUI/CreateChannelController.swift:172` |

## DataUsageUI (7)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `DataAndStorageViewController` | class:TableViewController |  |  |  | `packages/DataUsageUI/Sources/DataUsageUI/DataAndStorageViewController.swift:519` |
| `DataStorageExceptions` | func->InputDataController |  |  |  | `packages/DataUsageUI/Sources/DataUsageUI/DataStorageExceptions.swift:171` |
| `DownloadSettingsViewController` | class:TableViewController |  |  |  | `packages/DataUsageUI/Sources/DataUsageUI/DownloadSettingsViewController.swift:168` |
| `StorageUsageBlockController` | class:TelegramGenericViewController |  |  |  | `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockController.swift:375` |
| `StorageUsageController` | class:EditableViewController |  |  |  | `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageController.swift:1055` |
| `controller` | func->ViewController |  |  |  | `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockController.swift:593` |
| `networkUsageStatsController` | func->ViewController | networkUsageNetworkUsage | Network Usage |  | `packages/DataUsageUI/Sources/DataUsageUI/NetworkUsageStatsController.swift:304` |

## DateSelectorUI (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `DateSelectorModalController` | class:ModalViewController |  |  |  | `packages/DateSelectorUI/Sources/DateSelectorUI/DateSelectorModalController.swift:367` |
| `TimeRangeSelectorController` | func->InputDataModalController |  |  |  | `packages/DateSelectorUI/Sources/DateSelectorUI/TimeRangeSelectorController.swift:162` |

## EditTagLabelUI (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EditTagLabelController` | func->InputDataModalController | chatReactionContextEditTag | Edit Name |  | `packages/EditTagLabelUI/Sources/EditTagLabelUI/EditTagLabelController.swift:48` |
| `UserTagInfoModalController` | func->InputDataModalController | userTagInfoUnderstood | Understood |  | `packages/EditTagLabelUI/Sources/EditTagLabelUI/UserTagInfoModalController.swift:499` |

## EntertainmentUI (9)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EmojiesController` | class:TelegramGenericViewController |  |  |  | `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:2034` |
| `EntertainmentSidebarController` | class:GenericViewController |  |  |  | `packages/EntertainmentUI/Sources/EntertainmentUI/EntertainmentSidebarController.swift:64` |
| `EntertainmentViewController` | class:TelegramGenericViewController | entertainmentEmoji | EMOJI |  | `packages/EntertainmentUI/Sources/EntertainmentUI/EntertainmentViewController.swift:235` |
| `GifKeyboardController` | class:TelegramGenericViewController | chatContextFavoriteGifsLimitTitle | The Limit of Saved GIFs Reached |  | `packages/EntertainmentUI/Sources/EntertainmentUI/GifKeyboardController.swift:401` |
| `NStickersViewController` | class:TelegramGenericViewController |  |  |  | `packages/EntertainmentUI/Sources/EntertainmentUI/StickersViewController.swift:1149` |
| `PremiumStatusController` | class:TelegramViewController |  |  |  | `packages/EntertainmentUI/Sources/EntertainmentUI/PremiumStatusController.swift:37` |
| `SetupQuickReactionController` | class:TelegramViewController |  |  |  | `packages/EntertainmentUI/Sources/EntertainmentUI/PremiumStatusController.swift:96` |
| `StickerPackPreviewModalController` | func->InputDataModalController | stickerPackPreviewModalControllerEditNameTitle | Edit Sticker Set Name |  | `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPreviewModalController.swift:356` |
| `StickerPackTitleController` | func->InputDataModalController | modalDone | Done |  | `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackEditing.swift:222` |

## FolderSharingUI (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ShareCloudFolderController` | func->InputDataModalController | modalDone | Done |  | `packages/FolderSharingUI/Sources/FolderSharingUI/ShareCloudFolderController.swift:218` |
| `SharedFolderClosureController` | func->InputDataModalController | modalOK | OK |  | `packages/FolderSharingUI/Sources/FolderSharingUI/SharedFolderClosureController.swift:577` |

## ForumSettingsUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ForumSettingsController` | func->InputDataController | forumSettingsTitle | Topics |  | `packages/ForumSettingsUI/Sources/ForumSettingsUI/ForumSettingsController.swift:80` |

## GalleryUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `GalleryModernControls` | class:GenericViewController |  |  |  | `packages/GalleryUI/Sources/GalleryUI/GalleryModernControls.swift:429` |
| `GalleryThumbsControl` | class:ViewController |  |  |  | `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControl.swift:26` |
| `SVideoController` | class:GenericViewController |  |  |  | `packages/GalleryUI/Sources/GalleryUI/SVideoController.swift:50` |
| `SaveModalController` | class:ModalViewController |  |  |  | `packages/GalleryUI/Sources/GalleryUI/SaveModalController.swift:127` |

## GigagroupUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `GigagroupLandingController` | func->InputDataModalController | broadcastGroupsIntroTitle | Broadcast Groups |  | `packages/GigagroupUI/Sources/GigagroupUI/GigagroupLanding.swift:58` |

## GroupCallScreenUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `GroupCallSettingsController` | class:GenericViewController |  |  |  | `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSettingsController.swift:652` |
| `GroupCallUIController` | class:ViewController |  |  |  | `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallController.swift:774` |
| `RTMPStartController` | func->InputDataModalController | voiceChatRTMPTitle | Stream With... |  | `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/RTMPStartController.swift:82` |

## GroupsInCommonUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `GroupsInCommonViewController` | func->ViewController | peerInfoGroupsInCommon | Groups In Common |  | `packages/GroupsInCommonUI/Sources/GroupsInCommonUI/GroupsInCommonViewController.swift:78` |

## ImageCanvasUI (6)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EditImageCanvasController` | class:ModalViewController |  |  |  | `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasController.swift:150` |
| `EditImageControls` | class:GenericViewController |  |  |  | `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageControls.swift:489` |
| `EditImageCutoutController` | class:ModalViewController |  |  |  | `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:229` |
| `EditVideoController` | class:ModalViewController |  |  |  | `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditVideoController.swift:255` |
| `EditVideoCropController` | class:ModalViewController |  |  |  | `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditVideoCropController.swift:63` |
| `EditVideoToolsController` | class:ModalViewController |  |  |  | `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditVideoToolsController.swift:377` |

## InactiveChannelsUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `InactiveChannelsController` | func->InputDataModalController | inactiveChannelsTitle | Limit Reached |  | `packages/InactiveChannelsUI/Sources/InactiveChannelsUI/InactiveChannelsController.swift:144` |

## InputDataUI (10)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `InputDataController` | class:GenericViewController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:685` |
| `InputDataModalController` | class:ModalViewController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:13` |
| `InputPasswordController` | func->InputDataModalController | navigationDone | Done |  | `packages/InputDataUI/Sources/InputDataUI/InputPasswordController.swift:63` |
| `InputURLFormatterModalController` | func->InputDataModalController | inputFormatterURLHeader | URL |  | `packages/InputDataUI/Sources/InputDataUI/InputURLFormatterModalController.swift:105` |
| `ModalOptionSetController` | func->InputDataModalController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/ModalOptionSetController.swift:110` |
| `NumberSelectorController` | func->InputDataModalController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/NumberSelectorController.swift:47` |
| `TextInputController` | func->InputDataModalController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/TextInputController.swift:42` |
| `ValuesSelectorModalController` | class:ModalViewController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/ValuesSelectorModalController.swift:148` |
| `makeChannelAdminControllerObserved` | func->ModalViewController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/FeatureNavigationHooks.swift:234` |
| `makePaymentsCheckoutObserved` | func->ModalViewController |  |  |  | `packages/InputDataUI/Sources/InputDataUI/FeatureNavigationHooks.swift:185` |

## InstantPageUI (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `InstantPageViewController` | class:GenericViewController |  |  |  | `packages/InstantPageUI/Sources/InstantPageUI/InstantPageViewController.swift:21` |
| `InstantViewController` | class:GenericViewController |  |  |  | `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:247` |

## InviteLinksUI (9)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ClosureInviteLinkController` | func->InputDataModalController |  |  |  | `packages/InviteLinksUI/Sources/InviteLinksUI/ClosureInviteLinkController.swift:323` |
| `ExportedInvitationController` | func->InputDataModalController | exportedInvitationTitle | Invite Link |  | `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationController.swift:354` |
| `InviteLinkQrController` | func->InputDataModalController | inviteLinkQrCodeTitle | Invite by QR Code |  | `packages/InviteLinksUI/Sources/InviteLinksUI/InviteLinkQrController.swift:231` |
| `InviteLinksController` | func->InputDataController | manageLinksTitleNew | Invite Links |  | `packages/InviteLinksUI/Sources/InviteLinksUI/InviteLinksController.swift:651` |
| `InvitePrivacyLimitedController` | func->InputDataModalController | inviteFailedTitle | Invite Via Link |  | `packages/InviteLinksUI/Sources/InviteLinksUI/InvitePrivacyLimitedController.swift:410` |
| `JoinLinkPreviewModalController` | func->InputDataModalController | joinLinkJoin | Join |  | `packages/InviteLinksUI/Sources/InviteLinksUI/JoinLinkPreviewModalController.swift:235` |
| `LinkInvationController` | class:TableViewController |  |  |  | `packages/InviteLinksUI/Sources/InviteLinksUI/LinkInvationController.swift:212` |
| `RequestJoinChatModalController` | func->InputDataModalController | requestJoinButton | Request to Join |  | `packages/InviteLinksUI/Sources/InviteLinksUI/RequestJoinChatModalController.swift:74` |
| `RequestJoinMemberListController` | func->InputDataController | requestJoinListTitle | Join Requests |  | `packages/InviteLinksUI/Sources/InviteLinksUI/RequestJoinMemberListController.swift:247` |

## LocationUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `LocationModalController` | class:ModalViewController |  |  |  | `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:514` |
| `LocationModalPreview` | func->InputDataModalController | locationPreviewTitle | Location Preview |  | `packages/LocationUI/Sources/LocationUI/LiveLocationViewController.swift:69` |
| `LocationModalPreview` | func->InputDataModalController | locationPreviewTitle | Location Preview |  | `packages/LocationUI/Sources/LocationUI/LocationPreviewController.swift:525` |

## MediaRecorderUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `VideoRecorderModalController` | class:ModalViewController |  |  |  | `packages/MediaRecorderUI/Sources/MediaRecorderUI/VideoRecorderModalController.swift:18` |

## MonetizationUI (11)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `FragmentAdsInfoController` | func->InputDataModalController | fragmentAdsInfoOK | Understood |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentAdsInfoController.swift:268` |
| `FragmentMonetizationController` | func->InputDataController | monetizationWithdrawEnterPasswordTitle | Enter Password |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentMonetizationController.swift:621` |
| `FragmentMonetizationPromoController` | func->InputDataModalController | monetizationIntroUnderstood | Understood |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentMonetizationPromoController.swift:220` |
| `FragmentStarMonetizationController` | func->InputDataController | monetizationWithdrawEnterPasswordTitle | Enter Password |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentStarMonetizationController.swift:390` |
| `FragmentUsernameController` | func->InputDataModalController | collectibleItemInfoButtonOpenInfo | Learn More |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentUsernameController.swift:252` |
| `SearchAdAboutController` | func->InputDataModalController | fragmentAdsInfoOK | Understood |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentAdsInfoController.swift:272` |
| `adsInfoController` | func->InputDataModalController | fragmentAdsInfoOK | Understood |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentAdsInfoController.swift:276` |
| `withdraw` | func->InputDataModalController |  |  |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentStarMonetizationController.swift:1012` |
| `withdrawStarBalance` | func->InputDataModalController |  |  |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentMonetizationController.swift:1352` |
| `withdrawStarBalance` | func->InputDataModalController |  |  |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentStarMonetizationController.swift:1099` |
| `withdrawStarBalance` | func->InputDataModalController |  |  |  | `packages/MonetizationUI/Sources/MonetizationUI/FragmentStarMonetizationController.swift:1113` |

## PasscodeUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ColdStartPasslockController` | class:ModalViewController |  |  |  | `packages/PasscodeUI/Sources/PasscodeUI/ColdStartPasslockController.swift:21` |
| `PasscodeController` | func->ViewController |  |  |  | `packages/PasscodeUI/Sources/PasscodeUI/PasscodeControllers.swift:158` |
| `PasscodeLockController` | class:ModalViewController |  |  |  | `packages/PasscodeUI/Sources/PasscodeUI/PasscodeLockController.swift:352` |
| `PasscodeSettingsViewController` | class:TableViewController |  |  |  | `packages/PasscodeUI/Sources/PasscodeUI/PasscodeSettingsViewController.swift:237` |

## PasskeysUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `FrozenAccountController` | func->InputDataModalController | freezeAccountOK | Submit an Appeal |  | `packages/PasskeysUI/Sources/PasskeysUI/FrozenAccountController.swift:256` |
| `PasskeysController` | func->InputDataModalController | passkeysTitle | Passkeys |  | `packages/PasskeysUI/Sources/PasskeysUI/PasskeysController.swift:525` |
| `SetupEmailController` | func->InputDataModalController | loginEnterNewEmailTitle | Enter New Email |  | `packages/PasskeysUI/Sources/PasskeysUI/SetupEmailController.swift:156` |
| `SuspiciousRevokeModal` | func->InputDataModalController |  |  |  | `packages/PasskeysUI/Sources/PasskeysUI/SuspiciousRevokeModal.swift:228` |

## PassportUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PassportController` | class:GenericViewController |  |  |  | `packages/PassportUI/Sources/PassportUI/PassportController.swift:2486` |

## PaymentsUI (9)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PamentsSelectMethodController` | func->InputDataModalController | checkoutPaymentMethodTitle | Payment Method |  | `packages/PaymentsUI/Sources/PaymentsUI/PamentsSelectMethodController.swift:84` |
| `PaymentWebInteractionController` | class:ModalViewController |  |  |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentWebInteractionController.swift:31` |
| `PaymentsCheckoutController` | func->InputDataModalController | checkoutPasswordEntryTitle | Payment Confirmation |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutController.swift:443` |
| `PaymentsPaymentMethodController` | func->InputDataModalController | checkoutNewCardTitle | New Card |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentsPaymentMethodController.swift:436` |
| `PaymentsReceiptController` | func->InputDataModalController | checkoutReceiptTitle | Receipt |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentsReceiptController.swift:194` |
| `PaymentsShippingInfoController` | func->InputDataModalController | checkoutInfoTitle | Shipping Information |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentsShippingInfoController.swift:217` |
| `PaymentsShippingMethodController` | func->InputDataModalController | checkoutShippingMethod | Shipping Method |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentsShippingMethodController.swift:55` |
| `paymentChildController` | func->ModalViewController |  |  |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentPresentationContext.swift:3` |
| `showPaymentChild` | func->ModalViewController | checkoutPasswordEntryTitle | Payment Confirmation |  | `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutController.swift:460` |

## PeerInfoUI (12)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EditBotUsernameController` | func->InputDataController | botUsernameActivateTitle | Activate Username |  | `packages/PeerInfoUI/Sources/PeerInfoUI/EditBotUsernameController.swift:104` |
| `PeerInfoController` | class:EditableViewController |  |  |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoController.swift:476` |
| `PeerMediaController` | class:EditableViewController |  |  |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:808` |
| `PeerRatingModalController` | func->InputDataModalController | peerRatingPreviewTitle | Rating |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PeerRatingModalController.swift:601` |
| `PreHistorySettingsController` | func->InputDataController | peerInfoPreHistory | Chat History For New Members |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PreHistorySettingsController.swift:81` |
| `SecretChatKeyViewController` | class:TelegramGenericViewController |  |  |  | `packages/PeerInfoUI/Sources/PeerInfoUI/SecretChatKeyViewController.swift:106` |
| `SimilarBotsController` | func->InputDataController | peerMediaSimilarChannels | Similar Channels |  | `packages/PeerInfoUI/Sources/PeerInfoUI/SimilarBotsController.swift:102` |
| `SimilarChannelsController` | func->InputDataController | peerMediaSimilarChannels | Similar Channels |  | `packages/PeerInfoUI/Sources/PeerInfoUI/SimilarChannelsController.swift:94` |
| `UserInfoPhotoConfirmController` | func->InputDataModalController |  |  |  | `packages/PeerInfoUI/Sources/PeerInfoUI/UserInfoPhotoConfirmController.swift:65` |
| `controller` | func->ViewController | selectPeersTitleSearchMembers | Search Members |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:2328` |
| `makeGroupsInCommonControllerObserved` | func->ViewController |  |  |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoNavigationHooks.swift:18` |
| `prepareController` | func->ViewController |  |  |  | `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:2052` |

## PeerMediaUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PeerMediaGifsController` | class:TelegramGenericViewController |  |  |  | `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaGifsController.swift:134` |
| `PeerMediaListController` | class:TableViewController |  |  |  | `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaListController.swift:295` |
| `PeerMediaPhotosController` | class:TableViewController |  |  |  | `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaPhotosController.swift:339` |
| `SendAudioModalController` | func->InputDataModalController | sendAudioTitle | Audio |  | `packages/PeerMediaUI/Sources/PeerMediaUI/SendAudioModalController.swift:257` |

## PeerModerationUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChannelBlacklistViewController` | class:EditableViewController | channelBlacklistSelectNewUserTitle | Members |  | `packages/PeerModerationUI/Sources/PeerModerationUI/ChannelBlocklistViewController.swift:240` |
| `ChannelMembersViewController` | class:EditableViewController | channelMembersSelectTitle | Add Members |  | `packages/PeerModerationUI/Sources/PeerModerationUI/ChannelMembersViewController.swift:385` |
| `ChannelPermissionsController` | class:TableViewController | channelBlacklistSelectNewUserTitle | Members |  | `packages/PeerModerationUI/Sources/PeerModerationUI/ChannelPermissionsController.swift:625` |
| `RestrictedModalController` | func->InputDataModalController | groupPermissionTitle | Exception |  | `packages/PeerModerationUI/Sources/PeerModerationUI/RestictedModalViewController.swift:452` |

## PollResultsUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `MessagePollStatsController` | func->ViewController | messagePollStatsTitle | Poll Stats |  | `packages/PollResultsUI/Sources/PollResultsUI/MessagePollStatsController.swift:91` |
| `NewPollController` | func->InputDataModalController | newPollDeadline | Deadline |  | `packages/PollResultsUI/Sources/PollResultsUI/NewPollController.swift:1057` |
| `NewTodoController` | func->InputDataModalController |  |  |  | `packages/PollResultsUI/Sources/PollResultsUI/NewTodoController.swift:330` |
| `PollResultController` | func->InputDataModalController | pollResultsTitlePoll | Poll Results |  | `packages/PollResultsUI/Sources/PollResultsUI/PollResultController.swift:301` |

## PremiumUI (5)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PremiumBoardingController` | class:ModalViewController |  |  |  | `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1219` |
| `PremiumBoardingFeaturesController` | class:GenericViewController |  |  |  | `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingFeaturesController.swift:492` |
| `PremiumLimitController` | class:ModalViewController |  |  |  | `packages/PremiumUI/Sources/PremiumUI/PremiumLimitController.swift:698` |
| `PremiumLockModalController` | class:ModalViewController |  |  |  | `packages/PremiumUI/Sources/PremiumUI/PremiumLockModalController.swift:26` |
| `PremiumShowStatusController` | func->InputDataModalController |  |  |  | `packages/PremiumUI/Sources/PremiumUI/PremiumShowStatusController.swift:287` |

## PreviewSenderUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `MediaPaidSetterController` | func->InputDataModalController | paidMediaTitle | Paid Content |  | `packages/PreviewSenderUI/Sources/PreviewSenderUI/MediaPaidSetterController.swift:237` |
| `PreviewSenderController` | class:ModalViewController | previewDraggingAddItemsOther | Add Items |  | `packages/PreviewSenderUI/Sources/PreviewSenderUI/PreviewSenderController.swift:1303` |
| `PreviewSenderPlaceholderEmojiesController` | class:ViewController |  |  |  | `packages/PreviewSenderUI/Sources/PreviewSenderUI/PreviewSenderUIHooks.swift:70` |

## PrivateCallScreen (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PeerCallScreen` | class:ViewController |  |  |  | `packages/PrivateCallScreen/Sources/PeerCallScreen.swift:18` |

## ProxyUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `proxyListController` | func->ViewController | proxySettingsTitle | Proxy Settings |  | `packages/ProxyUI/Sources/ProxyUI/ProxyListController.swift:199` |

## QrStudioUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `QrStudioController` | class:ModalViewController |  |  |  | `packages/QrStudioUI/Sources/QrStudioUI/QrStudioController.swift:1813` |

## QuickSwitcher (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AltTabSwitcherController` | class:ModalViewController |  |  |  | `packages/QuickSwitcher/Sources/QuickSwitcher/AltTabSwitcherController.swift:285` |
| `QuickSwitcherModalController` | class:ModalViewController |  |  |  | `packages/QuickSwitcher/Sources/QuickSwitcher/QuickSwitcherModalController.swift:326` |

## ReportUI (5)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ReportController` | func->InputDataController |  |  |  | `packages/ReportUI/Sources/ReportUI/ComplicatedReportController.swift:186` |
| `ReportController` | func->InputDataModalController |  |  |  | `packages/ReportUI/Sources/ReportUI/ComplicatedReportController.swift:108` |
| `ReportDetailsController` | func->InputDataController |  |  |  | `packages/ReportUI/Sources/ReportUI/ComplicatedReportController.swift:275` |
| `ReportDetailsController` | func->InputDataModalController | reportAdditionTextButton | Report |  | `packages/ReportUI/Sources/ReportUI/ReportDetailsController.swift:54` |
| `ReportReasonController` | func->InputDataModalController | peerInfoReport | Report |  | `packages/ReportUI/Sources/ReportUI/ReportReasonModalController.swift:171` |

## SelectColorUI (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `SelectColorController` | func->InputDataController | starNftGiftConfirmTitle | Buy Gift |  | `packages/SelectColorUI/Sources/SelectColorUI/SelectColorController.swift:1744` |
| `SelectColorParentController` | class:SectionViewController |  |  |  | `packages/SelectColorUI/Sources/SelectColorUI/SelectColorParentController.swift:67` |

## SelectCountryUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `SelectCountries` | func->InputDataModalController | selectCountriesTitle | Select Countries |  | `packages/SelectCountryUI/Sources/SelectCountryUI/SelectCountryModalController.swift:58` |

## SelectPeersUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EmptyComposeController` | class:TelegramGenericViewController |  |  |  | `packages/SelectPeersUI/Sources/SelectPeersUI/EmptyComposeController.swift:16` |
| `SelectPeersMainController` | class:GenericViewController |  |  |  | `packages/SelectPeersUI/Sources/SelectPeersUI/SelectPeersController.swift:1501` |
| `SelectPeersModalController` | class:ModalViewController |  |  |  | `packages/SelectPeersUI/Sources/SelectPeersUI/SelectPeersController.swift:1789` |

## SessionsUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `RecentSessionsController` | class:TableViewController |  |  |  | `packages/SessionsUI/Sources/SessionsUI/RecentSessionsController.swift:458` |
| `RenameDeviceController` | func->InputDataModalController | modalSave | Save |  | `packages/SessionsUI/Sources/SessionsUI/RenameDeviceController.swift:45` |
| `SessionModalController` | func->InputDataModalController | sessionPreviewTitle | Session |  | `packages/SessionsUI/Sources/SessionsUI/SessionModalController.swift:297` |
| `WebSessionsController` | class:TableViewController |  |  |  | `packages/SessionsUI/Sources/SessionsUI/WebSessionsController.swift:250` |

## SettingsUI (34)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AboutModalController` | class:ModalViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/AboutModalController.swift:91` |
| `AccountViewController` | class:TelegramGenericViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/AccountViewController.swift:819` |
| `AppAppearanceViewController` | func->InputDataController | telegramAppearanceViewController | Appearance |  | `packages/SettingsUI/Sources/SettingsUI/AppAppearanceViewController.swift:586` |
| `ArchiveSettingsController` | func->InputDataController | archiveTitle | Archive Settings |  | `packages/SettingsUI/Sources/SettingsUI/ArchiveSettingsController.swift:102` |
| `AutoNightSettingsController` | func->InputDataController | autoNightSettingsTitle | Auto-Night Mode |  | `packages/SettingsUI/Sources/SettingsUI/AutoNightViewController.swift:199` |
| `AutoremoveMessagesController` | func->InputDataModalController | autoremoveMessagesTitleDeleteOnly | Auto-Deletion |  | `packages/SettingsUI/Sources/SettingsUI/AutoremoMessagesController.swift:115` |
| `BlockedPeersViewController` | class:EditableViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/BlockedPeersViewController.swift:221` |
| `CustomAccentColorModalController` | class:ModalViewController | appearanceThemeAccent | Accent |  | `packages/SettingsUI/Sources/SettingsUI/CustomAccentColorModalController.swift:175` |
| `DeveloperViewController` | func->InputDataController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/DeveloperViewController.swift:260` |
| `EditThemeController` | func->InputDataModalController | editThemeTitle | Edit Theme |  | `packages/SettingsUI/Sources/SettingsUI/EditThemeController.swift:161` |
| `GeneralSettingsViewController` | class:TableViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/GeneralSettingsViewController.swift:456` |
| `GlobalAutoremoveMessagesController` | func->InputDataController | globalTimerTitle | Auto-Delete Messages |  | `packages/SettingsUI/Sources/SettingsUI/GlobalAutoremoveMessagesController.swift:143` |
| `LanguageController` | func->InputDataController | telegramLanguageViewController | Language |  | `packages/SettingsUI/Sources/SettingsUI/LanguageController.swift:261` |
| `LiteModeController` | func->InputDataController | liteModeTitle | Power Saving |  | `packages/SettingsUI/Sources/SettingsUI/LiteModeController.swift:162` |
| `LocalizationPreviewModalController` | func->InputDataModalController | applyLanguageChangeLanguageTitle | Change Language? |  | `packages/SettingsUI/Sources/SettingsUI/LocalizationPreviewModalController.swift:71` |
| `NewThemeController` | func->InputDataModalController | newThemeTitle | New Theme |  | `packages/SettingsUI/Sources/SettingsUI/NewThemeController.swift:62` |
| `NotificationCategorySettingsController` | func->InputDataController | notificationSettingsExceptionsAdd | Add an Exception |  | `packages/SettingsUI/Sources/SettingsUI/NotificationCategorySettingsController.swift:543` |
| `NotificationExceptionSettingsModalController` | func->InputDataModalController | modalDone | Done |  | `packages/SettingsUI/Sources/SettingsUI/NotificationExceptionSettingsController.swift:211` |
| `NotificationPreferencesController` | func->ViewController | telegramNotificationSettingsViewController | Notifications |  | `packages/SettingsUI/Sources/SettingsUI/NotificationPreferencesController.swift:380` |
| `NotificationSoundController` | func->InputDataController | notificationSoundTitle | Notification Sound |  | `packages/SettingsUI/Sources/SettingsUI/NotificationSoundController.swift:193` |
| `PersonalChannelController` | func->InputDataModalController | personalChannelTitle | Personal Channel |  | `packages/SettingsUI/Sources/SettingsUI/PersonalChannelController.swift:187` |
| `PrivacyAndSecurityViewController` | class:TableViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/PrivacyAndSecurityViewController.swift:811` |
| `ReactionNotificationSettingsController` | func->InputDataController | notificationSettingsReactions | Reactions |  | `packages/SettingsUI/Sources/SettingsUI/ReactionNotificationSettingsController.swift:128` |
| `SelectColorPlaceholderEmojisController` | class:ViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/SettingsHooks.swift:442` |
| `SelectivePrivacySettingsController` | class:TableViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/SelectivePrivacySettingsController.swift:663` |
| `SelectivePrivacySettingsPeersController` | class:EditableViewController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/SelectivePrivacySettingsPeersController.swift:193` |
| `ShortcutListController` | func->ViewController | shortcutsControllerTitle | Shortcuts |  | `packages/SettingsUI/Sources/SettingsUI/ShortcutListController.swift:161` |
| `SuggestionLocalizationViewController` | class:ModalViewController | modalOK | OK |  | `packages/SettingsUI/Sources/SettingsUI/SuggestionLocalizationViewController.swift:66` |
| `ThemePreviewModalController` | func->InputDataModalController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/ThemePreviewModalController.swift:254` |
| `UsernameController` | func->InputDataController | usernameActivateTitle | Activate Username |  | `packages/SettingsUI/Sources/SettingsUI/UsernameController.swift:143` |
| `cancelResetAccountController` | func->InputDataModalController | cancelResetAccountTitle | Cancel Account Reset |  | `packages/SettingsUI/Sources/SettingsUI/CancelResetAccountController.swift:168` |
| `twoStepVerificationPasswordEntryController` | func->InputDataController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/TwoStepVerificationUnlockController.swift:1102` |
| `twoStepVerificationResetPasswordController` | func->InputDataController | twoStepAuthRecoveryTitle | Email Code |  | `packages/SettingsUI/Sources/SettingsUI/TwoStepVerificationUnlockController.swift:918` |
| `twoStepVerificationUnlockController` | func->InputDataController |  |  |  | `packages/SettingsUI/Sources/SettingsUI/TwoStepVerificationUnlockController.swift:302` |

## ShareUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ShareModalController` | class:ModalViewController |  |  |  | `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:1589` |

## SidebarUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChatListFilterController` | func->InputDataController |  |  |  | `packages/SidebarUI/Sources/SidebarUI/ChatListFilterController.swift:882` |
| `ChatListFiltersListController` | func->InputDataController | chatListFilterListTitle | Chat Folders |  | `packages/SidebarUI/Sources/SidebarUI/ChatListFiltersListController.swift:251` |
| `SidebarViewController` | class:GenericViewController |  |  |  | `packages/SidebarUI/Sources/SidebarUI/SidebarViewController.swift:7` |

## StarsUI (30)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `GiftingController` | func->InputDataModalController | starAuctionChangePeerTitle | Change Recipient |  | `packages/StarsUI/Sources/StarsUI/GiftingController.swift:737` |
| `GridController` | class:ViewController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:315` |
| `InputCustomController` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/Star_AuctionBidController.swift:1315` |
| `PeerMediaGiftsController` | func->InputDataController | peerMediaGiftsCollectionUpdateTitle | Update Name |  | `packages/StarsUI/Sources/StarsUI/PeerMediaGiftsController.swift:549` |
| `PremiumGiftingController` | func->InputDataModalController | premiumGiftTitle | Gift Telegram Premium |  | `packages/StarsUI/Sources/StarsUI/PremiumGiftingController.swift:469` |
| `PreviewStarGiftController` | func->InputDataModalController | starGiftPreviewTitleBuy | Buy a Gift |  | `packages/StarsUI/Sources/StarsUI/PreviewStarGiftController.swift:1274` |
| `SelectGiftsModalController` | func->InputDataModalController | selectGiftsTitle | Add Gifts |  | `packages/StarsUI/Sources/StarsUI/SelectGiftsModalController.swift:89` |
| `StarGift_AddMessage_Controller` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarGift_Nft_Controller.swift:4902` |
| `StarGift_LearnAboutGifts` | func->InputDataModalController | monetizationIntroUnderstood | Understood |  | `packages/StarsUI/Sources/StarsUI/StarGift_LearnAboutGifts.swift:176` |
| `StarGift_MarketplaceController` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarGift_MarketplaceController.swift:1245` |
| `StarGift_ModelBuilderController` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:1101` |
| `StarGift_NftValue_Controller` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarGift_NftValue_Controller.swift:355` |
| `StarGift_Nft_Controller` | func->InputDataModalController | starNftGiftConfirmTitle | Buy Gift |  | `packages/StarsUI/Sources/StarsUI/StarGift_Nft_Controller.swift:2643` |
| `StarGift_SelfAuction_Controller` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarGift_SelfAuction_Controller.swift:522` |
| `StarNftOfferController` | func->InputDataModalController | starGiftOfferTitle | Offer to Buy |  | `packages/StarsUI/Sources/StarsUI/StarGift_OfferController.swift:574` |
| `StarUsePromoController` | func->InputDataModalController | fragmentAdsInfoOK | Understood |  | `packages/StarsUI/Sources/StarsUI/StarUsePromoController.swift:193` |
| `Star_AppExamples` | func->InputDataModalController | exampleAppsTitle | Examples |  | `packages/StarsUI/Sources/StarsUI/Star_AppExamples.swift:87` |
| `Star_AuctionAcquiredController` | func->InputDataModalController | starAuctionAcquiredItemsBoughtOther | %d Items Bought |  | `packages/StarsUI/Sources/StarsUI/Star_AuctionAcquiredController.swift:186` |
| `Star_AuctionBidController` | func->InputDataModalController | starAuctionBidPlaceCustomBid | Place a Custom Bid |  | `packages/StarsUI/Sources/StarsUI/Star_AuctionBidController.swift:804` |
| `Star_AuctionInfoController` | func->InputDataModalController | monetizationIntroUnderstood | Understood |  | `packages/StarsUI/Sources/StarsUI/Star_AuctionInfoController.swift:241` |
| `Star_AuctionListController` | func->InputDataModalController | starAuctionListActiveAuctionsOther | %d Active Auctions |  | `packages/StarsUI/Sources/StarsUI/Star_AuctionListController.swift:288` |
| `Star_AuctionPreviewController` | func->InputDataModalController | starAuctionPreviewJoin | Join Auction |  | `packages/StarsUI/Sources/StarsUI/Star_AuctionPreviewController.swift:567` |
| `Star_ListScreen` | func->InputDataModalController | monetizationWithdrawEnterPasswordTitle | Enter Password |  | `packages/StarsUI/Sources/StarsUI/Star_ListScreen.swift:1297` |
| `Star_PurschaseInApp` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/Star_PurchaseInApp.swift:707` |
| `Star_ReactionsController` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/Star_ReactionsController.swift:1002` |
| `Star_SubscriptionScreen` | func->InputDataModalController | starSubScreenActionJoin | Join Channel |  | `packages/StarsUI/Sources/StarsUI/Star_Subscription.swift:350` |
| `Star_TransactionScreen` | func->InputDataModalController |  |  |  | `packages/StarsUI/Sources/StarsUI/Star_Transaction.swift:1780` |
| `giftTransferConfirmController` | func->InputDataController | giftTransferConfirmationTitle | Confirm Transfer |  | `packages/StarsUI/Sources/StarsUI/GiftTransferController.swift:319` |
| `sellNft` | func->InputDataModalController | starNftSellTitle | Sell Gift |  | `packages/StarsUI/Sources/StarsUI/StarGift_Nft_Controller.swift:4194` |
| `showChild` | func->ModalViewController |  |  |  | `packages/StarsUI/Sources/StarsUI/StarsScreenContext.swift:44` |

## StatisticsUI (6)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChannelBoostStatsController` | func->InputDataController | statsBoosts | Boosts |  | `packages/StatisticsUI/Sources/StatisticsUI/ChannelBoostStatsController.swift:873` |
| `ChannelStatisticsController` | class:TelegramGenericViewController |  |  |  | `packages/StatisticsUI/Sources/StatisticsUI/ChannelStatisticsController.swift:26` |
| `ChannelStatsSegmentController` | class:SectionViewController |  |  |  | `packages/StatisticsUI/Sources/StatisticsUI/ChannelStatsSegmentController.swift:90` |
| `ChannelStatsViewController` | func->ViewController | channelStatsTitle | Channel Statistics |  | `packages/StatisticsUI/Sources/StatisticsUI/ChannelStatsViewController.swift:453` |
| `GroupStatsViewController` | func->ViewController | groupStatsTitle | Group Statistics |  | `packages/StatisticsUI/Sources/StatisticsUI/GroupsStatsController.swift:382` |
| `MessageStatsController` | func->ViewController |  |  |  | `packages/StatisticsUI/Sources/StatisticsUI/MessageStatsController.swift:260` |

## StickerSettingsUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ArchivedStickerPacksController` | class:TableViewController |  |  |  | `packages/StickerSettingsUI/Sources/StickerSettingsUI/ArchivedStickerPacksController.swift:204` |
| `CustomEmojiController` | func->InputDataController | installedStickersCustomEmoji | Custom Emoji |  | `packages/StickerSettingsUI/Sources/StickerSettingsUI/CustomEmojiController.swift:96` |
| `FeaturedStickerPacksController` | class:TableViewController |  |  |  | `packages/StickerSettingsUI/Sources/StickerSettingsUI/FeaturedStickerPacksController.swift:146` |
| `InstalledStickerPacksController` | class:TableViewController |  |  |  | `packages/StickerSettingsUI/Sources/StickerSettingsUI/InstalledStickerPacksController.swift:382` |

## StoriesUI (6)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `SelectStoryModalController` | func->InputDataModalController | selectStoryTitle | Add Stories |  | `packages/StoriesUI/Sources/StoriesUI/SelectStoryModalController.swift:171` |
| `StoryFoundListController` | func->InputDataModalController | storySearchSubtitleOther | %d stories |  | `packages/StoriesUI/Sources/StoriesUI/StoryFoundListController.swift:354` |
| `StoryMediaController` | class:TelegramGenericViewController | storyMediaAlbumNewTitle | Create a New Album |  | `packages/StoriesUI/Sources/StoriesUI/StoryMediaController.swift:844` |
| `StoryModalController` | class:ModalViewController |  |  |  | `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:2182` |
| `StoryStealthModeController` | class:ModalViewController |  |  |  | `packages/StoriesUI/Sources/StoriesUI/StoryStealthModeController.swift:220` |
| `StoryStreamStarMessageController` | func->InputDataModalController | storyLiveStreamStarMessageHighlightAndPin | Highlight and Pin |  | `packages/StoriesUI/Sources/StoriesUI/StoryStreamStarMessageController.swift:322` |

## TGUIKit (16)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `CatalinaStyledSegmentController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/CatalinaStyledSegmentController.swift:302` |
| `GenericViewController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/ViewController.swift:1162` |
| `MajorNavigationController` | class:NavigationViewController |  |  |  | `packages/TGUIKit/Sources/MajorNavigationController.swift:6` |
| `ModalController` | class:ModalViewController |  |  |  | `packages/TGUIKit/Sources/ViewController.swift:1393` |
| `ModalViewController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/ViewController.swift:1233` |
| `NavigationViewController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/NavigationViewController.swift:288` |
| `ProgressModalController` | class:ModalViewController |  |  |  | `packages/TGUIKit/Sources/ProgressModal.swift:35` |
| `RevealTableItemController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/TableView.swift:25` |
| `SPopoverViewController` | class:GenericViewController |  |  |  | `packages/TGUIKit/Sources/SPopoverViewController.swift:56` |
| `SectionViewController` | class:GenericViewController |  |  |  | `packages/TGUIKit/Sources/SectionViewController.swift:44` |
| `SuccessModalController` | class:ModalViewController |  |  |  | `packages/TGUIKit/Sources/ProgressModal.swift:143` |
| `TabBarController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/TabBarController.swift:60` |
| `TextAndLabelModalController` | class:ModalViewController |  |  |  | `packages/TGUIKit/Sources/ProgressModal.swift:418` |
| `TooltipController` | class:ViewController |  |  |  | `packages/TGUIKit/Sources/TooltipController.swift:156` |
| `VolumeControllerPopover` | class:GenericViewController |  |  |  | `packages/TGUIKit/Sources/VolumeControllerPopover.swift:3` |
| `first` | func->ViewController |  |  |  | `packages/TGUIKit/Sources/NavigationViewController.swift:1235` |

## Telegram-Mac/app (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AuthModalController` | class:ModalController |  |  |  | `Telegram-Mac/app/ApplicationContext.swift:138` |
| `MainViewController` | class:TelegramGenericViewController |  |  |  | `Telegram-Mac/app/MainViewController.swift:378` |
| `UpdateTabController` | class:GenericViewController |  |  |  | `Telegram-Mac/app/MainViewController.swift:155` |

## Telegram-Mac/packages-integration (11)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChatListFilterController` | func->InputDataController |  |  |  | `Telegram-Mac/packages-integration/bridges/SidebarUIIntegration.swift:32` |
| `ChatListFiltersListController` | func->InputDataController |  |  |  | `Telegram-Mac/packages-integration/bridges/SidebarUIIntegration.swift:28` |
| `ShareCloudFolderController` | func->InputDataModalController | shareFolderNameLinkTitle | Name Link |  | `Telegram-Mac/packages-integration/bridges/FolderSharingUIIntegration.swift:8` |
| `SharedFolderClosureController` | func->InputDataModalController | shareFolderNameLinkTitle | Name Link |  | `Telegram-Mac/packages-integration/bridges/FolderSharingUIIntegration.swift:12` |
| `WalletController` | func->InputDataModalController |  |  |  | `Telegram-Mac/packages-integration/bridges/WalletUIIntegration.swift:35` |
| `WalletInfoController` | func->InputDataModalController |  |  |  | `Telegram-Mac/packages-integration/bridges/WalletUIIntegration.swift:80` |
| `WalletSendController` | func->InputDataModalController |  |  |  | `Telegram-Mac/packages-integration/bridges/WalletUIIntegration.swift:40` |
| `WalletSendController` | func->InputDataModalController |  |  |  | `Telegram-Mac/packages-integration/bridges/WalletUIIntegration.swift:45` |
| `WalletSendController` | func->InputDataModalController |  |  |  | `Telegram-Mac/packages-integration/bridges/WalletUIIntegration.swift:50` |
| `WalletTransactionController` | func->InputDataModalController |  |  |  | `Telegram-Mac/packages-integration/bridges/WalletUIIntegration.swift:75` |
| `makePremiumBusinessController` | func->ViewController |  |  |  | `Telegram-Mac/packages-integration/hooks/PremiumHooksInstall.swift:106` |

## Telegram-Mac/updater (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AppUpdateViewController` | func->InputDataController | appUpdateTitle | Updates |  | `Telegram-Mac/updater/AppUpdateViewController.swift:238` |

## TelegramMediaUtils (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `PreviewModalController` | class:ModalViewController |  |  |  | `packages/TelegramMediaUtils/Sources/TelegramMediaUtils/StickerPreviewHandler.swift:210` |

## TelegramUtils (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EditableViewController` | class:TelegramGenericViewController |  |  |  | `packages/TelegramUtils/Sources/TelegramUtils/ControllerExtension.swift:112` |
| `TableViewController` | class:TelegramGenericViewController |  |  |  | `packages/TelegramUtils/Sources/TelegramUtils/ControllerExtension.swift:55` |
| `TelegramGenericViewController` | class:GenericViewController |  |  |  | `packages/TelegramUtils/Sources/TelegramUtils/ControllerExtension.swift:15` |
| `TelegramViewController` | class:TelegramGenericViewController |  |  |  | `packages/TelegramUtils/Sources/TelegramUtils/ControllerExtension.swift:48` |

## TranslateUI (3)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `AIStyleModalController` | func->InputDataModalController | aiStyleModalEditStyleTitle | Edit Style |  | `packages/TranslateUI/Sources/TranslateUI/AIStyleModalController.swift:213` |
| `AiStylePreviewModalController` | func->InputDataModalController | aiStylePreviewAddStyle | Add Style |  | `packages/TranslateUI/Sources/TranslateUI/AiStylePreviewModalController.swift:373` |
| `TranslateModalController` | func->InputDataModalController |  |  |  | `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:1029` |

## VerifyAgeUI (1)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `VerifyAgeAlertController` | func->InputDataModalController | ageVerificationVerify | Verify My Age |  | `packages/VerifyAgeUI/Sources/VerifyAgeUI/VerifyAgeAlertController.swift:70` |

## WalletUI (24)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `WalletAuthorizeController` | class:ModalViewController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletAuthorizeController.swift:210` |
| `WalletCollectibleDetailsController` | func->InputDataModalController | walletCollectibleDetailsControllerOK | OK |  | `packages/WalletUI/Sources/WalletUI/WalletCollectibleDetailsController.swift:906` |
| `WalletCollectibleDetailsController` | func->InputDataModalController | walletCollectibleDetailsControllerOK | OK |  | `packages/WalletUI/Sources/WalletUI/WalletCollectibleDetailsController.swift:911` |
| `WalletConnectLinkController` | func->InputDataModalController | walletControllerConnectApp | Connect an App |  | `packages/WalletUI/Sources/WalletUI/WalletController.swift:1252` |
| `WalletConnectedAppInfoController` | func->InputDataModalController | walletConnectedAppsControllerDisconnect | Disconnect |  | `packages/WalletUI/Sources/WalletUI/WalletConnectedAppsController.swift:395` |
| `WalletConnectedAppsController` | func->InputDataModalController | walletConnectedAppsControllerTitle | Connected Apps |  | `packages/WalletUI/Sources/WalletUI/WalletConnectedAppsController.swift:112` |
| `WalletController` | func->InputDataModalController | walletControllerPasswordSet | Password set |  | `packages/WalletUI/Sources/WalletUI/WalletController.swift:580` |
| `WalletImportController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletImportController.swift:1156` |
| `WalletInfoController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletInfoController.swift:304` |
| `WalletModalController` | class:InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletClassicAccent.swift:39` |
| `WalletPeerBalanceController` | class:ModalViewController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletPeerBalanceController.swift:406` |
| `WalletReceiveController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:1235` |
| `WalletReplaceController` | func->InputDataModalController | walletReplaceControllerTitle | Replace Wallet |  | `packages/WalletUI/Sources/WalletUI/WalletReplaceController.swift:55` |
| `WalletSendController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletSendController.swift:744` |
| `WalletSendController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletSendController.swift:752` |
| `WalletSendController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletSendController.swift:757` |
| `WalletSettingsController` | func->InputDataModalController | walletSettingsControllerBackupDisabled | Backup Disabled |  | `packages/WalletUI/Sources/WalletUI/WalletSettingsController.swift:190` |
| `WalletTransactionController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletTransactionController.swift:1113` |
| `WalletWordsController` | func->InputDataModalController | walletWordsControllerDone | Done |  | `packages/WalletUI/Sources/WalletUI/WalletWordsController.swift:139` |
| `makeWalletRecipientController` | func->InputDataModalController | walletRecipientControllerTitle | Choose Recipient |  | `packages/WalletUI/Sources/WalletUI/WalletRecipientController.swift:315` |
| `makeWalletSendController` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletSendController.swift:1037` |
| `makeWalletSendModal` | func->InputDataModalController |  |  |  | `packages/WalletUI/Sources/WalletUI/WalletSendController.swift:779` |
| `makeWordsController` | func->InputDataController | walletWordsControllerTitle | Wallet |  | `packages/WalletUI/Sources/WalletUI/WalletWordsController.swift:79` |
| `walletCommentInputController` | func->InputDataModalController | walletSendControllerEditComment | Edit Comment |  | `packages/WalletUI/Sources/WalletUI/WalletSendController.swift:1765` |

## WallpaperUI (4)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `ChannelWallpapersController` | func->InputDataModalController | channelWallpaperTitleGroup | Group Wallpaper |  | `packages/WallpaperUI/Sources/WallpaperUI/ChannelWallpapersController.swift:318` |
| `ChatWallpaperModalController` | func->InputDataModalController | chatWPBackgroundTitle | Chat Wallpaper |  | `packages/WallpaperUI/Sources/WallpaperUI/ChatWallpaperModalController.swift:240` |
| `WallpaperPatternPreviewController` | class:GenericViewController |  |  |  | `packages/WallpaperUI/Sources/WallpaperUI/WallpaperPatternPreviewController.swift:186` |
| `WallpaperPreviewController` | func->InputDataModalController |  |  |  | `packages/WallpaperUI/Sources/WallpaperUI/WallpaperPreviewController.swift:1409` |

## WebAppUI (12)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `InstantViewInBrowser` | class:TelegramGenericViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/InstantViewInBrowser.swift:22` |
| `TabsController` | class:GenericViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:1105` |
| `WebGameViewController` | class:ModalViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebGameViewController.swift:90` |
| `WebappBrowserController` | class:ViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:1805` |
| `WebappTransferDataController` | func->InputDataModalController | webAppTransferDataImportData | Import Data |  | `packages/WebAppUI/Sources/WebAppUI/WebappTransferDataController.swift:172` |
| `WebbotEmojisetModal` | func->InputDataModalController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebbotEmojisetModal.swift:240` |
| `WebbotShareMessageModal` | func->InputDataModalController | webappShareMessageShare | Share Message |  | `packages/WebAppUI/Sources/WebAppUI/WebbotShareMessageModal.swift:140` |
| `WebpageContainerController` | class:GenericViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:1646` |
| `WebpageModalController` | class:ModalViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:1002` |
| `WebsiteController` | class:ModalViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/WebsiteController.swift:384` |
| `makeShareChatContextResultModalObserved` | func->ModalViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/BrowserHooks.swift:101` |
| `makeShareChatContextResultModalObservedResult` | func->ModalViewController |  |  |  | `packages/WebAppUI/Sources/WebAppUI/BrowserHooks.swift:84` |

## WidgetUI (6)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `EmptyChatViewController` | class:TelegramGenericViewController |  |  |  | `packages/WidgetUI/Sources/WidgetUI/EmptyChatViewController.swift:153` |
| `WidgetAppIconController` | class:TelegramGenericViewController | emptyChatAppIcon | Dock Icon |  | `packages/WidgetUI/Sources/WidgetUI/WidgetAppIconController.swift:62` |
| `WidgetAppearanceController` | class:TelegramGenericViewController | emptyChatAppearance | Appearance |  | `packages/WidgetUI/Sources/WidgetUI/WidgetAppearance.swift:197` |
| `WidgetController` | class:TelegramGenericViewController |  |  |  | `packages/WidgetUI/Sources/WidgetUI/WidgetController.swift:235` |
| `WidgetRecentPeersController` | class:TelegramGenericViewController | widgetRecentTitle | Chats |  | `packages/WidgetUI/Sources/WidgetUI/WidgetRecentPeersController.swift:119` |
| `WidgetStickersController` | class:TelegramGenericViewController | emptyChatStickers | Suggest Stickers By Emoji |  | `packages/WidgetUI/Sources/WidgetUI/WidgetStickersController.swift:200` |

## docs/swift (2)

| controller | kind | title key | EN | RU | file:line |
|---|---|---|---|---|---|
| `TemplateController` | func->InputDataController | modalDone | Done |  | `docs/swift/TemplateController/TemplateController.swift:41` |
| `TemplateModalController` | func->InputDataModalController | modalDone | Done |  | `docs/swift/TemplateController/TemplateController.swift:81` |
