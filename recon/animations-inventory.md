# Полный инвентарь анимаций (авто-извлечение)

Всего вызовов: **2421** в 377 файлах. Сгенерировано скриптом `recon/tools/anims.py` по `refs/Telegram-macOS` (без Tests/tools/submodules). Колонки: тип/функция-контекст, вызов, duration, curve/timingFunction, keyPath, исходная строка. Дефолты хелперов см. в `animations.md` §0.

## Статистика длительностей (топ)

| duration | вызовов |
|---|---|
| `0.2` | 648 |
| `duration` | 269 |
| `0.3` | 84 |
| `0.25` | 61 |
| `0.35` | 46 |
| `0.4` | 46 |
| `springAnimation.settlingDuration *` | 24 |
| `0.5` | 22 |
| `0.15` | 20 |
| `Double` | 18 |
| `animationDuration` | 14 |
| `0.18` | 13 |
| `animationStyle.duration` | 13 |
| `0.6` | 12 |
| `0.45` | 11 |
| `1.0` | 10 |
| `duration / 2` | 10 |
| `0.12` | 10 |
| `duration if` | 10 |
| `2.0` | 9 |
| `4.5` | 8 |
| `transition.duration` | 7 |
| `animation.settlingDuration` | 6 |
| `scaledDuration` | 6 |
| `4.0` | 5 |
| `0.1` | 5 |
| `springAnimation.settlingDuration` | 5 |
| `DynamicCounterTextView.rollingMotionDuration` | 5 |
| `3.0` | 5 |
| `2.5` | 4 |

## Статистика кривых (топ)

| curve | вызовов |
|---|---|
| `.spring` | 130 |
| `timingFunction` | 118 |
| `.easeOut` | 102 |
| `.easeInEaseOut` | 37 |
| `CAMediaTimingFunctionName` | 35 |
| `CAMediaTimingFunctionName.spring` | 22 |
| `.linear` | 22 |
| `animationStyle.function` | 19 |
| `curve.timingFunction` | 15 |
| `Self.timingFunction` | 7 |
| `transition.timingFunction` | 6 |
| `CAMediaTimingFunctionName.easeOut` | 3 |
| `.easeInOut` | 2 |
| `.default` | 2 |
| `.easeIn` | 2 |
| `AnimationCurve` | 1 |
| `CAMediaTimingFunctionName.linear` | 1 |

## AlertsUI (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/AlertsUI/Sources/AlertsUI/ModalAlertController.swift:645` | DisclaimerView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AlertsUI/Sources/AlertsUI/ModalAlertController.swift:646` | DisclaimerView.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `packages/AlertsUI/Sources/AlertsUI/ModalAlertController.swift:671` | DisclaimerView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AlertsUI/Sources/AlertsUI/ModalAlertController.swift:672` | DisclaimerView.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |

## AudioPlayerUI (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/AudioPlayerUI/Sources/AudioPlayerUI/PlayerListController.swift:407` | PlayerListControlsView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak current] _ in` |
| `packages/AudioPlayerUI/Sources/AudioPlayerUI/PlayerListController.swift:425` | PlayerListControlsView.update | `animateAlpha` | 0.2 |  |  | `trackView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AudioPlayerUI/Sources/AudioPlayerUI/PlayerListController.swift:505` | PlayerListControlsView.updateScroll | `change` |  |  |  | `separator.change(opacity: position.rect.minY > tableFrame.height ? 1 : 0)` |
| `packages/AudioPlayerUI/Sources/AudioPlayerUI/InlineAudioPlayerView.swift:532` | ContextObject.update | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |

## AuthUI (7)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/AuthUI/Sources/AuthUI/Auth_AwaitingReset.swift:182` | Auth_AwaitingResetView.updateTimerValue | `change` |  |  |  | `resetIn.change(opacity: timerSeconds > 0 ? 1 : 0)` |
| `packages/AuthUI/Sources/AuthUI/Auth_Token.swift:223` | Auth_TokenView.update | `change` | 1.2 | .spring |  | `self?.imageView.change(opacity: 1, animated: true, duration: 1.2, timingFunction: .spring)` |
| `packages/AuthUI/Sources/AuthUI/Auth_Token.swift:224` | Auth_TokenView.update | `change` | 1.2 | .spring |  | `self?.animationContainer.change(opacity: 0, animated: true, duration: 1.2, timingFunction: .spring, completion: { [weak self] _ in` |
| `packages/AuthUI/Sources/AuthUI/AuthController.swift:167` | AuthView.showLanguage | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AuthUI/Sources/AuthUI/AuthController.swift:185` | AuthView.updateBack | `change` |  |  |  | `self.back.change(opacity: isHidden ? 0 : 1, animated: animated)` |
| `packages/AuthUI/Sources/AuthUI/AuthController.swift:1351` | State.set | `animateAlpha` | 0.2 |  |  | `controller.view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, completion: { [weak controller] completed in` |
| `packages/AuthUI/Sources/AuthUI/AuthController.swift:1357` | State.set | `animateScaleSpring` | 0.3 |  |  | `controller.view.layer?.animateScaleSpring(from: 1.15, to: 1.0, duration: 0.3, bounce: false)` |

## AvatarEditorUI (23)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/VideoEditorScrubbler.swift:403` | VideoEditorScrubblerControl.apply | `change` |  |  |  | `self.scrubber.change(opacity: values.paused && !values.suspended ? 0 : 1, animated: !values.paused)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:331` | CursorView.applyFg | `animateAlpha` | 0.2 |  |  | `foregroundTextView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:332` | CursorView.applyFg | `animateScaleSpring` | 0.2 |  |  | `foregroundTextView.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:367` | CursorView.applyFg | `animateAlpha` | 0.2 |  |  | `foregroundView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:368` | CursorView.applyFg | `animateScaleSpring` | 0.2 |  |  | `foregroundView.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:805` | HeaderView.updateContent | `animateAlpha` | 0.2 |  |  | `initiedContent.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/AvatarConstructorController.swift:898` | AvatarConstructorView.previewPremium | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:53` | PeerInfoPhotoEditableView.withUpdatedProgress | `change` |  |  |  | `self?.backgroundView.change(opacity: 0.8, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:54` | PeerInfoPhotoEditableView.withUpdatedProgress | `change` |  |  |  | `self?.camera.change(opacity: 0.8, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:60` | PeerInfoPhotoEditableView.withUpdatedProgress | `change` |  |  |  | `self?.backgroundView.change(opacity: 1.0, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:61` | PeerInfoPhotoEditableView.withUpdatedProgress | `change` |  |  |  | `self?.camera.change(opacity: 1.0, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:67` | PeerInfoPhotoEditableView.withUpdatedProgress | `change` |  |  |  | `self?.backgroundView.change(opacity: 1.0, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:68` | PeerInfoPhotoEditableView.withUpdatedProgress | `change` |  |  |  | `self?.camera.change(opacity: 1.0, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:91` | PeerInfoPhotoEditableView.updateState | `change` |  |  |  | `self.camera.change(opacity: updatingPhotoState == nil ? 1.0 : 0.0, animated: true)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:112` | PeerInfoPhotoEditableView.updateState | `animateAlpha` | 0.2 |  |  | `self.tempImageView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:120` | PeerInfoPhotoEditableView.updateState | `animateAlpha` | 0.2 |  |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak progressView] _ in` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/PeerInfoPhotoEditableView.swift:130` | PeerInfoPhotoEditableView.updateState | `animateAlpha` | 0.2 |  |  | `tempImageView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak tempImageView] _ in` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/VideoAvatarModalController.swift:35` | VideoAvatarKeyFramePreviewView.update | `animateAlpha` | 0.8 | .easeIn |  | `flash.layer?.animateAlpha(from: 1, to: 0, duration: 0.8, timingFunction: .easeIn, removeOnCompletion: false, completion: { [weak self] compl` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/VideoAvatarModalController.swift:198` | VideoAvatarModalView.setKeyFrame | `animateScale` | 0.23 |  |  | `keyFramePreview.layer?.animateScale(from: 1, to: 30 / keyFramePreview.frame.width, duration: 0.23, removeOnCompletion: false)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/VideoAvatarModalController.swift:199` | VideoAvatarModalView.setKeyFrame | `animatePosition` | 0.3 |  |  | `keyFramePreview.layer?.animatePosition(from: keyFramePreview.frame.origin, to: point, duration: 0.3, removeOnCompletion: false, completion: ` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/VideoAvatarModalController.swift:200` | VideoAvatarModalView.setKeyFrame | `animateAlpha` | 0.2 |  |  | `keyFrameDotView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/Avatar_BgListView.swift:174` | Container.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarEditorUI/Sources/AvatarEditorUI/Avatar_BgListView.swift:307` | ColorPreviewView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## AvatarUI (27)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/AvatarUI/Sources/AvatarUI/AvatarContentView.swift:156` | AvatarContentView.updateLayout | `change` |  |  |  | `self.unclippedView.change(opacity: isClipped ? 0.0 : 1.0, animated: animated)` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarContentView.swift:157` | AvatarContentView.updateLayout | `change` |  |  |  | `self.clippedView.change(opacity: isClipped ? 1.0 : 0.0, animated: animated)` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarContentView.swift:252` | AvatarContentLayer.updateLayout | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: from, to: CGFloat(target), duration: 0.2, timingFunction: .easeOut)` |
| `packages/AvatarUI/Sources/AvatarUI/ApplyAvatarStack.swift:17` | .applyAvatarStack | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [we` |
| `packages/AvatarUI/Sources/AvatarUI/ApplyAvatarStack.swift:20` | .applyAvatarStack | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 1.0, to: 0.2, duration: duration)` |
| `packages/AvatarUI/Sources/AvatarUI/ApplyAvatarStack.swift:35` | .applyAvatarStack | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: NSMakePoint(CGFloat(index) * (photoSize.width - 18), 0), to: control.frame.origin, timingFunction: timi` |
| `packages/AvatarUI/Sources/AvatarUI/ApplyAvatarStack.swift:37` | .applyAvatarStack | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/AvatarUI/Sources/AvatarUI/ApplyAvatarStack.swift:38` | .applyAvatarStack | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration)` |
| `packages/AvatarUI/Sources/AvatarUI/ApplyAvatarStack.swift:47` | .applyAvatarStack | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, add` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryIndicatorComponent.swift:85` | Params.updateAnimations | `CABasicAnimation` | 2.0 |  | transform.rotation.z | `let rotationAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryIndicatorComponent.swift:86` | Params.updateAnimations | `.duration =` | 2.0 |  |  | `rotationAnimation.duration = 2.0` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryIndicatorComponent.swift:101` | Params.updateAnimations | `CABasicAnimation` | 4.0 |  | transform.rotation.z | `let rotationAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryIndicatorComponent.swift:102` | Params.updateAnimations | `.duration =` | 4.0 |  |  | `rotationAnimation.duration = 4.0` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryIndicatorComponent.swift:110` | Params.updateAnimations | `CAKeyframeAnimation` |  |  | strokeStart | `let dashAnimation = CAKeyframeAnimation(keyPath: "strokeStart")` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryIndicatorComponent.swift:119` | Params.updateAnimations | `.duration =` | 2.5 |  |  | `dashAnimation.duration = 2.5` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryControl.swift:77` | AvatarStoryControl.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarStoryControl.swift:78` | AvatarStoryControl.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarUI/Sources/AvatarUI/AvatarLayer.swift:258` | AvatarImageRenderer.setSignal | `animateContents` |  |  |  | `strongSelf.host?.avatarHostLayer?.animateContents()` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryIndicatorComponent.swift:85` | Params.updateAnimations | `CABasicAnimation` | 2.0 |  | transform.rotation.z | `let rotationAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryIndicatorComponent.swift:86` | Params.updateAnimations | `.duration =` | 2.0 |  |  | `rotationAnimation.duration = 2.0` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryIndicatorComponent.swift:101` | Params.updateAnimations | `CABasicAnimation` | 4.0 |  | transform.rotation.z | `let rotationAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryIndicatorComponent.swift:102` | Params.updateAnimations | `.duration =` | 4.0 |  |  | `rotationAnimation.duration = 4.0` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryIndicatorComponent.swift:110` | Params.updateAnimations | `CAKeyframeAnimation` |  |  | strokeStart | `let dashAnimation = CAKeyframeAnimation(keyPath: "strokeStart")` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryIndicatorComponent.swift:119` | Params.updateAnimations | `.duration =` | 2.5 |  |  | `dashAnimation.duration = 2.5` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryControl.swift:77` | AvatarStoryControl.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarStoryControl.swift:78` | AvatarStoryControl.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/AvatarUI/Sources/AvatarUIShare/AvatarLayer.swift:258` | AvatarImageRenderer.setSignal | `animateContents` |  |  |  | `strongSelf.host?.avatarHostLayer?.animateContents()` |

## BoostUI (1)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/BoostUI/Sources/BoostUI/BoostChannelModalController.swift:599` | LineView.set | `animateAlpha` | 0.2 |  |  | `text.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## BusinessUI (3)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/BusinessUI/Sources/BusinessUI/PeerInfoBusinessItems.swift:542` | Day.set | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/BusinessUI/Sources/BusinessUI/BusinessQuickReplyController.swift:334` | QuickReplyRowItemView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/BusinessUI/Sources/BusinessUI/BusinessQuickReplyController.swift:378` | QuickReplyRowItemView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## CalendarUI (5)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/CalendarUI/Sources/CalendarUI/ChatCalendarHeaderRowItem.swift:84` | ChatCalendarHeaderRowView.updateColors | `change` |  |  |  | `borderView.change(opacity: header ? 1 : 0, animated: true)` |
| `packages/CalendarUI/Sources/CalendarUI/ChatCalendarHeaderRowItem.swift:109` | ChatCalendarHeaderRowView.set | `change` |  |  |  | `borderView.change(opacity: 0, animated: animated)` |
| `packages/CalendarUI/Sources/CalendarUI/CalendarMonthController.swift:278` | CalendarMonthView.updateDayPreviews | `animateAlpha` | 0.2 |  |  | `preview.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/CalendarUI/Sources/CalendarUI/CalendarMonthController.swift:279` | CalendarMonthView.updateDayPreviews | `animateAlpha` | 0.16 |  |  | `day.layer?.animateAlpha(from: 0, to: 1, duration: 0.16)` |
| `packages/CalendarUI/Sources/CalendarUI/CalendarMonthController.swift:280` | CalendarMonthView.updateDayPreviews | `animateAlpha` | 0.2 |  |  | `previous?.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak previous] _ in` |

## CallVideoLayer (17)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:246` | Channel.present | `animate` |  |  |  | `transition.animate(from: transition.local(rect), to: transition.local(frame), cornerRadius: cornerRadius, opening: true, sourceView: source?` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:256` | Channel.present | `NSAnimationContext.runAnimationGroup` | CallWindowTransition.fadeDuration |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:257` | Channel.present | `.duration =` | CallWindowTransition.fadeDuration |  |  | `context.duration = CallWindowTransition.fadeDuration` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:293` | Channel.collapse | `animate` |  |  |  | `transition.animate(from: transition.local(frame), to: transition.local(rect), cornerRadius: cornerRadius, opening: false, sourceView: source` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:345` | Channel.animate | `animate` |  |  |  | `private func animate(from start: NSRect, to end: NSRect, cornerRadius: CGFloat, opening: Bool, sourceView: NSView?, completion: @escaping ()` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:486` | Channel.keyframes | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:489` | Channel.keyframes | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:512` | Channel.popIn | `animateScaleCenter` | 0.3 |  |  | `content.layer?.animateScaleCenter(from: 1.04, to: 1, duration: 0.3)` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:514` | Channel.popIn | `NSAnimationContext.runAnimationGroup` | 0.2 |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:515` | Channel.popIn | `.duration =` | 0.2 |  |  | `context.duration = 0.2` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:522` | Channel.popOut | `animateScaleCenter` | 0.3 |  |  | `content.layer?.animateScaleCenter(from: 1, to: 1.04, duration: 0.3, removeOnCompletion: false)` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:524` | Channel.popOut | `NSAnimationContext.runAnimationGroup` | 0.3 |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/CallVideoLayer/Sources/CallWindowTransition.swift:525` | Channel.popOut | `.duration =` | 0.3 |  |  | `context.duration = 0.3` |
| `packages/CallVideoLayer/Sources/CallBlobView.swift:42` | CallBlobView.updateLevel | `animateTransform` |  |  |  | `self.blob.animateTransform()` |
| `packages/CallVideoLayer/Sources/CallBlobView.swift:49` | CallBlobView.setColor | `animateBackground` |  |  |  | `self.maskLayer.animateBackground()` |
| `packages/CallVideoLayer/Sources/CallBackgroundLayer.swift:190` | RenderState.update | `animate` | 2.0 | .easeInOut |  | `self.phaseAcceleration.animate(from: 1.0, to: 0.0, duration: 2.0, curve: .easeInOut)` |
| `packages/CallVideoLayer/Sources/Animation/Animation.swift:146` | AnimatedProperty.animate | `animate` | Double | AnimationCurve |  | `public func animate(from: T, to: T, duration: Double, curve: AnimationCurve) {` |

## CallsUI (76)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:68` | CallControl.updateLoading | `animateAlpha` | 0.4 |  |  | `progressView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.4)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:80` | CallControl.updateLoading | `animateAlpha` | 0.4 |  |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.4, removeOnCompletion: false, completion: { [weak progressView] _ in` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:108` | CallControl.stateDidUpdate | `_change` |  |  |  | `imageBackgroundView?._change(opacity: 0.9)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:109` | CallControl.stateDidUpdate | `change` | 0.2 |  |  | `textView?.change(opacity: 0.9)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:111` | CallControl.stateDidUpdate | `animateScaleCenter` | 0.2 |  |  | `imageBackgroundView?.layer?.animateScaleCenter(from: 1, to: 0.95, duration: 0.2, removeOnCompletion: false)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:114` | CallControl.stateDidUpdate | `_change` |  |  |  | `imageBackgroundView?._change(opacity: 1.0)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:115` | CallControl.stateDidUpdate | `change` | 0.2 |  |  | `textView?.change(opacity: 1.0)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:117` | CallControl.stateDidUpdate | `animateScaleCenter` | 0.2 |  |  | `imageBackgroundView?.layer?.animateScaleCenter(from: 0.95, to: 1.0, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:126` | CallControl.updateEnabled | `change` |  |  |  | `change(opacity: enabled ? 1 : 0.7, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:154` | CallControl.updateWithData | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:162` | CallControl.updateWithData | `animateAlpha` | 0.2 |  |  | `textView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak textView] _ in` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:229` | CallControl.updateWithData | `_change` |  |  |  | `imageBackgroundView!._change(size: data.iconSize, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:234` | CallControl.updateWithData | `change` |  |  |  | `change(size: NSMakeSize(data.iconSize.width, data.iconSize.height + 5 + textView.frame.height), animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:236` | CallControl.updateWithData | `_change` |  |  |  | `imageView._change(pos: imageBackgroundView!.focus(imageView.frame.size).origin, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:237` | CallControl.updateWithData | `_change` |  |  |  | `textView._change(pos: NSMakePoint(floorToScreenPixels(backingScaleFactor, (frame.width - textView.frame.width) / 2), imageBackgroundView!.fr` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:238` | CallControl.updateWithData | `_change` |  |  |  | `imageBackgroundView!._change(pos: NSMakePoint(floorToScreenPixels(backingScaleFactor, (frame.width - imageBackgroundView!.frame.width) / 2),` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:240` | CallControl.updateWithData | `change` |  |  |  | `change(size: data.iconSize, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:241` | CallControl.updateWithData | `_change` |  |  |  | `imageView._change(pos: imageBackgroundView!.focus(imageView.frame.size).origin, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallControl.swift:242` | CallControl.updateWithData | `_change` |  |  |  | `imageBackgroundView!._change(pos: focus(imageBackgroundView!.frame.size).origin, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:126` | PTTMode.toggleMode | `change` |  |  |  | `button.change(size: NSMakeSize(textView.frame.width + 20, containerView.frame.height - 8), animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:127` | PTTMode.toggleMode | `change` |  |  |  | `button.change(pos: NSMakePoint(containerView.frame.width - button.frame.width - 4, button.frame.minY), animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:130` | PTTMode.toggleMode | `animateAlpha` | 0.2 |  |  | `textView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:134` | PTTMode.toggleMode | `animateAlpha` | 0.2 |  |  | `textView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak textView] _ in` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:148` | PTTMode.toggleMode | `animateBackground` |  |  |  | `button.layer?.animateBackground()` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:152` | PTTMode.toggleMode | `change` |  |  |  | `shimmerView.change(opacity: 0, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:155` | PTTMode.toggleMode | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/CallsUI/Sources/CallsUI/PushToTalkRowItem.swift:158` | PTTMode.toggleMode | `.duration =` | 0.8 |  |  | `animation.duration = 0.8` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:165` | State.setupProgressAnimations | `CABasicAnimation` | 1.0 |  | transform.rotation.z | `let animation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:167` | State.setupProgressAnimations | `.duration =` | 1.0 |  |  | `animation.duration = 1.0` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:174` | State.setupProgressAnimations | `CABasicAnimation` |  |  | strokeEnd | `let shrinkAnimation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:177` | State.setupProgressAnimations | `.duration =` | 1.0 |  |  | `shrinkAnimation.duration = 1.0` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:180` | State.setupProgressAnimations | `CABasicAnimation` |  |  | strokeEnd | `let growthAnimation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:183` | State.setupProgressAnimations | `.duration =` | 1.0 |  |  | `growthAnimation.duration = 1.0` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:186` | State.setupProgressAnimations | `CABasicAnimation` |  |  | transform.rotation.z | `let rotateAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:190` | State.setupProgressAnimations | `.duration =` | 1.0 |  |  | `rotateAnimation.duration = 1.0` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:196` | State.setupProgressAnimations | `.duration =` | 2.0 |  |  | `groupAnimation.duration = 2.0` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:224` | State.updateStateColors | `animate` | 0.2 | .easeInEaseOut | colors | `self.foregroundGradientLayer.animate(from: previousColors as AnyObject, to: gradientColors as AnyObject, keyPath: "colors", timingFunction: ` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:266` | State.playBlobsDisappearanceAnimation | `animateScale` | 0.15 |  |  | `self.blobLayer.animateScale(from: 1.0, to: 0, duration: 0.15, removeOnCompletion: false)` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:313` | State.playConnectionAnimation | `CABasicAnimation` |  |  | strokeEnd | `let growthAnimation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:316` | State.playConnectionAnimation | `.duration =` | duration |  |  | `growthAnimation.duration = duration` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:319` | State.playConnectionAnimation | `CABasicAnimation` |  |  | transform.rotation.z | `let rotateAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:323` | State.playConnectionAnimation | `.duration =` | duration |  |  | `rotateAnimation.duration = duration` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:328` | State.playConnectionAnimation | `.duration =` | duration |  |  | `groupAnimation.duration = duration` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:344` | State.playConnectionAnimation | `animateSpring` | 0.45 |  | transform.scale | `self.blobLayer.animateSpring(from: 0.1 as NSNumber, to: 1.0 as NSNumber, keyPath: "transform.scale", duration: 0.45)` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:345` | State.playConnectionAnimation | `animateAlpha` | 0.15 |  |  | `self.blobLayer.animateAlpha(from: 0.0, to: 1.0, duration: 0.15)` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:350` | State.playConnectionAnimation | `CABasicAnimation` |  |  | transform.scale | `let shrinkAnimation = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:353` | State.playConnectionAnimation | `.duration =` | 0.15 |  |  | `shrinkAnimation.duration = 0.15` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:457` | State.updateColors | `animate` | 0.3 | .linear | fillColor | `self.backgroundCircleLayer.animate(from: previousColor, to: targetColor, keyPath: "fillColor", timingFunction: .linear, duration: 0.3)` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:458` | State.updateColors | `animate` | 0.3 | .linear | fillColor | `self.foregroundCircleLayer.animate(from: previousColor, to: targetColor, keyPath: "fillColor", timingFunction: .linear, duration: 0.3)` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:658` | VoiceChatBlobLayer.setColor | `animate` | 0.2 | .easeInEaseOut | contentsMultiplyColor | `metalBlobs.animate(from: previousColor, to: color.cgColor, keyPath: "contentsMultiplyColor", timingFunction: .easeInEaseOut, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/VoiceChatActionButton.swift:797` | BlobLayer.setColor | `animate` | 0.2 | .easeInEaseOut | fillColor | `shapeLayer.animate(from: previousColor, to: color.cgColor, keyPath: "fillColor", timingFunction: .easeInEaseOut, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturerWindow.swift:244` | Micro.swapView | `animateAlpha` | 0.2 |  |  | `previous.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak previous] _ in` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturerWindow.swift:253` | Micro.swapView | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/CallNavigationHeaderView.swift:437` | CallNavigationHeaderView.updateState | `animateBackground` |  |  |  | `backgroundView.layer?.animateBackground()` |
| `packages/CallsUI/Sources/CallsUI/CallNavigationHeaderView.swift:450` | CallNavigationHeaderView.updateState | `change` |  |  |  | `muteControl.change(opacity: 0.8, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallNavigationHeaderView.swift:451` | CallNavigationHeaderView.updateState | `change` |  |  |  | `endCall.change(opacity: 0.8, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallNavigationHeaderView.swift:452` | CallNavigationHeaderView.updateState | `_change` |  |  |  | `statusTextView._change(opacity: 0.8, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/CallNavigationHeaderView.swift:453` | CallNavigationHeaderView.updateState | `_change` |  |  |  | `callInfo._change(opacity: 0.8, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallAvatarView.swift:107` | GroupCallAvatarView.updateAudioLevel | `_change` |  |  |  | `playbackAudioLevelView._change(opacity: (value != nil \|\| data.isSpeaking) ? 1 : 0, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallInviteRowItem.swift:122` | GroupCallInviteRowView.set | `change` |  |  |  | `textView.change(opacity: item.isVertical ? 0 : 1, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallInviteRowItem.swift:131` | GroupCallInviteRowView.set | `change` |  |  |  | `thumbView.change(pos: NSMakePoint(floorToScreenPixels(backingScaleFactor, (160 - thumbView.frame.width) / 2), floorToScreenPixels(backingSca` |
| `packages/CallsUI/Sources/CallsUI/GroupCallInviteRowItem.swift:133` | GroupCallInviteRowView.set | `change` |  |  |  | `thumbView.change(pos: NSMakePoint(item.viewType.innerInset.left, floorToScreenPixels(backingScaleFactor, (containerView.frame.height - thumb` |
| `packages/CallsUI/Sources/CallsUI/GroupCallInviteRowItem.swift:134` | GroupCallInviteRowView.set | `change` |  |  |  | `textView.change(pos: NSMakePoint(thumbView.frame.maxX + 20, floorToScreenPixels(backingScaleFactor, (containerView.frame.height - textView.f` |
| `packages/CallsUI/Sources/CallsUI/CallRatingModalViewController.swift:85` | CallRatingModalView.updateState | `change` |  |  |  | `rating.change(pos: focus(rating.frame.size).origin, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturePreviewItem.swift:152` | DesktopCaptureSourceMacView.viewClass | `change` |  |  |  | `self?.picture.change(opacity: 1)` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturePreviewItem.swift:158` | DesktopCaptureSourceMacView.viewClass | `change` |  |  |  | `self?.picture.change(opacity: 1)` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturePreviewItem.swift:164` | DesktopCaptureSourceMacView.viewClass | `change` |  |  |  | `self?.picture.change(opacity: 0)` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturePreviewItem.swift:182` | DesktopCaptureSourceMacView.stateDidUpdate | `change` |  |  |  | `self.picture.change(opacity: 0)` |
| `packages/CallsUI/Sources/CallsUI/DesktopCapturePreviewItem.swift:186` | DesktopCaptureSourceMacView.stateDidUpdate | `change` |  |  |  | `self.picture.change(opacity: 1)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:211` | GroupCallRecorderRowView.set | `animateAlpha` | 0.2 |  |  | `statusView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:224` | GroupCallRecorderRowView.set | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:228` | GroupCallRecorderRowView.set | `.duration =` | 1.0 |  |  | `animation.duration = 1.0` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:246` | GroupCallRecorderRowView.set | `change` |  |  |  | `textView.change(pos: titlePos, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:263` | GroupCallRecorderRowView.set | `animateAlpha` | 0.2 |  |  | `statusView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false,completion: { [weak statusView] _ in` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:269` | GroupCallRecorderRowView.set | `change` |  |  |  | `textView.change(pos: titlePos, animated: animated)` |
| `packages/CallsUI/Sources/CallsUI/GroupCallRecorderRowItem.swift:274` | GroupCallRecorderRowView.set | `animateAlpha` | 0.2 |  |  | `indicator.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false,completion: { [weak indicator] _ in` |

## ChannelAdminUI (1)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ChannelAdminUI/Sources/ChannelAdminUI/ChannelEventLogController.swift:221` | ChannelEventLogView.showSearch | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: NSMakePoint(0, -current.frame.height), to: NSMakePoint(0, ChannelEventLogView.searchTopInset))` |

## ChannelSettingsUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ChannelSettingsUI/Sources/ChannelSettingsUI/EmptyGroupstickerSearchRowItem.swift:58` | EmptyGroupstickerSearchRowView.set | `change` |  |  |  | `self.containerView.change(size: contentRect.size, animated: animated, corners: item.viewType.corners)` |
| `packages/ChannelSettingsUI/Sources/ChannelSettingsUI/EmptyGroupstickerSearchRowItem.swift:59` | EmptyGroupstickerSearchRowView.set | `change` |  |  |  | `self.containerView.change(pos: contentRect.origin, animated: animated)` |

## ChatHistoryModel (8)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/ChatAccessoryModel.swift:109` | ChatAccessoryTextContent.updateDrawingGeometry | `animateBounds` | duration | curve.timingFunction |  | `drawingLayer.animateBounds(from: previous, to: drawingBounds, duration: duration, timingFunction: curve.timingFunction)` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/ChatAccessoryModel.swift:114` | ChatAccessoryTextContent.updateDrawingGeometry | `animatePosition` | duration | curve.timingFunction |  | `drawingLayer.animatePosition(from: previous, to: drawingPosition, duration: duration, timingFunction: curve.timingFunction)` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/ChatAccessoryModel.swift:556` | ChatAccessoryView.updateModel | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/InputTextDataRowItem.swift:618` | InputTextDataRowView.set | `animateAlpha` | 0.2 |  |  | `placeholderAction!.layer?.animateAlpha(from: 0, to: 2, duration: 0.2)` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/InputTextDataRowItem.swift:720` | InputTextDataRowView.set | `change` |  |  |  | `self.textView.change(opacity: item.enabled ? 1 : 0.5, animated: animated)` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/InputSwapSuggestionsPanel.swift:230` | Entry.apply | `animateAlpha` | 0.2 |  |  | `self.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/InputSwapSuggestionsPanel.swift:320` | Entry.adjustBackground | `animateFrame` |  |  |  | `self.backgroundLayer.animateFrameFast()` |
| `packages/ChatHistoryModel/Sources/ChatHistoryModel/InputSwapSuggestionsPanel.swift:322` | Entry.adjustBackground | `animateShadow` |  |  |  | `self.backgroundLayer.animateShadow()` |

## ChatListUI (127)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:691` | Control.update | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:692` | Control.update | `animateScaleSpring` | 0.5 |  |  | `view.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.5, bounce: true)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:721` | Control.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:722` | Control.update | `animateScaleSpring` | 0.5 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.5, bounce: true)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:738` | Control.update | `animateBorder` |  |  |  | `view.layer?.animateBorder()` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:739` | Control.update | `animateCornerRadius` |  |  |  | `view.layer?.animateCornerRadius()` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:896` | TitleKey.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:1330` | PeerListContainerView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:1358` | PeerListContainerView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:1376` | PeerListContainerView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:1480` | PeerListContainerView.updateScroller | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:1956` | PeerListContainerView.applyRemovalUndoVisibility | `animateAlpha` | 0.2 | .easeInEaseOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeInEaseOut)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:1994` | PeerListContainerView.applyDownloadsVisibility | `animateAlpha` | 0.2 | .easeInEaseOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeInEaseOut)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3310` | PeersListController.showSearchController | `animateAlpha` | 0.25 |  |  | `container.layer?.animateAlpha(from: 0.0, to: 1.0, duration: 0.25, completion:{ [weak self] complete in` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3315` | PeersListController.showSearchController | `animateScaleSpring` | 0.4 | .spring |  | `container.layer?.animateScaleSpring(from: 1.05, to: 1.0, duration: 0.4, bounce: false)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3316` | PeersListController.showSearchController | `animatePosition` | 0.4 | .spring |  | `container.layer?.animatePosition(from: NSMakePoint(rect.minX, rect.minY + 15), to: rect.origin, duration: 0.4, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3323` | PeersListController.showSearchController | `change` |  |  |  | `self.genericView.tableView.change(opacity: 0, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3325` | PeersListController.showSearchController | `_change` |  |  |  | `sibling.view._change(opacity: 0, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3349` | PeersListController.hideSearchController | `change` |  |  |  | `self.genericView.tableView.change(opacity: 1, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3351` | PeersListController.hideSearchController | `_change` |  |  |  | `sibling.view._change(opacity: 1, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3354` | PeersListController.hideSearchController | `_change` | 0.25 | .spring |  | `container._change(opacity: 0, animated: animated, duration: 0.25, timingFunction: .spring, completion: { [weak container] completed in` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3358` | PeersListController.hideSearchController | `animateScaleSpring` | 0.4 |  |  | `container.layer?.animateScaleSpring(from: 1.0, to: 1.05, duration: 0.4, removeOnCompletion: false, bounce: false)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3679` | PeersListController.setToPreviousController | `change` |  |  |  | `genericView.backgroundView.change(opacity: 0, animated: true)` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3726` | PeersListController.viewWillDisappear | `_change` |  |  |  | `self.searchSection?.view._change(opacity: 0, animated: true, completion: { [weak self] completed in` |
| `packages/ChatListUI/Sources/ChatListUI/PeersListController.swift:3743` | PeersListController.viewWillAppear | `_change` |  |  |  | `self.searchSection?.view._change(opacity: 1, animated: true)` |
| `packages/ChatListUI/Sources/ChatListUI/DownloadsControl.swift:127` | DownloadsControl.update | `change` |  |  |  | `self.progressView.change(opacity: 1, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/DownloadsControl.swift:130` | DownloadsControl.update | `change` |  |  |  | `self.progressView.change(opacity: 0, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/DownloadsControl.swift:134` | DownloadsControl.update | `change` |  |  |  | `self.progressView.change(opacity: 0, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatRemovalUndoView.swift:101` | ChatRemovalUndoView.startRing | `CABasicAnimation` |  |  | strokeEnd | `let animation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/ChatListUI/Sources/ChatListUI/ChatRemovalUndoView.swift:104` | ChatRemovalUndoView.startRing | `.duration =` | remaining |  |  | `animation.duration = remaining` |
| `packages/ChatListUI/Sources/ChatListUI/ChatRemovalUndoView.swift:143` | ChatRemovalUndoView.updateSeconds | `animateAlpha` | 0.12 |  |  | `previous.layer?.animateAlpha(from: 1, to: 0, duration: 0.12, removeOnCompletion: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatRemovalUndoView.swift:144` | ChatRemovalUndoView.updateSeconds | `animatePosition` | 0.12 |  |  | `previous.layer?.animatePosition(from: previous.frame.origin, to: NSMakePoint(previous.frame.minX, previous.frame.minY + 10), duration: 0.12,` |
| `packages/ChatListUI/Sources/ChatListUI/ChatRemovalUndoView.swift:155` | ChatRemovalUndoView.updateSeconds | `animateAlpha` | 0.12 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.12)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatRemovalUndoView.swift:156` | ChatRemovalUndoView.updateSeconds | `animatePosition` | 0.12 |  |  | `view.layer?.animatePosition(from: NSMakePoint(view.frame.minX, view.frame.minY - 10), to: view.frame.origin, duration: 0.12)` |
| `packages/ChatListUI/Sources/ChatListUI/SearchController.swift:2130` | SearchController.fadeOutShimmer | `animate` | 0.2 | .easeOut | opacity | `view.layer?.animate(from: 1 as NSNumber, to: 0 as NSNumber, keyPath: "opacity", timingFunction: .easeOut, duration: 0.2, removeOnCompletion:` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:693` | ChatListExpandView.animateOnce | `animateScaleSpring` | 0.35 |  |  | `container.layer?.animateScaleSpring(from: 0.7, to: 1, duration: 0.35, removeOnCompletion: true, bounce: true, completion: nil)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:721` | ChatListExpandView.chatListAnimateLayerFrame | `animateBounds` | 0.2 | .easeOut |  | `layer.animateBounds(from: presentBounds, to: NSMakeRect(0, 0, frame.width, frame.height), duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:729` | ChatListExpandView.chatListAnimateLayerFrame | `animatePosition` | 0.2 | .easeOut |  | `layer.animatePosition(from: presentOrigin, to: frame.origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1059` | DrawLayer.remove | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(from), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak layer` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1347` | ForumTopicArrow.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let animation: CABasicAnimation = makeSpringAnimation("opacity")` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1642` | ForumTopicArrow.updateColors | `animateAlpha` | 0.2 |  |  | `selectionBackgroundLayer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1644` | ForumTopicArrow.updateColors | `animateAlpha` | 0.2 |  |  | `selectionBackgroundLayer.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak self] _ in` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1746` | ForumTopicArrow.set | `change` |  |  |  | `contentView.change(opacity: unhideProgress ?? (item.shouldHideContent ? 0 : 1), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1747` | ForumTopicArrow.set | `change` |  |  |  | `contentView.change(pos: contentPoint(item), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1767` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1768` | ForumTopicArrow.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1770` | ForumTopicArrow.set | `change` |  |  |  | `current.change(pos: rect.origin, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:1771` | ForumTopicArrow.set | `change` |  |  |  | `current.change(size: rect.size, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2062` | ForumTopicArrow.set | `change` |  |  |  | `expandView?.change(pos: NSMakePoint(0, item.isCollapsed ? 0 : item.height), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2063` | ForumTopicArrow.set | `change` |  |  |  | `containerView.change(pos: NSMakePoint(0, item.isCollapsed ? -item.height : 0), animated: !revealActionInvoked && animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2208` | ForumTopicArrow.set | `animateScaleSpring` | 0.4 |  |  | `self.badgeView?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.4)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2209` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `self.badgeView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2212` | ForumTopicArrow.set | `change` |  |  |  | `badgeView?.change(pos: point, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2236` | ForumTopicArrow.set | `change` | 0.4 |  |  | `badgeShortView?.change(opacity: opacity, animated: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2238` | ForumTopicArrow.set | `animateScaleSpring` | 0.4 |  |  | `self.badgeShortView?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.4)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2239` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `self.badgeShortView?.layer?.animateAlpha(from: 0, to: opacity, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2242` | ForumTopicArrow.set | `change` |  |  |  | `badgeShortView?.change(pos: point, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2243` | ForumTopicArrow.set | `change` |  |  |  | `badgeShortView?.change(opacity: opacity, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2267` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `groupActivityView.layer?.animateAlpha(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2268` | ForumTopicArrow.set | `animateScaleSpring` | 0.3 |  |  | `groupActivityView.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.3)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2291` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `activeImage.layer?.animateAlpha(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2292` | ForumTopicArrow.set | `animateScaleSpring` | 0.3 |  |  | `activeImage.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.3)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2326` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2327` | ForumTopicArrow.set | `animateScaleSpring` | 0.3 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.3)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2358` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2359` | ForumTopicArrow.set | `animateScaleSpring` | 0.3 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.3)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2410` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2411` | ForumTopicArrow.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2449` | ForumTopicArrow.set | `animateScaleSpring` | 0.4 |  |  | `self.mentionsView?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.4)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2450` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `self.mentionsView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2453` | ForumTopicArrow.set | `change` |  |  |  | `self.mentionsView?.change(pos: point, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2486` | ForumTopicArrow.set | `animateScaleSpring` | 0.4 |  |  | `self.reactionsView?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.4)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2487` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `self.reactionsView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2490` | ForumTopicArrow.set | `change` |  |  |  | `self.reactionsView?.change(pos: point, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2523` | ForumTopicArrow.set | `animateScaleSpring` | 0.4 |  |  | `self.pollVotesView?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.4)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2524` | ForumTopicArrow.set | `animateAlpha` | 0.2 |  |  | `self.pollVotesView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2527` | ForumTopicArrow.set | `change` |  |  |  | `self.pollVotesView?.change(pos: point, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2569` | ForumTopicArrow.set | `_change` |  |  |  | `self.photoVideoView?._change(size: NSMakeSize(44, 44), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2570` | ForumTopicArrow.set | `_change` |  |  |  | `self.archivedPhoto?._change(size: NSMakeSize(44, 44), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2572` | ForumTopicArrow.set | `_change` |  |  |  | `self.photoVideoView?._change(pos: NSMakePoint(3, 3), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2573` | ForumTopicArrow.set | `_change` |  |  |  | `self.archivedPhoto?._change(pos: NSMakePoint(3, 3), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2582` | ForumTopicArrow.set | `_change` |  |  |  | `self.photoVideoView?._change(size: NSMakeSize(50, 50), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2583` | ForumTopicArrow.set | `_change` |  |  |  | `self.archivedPhoto?._change(size: NSMakeSize(50, 50), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2585` | ForumTopicArrow.set | `_change` |  |  |  | `self.photoVideoView?._change(pos: NSMakePoint(0, 0), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2586` | ForumTopicArrow.set | `_change` |  |  |  | `self.archivedPhoto?._change(pos: NSMakePoint(0, 0), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2892` | ForumTopicArrow.layoutReveal | `change` |  |  |  | `containerView.change(pos: NSMakePoint(delta, containerView.frame.minY), animated: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2893` | ForumTopicArrow.layoutReveal | `change` |  |  |  | `revealLeftView.change(pos: NSMakePoint(min(-leftRevealWidth + delta, 0), revealLeftView.frame.minY), animated: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2894` | ForumTopicArrow.layoutReveal | `change` |  |  |  | `revealRightView.change(pos: NSMakePoint(frame.width + delta, revealRightView.frame.minY), animated: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2897` | ForumTopicArrow.layoutReveal | `change` |  |  |  | `revealLeftView.change(size: NSMakeSize(max(leftRevealWidth, delta), revealLeftView.frame.height), animated: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2899` | ForumTopicArrow.layoutReveal | `change` |  |  |  | `revealRightView.change(size: NSMakeSize(max(rightRevealWidth, abs(delta)), revealRightView.frame.height), animated: false)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2913` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `action.layer?.animatePosition(from: NSMakePoint(-(revealLeftView.frame.width - action.frame.width - inset * 2), action.frame.minY), to: NSMa` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2917` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `action.layer?.animatePosition(from: NSMakePoint(-(action.frame.width + inset), action.frame.minY), to: NSMakePoint(0, 0), duration: 0.2, tim` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2934` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `action.layer?.animatePosition(from: NSMakePoint(revealLeftView.frame.width - action.frame.width - inset * 2 - (leftRevealWidth - action.fram` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2938` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `action.layer?.animatePosition(from: NSMakePoint(action.frame.width + inset, action.frame.minY), to: NSMakePoint(0, 0), duration: 0.2, timing` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2964` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `action.layer?.animatePosition(from: NSMakePoint((revealRightView.frame.width - rightRevealWidth), action.frame.minY), to: NSMakePoint(0, 0),` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2967` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `subviews[i].layer?.animatePosition(from: NSMakePoint((subviews[i].frame.width * CGFloat(i + 1)), subviews[i].frame.minY), to: NSMakePoint(0,` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2983` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `action.layer?.animatePosition(from: NSMakePoint(-(revealRightView.frame.width - rightRevealWidth), action.frame.minY), to: NSMakePoint(0, 0)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:2986` | ForumTopicArrow.layoutReveal | `animatePosition` | 0.2 | CAMediaTimingFunctionName.spring |  | `subviews[i].layer?.animatePosition(from: NSMakePoint(-(subviews[i].frame.width * CGFloat(i + 1)), subviews[i].frame.minY), to: NSMakePoint(0` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3032` | ForumTopicArrow.completeReveal | `_change` |  | .spring |  | `subview._change(pos: NSMakePoint(x, 0), animated: animated, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3035` | ForumTopicArrow.completeReveal | `_change` |  | .spring |  | `subview._change(pos: NSMakePoint(self.rightRevealWidth - subview.frame.width - inset * 2, 0), animated: animated, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3045` | ForumTopicArrow.completeReveal | `_change` |  | .spring |  | `subview._change(pos: NSMakePoint(x, 0), animated: animated, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3052` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `self.containerView.change(pos: NSMakePoint(0, self.containerView.frame.minY), animated: true, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3053` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `self.revealLeftView.change(pos: NSMakePoint(-self.revealLeftView.frame.width, self.revealLeftView.frame.minY), animated: true, timingFunctio` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3054` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `self.revealRightView.change(pos: NSMakePoint(self.frame.width, self.revealRightView.frame.minY), animated: true, timingFunction: .spring, co` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3067` | ForumTopicArrow.completeReveal | `change` | duration | .spring |  | `self.containerView.change(pos: NSMakePoint(-self.containerView.frame.width, self.containerView.frame.minY), animated: true, duration: durati` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3068` | ForumTopicArrow.completeReveal | `change` | duration | .spring |  | `self.revealRightView.change(size: NSMakeSize(self.frame.width + self.rightRevealWidth, self.revealRightView.frame.height), animated: true, d` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3069` | ForumTopicArrow.completeReveal | `change` | duration | .spring |  | `self.revealRightView.change(pos: NSMakePoint(-self.rightRevealWidth, self.revealRightView.frame.minY), animated: true, duration: duration, t` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3095` | ForumTopicArrow.completeReveal | `change` | duration | .spring |  | `containerView.change(pos: NSMakePoint(leftRevealWidth, containerView.frame.minY), animated: true, duration: duration, timingFunction: .sprin` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3096` | ForumTopicArrow.completeReveal | `change` | duration | .spring |  | `revealLeftView.change(size: NSMakeSize(leftRevealWidth, revealLeftView.frame.height), animated: true, duration: duration, timingFunction: .s` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3098` | ForumTopicArrow.completeReveal | `change` |  |  |  | `revealRightView.change(pos: NSMakePoint(frame.width, revealRightView.frame.minY), animated: true)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3103` | ForumTopicArrow.completeReveal | `change` | duration | .spring |  | `revealLeftView.change(pos: NSMakePoint(0, revealLeftView.frame.minY), animated: true, duration: duration, timingFunction: .spring, completio` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3159` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `revealRightView.change(pos: NSMakePoint(frame.width - rightRevealWidth, revealRightView.frame.minY), animated: true, timingFunction: .spring` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3160` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `revealRightView.change(size: NSMakeSize(rightRevealWidth, revealRightView.frame.height), animated: true, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3161` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `containerView.change(pos: NSMakePoint(-rightRevealWidth, containerView.frame.minY), animated: true, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3162` | ForumTopicArrow.completeReveal | `change` |  | .spring |  | `revealLeftView.change(pos: NSMakePoint(-leftRevealWidth, revealLeftView.frame.minY), animated: true, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3223` | ForumTopicArrow.updateHideProgress | `change` |  |  |  | `contentView.change(opacity: progress ?? (item.shouldHideContent ? 0 : 1), animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:3224` | ForumTopicArrow.updateHideProgress | `change` |  |  |  | `badgeShortView?.change(opacity: progress.map { 1 - $0 } ?? 1, animated: animated)` |
| `packages/ChatListUI/Sources/ChatListUI/TabBadgeItem.swift:63` | AvatarTabContainer.setSelected | `change` | 0.4 | .spring |  | `circle.change(opacity: selected ? 1 : 0, animated: animated, duration: 0.4, timingFunction: .spring)` |
| `packages/ChatListUI/Sources/ChatListUI/TabBadgeItem.swift:121` | AvatarTabContainer.updateScale | `animate` | 0.3 | .spring | transform | `layer.animate(from: NSValue(caTransform3D: current), to: NSValue(caTransform3D: target), keyPath: "transform", timingFunction: .spring, dura` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListBirthdayItem.swift:296` | ChatListBirthdayView.set | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [we` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListBirthdayItem.swift:299` | ChatListBirthdayView.set | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 1.0, to: 0.2, duration: duration)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListBirthdayItem.swift:314` | ChatListBirthdayView.set | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: NSMakePoint(CGFloat(index) * 22, 0), to: control.frame.origin, timingFunction: timingFunction)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListBirthdayItem.swift:316` | ChatListBirthdayView.set | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListBirthdayItem.swift:317` | ChatListBirthdayView.set | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration)` |
| `packages/ChatListUI/Sources/ChatListUI/ChatListBirthdayItem.swift:326` | ChatListBirthdayView.set | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, add` |
| `packages/ChatListUI/Sources/ChatListUI/GCChatListIndicator.swift:78` | GCChatListIndicator.startAnimation | `CAKeyframeAnimation` |  |  | path | `let animation = CAKeyframeAnimation(keyPath: "path")` |
| `packages/ChatListUI/Sources/ChatListUI/GCChatListIndicator.swift:82` | GCChatListIndicator.startAnimation | `.duration =` | 0.4 * 8 |  |  | `animation.duration = 0.4 * 8` |

## ChatUI (489)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:443` | Kind.update | `animateAlpha` | ChatInputSendButton.fieldFadeDuration |  |  | `newView.layer?.animateAlpha(from: 0.0, to: 1.0, duration: ChatInputSendButton.fieldFadeDuration)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:454` | Kind.update | `animateAlpha` | 0.1 |  |  | `newView.layer?.animateAlpha(from: 0.0, to: 1.0, duration: 0.1)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:455` | Kind.update | `animateScaleSpring` | 0.6 |  |  | `newView.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.6)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:457` | Kind.update | `animateAlpha` |  |  |  | `prevView.layer?.animateAlpha(from: 1.0, to: 0.0, duration: isFieldTransition ? ChatInputSendButton.fieldFadeDuration : 0.2, completion: { [w` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:504` | Kind.animateFieldTransition | `CASpringAnimation` |  |  | transform | `let scale = CASpringAnimation(keyPath: "transform")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:518` | Kind.animateFieldTransition | `CABasicAnimation` |  |  | filters.gaussianBlur.inputRadius | `let animation = CABasicAnimation(keyPath: "filters.gaussianBlur.inputRadius")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:521` | Kind.animateFieldTransition | `.duration =` | ChatInputSendButton.fieldBlurDuration |  |  | `animation.duration = ChatInputSendButton.fieldBlurDuration` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:535` | Kind.animatePlaneFlight | `CASpringAnimation` |  |  | position | `let flight = CASpringAnimation(keyPath: "position")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:561` | Kind.animateSendIconChange | `CABasicAnimation` |  |  | transform.scale | `let shrink = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:567` | Kind.animateSendIconChange | `animateAlpha` | duration | .easeInEaseOut |  | `outgoing.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: .easeInEaseOut, completion: { [weak outgoing] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:571` | Kind.animateSendIconChange | `animateAlpha` | duration | .easeInEaseOut |  | `iconLayer.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: .easeInEaseOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:572` | Kind.animateSendIconChange | `animateScaleCenter` | duration |  |  | `iconLayer.animateScaleCenter(from: scale, to: 1, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChatStickerContentView.swift:100` | ChatStickerContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatStickerContentView.swift:143` | ChatStickerContentView.removePlaceholder | `animateAlpha` | 0.2 |  |  | `placeholderView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak placeholderView] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendAsView.swift:115` | ChatInputSendAsView.update | `animateScaleSpring` | 0.3 |  |  | `view.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.3, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputSendAsView.swift:135` | ChatInputSendAsView.update | `animateScaleSpring` | 0.3 |  |  | `avatar.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/WPArticleContentView.swift:414` | WPArticleContentView.update | `change` |  |  |  | `groupedContents[i].change(size: groupLayout.frame(at: i).size, animated: false)` |
| `packages/ChatUI/Sources/ChatUI/WPArticleContentView.swift:420` | WPArticleContentView.update | `change` |  |  |  | `groupedContents[i].change(pos: groupLayout.frame(at: i).origin, animated: false)` |
| `packages/ChatUI/Sources/ChatUI/WPArticleContentView.swift:551` | WPArticleContentView.update | `animateAlpha` | 0.25 | .linear |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.25, timingFunction: .linear, removeOnCompletion: false, completion: { [weak pro` |
| `packages/ChatUI/Sources/ChatUI/ChatInputActionsView.swift:350` | ChatInputActionsView.setExtraButton | `animateScaleSpring` | 0.3 |  |  | `button.layer?.animateScaleSpring(from: scale, to: hidden ? 0.2 : 1, duration: 0.3, bounce: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputActionsView.swift:356` | ChatInputActionsView.setExtraButton | `change` |  |  |  | `button.change(opacity: hidden ? 0 : 1, animated: animated, completion: { [weak button] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageDateHeader.swift:440` | ChatDateStickView.updateDateVisibility | `change` |  |  |  | `containerView.change(opacity: CGFloat(opacity), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageDateHeader.swift:544` | ChatDateStickView.onInsert | `animateScaleSpring` | 0.4 |  |  | `self.containerView.layer?.animateScaleSpring(from: 0.5, to: 1, duration: 0.4, bounce: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageDateHeader.swift:545` | ChatDateStickView.onInsert | `animateAlpha` | 0.35 |  |  | `self.containerView.layer?.animateAlpha(from: 0, to: 1, duration: 0.35)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:242` | ReactionView.startLargeHold | `animateScaleCenter` | largeReactionHoldDuration |  |  | `self.layer?.animateScaleCenter(from: 1, to: 1.5, duration: largeReactionHoldDuration, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:265` | ReactionView.cancelLargeHold | `animateScaleCenter` | 0.2 |  |  | `self.layer?.animateScaleCenter(from: current, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:318` | ReactionView.stateDidUpdate | `animateScaleCenter` | 0.2 |  |  | `self.layer?.animateScaleCenter(from: 1, to: 0.8, duration: 0.2, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:320` | ReactionView.stateDidUpdate | `animateScaleCenter` | 0.2 |  |  | `self.layer?.animateScaleCenter(from: 0.8, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:352` | ReactionView.playAppearAnimation | `animateScaleSpring` | 0.35 |  |  | `imageView?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.35, bounce: true)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:412` | ShowMore.startLoading | `animate` | 0.25 | .spring | transform.translation.y | `layer.animate(from: NSNumber(value: Float(-offset)), to: NSNumber(value: 0), keyPath: "transform.translation.y", timingFunction: .spring, du` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:414` | ShowMore.startLoading | `CAKeyframeAnimation` |  |  | transform.translation.y | `let bounce = CAKeyframeAnimation(keyPath: "transform.translation.y")` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:609` | ShowMore.revealDidStart | `animateScaleCenter` | 0.2 |  |  | `button.layer?.animateScaleCenter(from: 1, to: 0.1, duration: 0.2, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/AddReactionManager.swift:610` | ShowMore.revealDidStart | `animateAlpha` | 0.2 |  |  | `button.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak button] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:231` | Flight.addVertical | `CASpringAnimation` |  |  | keyPath | `let animation = CASpringAnimation(keyPath: keyPath)` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:232` | Flight.addVertical | `.mass =` |  |  |  | `animation.mass = 1.0` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:233` | Flight.addVertical | `.stiffness =` |  |  |  | `animation.stiffness = ChatTextSendFlightMotion.verticalStiffness` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:234` | Flight.addVertical | `.damping =` |  |  |  | `animation.damping = ChatTextSendFlightMotion.verticalDamping` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:237` | Flight.addVertical | `.duration =` | animation.settlingDuration |  |  | `animation.duration = animation.settlingDuration` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:250` | Flight.animateFrame | `animateFrame` |  |  |  | `func animateFrame(_ layer: CALayer, from: NSRect, to: NSRect) {` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:264` | Flight.animateFrame | `animateFrame` |  |  |  | `animateFrame(mask, from: startField, to: bubble)` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:285` | Flight.animateFrame | `animateFrame` |  |  |  | `animateFrame(layer, from: startFrame, to: bubbleFrame)` |
| `packages/ChatUI/Sources/ChatUI/ChatTextSendFlight.swift:288` | Flight.animateFrame | `animateFrame` |  |  |  | `animateFrame(slice, from: startFrame.size.bounds, to: bubbleFrame.size.bounds)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3726` | Status.updateClockAnimation | `CABasicAnimation` |  |  | transform.rotation.z | `let rotation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3757` | Status.animateSent | `animateScale` | 3 * frameDuration | .linear | opacity | `handsLayer.animateScale(from: 1, to: 0, duration: 3 * frameDuration, timingFunction: .linear, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3758` | Status.animateSent | `animatePosition` | 11 * frameDuration | .default | opacity | `textLayer.animatePosition(from: Self.textSlideOffset, to: .zero, duration: 11 * frameDuration, timingFunction: .default, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3759` | Status.animateSent | `animate` | 12 * frameDuration | .default | opacity | `textLayer.animate(from: NSNumber(value: 0), to: NSNumber(value: 1), keyPath: "opacity", timingFunction: .default, duration: 12 * frameDurati` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3760` | Status.animateSent | `animateAlpha` | 13 * frameDuration | .easeOut |  | `tintLayer.animateAlpha(from: 1, to: 0, duration: 13 * frameDuration, timingFunction: .easeOut, completion: { [weak self] completed in` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3778` | Status.point | `animate` | duration | .linear | startPoint | `glintLayer.animate(from: NSValue(point: point(136, 0)), to: NSValue(point: glintLayer.startPoint), keyPath: "startPoint", timingFunction: .l` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3779` | Status.point | `animate` | duration | .linear | endPoint | `glintLayer.animate(from: NSValue(point: point(164, 12)), to: NSValue(point: glintLayer.endPoint), keyPath: "endPoint", timingFunction: .line` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:3789` | Status.point | `CAKeyframeAnimation` |  |  | opacity | `let opacity = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:4062` | ChatWalletTransferView.setAwaitingTransferFlight | `animateAlpha` | 0.15 |  |  | `badgeView.layer?.animateAlpha(from: 0, to: 1, duration: 0.15)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:4093` | ChatWalletTransferView.animateTransferFlightLanding | `CAKeyframeAnimation` |  |  | transform | `let landing = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:4243` | ChatWalletTransferView.animateSentBounce | `CAKeyframeAnimation` |  |  | transform | `let bounce = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:4265` | ChatWalletTransferView.animateDiamondLandingBump | `CAKeyframeAnimation` |  |  | transform | `let bump = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:4303` | ChatWalletTransferView.animateHighlightBump | `CAKeyframeAnimation` |  |  | transform | `let bump = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6595` | _StoryView.set | `animateAlpha` | 0.2 | .easeOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6596` | _StoryView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `current.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6616` | _StoryView.set | `animateAlpha` | 0.2 | .easeOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6617` | _StoryView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `current.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6637` | _StoryView.set | `animateAlpha` | 0.2 | .easeOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6638` | _StoryView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `current.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6658` | _StoryView.set | `animateAlpha` | 0.2 | .easeOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6659` | _StoryView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `current.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6679` | _StoryView.set | `animateAlpha` | 0.2 | .easeOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6680` | _StoryView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `current.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6699` | _StoryView.set | `animateAlpha` | 0.2 | .easeOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6700` | _StoryView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `current.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6954` | _StoryView.onInsert | `animateScaleSpring` | 0.4 |  |  | `self.layer?.animateScaleSpring(from: 0.5, to: 1, duration: 0.4, bounce: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatServiceItem.swift:6955` | _StoryView.onInsert | `animateAlpha` | 0.35 |  |  | `self.layer?.animateAlpha(from: 0, to: 1, duration: 0.35)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchView.swift:298` | ChatSearchView.cancelEmojiToken | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchView.swift:323` | ChatSearchView.cancelEmojiToken | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:77` | VoiceView.songDidChanged | `change` |  |  |  | `self.durationView.change(size: value.size, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:91` | VoiceView.songDidChangedState | `change` |  |  |  | `self.durationView.change(size: value.size, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:116` | VoiceView.songDidChangedState | `change` |  |  |  | `self.durationView.change(size: value.size, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:266` | VideoView.songDidChanged | `change` |  |  |  | `self.durationView.change(size: value.size, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:278` | VideoView.songDidChangedState | `change` |  |  |  | `self.durationView.change(size: value.size, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:287` | VideoView.songDidChangedState | `change` |  |  |  | `self.durationView.change(size: value.size, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/SingleTimeMediaViewer.swift:513` | SingleTimeMediaViewer.show | `animateBackground` |  |  |  | `showModal(with: SingleTimeMediaViewer(context: context, message: message), for: context.window, animationType: .animateBackground)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:217` | DescriptionMode.updateSendButtonCenter | `animateScaleSpring` | 0.4 |  |  | `overlayView.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.4)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:218` | DescriptionMode.updateSendButtonCenter | `animateAlpha` | 0.2 |  |  | `overlayView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:311` | DescriptionMode.updateFloatingVisibility | `change` |  |  |  | `lockControl.change(opacity: 0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:312` | DescriptionMode.updateFloatingVisibility | `change` |  |  |  | `pauseControl.change(opacity: 0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:313` | DescriptionMode.updateFloatingVisibility | `change` |  |  |  | `singleTimeControl.change(opacity: 0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:315` | DescriptionMode.updateFloatingVisibility | `change` |  |  |  | `lockControl.change(opacity: 0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:319` | DescriptionMode.updateFloatingVisibility | `animateAlpha` | 0.2 |  |  | `pauseControl.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:325` | DescriptionMode.updateFloatingVisibility | `animateAlpha` | 0.2 |  |  | `singleTimeControl.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:401` | DescriptionMode.updateDescription | `animateAlpha` | 0.2 |  |  | `descView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:588` | DescriptionMode.animateOut | `animateScaleSpring` | duration |  |  | `overlayLayer.animateScaleSpring(from: 1.0, to: 0.1, duration: duration, removeOnCompletion: false, bounce: false, completion: { _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:591` | DescriptionMode.animateOut | `animateAlpha` | fade | .spring |  | `overlayLayer.animateAlpha(from: 1, to: 0, duration: fade, timingFunction: .spring, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:600` | DescriptionMode.animateOut | `animateAlpha` | fade | .spring |  | `view.layer?.animateAlpha(from: CGFloat(from), to: 0, duration: fade, timingFunction: .spring, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:603` | DescriptionMode.animateOut | `animateAlpha` | fade | .spring |  | `layer?.animateAlpha(from: 1, to: 0, duration: fade, timingFunction: .spring, removeOnCompletion: false, completion: { _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:835` | DescriptionMode.startBlinking | `CABasicAnimation` |  |  | opacity | `let animate = CABasicAnimation(keyPath: "opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordingView.swift:839` | DescriptionMode.startBlinking | `.duration =` | 1.5 |  |  | `animate.duration = 1.5` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceContentView.swift:229` | ChatVoiceContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceContentView.swift:230` | ChatVoiceContentView.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceContentView.swift:263` | ChatVoiceContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceContentView.swift:264` | ChatVoiceContentView.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceContentView.swift:340` | ChatVoiceContentView.fillTranscribedAudio | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordModeIcon.swift:165` | Pose.apply | `.duration =` |  |  |  | `group.duration = animations.map(\.duration).max() ?? 0` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordModeIcon.swift:184` | Pose.spring | `CASpringAnimation` |  |  | keyPath | `let animation = CASpringAnimation(keyPath: keyPath)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordModeIcon.swift:185` | Pose.spring | `.mass =` |  |  |  | `animation.mass = 1` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordModeIcon.swift:186` | Pose.spring | `.stiffness =` |  |  |  | `animation.stiffness = springStiffness` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordModeIcon.swift:187` | Pose.spring | `.damping =` |  |  |  | `animation.damping = springDamping` |
| `packages/ChatUI/Sources/ChatUI/ChatInputRecordModeIcon.swift:190` | Pose.spring | `.duration =` |  |  |  | `animation.duration = animation.settlingDuration` |
| `packages/ChatUI/Sources/ChatUI/ChatFileContentView.swift:362` | ChatFileContentView.update | `animateAlpha` | 0.25 | .linear |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.25, timingFunction: .linear, removeOnCompletion: false, completion: { [weak pro` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:954` | ChatPollItemView.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let animation: CABasicAnimation = makeSpringAnimation("opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:957` | ChatPollItemView.focusAnimation | `.duration =` | 0.5 |  |  | `animation.duration = 0.5` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:994` | ChatPollItemView.onShowContextMenu | `animateAlpha` | 0.2 |  |  | `bg.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1019` | ChatPollItemView.set | `change` |  |  |  | `contentNode.change(size: NSMakeSize(contentFrameModifier(item).width, item.contentSize.height), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1290` | PollOptionView.update | `change` | duration | timingFunction |  | `borderView.change(opacity: option.percent != nil ? 0 : 1, animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1291` | PollOptionView.update | `change` | duration | timingFunction |  | `progressView.change(opacity: option.percent == nil ? 0 : 1, animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1292` | PollOptionView.update | `change` | duration | timingFunction |  | `progressBackgroundView.change(opacity: option.percent == nil ? 0 : 1, animated: animated, duration: duration, timingFunction: timingFunction` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1322` | PollOptionView.update | `animateScaleSpring` | duration | timingFunction |  | `current.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1323` | PollOptionView.update | `animateAlpha` | duration | timingFunction |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1347` | PollOptionView.update | `animateScaleSpring` | duration | timingFunction |  | `current.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1348` | PollOptionView.update | `animateAlpha` | duration | timingFunction |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1355` | PollOptionView.update | `animateScaleSpring` | duration |  |  | `view.layer?.animateScaleSpring(from: 1, to: 0.2, duration: duration, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1391` | PollOptionView.update | `animateAlpha` | duration / 2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: duration / 2)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1402` | PollOptionView.update | `CAKeyframeAnimation` | duration / 2 |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1404` | PollOptionView.update | `.duration =` | duration / 2 |  |  | `animation.duration = duration / 2` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1426` | PollOptionView.update | `CAKeyframeAnimation` | duration / 2 |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1428` | PollOptionView.update | `.duration =` | duration / 2 |  |  | `animation.duration = duration / 2` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1453` | PollOptionView.update | `animateAlpha` | duration / 2 |  |  | `pi.layer?.animateAlpha(from: 0, to: 1, duration: duration / 2)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1481` | PollOptionView.update | `animateAlpha` | duration / 2 |  |  | `sv.layer?.animateAlpha(from: 0, to: 1, duration: duration / 2)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1518` | PollOptionView.update | `animateAlpha` | duration / 2 |  |  | `sv.layer?.animateAlpha(from: 0, to: 1, duration: duration / 2)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1908` | PollView.update | `animateAlpha` | 0.3 |  |  | `contentView.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:1963` | PollView.update | `animateAlpha` | 0.2 |  |  | `option.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:2186` | PollView.update | `animateScaleSpring` | 0.3 |  |  | `solutionButton.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:2224` | PollView.update | `animateScaleSpring` | 0.3 |  |  | `timerView.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:2225` | PollView.update | `animateAlpha` | 0.3 |  |  | `timerView.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:2247` | PollView.update | `animateScaleSpring` | 0.3 |  |  | `timerView.layer?.animateScaleSpring(from: 1, to: 0, duration: 0.3, removeOnCompletion: false, completion: { [weak timerView] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatPollItem.swift:2250` | PollView.update | `animateAlpha` | 0.3 |  |  | `timerView.layer?.animateAlpha(from: 1, to: 0.2, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatRichTextRowItem.swift:703` | ChatRichTextRowView.deactivateRichContent | `change` |  |  |  | `self.rightView.change(opacity: 1.0, animated: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRichTextRowItem.swift:733` | ChatRichTextRowView.set | `change` |  |  |  | `self.rightView.change(opacity: item.isRevealAnimationActive ? 0.0 : 1.0, animated: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRichTextRowItem.swift:1117` | ChatRichTextRowView.finishReveal | `change` | 0.2 | .easeInEaseOut |  | `self.rightView.change(opacity: 1.0, animated: animateStatus, duration: 0.2, timingFunction: .easeInEaseOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputGlassSpring.swift:5` | ChatInputGlassSpring.animate | `NSAnimationContext.runAnimationGroup` | 0.5 |  |  | `NSAnimationContext.runAnimationGroup { context in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputGlassSpring.swift:6` | ChatInputGlassSpring.animate | `.duration =` | 0.5 |  |  | `context.duration = 0.5` |
| `packages/ChatUI/Sources/ChatUI/StickerMediaContentView.swift:101` | LockView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/MediaAnimatedStickerView.swift:391` | MediaAnimatedStickerView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/MediaAnimatedStickerView.swift:479` | MediaAnimatedStickerView.removePlaceholder | `animateAlpha` | 0.2 |  |  | `placeholderView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak placeholderView] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:608` | ChatGroupedView.updateSelectingState | `animateAlpha` | 0.2 |  |  | `selectingControl?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:609` | ChatGroupedView.updateSelectingState | `animateScaleSpring` | 0.2 |  |  | `selectingControl?.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:623` | ChatGroupedView.updateSelectingState | `animateAlpha` | 0.2 |  |  | `subview.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:624` | ChatGroupedView.updateSelectingState | `animateScaleSpring` | 0.2 |  |  | `subview.layer?.animateScaleSpring(from: 1, to: 0.2, duration: 0.2, removeOnCompletion: false, completion: { [weak subview] completed in` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:713` | ChatGroupedView.set | `change` |  |  |  | `contents[i].change(size: item.layout.frame(at: i).size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:1076` | ChatGroupedView.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let animation: CABasicAnimation = makeSpringAnimation("opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:1080` | ChatGroupedView.focusAnimation | `.duration =` | 0.5 |  |  | `animation.duration = 0.5` |
| `packages/ChatUI/Sources/ChatUI/ChatGroupedItem.swift:1138` | ChatGroupedView.onShowContextMenu | `animateAlpha` | 0.2 |  |  | `selectionBackground.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputMenuView.swift:141` | ChatInputMenuView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderBubblesView.swift:141` | RightActionsCluster.animateIconIn | `animateAlpha` | Self.iconMorphDuration | .easeInEaseOut |  | `layer.animateAlpha(from: 0, to: 1, duration: Self.iconMorphDuration, timingFunction: .easeInEaseOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderBubblesView.swift:142` | RightActionsCluster.animateIconIn | `animateScaleCenter` | Self.iconMorphDuration |  |  | `layer.animateScaleCenter(from: Self.iconMorphScale, to: 1, duration: Self.iconMorphDuration)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderBubblesView.swift:154` | RightActionsCluster.addOutgoingIcon | `CABasicAnimation` |  |  | transform.scale | `let shrink = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderBubblesView.swift:160` | RightActionsCluster.addOutgoingIcon | `animateAlpha` | Self.iconMorphDuration | .easeInEaseOut |  | `outgoing.animateAlpha(from: 1, to: 0, duration: Self.iconMorphDuration, timingFunction: .easeInEaseOut, completion: { [weak outgoing] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderBubblesView.swift:661` | MenuMode.applyMenuMode | `change` | Self.menuModeTransition.duration |  |  | `rightCluster.doneFill.change(opacity: menuMode == .done ? 1 : 0, animated: animated, duration: Self.menuModeTransition.duration)` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:47` | StickerPreviewModalView.update | `animateScaleSpring` | 0.2 |  |  | `imageView.layer?.animateScaleSpring(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:57` | StickerPreviewModalView.update | `animateScaleSpring` | 0.2 |  |  | `textView.layer?.animateScaleSpring(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:98` | GifPreviewModalView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak current] completed in` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:117` | GifPreviewModalView.update | `animateAlpha` | 0.2 |  |  | `player.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:149` | ImagePreviewModalView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak current] completed in` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:176` | ImagePreviewModalView.update | `animateScaleSpring` | 0.2 |  |  | `imageView.layer?.animateScaleSpring(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:208` | VideoPreviewModalView.update | `animateAlpha` | 0.2 |  |  | `currentView?.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak currentView] completed in` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:355` | AnimatedStickerPreviewModalView.update | `animateAlpha` | 0.2 |  |  | `player.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ModalPreviewViews.swift:363` | AnimatedStickerPreviewModalView.update | `animateScaleSpring` | 0.2 |  |  | `textView.layer?.animateScaleSpring(from: 0.5, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:399` | ChatTodoItemView.set | `change` |  |  |  | `contentNode.change(size: NSMakeSize(contentFrameModifier(item).width, item.contentSize.height), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:531` | ChatTodoItemView.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let animation: CABasicAnimation = makeSpringAnimation("opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:535` | ChatTodoItemView.focusAnimation | `.duration =` | 0.5 |  |  | `animation.duration = 0.5` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:607` | TodoOptionView.update | `change` | duration | timingFunction |  | `borderView.change(opacity: 1, animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:608` | TodoOptionView.update | `change` | duration | timingFunction |  | `progressView.change(opacity: 1, animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:621` | TodoOptionView.update | `animateAlpha` | duration / 2 |  |  | `selectingView?.layer?.animateAlpha(from: 0, to: 1, duration: duration / 2)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:655` | TodoOptionView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:656` | TodoOptionView.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatTodoItem.swift:681` | TodoOptionView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:837` | InputContextViewController.layout | `change` |  |  |  | `genericView.change(size: future, animated: animated, duration: future.height > frame.height \|\| genericView.position == .below ? 0 : 0.5)` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:910` | InputContextHelper.updateLayout | `_change` | 0.4 | .spring |  | `accessoryContainerView._change(pos: NSMakePoint(relativeRect.minX, y), animated: animated, duration: 0.4, timingFunction: .spring, forceAnim` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:927` | InputContextHelper.context | `change` |  |  |  | `self.accessoryContainerView.change(size: size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:1028` | InputContextHelper.context | `change` | 0.4 | .spring |  | `container.change(opacity: 1, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:1030` | InputContextHelper.context | `_change` | 0.4 | .spring |  | `container._change(pos: NSMakePoint(relativeRect.minX, y), animated: animated, duration: 0.4, timingFunction: .spring, forceAnimateIfHasAnima` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:1039` | InputContextHelper.context | `_change` | 0.4 | CAMediaTimingFunctionName.spring |  | `container._change(pos: NSMakePoint(relativeRect.minX, relativeRect.minY), animated: animated, removeOnCompletion: false, duration: 0.4, timi` |
| `packages/ChatUI/Sources/ChatUI/InputContextHelper.swift:1048` | InputContextHelper.context | `change` |  |  |  | `container.change(opacity: 0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatRecorderOverlayWindow.swift:394` | ChatRecorderOverlayView.setTranscribing | `animateScaleSpring` | 0.45 |  |  | `layer?.animateScaleSpring(from: 0.8, to: 1, duration: 0.45, bounce: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatRecorderOverlayWindow.swift:413` | ChatRecorderOverlayView.morphToStop | `animateAlpha` | 0.2 |  |  | `linesLayer.animateAlpha(from: 1, to: 0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRecorderOverlayWindow.swift:414` | ChatRecorderOverlayView.morphToStop | `animateAlpha` | 0.2 |  |  | `stopLayer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRecorderOverlayWindow.swift:415` | ChatRecorderOverlayView.morphToStop | `animateScaleSpring` | 0.35 |  |  | `stopLayer.animateScaleSpring(from: 0.4, to: 1, duration: 0.35, bounce: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:610` | EdgeBlur.moveFloatingAvatar | `animatePosition` | 0.2 | .easeOut |  | `layer.animatePosition(from: present, to: origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:707` | EdgeBlur.updateFloating | `animateAlpha` | 0.2 | .easeOut |  | `node.layer.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:708` | EdgeBlur.updateFloating | `animatePosition` | 0.2 | .easeOut |  | `node.layer.animatePosition(from: from, to: node.frame.origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:738` | EdgeBlur.updateFloating | `animateAlpha` | 0.2 | .easeOut |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:739` | EdgeBlur.updateFloating | `animatePosition` | 0.2 | .easeOut |  | `view.layer?.animatePosition(from: value.point - (moveAsNew.to - moveAsNew.from), to: value.point, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:751` | EdgeBlur.updateFloating | `_change` | 0.2 | .easeOut |  | `view._change(pos: value.point, animated: animated && view.superview == superview && checker, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:903` | EdgeBlur.updateScroller | `change` |  |  |  | `scroller.change(opacity: isHidden ? 0 : 1, animated: transition.isAnimated) { [weak self] completed in` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1413` | EdgeBlur.updateMonoforumState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0.5, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1414` | EdgeBlur.updateMonoforumState | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: NSMakePoint(-current.frame.width, 0), to: .zero)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1537` | EdgeBlur.updateMentionsCount | `animateAlpha` | 0.2 |  |  | `mentions.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1561` | EdgeBlur.updateMentionsCount | `animateAlpha` | 0.2 |  |  | `reactions.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1585` | EdgeBlur.updateMentionsCount | `animateAlpha` | 0.2 |  |  | `pollVotes.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1663` | EdgeBlur.updateStars | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1664` | EdgeBlur.updateStars | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1695` | EdgeBlur.showVideoProccessingTooltip | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1696` | EdgeBlur.showVideoProccessingTooltip | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1743` | EdgeBlur.showToaster | `animateAlpha` | 0.2 | .spring |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1744` | EdgeBlur.showToaster | `animateScaleSpring` | 0.3 | .spring |  | `view.layer?.animateScaleSpring(from: 0.5, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1745` | EdgeBlur.showToaster | `animatePosition` | 0.25 | .spring |  | `view.layer?.animatePosition(from: NSMakePoint(view.frame.minX, view.frame.minY - 12), to: view.frame.origin, duration: 0.25, timingFunction:` |
| `packages/ChatUI/Sources/ChatUI/ChatController.swift:1764` | EdgeBlur.removeToaster | `animatePosition` | 0.2 |  |  | `view.layer?.animatePosition(from: view.frame.origin, to: NSMakePoint(view.frame.minX, view.frame.minY - 12), duration: 0.2, removeOnCompleti` |
| `packages/ChatUI/Sources/ChatUI/ChatMediaSendFlight.swift:297` | Flight.move | `CASpringAnimation` |  |  | position | `let animation = CASpringAnimation(keyPath: "position")` |
| `packages/ChatUI/Sources/ChatUI/ChatMediaSendFlight.swift:298` | Flight.move | `.mass =` |  |  |  | `animation.mass = 1.0` |
| `packages/ChatUI/Sources/ChatUI/ChatMediaSendFlight.swift:299` | Flight.move | `.stiffness =` |  |  |  | `animation.stiffness = ChatTextSendFlightMotion.verticalStiffness` |
| `packages/ChatUI/Sources/ChatUI/ChatMediaSendFlight.swift:300` | Flight.move | `.damping =` |  |  |  | `animation.damping = ChatTextSendFlightMotion.verticalDamping` |
| `packages/ChatUI/Sources/ChatUI/ChatMediaSendFlight.swift:303` | Flight.move | `.duration =` | animation.settlingDuration |  |  | `animation.duration = animation.settlingDuration` |
| `packages/ChatUI/Sources/ChatUI/ChatVideoMessageContentView.swift:448` | ChatVideoMessageContentView.update | `animateAlpha` | 0.25 | .linear |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.25, timingFunction: .linear, removeOnCompletion: false, completion: { [weak pro` |
| `packages/ChatUI/Sources/ChatUI/ChatVideoMessageContentView.swift:490` | ChatVideoMessageContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0.3, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVideoMessageContentView.swift:519` | ChatVideoMessageContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVideoMessageContentView.swift:520` | ChatVideoMessageContentView.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:611` | ChatHeaderController.updateState | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:627` | ChatHeaderController.updateState | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1113` | ChatPinnedView.update | `animatePosition` | 0.2 | .easeInEaseOut |  | `oldContainer.layer?.animatePosition(from: oldFrom, to: oldTo, duration: 0.2, timingFunction: .easeInEaseOut, removeOnCompletion: false, comp` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1116` | ChatPinnedView.update | `animateAlpha` | 0.2 | .easeInEaseOut |  | `oldContainer.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, timingFunction: .easeInEaseOut, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1120` | ChatPinnedView.update | `animateAlpha` | 0.2 | .easeInEaseOut |  | `newContainer.layer?.animateAlpha(from: 0, to: 1, duration: 0.2` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1154` | ChatPinnedView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1209` | ChatPinnedView.installReplyMarkup | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1802` | TimerButtonView.setTime | `change` |  |  |  | `counter.change(size: value.size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1807` | TimerButtonView.setTime | `change` |  |  |  | `counter.change(pos: point, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1873` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.headerView.change(opacity: 0.6, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1874` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.membersCountView.change(opacity: 0.6, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1875` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.avatarsContainer.change(opacity: 0.6, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1879` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.headerView.change(opacity: 1, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1880` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.membersCountView.change(opacity: 1, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1881` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.avatarsContainer.change(opacity: 1.0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1885` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.headerView.change(opacity: 1, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1886` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.membersCountView.change(opacity: 1, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1887` | ChatGroupCallView.setTime | `change` |  |  |  | `self?.avatarsContainer.change(opacity: 1.0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1919` | ChatGroupCallView.update | `change` |  |  |  | `joinButton.change(opacity: activeCall ? 0 : 1, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1951` | ChatGroupCallView.update | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [we` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1954` | ChatGroupCallView.update | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 1.0, to: 0.2, duration: duration, bounce: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1969` | ChatGroupCallView.update | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: NSMakePoint(CGFloat(index) * (avatarSize.width - 14), 0), to: control.frame.origin, timingFunction: tim` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1971` | ChatGroupCallView.update | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1972` | ChatGroupCallView.update | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration, bounce: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:1981` | ChatGroupCallView.update | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, add` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2035` | ChatGroupCallView.update | `change` |  |  |  | `self.avatarsContainer.change(pos: pos, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2069` | ChatGroupCallView.update | `_change` |  |  |  | `button._change(size: size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2070` | ChatGroupCallView.update | `_change` |  |  |  | `button._change(pos: button.centerFrameY(x: strongSelf.frame.width - button.frame.width - 23).origin, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2086` | ChatGroupCallView.update | `change` |  |  |  | `self.membersCountView.change(size: dynamicValues.size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2379` | ChatPendingRequests.update | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [we` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2382` | ChatPendingRequests.update | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 1.0, to: 0.2, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2397` | ChatPendingRequests.update | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: NSMakePoint(CGFloat(index) * 32, 0), to: control.frame.origin, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2399` | ChatPendingRequests.update | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2400` | ChatPendingRequests.update | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2409` | ChatPendingRequests.update | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, add` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2703` | ChatTranslateHeader.update | `animateAlpha` | 0.2 |  |  | `container.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatHeaderController.swift:2704` | ChatTranslateHeader.update | `animatePosition` |  |  |  | `container.layer?.animatePosition(from: appearFrom, to: .zero)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchHeader.swift:163` | TagView.update | `change` |  |  |  | `self.change(opacity: item.enabled ? 1.0 : 0.8, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchHeader.swift:838` | ChatSearchHeader.notify | `change` |  |  |  | `searchView.change(size: NSMakeSize(searchWidth, searchView.frame.height), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchHeader.swift:894` | ChatSearchHeader.notify | `change` |  |  |  | `searchView.change(size: NSMakeSize(searchWidth, searchView.frame.height), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchHeader.swift:939` | ChatSearchHeader.notify | `change` |  |  |  | `searchView.change(size: NSMakeSize(searchWidth, searchView.frame.height), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchHeader.swift:1315` | ChatSearchHeader.updateCount | `CATransition` | 0.12 |  |  | `let fade = CATransition()` |
| `packages/ChatUI/Sources/ChatUI/ChatSearchHeader.swift:1326` | ChatSearchHeader.updateCount | `change` | 0.2 | .easeOut |  | `countContainer.change(opacity: isVisible ? 1 : 0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputAttachView.swift:123` | ChatInputAttachButton.setAI | `animateAlpha` | 0.2 |  |  | `ai.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionEmojiLayer.swift:35` | ChatReactionEmojiLayer.updateLayer | `animateAlpha` | 0.2 |  |  | `imageLayer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:269` | Action.setListening | `animateAlpha` |  |  |  | `glow.animateAlpha(from: from, to: listening ? 1 : 0, duration: listening ? 0.3 : 0.5)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:273` | Action.setListening | `CABasicAnimation` |  |  | transform.rotation.z | `let rotation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:282` | Action.setListening | `CABasicAnimation` |  |  | locations | `let animation = CABasicAnimation(keyPath: "locations")` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:285` | Action.setListening | `.duration =` | 1.4 |  |  | `animation.duration = 1.4` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:315` | Action.updateLevel | `CABasicAnimation` |  |  | shadowOpacity | `let opacityAnimation = CABasicAnimation(keyPath: "shadowOpacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:318` | Action.updateLevel | `.duration =` | 0.12 let |  | shadowRadius | `opacityAnimation.duration = 0.12` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:319` | Action.updateLevel | `CABasicAnimation` |  |  | shadowRadius | `let radiusAnimation = CABasicAnimation(keyPath: "shadowRadius")` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:322` | Action.updateLevel | `.duration =` | 0.12 |  |  | `radiusAnimation.duration = 0.12` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:422` | Action.animateIn | `animatePosition` | 0.35 | .spring |  | `layer.animatePosition(from: NSMakePoint(0, offset), to: .zero, duration: 0.35, timingFunction: .spring, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:423` | Action.animateIn | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:425` | Action.animateIn | `animateScaleSpring` | 0.4 |  |  | `layer.animateScaleSpring(from: 0.85, to: 1, duration: 0.4, bounce: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:433` | Action.animateOut | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceTranscriptionView.swift:436` | Action.animateOut | `animateScaleSpring` | 0.25 |  |  | `bubbleContainer.layer?.animateScaleSpring(from: 1, to: 0.85, duration: 0.25, removeOnCompletion: false, bounce: false)` |
| `packages/ChatUI/Sources/ChatUI/TopicReplyItemView.swift:193` | TopicReplyItemView.updateLayout | `animateBounds` | duration | curve.timingFunction |  | `textLayer.animateBounds(from: previous, to: drawingBounds, duration: duration, timingFunction: curve.timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/TopicReplyItemView.swift:198` | TopicReplyItemView.updateLayout | `animatePosition` | duration | curve.timingFunction |  | `textLayer.animatePosition(from: previous, to: position, duration: duration, timingFunction: curve.timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChatInteractiveContentView.swift:359` | ChatMediaImageHost.change | `change` |  |  |  | `func change(size: NSSize, animated: Bool) {` |
| `packages/ChatUI/Sources/ChatUI/ChatInteractiveContentView.swift:361` | ChatMediaImageHost.change | `_change` |  |  |  | `view._change(size: size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatInteractiveContentView.swift:370` | ChatMediaImageHost.change | `animateBounds` | 0.2 | .easeOut |  | `layer.animateBounds(from: presentBounds, to: NSMakeRect(0, 0, size.width, size.height), duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatInteractiveContentView.swift:705` | ChatInteractiveContentView.hideLivePhotoVideo | `animateAlpha` | 0.3 |  |  | `layer.animateAlpha(from: 1, to: 0, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatInteractiveContentView.swift:1183` | ChatInteractiveContentView.update | `change` |  |  |  | `self.image.change(size: size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatInteractiveContentView.swift:1204` | ChatInteractiveContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0.3, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatFloatingAvatars.swift:133` | ChatFloatingAvatarScene.remove | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(from), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak self,` |
| `packages/ChatUI/Sources/ChatUI/VideoStickerContentView.swift:179` | VideoStickerContentView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:109` | ChatSwipeToReplyView.animateOut | `animateAlpha` | 0.3 |  |  | `layer?.animateAlpha(from: 1.0, to: 0.0, duration: 0.3, removeOnCompletion: false, completion: { _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:115` | ChatSwipeToReplyView.animateOut | `animateScale` | 0.3 | .spring |  | `contentLayer.animateScale(from: from, to: 0.2, duration: 0.3, timingFunction: .spring, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:160` | ChatSwipeToReplyView.playSuccessAnimation | `animateScale` | 0.2 |  |  | `contentLayer.animateScale(from: 1.0, to: 1.1, duration: 0.2, completion: { [weak self] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:164` | ChatSwipeToReplyView.playSuccessAnimation | `animateScale` | 0.15 |  |  | `self.contentLayer.animateScale(from: 1.1, to: 1.0, duration: 0.15)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:169` | ChatSwipeToReplyView.playSuccessAnimation | `animate` | 0.3 | .linear | lineWidth | `progressLayer.animate(from: NSNumber(value: Double(progressLineWidth)), to: NSNumber(value: 0.0), keyPath: "lineWidth", timingFunction: .lin` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:175` | ChatSwipeToReplyView.playSuccessAnimation | `animate` | 0.3 | .spring | path | `progressLayer.animate(from: currentRing, to: expandedRing, keyPath: "path", timingFunction: .spring, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:177` | ChatSwipeToReplyView.playSuccessAnimation | `animateAlpha` | 0.3 |  |  | `progressLayer.animateAlpha(from: 1.0, to: 0.0, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:184` | ChatSwipeToReplyView.playSuccessAnimation | `animate` | 0.3 | .linear | lineWidth | `fillLayer.animate(from: NSNumber(value: Double(ChatSwipeToReplyView.progressLineWidth)), to: NSNumber(value: Double(ChatSwipeToReplyView.suc` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:188` | ChatSwipeToReplyView.playSuccessAnimation | `animate` | 0.3 | .linear | path | `fillLayer.animate(from: outerFill, to: innerFill, keyPath: "path", timingFunction: .linear, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:576` | RightToolTip.updateSelectingState | `animateAlpha` | 0.2 |  |  | `selectingView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:582` | RightToolTip.updateSelectingState | `animatePosition` |  |  |  | `view.layer?.animatePosition(from: view.frame.origin, to: view.frame.origin.offsetBy(dx: 20, dy: 0), removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:802` | RightToolTip.updateMouse | `change` |  |  |  | `shareView?.change(opacity: 1, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:811` | RightToolTip.updateMouse | `change` |  |  |  | `commentsView.change(opacity: mouseInsideRow() && contextMenu == nil && item.chatInteraction.presentation.state != .selecting ? 1.0 : 0.0, an` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:1733` | RightToolTip.updateCaptions | `animateAlpha` | 0.2 |  |  | `if animated { current.view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2) }` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:1883` | RightToolTip.fillChannelComments | `change` |  |  |  | `current.change(opacity: 0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:1896` | RightToolTip.fillChannelComments | `change` |  |  |  | `current.change(pos: channelCommentsOverlayFrame(item).origin, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:1901` | RightToolTip.fillChannelComments | `animateAlpha` | 0.2 |  |  | `channelCommentsBubbleSmallControl.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak channelC` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:1991` | RightToolTip.fillReplyMarkup | `animateScaleCenter` | 0.2 |  |  | `replyMarkupView.layer?.animateScaleCenter(from: 1, to: 0.1, duration: 0.2, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:1992` | RightToolTip.fillReplyMarkup | `animateAlpha` | 0.2 |  |  | `replyMarkupView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak replyMarkupView] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2172` | RightToolTip.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let animation: CABasicAnimation = makeSpringAnimation("opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2357` | FrostedPanel.shakeContentView | `CAKeyframeAnimation` |  |  | transform.translation.x | `let translation = CAKeyframeAnimation(keyPath: "transform.translation.x");` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2361` | FrostedPanel.shakeContentView | `CAKeyframeAnimation` |  |  | transform.rotation.z | `let rotation = CAKeyframeAnimation(keyPath: "transform.rotation.z")` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2372` | FrostedPanel.shakeContentView | `.duration =` | 0.5 |  |  | `shakeGroup.duration = 0.5` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2856` | ShakeItem.moveReveal | `change` |  |  |  | `swipingRightView.change(pos: NSMakePoint(frame.width + delta, swipingRightView.frame.minY), animated: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2857` | ShakeItem.moveReveal | `change` |  |  |  | `swipingRightView.change(size: NSMakeSize(max(rightRevealWidth, -delta), swipingRightView.frame.height), animated: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2884` | ShakeItem.completeReveal | `change` |  |  |  | `rowView.change(pos: NSMakePoint(0, rowView.frame.minY), animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2885` | ShakeItem.completeReveal | `change` |  |  |  | `container.change(pos: NSMakePoint(frame.width, container.frame.minY), animated: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2907` | ShakeItem.onInsert | `animateScaleSpringFrom` | 0.35 |  |  | `self.rowView.layer?.animateScaleSpringFrom(anchor: NSMakePoint(bubbleView.frame.minX, rowView.frame.height / 2), from: 0.1, to: 1, duration:` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2909` | ShakeItem.onInsert | `animateScaleSpringFrom` | 0.35 |  |  | `self.rowView.layer?.animateScaleSpringFrom(anchor: NSMakePoint(rowView.frame.width - 20, rowView.frame.height / 2), from: 0.1, to: 1, durati` |
| `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:2911` | ShakeItem.onInsert | `animateAlpha` | 0.35 |  |  | `self.rowView.layer?.animateAlpha(from: 0, to: 1, duration: 0.35)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceSendFlight.swift:31` | ChatVoiceSendFlightMotion.flightAnimation | `CABasicAnimation` |  |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceSendFlight.swift:34` | ChatVoiceSendFlightMotion.flightAnimation | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceSendFlight.swift:117` | Pending.cancel | `animateScaleSpring` | 0.3 |  |  | `layer.animateScaleSpring(from: 1.0, to: 0.1, duration: 0.3, removeOnCompletion: false, bounce: false, completion: { [weak self, weak overlay` |
| `packages/ChatUI/Sources/ChatUI/ChatVoiceSendFlight.swift:121` | Pending.cancel | `animateAlpha` | 0.18 | .spring |  | `layer.animateAlpha(from: 1, to: 0, duration: 0.18, timingFunction: .spring, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:28` | .changeCommentsLayerPosition | `animatePosition` | 0.2 | .easeOut |  | `layer.animatePosition(from: from, to: position, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:92` | NumericAnimation.update | `animateAlpha` | duration | timingFunction |  | `field.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [weak field]` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:96` | NumericAnimation.update | `animateAlpha` | duration | timingFunction |  | `field.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [weak field]` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:103` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `field.animatePosition(from: field.frame.origin, to: NSMakePoint(field.frame.minX, field.frame.maxY), timingFunction: timingFunction, removeO` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:105` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `field.animatePosition(from: field.frame.origin, to: NSMakePoint(field.frame.minX, field.frame.minY - field.frame.height), timingFunction: ti` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:119` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `view.0.animatePosition(from: view.0.frame.origin - pos, to: .zero, timingFunction: timingFunction, removeOnCompletion: true, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:130` | NumericAnimation.update | `animateAlpha` | duration |  |  | `current.animateAlpha(from: 0, to: 1, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:135` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `current.animatePosition(from: NSMakePoint(pos.x, pos.y - layout.0.layoutSize.height), to: pos, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:137` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `current.animatePosition(from: NSMakePoint(pos.x, pos.y + layout.0.layoutSize.height), to: pos, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:142` | NumericAnimation.update | `animateAlpha` | duration |  |  | `current.animateAlpha(from: 0, to: 1, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:156` | NumericAnimation.update | `animateAlpha` | duration | timingFunction |  | `indicator.layer?.animateAlpha(from: 0, to: 1, duration: duration,  timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:164` | NumericAnimation.update | `animateAlpha` | duration | timingFunction |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: ` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:460` | ChannelCommentsBubbleControl.update | `animateAlpha` | duration | timingFunction |  | `control.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [weak cont` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:463` | ChannelCommentsBubbleControl.update | `animateScaleSpring` | duration |  |  | `control.animateScaleSpring(from: 1.0, to: 0.2, duration: duration, center: false )` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:481` | ChannelCommentsBubbleControl.update | `animatePosition` | duration | timingFunction |  | `control.animatePosition(from: NSMakePoint(CGFloat(index) * 18, 0).offsetBy(dx: imageSize.width/2, dy: imageSize.height/2), to: control.frame` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:483` | ChannelCommentsBubbleControl.update | `animateAlpha` | duration | timingFunction |  | `control.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:484` | ChannelCommentsBubbleControl.update | `animateScaleSpring` | duration |  |  | `control.animateScaleSpring(from: 0.2, to: 1.0, duration: duration, center: false)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:493` | ChannelCommentsBubbleControl.update | `animatePosition` | duration | timingFunction |  | `control.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, additive: ` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:520` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `arrowView.animatePosition(from: arrowView.frame.origin - f.origin, to: .zero, timingFunction: timingFunction, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:542` | NumericAnimation.update | `animateAlpha` | duration | timingFunction |  | `dot.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:543` | NumericAnimation.update | `animateScaleSpring` | duration |  |  | `dot.animateScaleSpring(from: 0.2, to: 1.0, duration: duration, bounce: true)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:550` | NumericAnimation.update | `animatePosition` |  | timingFunction |  | `dotView.animatePosition(from: dotView.frame.origin - f.origin, to: .zero, timingFunction: timingFunction, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:562` | NumericAnimation.update | `animateAlpha` | duration | timingFunction |  | `dotView.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [weak dotV` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:565` | NumericAnimation.update | `animateScaleSpring` | duration |  |  | `dotView.animateScaleSpring(from: 1, to: 0.2, duration: duration)` |
| `packages/ChatUI/Sources/ChatUI/ChannelCommentsControls.swift:675` | ChannelCommentsSmallControl.update | `change` |  |  |  | `change(size: size, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:249` | InstantVideoPIP.showIfNeeded | `_change` |  |  |  | `strongSelf.view._change(opacity: 1.0)` |
| `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:313` | InstantVideoPIP.hide | `_change` |  |  |  | `genericView._change(pos: point, animated: animated, completion: { [weak self, weak view] completed in` |
| `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:331` | InstantVideoPIP.alignToCorner | `_change` |  |  |  | `genericView._change(pos: NSMakePoint(contentView.frame.width - view.frame.width - 20, contentView.frame.height - view.frame.height - 130), a` |
| `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:333` | InstantVideoPIP.alignToCorner | `_change` |  |  |  | `genericView._change(pos: NSMakePoint(20, contentView.frame.height - view.frame.height - 130), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:335` | InstantVideoPIP.alignToCorner | `_change` |  |  |  | `genericView._change(pos: NSMakePoint(contentView.frame.width - view.frame.width - 20, 100), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/InstantVideoPIP.swift:337` | InstantVideoPIP.alignToCorner | `_change` |  |  |  | `genericView._change(pos: NSMakePoint(20, 100), animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatThemeSelectorController.swift:222` | ChatThemeSelectorView.updateThemes | `animateAlpha` | 0.2 |  |  | `accept.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatThemeSelectorController.swift:300` | ChatThemeSelectorView.updateThemes | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:749` | AnimationLayerContainer.updateLayer | `animateAlpha` | 0.2 |  |  | `imageLayer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:854` | ChatReactionEmojiLayer.animateAppear | `animateScaleCenter` | 0.2 |  |  | `animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:992` | ChatReactionEmojiViewHost.setOpacityImmediately | `_change` |  |  |  | `view._change(opacity: CGFloat(value), animated: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:998` | ChatReactionEmojiViewHost.animateAppear | `animateScaleCenter` | 0.2 |  |  | `view.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1269` | ReactionView.update | `animateAlpha` | 0.2 | .easeOut |  | `control.hostLayer?.animateAlpha(from: 1, to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak cont` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1272` | ReactionView.update | `animateScaleSpring` | 0.2 |  |  | `control.hostLayer?.animateScaleSpring(from: 1.0, to: 0.2, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1290` | ReactionView.update | `animatePosition` | 0.2 | .easeOut |  | `control.hostLayer?.animatePosition(from: NSMakePoint(CGFloat(index) * 12, 0), to: origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1292` | ReactionView.update | `animateAlpha` | 0.2 | .easeOut |  | `control.hostLayer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1293` | ReactionView.update | `animateScaleSpring` | 0.2 |  |  | `control.hostLayer?.animateScaleSpring(from: 0.2, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1303` | ReactionView.update | `animatePosition` | 0.2 | .easeOut |  | `control.hostLayer?.animatePosition(from: control.origin - updatedPoint, to: .zero, duration: 0.2, timingFunction: .easeOut, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1334` | ReactionView.update | `animateScaleSpring` | 0.3 |  |  | `background.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1335` | ReactionView.update | `animateAlpha` | 0.2 |  |  | `background.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1341` | ReactionView.update | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak la` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1344` | ReactionView.update | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1392` | ReactionView.update | `animateBorder` |  |  |  | `self.layer?.animateBorder()` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1393` | ReactionView.update | `animateBackground` |  |  |  | `self.layer?.animateBackground()` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1722` | ReactionChip.update | `animateAlpha` | 0.2 | .easeOut |  | `control.hostLayer?.animateAlpha(from: 1, to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak cont` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1725` | ReactionChip.update | `animateScaleSpring` | 0.2 |  |  | `control.hostLayer?.animateScaleSpring(from: 1.0, to: 0.2, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1743` | ReactionChip.update | `animatePosition` | 0.2 | .easeOut |  | `control.hostLayer?.animatePosition(from: NSMakePoint(CGFloat(index) * 12, 0), to: origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1745` | ReactionChip.update | `animateAlpha` | 0.2 | .easeOut |  | `control.hostLayer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1746` | ReactionChip.update | `animateScaleSpring` | 0.2 |  |  | `control.hostLayer?.animateScaleSpring(from: 0.2, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1756` | ReactionChip.update | `animatePosition` | 0.2 | .easeOut |  | `control.hostLayer?.animatePosition(from: control.origin - updatedPoint, to: .zero, duration: 0.2, timingFunction: .easeOut, additive: true)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1787` | ReactionChip.update | `animateScaleSpring` | 0.3 |  |  | `background.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1788` | ReactionChip.update | `animateAlpha` | 0.2 |  |  | `background.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1794` | ReactionChip.update | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak la` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1797` | ReactionChip.update | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1843` | ReactionChip.update | `animateBorder` |  |  |  | `layer.animateBorder()` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:1844` | ReactionChip.update | `animateBackground` |  |  |  | `layer.animateBackground()` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2104` | TagReactionView.update | `animateScaleSpring` | 0.3 |  |  | `background.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2105` | TagReactionView.update | `animateAlpha` | 0.2 |  |  | `background.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2112` | TagReactionView.update | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak la` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2115` | TagReactionView.update | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2146` | TagReactionView.update | `animateBorder` |  |  |  | `self.layer?.animateBorder()` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2147` | TagReactionView.update | `animateBackground` |  |  |  | `self.layer?.animateBackground()` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2294` | TagReactionView.detach | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(from), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak self,` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2300` | TagReactionView.detach | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2406` | TagReactionView.update | `animateScaleSpring` | 0.3 |  |  | `view.chipLayer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/ChatReactionsView.swift:2407` | TagReactionView.update | `animateAlpha` | 0.2 |  |  | `view.chipLayer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputStateContainers.swift:189` | ChatInputBlockView.animateActionTitle | `CABasicAnimation` |  |  | opacity | `let opacity = CABasicAnimation(keyPath: "opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputStateContainers.swift:204` | ChatInputBlockView.animateActionTitle | `CABasicAnimation` |  |  | filters.gaussianBlur.inputRadius | `let radius = CABasicAnimation(keyPath: "filters.gaussianBlur.inputRadius")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputStateContainers.swift:343` | PendingUpdate.applyTitleChange | `NSAnimationContext.runAnimationGroup` | actionTransitionDuration |  |  | `NSAnimationContext.runAnimationGroup { ctx in` |
| `packages/ChatUI/Sources/ChatUI/ChatInputStateContainers.swift:344` | PendingUpdate.applyTitleChange | `.duration =` | actionTransitionDuration |  |  | `ctx.duration = actionTransitionDuration` |
| `packages/ChatUI/Sources/ChatUI/ChatTopicSeparatorItem.swift:194` | LineView.updateIsVisible | `change` |  |  |  | `backgroundView.change(opacity: visible ? 1 : 0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatTopicSeparatorItem.swift:195` | LineView.updateIsVisible | `change` |  |  |  | `containerView.change(opacity: visible ? 1 : 0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatTopicSeparatorItem.swift:200` | LineView.updateIsVisible | `change` |  |  |  | `lineView.change(opacity: header ? 0 : 1, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1487` | TextHit.animateNewRevealCharacters | `CABasicAnimation` |  |  | filters.gaussianBlur.inputRadius | `let blurAnimation = CABasicAnimation(keyPath: "filters.gaussianBlur.inputRadius")` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1490` | TextHit.animateNewRevealCharacters | `.duration =` | 0.22 |  |  | `blurAnimation.duration = 0.22` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1494` | TextHit.animateNewRevealCharacters | `animateAlpha` | 0.2 | .easeInEaseOut |  | `snippetLayer.animateAlpha(from: 0.0, to: 1.0, duration: 0.2, timingFunction: .easeInEaseOut)` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1495` | TextHit.animateNewRevealCharacters | `animatePosition` |  |  |  | `snippetLayer.animatePosition(` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1502` | TextHit.animateNewRevealCharacters | `animateScale` | 0.2 | .easeInEaseOut |  | `snippetLayer.animateScale(from: 0.5, to: 1.0, duration: 0.2, timingFunction: .easeInEaseOut, completion: { [weak self, weak snippetLayer] _ ` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1559` | TextHit.applyRevealVisibility | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1562` | TextHit.applyRevealVisibility | `.duration =` | 0.12 |  |  | `animation.duration = 0.12` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1568` | TextHit.applyRevealVisibility | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:1571` | TextHit.applyRevealVisibility | `.duration =` | 0.12 |  |  | `animation.duration = 0.12` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:2336` | TextHit.flashAnchorHighlight | `animateAlpha` | 2.5 | .easeOut |  | `highlight.layer?.animateAlpha(from: 1.0, to: 0.0, duration: 2.5, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak hi` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:2748` | TextHit.updateInlineEmojiReveal | `animateAlpha` | 0.2 |  |  | `data.layer.animateAlpha(from: 0.0, to: data.revealedAlpha, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:2749` | TextHit.updateInlineEmojiReveal | `animateScale` | 0.2 |  |  | `data.layer.animateScale(from: 0.1, to: 1.0, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/InstantPageV2View.swift:4069` | ScrollAxis.endDrag | `ContainedViewLayoutTransition.animated` | 0.35 | .spring |  | `ContainedViewLayoutTransition.animated(duration: 0.35, curve: .spring).updateFrame(view: self.pagesView, frame: frame, completion: { [weak s` |
| `packages/ChatUI/Sources/ChatUI/TranscribeAudioTextView.swift:71` | TranscribeAudioTextView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:34` | ChatLayerRowView.updateStatus | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(layer.opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [w` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:206` | ChatLayerRowView.removeAdminBadgeNode | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(from), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak self,` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:210` | ChatLayerRowView.removeAdminBadgeNode | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:287` | ChatLayerRowView.updateForwardHeader | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(layer.presentation()?.opacity ?? layer.opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCo` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:368` | ChatLayerRowView.updateSenderName | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(layer.opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [w` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:372` | ChatLayerRowView.updateSenderName | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:411` | ChatLayerRowView.updateForwardName | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(layer.opacity), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [w` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerRowView.swift:415` | ChatLayerRowView.updateForwardName | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1344` | ChatInputView.notify | `change` | 0.2 | .easeOut |  | `self.messageEffect?.change(opacity: value.effectiveInput.inputText.isEmpty \|\| value.interfaceState.editState != nil ? 0 : 1, animated: anima` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1520` | ChatInputView.morphGlassIn | `animateAlpha` | ChatInputView.glassMorphFadeIn |  |  | `layer.animateAlpha(from: CGFloat(from), to: 1, duration: ChatInputView.glassMorphFadeIn)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1549` | ChatInputView.morphGlassOut | `CAKeyframeAnimation` |  |  | opacity | `let fade = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1689` | ChatInputView.needUpdateChatState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1717` | ChatInputView.needUpdateChatState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1731` | ChatInputView.installStateView | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1733` | ChatInputView.installStateView | `change` |  |  |  | `self.contentView.change(opacity: 0.0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1745` | ChatInputView.installStateView | `change` |  |  |  | `self.contentView.change(opacity: 1.0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1748` | ChatInputView.installStateView | `animateAlpha` | 0.25 | .spring |  | `self.container.layer?.animateAlpha(from: 0.1, to: 1, duration: 0.25, timingFunction: .spring)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1751` | ChatInputView.installStateView | `change` |  |  |  | `self.contentView.change(opacity: 0.0, animated: animated)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1918` | ChatInputView.updateAttachments | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1962` | ChatInputView.updateAttachments | `animateAlpha` | 0.2 | .easeOut |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatInputView.swift:1963` | ChatInputView.updateAttachments | `animateScaleCenter` | 0.2 | .easeOut |  | `view.layer?.animateScaleCenter(from: 0.01, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageView.swift:390` | AdSettingsView.updateText | `animateAlpha` | 0.2 |  |  | `if animated { current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2) }` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageView.swift:457` | AdSettingsView.updateNativeText | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageView.swift:490` | AdSettingsView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageView.swift:520` | AdSettingsView.set | `animateScaleCenter` | 0.2 | .easeOut |  | `actionButton?.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageView.swift:521` | AdSettingsView.set | `animateAlpha` | 0.2 |  |  | `actionButton?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatMessageView.swift:542` | AdSettingsView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/VoiceTranscriptionControl.swift:129` | TranscriptionState.update | `CABasicAnimation` |  |  | strokeEnd | `let endAnimation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/ChatUI/Sources/ChatUI/VoiceTranscriptionControl.swift:132` | TranscriptionState.update | `.duration =` | 1.25 |  |  | `endAnimation.duration = 1.25` |
| `packages/ChatUI/Sources/ChatUI/VoiceTranscriptionControl.swift:138` | TranscriptionState.update | `CABasicAnimation` |  |  | strokeStart | `let startAnimation = CABasicAnimation(keyPath: "strokeStart")` |
| `packages/ChatUI/Sources/ChatUI/VoiceTranscriptionControl.swift:141` | TranscriptionState.update | `.duration =` | 1.25 |  |  | `startAnimation.duration = 1.25` |
| `packages/ChatUI/Sources/ChatUI/VoiceTranscriptionControl.swift:153` | TranscriptionState.update | `animateAlpha` | 0.15 |  |  | `inProgressLayer.animateAlpha(from: 1.0, to: 0.0, duration: 0.15, removeOnCompletion: false, completion: { [weak inProgressLayer] _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerControlNode.swift:237` | ToolTipOwner.stateDidUpdate | `animateScaleSpring` | 0.3 |  |  | `layer.animateScaleSpring(from: 1, to: pressed, duration: 0.3, removeOnCompletion: false)` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerControlNode.swift:239` | ToolTipOwner.stateDidUpdate | `animateScaleSpring` | 0.3 |  |  | `layer.animateScaleSpring(from: pressed, to: 1.0, duration: 0.3)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:529` | AvatarContentView.set | `animateAlpha` | 0.2 |  |  | `avatars.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1202` | ReactionPeerMenuItemView.applyState | `change` | 0.35 | .spring |  | `contentView.change(pos: NSMakePoint(0, -contentView.frame.height), animated: true, duration: 0.35, timingFunction: .spring)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1203` | ReactionPeerMenuItemView.applyState | `change` |  |  |  | `contentView.change(opacity: 0, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1216` | ReactionPeerMenuItemView.applyState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1218` | ReactionPeerMenuItemView.applyState | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: NSMakePoint(current.frame.minX, current.frame.height), to: current.frame.origin)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1223` | ReactionPeerMenuItemView.applyState | `change` | 0.35 | .spring |  | `contentView.change(pos: NSMakePoint(0, 0), animated: true, duration: 0.35, timingFunction: .spring)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1224` | ReactionPeerMenuItemView.applyState | `change` |  |  |  | `contentView.change(opacity: 1, animated: true)` |
| `packages/ChatUI/Sources/ChatUI/MessageReadMenuItem.swift:1229` | ReactionPeerMenuItemView.applyState | `animatePosition` | 0.35 | .spring |  | `view.layer?.animatePosition(from: view.frame.origin, to: NSMakePoint(view.frame.minX, view.frame.height),duration: 0.35, timingFunction: .sp` |
| `packages/ChatUI/Sources/ChatUI/ChatWalletTransferAnimation.swift:448` | Flight.cancel | `animateAlpha` | 0.15 |  |  | `overlay.layer?.animateAlpha(from: 1, to: 0, duration: 0.15, completion: { _ in` |
| `packages/ChatUI/Sources/ChatUI/ChatLayerTextNode.swift:460` | Highlight.updateFolding | `animateContents` |  |  |  | `if transition.isAnimated, wasRevealed != layout.isRevealed { decoration.arrow.animateContents() }` |
| `packages/ChatUI/Sources/ChatUI/ChatTitleBarView.swift:188` | ChatTitleBarView.updateStoryState | `change` | 0.2 |  |  | `view.change(opacity: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatTitleBarView.swift:190` | ChatTitleBarView.updateStoryState | `change` |  |  |  | `view.change(opacity: 0, completion: { [weak view] completed in` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:175` | ChatRightView.change | `change` | duration | CAMediaTimingFunctionName |  | `public override func change(opacity to: CGFloat, animated: Bool = true, _ save: Bool = true, removeOnCompletion: Bool = true, duration: Doub` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:176` | ChatRightView.change | `change` | duration | timingFunction |  | `super.change(opacity: to, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFuncti` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:183` | ChatRightView.change | `animateAlpha` | duration | timingFunction |  | `contentLayer.animateAlpha(from: from, to: to, duration: duration, timingFunction: timingFunction, removeOnCompletion: removeOnCompletion)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:217` | ChatRightView.removeIcon | `animateAlpha` | 0.2 | .easeOut |  | `layer.animateAlpha(from: CGFloat(from), to: 0, duration: 0.2, timingFunction: .easeOut, removeOnCompletion: false, completion: { [weak layer` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:220` | ChatRightView.removeIcon | `animateScaleCenter` | 0.2 | .easeOut |  | `layer.animateScaleCenter(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false, timingFunction: .easeOut)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:584` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.sendingView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:585` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.sendingView?.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:606` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.stateView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:607` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.stateView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:624` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.readImageView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:625` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.readImageView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:642` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.replyCountView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:643` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.replyCountView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:652` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.replyCountImage?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:653` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.replyCountImage?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:675` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.paidMessageCountView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:676` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.paidMessageCountView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:685` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.paidMessageImage?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:686` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.paidMessageImage?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:708` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.diceStakeCountView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:709` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.diceStakeCountView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:718` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.diceStakeImageView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:719` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.diceStakeImageView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:741` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.pinView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:742` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.pinView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:761` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.dateView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:762` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.dateView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:778` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.failedView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:779` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.failedView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:796` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.editView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:797` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.editView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:812` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.viewsCountView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:813` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.viewsCountView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:822` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.viewsImageView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:823` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.viewsImageView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:845` | Frames.set | `animateAlpha` | 0.2 |  |  | `self.postAuthorView?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ChatUI/Sources/ChatUI/ChatRightView.swift:846` | Frames.set | `animateScaleCenter` | 0.2 |  |  | `self.postAuthorView?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |

## ComponentsUI (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ComponentsUI/Sources/ComponentsUI/SendingClockProgress.swift:69` | SendingClockProgress.animateHour | `CABasicAnimation` | 6 |  | transform.rotation.z | `let animation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/ComponentsUI/Sources/ComponentsUI/SendingClockProgress.swift:71` | SendingClockProgress.animateHour | `.duration =` | 6 |  |  | `animation.duration = 6` |
| `packages/ComponentsUI/Sources/ComponentsUI/SendingClockProgress.swift:82` | SendingClockProgress.animateMin | `CABasicAnimation` | 1 |  | transform.rotation.z | `let animation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/ComponentsUI/Sources/ComponentsUI/SendingClockProgress.swift:84` | SendingClockProgress.animateMin | `.duration =` | 1 |  |  | `animation.duration = 1` |

## CrashRecoveryUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/CrashRecoveryUI/Sources/CrashRecoveryUI/CrashRecoveryView.swift:206` | CrashRecoveryView.update | `CATransition` | 0.2 |  |  | `let transition = CATransition()` |
| `packages/CrashRecoveryUI/Sources/CrashRecoveryUI/CrashRecoveryView.swift:208` | CrashRecoveryView.update | `.duration =` | 0.2 |  |  | `transition.duration = 0.2` |

## CubeUI (9)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/CubeUI/Sources/CubeUI/CubeAnimationView.swift:741` | CubeAnimationView.applyImpactSpring | `CASpringAnimation` |  |  | transform | `let springAnimation = CASpringAnimation(keyPath: "transform")` |
| `packages/CubeUI/Sources/CubeUI/CubeAnimationView.swift:744` | CubeAnimationView.applyImpactSpring | `.damping =` |  |  |  | `springAnimation.damping = 12.0` |
| `packages/CubeUI/Sources/CubeUI/CubeAnimationView.swift:745` | CubeAnimationView.applyImpactSpring | `.stiffness =` | springAnimation.settlingDuration |  |  | `springAnimation.stiffness = 200.0` |
| `packages/CubeUI/Sources/CubeUI/CubeAnimationView.swift:746` | CubeAnimationView.applyImpactSpring | `.mass =` | springAnimation.settlingDuration |  |  | `springAnimation.mass = 1.0` |
| `packages/CubeUI/Sources/CubeUI/CubeAnimationView.swift:747` | CubeAnimationView.applyImpactSpring | `.duration =` | springAnimation.settlingDuration |  |  | `springAnimation.duration = springAnimation.settlingDuration` |
| `packages/CubeUI/Sources/CubeUI/CraftGiftLayer.swift:227` | CraftResultLayer.update | `CABasicAnimation` |  |  | strokeEnd | `let animation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/CubeUI/Sources/CubeUI/CraftGiftLayer.swift:230` | CraftResultLayer.update | `.duration =` | 0.3 |  |  | `animation.duration = 0.3` |
| `packages/CubeUI/Sources/CubeUI/CraftGiftLayer.swift:332` | CraftSideFaceLayer.update | `CABasicAnimation` |  |  | backgroundColor | `let colorAnimation = CABasicAnimation(keyPath: "backgroundColor")` |
| `packages/CubeUI/Sources/CubeUI/CraftGiftLayer.swift:335` | CraftSideFaceLayer.update | `.duration =` | 0.3 |  |  | `colorAnimation.duration = 0.3` |

## DataUsageUI (14)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageMediaCells.swift:68` | Accessory.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockController.swift:300` | StorageUsageBlockControllerView.updateMainView | `_change` | duration | timingFunction |  | `mainView._change(pos: NSMakePoint(-mainView.frame.width, mainView.frame.minY), animated: true, duration: duration, timingFunction: timingFun` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockController.swift:305` | StorageUsageBlockControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `view.layer?.animatePosition(from: NSMakePoint(view.frame.width, mainView.frame.minY), to: NSMakePoint(0, mainView.frame.minY), duration: dur` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockController.swift:307` | StorageUsageBlockControllerView.updateMainView | `_change` | duration | timingFunction |  | `mainView._change(pos: NSMakePoint(mainView.frame.width, mainView.frame.minY), animated: true, duration: duration, timingFunction: timingFunc` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockController.swift:312` | StorageUsageBlockControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `view.layer?.animatePosition(from: NSMakePoint(-view.frame.width, mainView.frame.minY), to: NSMakePoint(0, mainView.frame.minY), duration: du` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageClearedItem.swift:96` | StorageUsageClearedView.set | `animateAlpha` | 0.2 |  |  | `current_circle.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageClearedItem.swift:97` | StorageUsageClearedView.set | `animateScaleSpring` | 0.45 |  |  | `current_circle.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.45)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageClearedItem.swift:114` | StorageUsageClearedView.set | `animateAlpha` | 0.2 |  |  | `current_check.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageClearedItem.swift:115` | StorageUsageClearedView.set | `animateScaleSpring` | 0.45 |  |  | `current_check.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.45)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockItem.swift:300` | StorageUsageBlockItemView.set | `change` |  |  |  | `item.controller.mediaView.change(pos: NSMakePoint(0, max(0, table.rectOf(item: item).minY)), animated: animated)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageBlockItem.swift:307` | StorageUsageBlockItemView.set | `change` |  |  |  | `item.controller.mediaView.change(opacity: item.isMediaVisible ? 1 : 0, animated: animated, completion: { [weak item] _ in` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageMediaItem.swift:322` | StorageUsageMediaItemView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageMediaItem.swift:323` | StorageUsageMediaItemView.set | `animateScaleSpring` | 0.3 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/DataUsageUI/Sources/DataUsageUI/StorageUsageController.swift:1028` | SelectPanel.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## EntertainmentUI (53)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/EntertainmentUI/Sources/EntertainmentUI/ReactionsWindowController.swift:84` | V.appearAnimated | `animateBounds` | duration | .spring |  | `self.container.layer?.animateBounds(from: from.size.bounds.offsetBy(dx: offset.x, dy: offset.y), to: to.size.bounds, duration: duration, tim` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/ReactionsWindowController.swift:86` | V.appearAnimated | `animatePosition` | duration | .spring |  | `self.container.layer?.animatePosition(from: offset, to: .zero, duration: duration, timingFunction: .spring)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/ReactionsWindowController.swift:93` | V.appearAnimated | `animate` | duration | .spring | shadowPath | `self.layer?.animate(from: fromPath, to: toPath, keyPath: "shadowPath", timingFunction: .spring, duration: duration)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/ReactionsWindowController.swift:434` | V.close | `animateScaleCenter` | 0.2 | .easeIn |  | `v.layer?.animateScaleCenter(from: 1, to: 0.9, duration: 0.2, removeOnCompletion: false, timingFunction: .easeIn)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/ReactionsWindowController.swift:436` | V.close | `animateAlpha` | 0.2 |  |  | `panel?.contentView?.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { _ in` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:1120` | CategoryView.apply | `animateAlpha` | 0.2 |  |  | `inline.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:1176` | CategoryView.update | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:1177` | CategoryView.update | `animateScale` | 0.2 |  |  | `current.animateScale(from: 0.1, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:1845` | AnimatedEmojiesView.updateSelectionState | `animatePosition` | 0.2 |  |  | `view.layer?.animatePosition(from: view.frame.origin, to: categoryRect.origin, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:1846` | AnimatedEmojiesView.updateSelectionState | `animateBounds` | 0.2 |  |  | `view.layer?.animateBounds(from: view.frame.size.bounds, to: categoryRect.size.bounds, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesController.swift:1879` | AnimatedEmojiesView.updateSelectionState | `animateCornerRadius` |  |  |  | `selectionView.layer?.animateCornerRadius()` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/GifKeyboardTabRowItem.swift:183` | GifKeyboardTabRowView.set | `change` |  |  |  | `selectView.change(opacity: item.selected ? 1 : 0, animated: animated)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackItems.swift:374` | StickerPackRowView.animateAppearance | `animateScale` | duration | .spring |  | `self.inlineSticker?.animateScale(from: 0.1, to: 1, duration: duration, timingFunction: .spring, delay: delay)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackItems.swift:375` | StickerPackRowView.animateAppearance | `animateScale` | duration | .spring |  | `self.lockedView?.animateScale(from: 0.1, to: 1, duration: duration, timingFunction: .spring, delay: delay)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackItems.swift:392` | StickerPackRowView.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackItems.swift:645` | ETabRowView.animateAppearance | `animateScaleSpring` | duration |  |  | `image.layer?.animateScaleSpring(from: 0.1, to: 1, duration: duration, delay: delay)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:652` | UnlockView.startLargeHold | `animateScale` | largeReactionHoldDuration |  |  | `layer.animateScale(from: layer.transform.m11, to: layer.transform.m11 * 1.5, duration: largeReactionHoldDuration, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:675` | UnlockView.cancelLargeHold | `animateScale` | 0.18 |  |  | `layer.animateScale(from: layer.presentation()?.transform.m11 ?? layer.transform.m11, to: layer.transform.m11, duration: 0.18, removeOnComple` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:690` | UnlockView.updateDown | `animateScale` | 0.12 |  |  | `itemUnderMouse.0.animateScale(from: itemUnderMouse.0.presentation()?.transform.m11 ?? itemUnderMouse.0.transform.m11, to: itemUnderMouse.0.t` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:706` | UnlockView.updateDragging | `animateScale` | 0.18 |  |  | `current.0.animateScale(from: current.0.presentation()?.transform.m11 ?? current.0.transform.m11 * 0.85, to: current.0.transform.m11, duratio` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:717` | UnlockView.updateDragging | `animateScale` | 0.18 |  |  | `current.0.animateScale(from: current.0.presentation()?.transform.m11 ?? current.0.transform.m11 * 0.85, to: current.0.transform.m11, duratio` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:720` | UnlockView.updateDragging | `animateScale` | 0.12 |  |  | `current.0.animateScale(from: current.0.presentation()?.transform.m11 ?? current.0.transform.m11, to: current.0.transform.m11 * 0.85, duratio` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:747` | UnlockView.updateUp | `animateScale` | 0.18 |  |  | `itemUnderMouse.0.animateScale(from: itemUnderMouse.0.presentation()?.transform.m11 ?? itemUnderMouse.0.transform.m11 * 0.85, to: itemUnderMo` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:867` | UnlockView.animateAppearance | `animateScale` | duration | .spring |  | `value.animateScale(from: 0.1, to: 1, duration: duration, timingFunction: .spring, delay: itemDelay)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:868` | UnlockView.animateAppearance | `animateScale` | duration | .spring |  | `locks[key]?.animateScale(from: 0.1, to: 1, duration: duration, timingFunction: .spring, delay: itemDelay)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:869` | UnlockView.animateAppearance | `animateScale` | duration | .spring |  | `selectedLayers[key]?.animateScale(from: 0.1, to: 1, duration: duration, timingFunction: .spring, delay: itemDelay)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:872` | UnlockView.animateAppearance | `animate` | 0.2 | .easeOut | cornerRadius | `selected.animate(from: NSNumber(value: selected.frame.height / 2), to: NSNumber(value: 10), keyPath: "cornerRadius", timingFunction: .easeOu` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:1237` | UnlockView.updateInlineStickers | `animateScale` | 0.3 | .spring |  | `view.animateScale(from: 0.1, to: 1, duration: 0.3, timingFunction: .spring)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:1238` | UnlockView.updateInlineStickers | `animateAlpha` | 0.2 |  |  | `view.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EmojiesSectionRowItem.swift:1281` | UnlockView.updateInlineStickers | `animateScale` | 0.18 | .easeOut |  | `view.animateScale(from: previousScale, to: scale, duration: 0.18, timingFunction: .easeOut)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickersViewController.swift:938` | NStickersView.updateSelectionState | `animatePosition` | 0.2 |  |  | `view.layer?.animatePosition(from: view.frame.origin, to: categoryRect.origin, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickersViewController.swift:939` | NStickersView.updateSelectionState | `animateBounds` | 0.2 |  |  | `view.layer?.animateBounds(from: view.frame.size.bounds, to: categoryRect.size.bounds, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickersViewController.swift:963` | NStickersView.updateSelectionState | `animateCornerRadius` |  |  |  | `selectionView.layer?.animateCornerRadius()` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/PanelSearchStatusView.swift:80` | PanelSearchStatusView.updateActivity | `animateAlpha` | 0.18 |  |  | `if !reduceMotion { view.layer?.animateAlpha(from: 0, to: 1, duration: 0.18) }` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/PanelSearchStatusView.swift:88` | PanelSearchStatusView.updateActivity | `CABasicAnimation` |  |  | locations | `let animation = CABasicAnimation(keyPath: "locations")` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/PanelSearchStatusView.swift:91` | PanelSearchStatusView.updateActivity | `.duration =` | 1.4 |  |  | `animation.duration = 1.4` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EBlockRowView.swift:63` | Key.setSelection | `animateScale` | 0.18 | .easeOut |  | `self.content.animateScale(from: previousScale, to: scale, duration: 0.18, timingFunction: .easeOut)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EBlockRowView.swift:139` | EBlockRowView.updateDown | `animateScale` | 0.2 |  |  | `itemUnderMouse.0.animateScale(from: 1, to: 0.85, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EBlockRowView.swift:148` | EBlockRowView.updateDragging | `animateScale` | 0.2 |  |  | `current.0.animateScale(from: 0.85, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EBlockRowView.swift:159` | EBlockRowView.updateDragging | `animateScale` | 0.2 |  |  | `current.0.animateScale(from: 0.85, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EBlockRowView.swift:162` | EBlockRowView.updateDragging | `animateScale` | 0.2 |  |  | `current.0.animateScale(from: 1, to: 0.85, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EBlockRowView.swift:175` | EBlockRowView.updateUp | `animateScale` | 0.2 |  |  | `itemUnderMouse.0.animateScale(from: 0.85, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/EntertainmentViewController.swift:181` | EntertainmentView.previewPremium | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:553` | ReorderState.updateDown | `animateScale` | 0.2 |  |  | `itemUnderMouse.0.animateScale(from: 1, to: 0.95, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:566` | ReorderState.updateDragging | `animateScale` | 0.2 |  |  | `current.0.animateScale(from: 0.95, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:569` | ReorderState.updateDragging | `animateScale` | 0.2 |  |  | `current.0.animateScale(from: 1, to: 0.95, duration: 0.2, removeOnCompletion: false)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:588` | ReorderState.updateUp | `animateScale` | 0.2 |  |  | `itemUnderMouse.0.animateScale(from: 0.95, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:606` | ReorderState.updateStickerDrag | `animateScale` | 0.2 |  |  | `current.0.animateScale(from: 0.95, to: 1, duration: 0.2, removeOnCompletion: true)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:627` | ReorderState.move | `animatePosition` | 0.2 |  |  | `layer.animatePosition(from: layer.presentation()?.position ?? layer.position, to: position, duration: 0.2, completion: completion)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:695` | ReorderState.startShaking | `CAKeyframeAnimation` | 0.4 |  | transform.rotation.z | `let animation = CAKeyframeAnimation(keyPath: "transform.rotation.z")` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:697` | ReorderState.startShaking | `.duration =` | 0.4 |  |  | `animation.duration = 0.4` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:724` | ReorderState.updateEditBadge | `animateScale` | 0.2 |  |  | `badge.animateScale(from: 0.01, to: 1, duration: 0.2)` |
| `packages/EntertainmentUI/Sources/EntertainmentUI/StickerPackPanelRowItem.swift:868` | ReorderState.updateInlineStickers | `animateScale` | 0.2 |  |  | `view.animateScale(from: 0.1, to: 1, duration: 0.2)` |

## FolderSharingUI (1)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/FolderSharingUI/Sources/FolderSharingUI/SharedFolderClosureController.swift:150` | JoinCloudFolderHeaderView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## ForumSettingsUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ForumSettingsUI/Sources/ForumSettingsUI/ForumNameRowItem.swift:133` | ForumNameRowItemView.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ForumSettingsUI/Sources/ForumSettingsUI/ForumNameRowItem.swift:134` | ForumNameRowItemView.set | `animateScaleSpring` | 0.2 |  |  | `current.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, center: false)` |

## GalleryUI (49)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControl.swift:177` | GalleryThumbsControl.layoutItems | `change` |  |  |  | `genericView.change(opacity: 0, animated: animated, completion: { [weak self] completed in` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControl.swift:184` | GalleryThumbsControl.layoutItems | `change` |  |  |  | `genericView.change(opacity: 1, animated: animated)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryViewer.swift:1675` | GalleryViewer.show | `_change` |  |  |  | `backgroundView._change(opacity: 0, animated: false)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryViewer.swift:1708` | GalleryViewer.show | `_change` |  |  |  | `strongSelf?.backgroundView._change(opacity: 1, animated: true)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryViewer.swift:1729` | GalleryViewer.close | `_change` |  |  |  | `backgroundView._change(opacity: 0, animated: true)` |
| `packages/GalleryUI/Sources/GalleryUI/MGalleryExternalVideoItem.swift:184` | VideoPlayerView.updateLayout | `_change` |  |  |  | `controls._change(opacity: _mouseInside() ? 1 : 0, animated: true)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControlView.swift:260` | GalleryThumbsControlView.removeItem | `change` |  |  |  | `subview?.opt?.change(opacity: 0, animated: animated, completion: { completed in` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControlView.swift:297` | GalleryThumbsControlView.layoutItems | `change` |  |  |  | `view?.overlay.change(opacity: 0.35)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControlView.swift:300` | GalleryThumbsControlView.layoutItems | `_change` | duration | CAMediaTimingFunctionName.spring |  | `view._change(size: rect.size, animated: animated, duration: duration, timingFunction: CAMediaTimingFunctionName.spring)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControlView.swift:303` | GalleryThumbsControlView.layoutItems | `_change` | duration | CAMediaTimingFunctionName.spring |  | `view.imageView._change(pos: f.origin, animated: animated, duration: duration, timingFunction: CAMediaTimingFunctionName.spring)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControlView.swift:305` | GalleryThumbsControlView.layoutItems | `_change` | duration | CAMediaTimingFunctionName.spring |  | `view._change(pos: rect.origin, animated: animated, duration: duration, timingFunction: CAMediaTimingFunctionName.spring)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryThumbsControlView.swift:314` | GalleryThumbsControlView.layoutItems | `change` |  |  |  | `view?.overlay.change(opacity: 0.0)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryModernControls.swift:389` | GalleryModernControlsView.updateInterface | `_change` |  |  |  | `photoView._change(opacity: NSPointInRect(point, photoView.frame) ? 1 : 0.7, animated: false)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryModernControls.swift:449` | GalleryModernControls.viewDidLoad | `change` |  |  |  | `self.thumbs.genericView.change(pos: NSMakePoint((self.frame.width - self.thumbs.frame.width) / 2 + (self.thumbs.frame.width - self.thumbs.ge` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryModernControls.swift:481` | GalleryModernControls.animateIn | `animateAlpha` | 0.2 | CAMediaTimingFunctionName.spring |  | `genericView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryModernControls.swift:482` | GalleryModernControls.animateIn | `change` |  | CAMediaTimingFunctionName.spring |  | `genericView.change(pos: NSMakePoint(0, 0), animated: true, timingFunction: CAMediaTimingFunctionName.spring)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryModernControls.swift:486` | GalleryModernControls.animateOut | `animateAlpha` | 0.2 |  |  | `genericView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false)` |
| `packages/GalleryUI/Sources/GalleryUI/MGalleryPhotoItem.swift:203` | MGalleryPhotoItem.setLivePhotoVideoVisible | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: visible ? 0 : 1, to: CGFloat(opacity), duration: 0.2)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:188` | GMagnifyView.updateProgress | `animateAlpha` | 0.25 | .linear |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.25, timingFunction: .linear, removeOnCompletion: false, completion: { [weak pro` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:587` | GalleryPageController.scrollWheel | `change` |  |  |  | `self.textScrollView.change(opacity: 1.0)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:591` | GalleryPageController.scrollWheel | `change` |  |  |  | `self.textScrollView.change(opacity: 0.0)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:655` | GalleryPageController.configureTextAutohide | `change` |  |  |  | `self.textScrollView.change(opacity: self.textScrollView._mouseInside() ? 1 : 0)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:892` | GalleryPageController.set | `NSAnimationContext.runAnimationGroup` |  |  |  | `NSAnimationContext.runAnimationGroup({ (context) in` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:940` | GalleryPageController.pageControllerWillStartLiveTransition | `change` |  |  |  | `textScrollView.change(opacity: 0)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:952` | GalleryPageController.pageControllerDidEndLiveTransition | `change` |  |  |  | `textScrollView.change(opacity: 0, animated: textScrollView.superview != nil, completion: { [weak textScrollView] completed in` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1015` | GalleryPageController.pageControllerDidEndLiveTransition | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1063` | GalleryPageController.pageControllerDidEndLiveTransition | `animateAlpha` | 0.25 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.25)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1331` | GalleryPageController.animateIn | `change` |  |  |  | `textScrollView.change(opacity: 0, animated: false)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1432` | GalleryPageController.animate | `animatePosition` | duration | timingFunction |  | `newView.layer?.animatePosition(from: oldRect.origin, to: newRect.origin, duration: duration, timingFunction: timingFunction, removeOnComplet` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1433` | GalleryPageController.animate | `animateAlpha` | duration / 2 | timingFunction |  | `newView.layer?.animateAlpha(from: newAlphaFrom, to: newAlphaTo, duration: duration / 2, timingFunction: timingFunction, removeOnCompletion: ` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1436` | GalleryPageController.animate | `animateScaleX` | duration | timingFunction |  | `newView.layer?.animateScaleX(from: oldRect.width / newRect.width, to: 1, duration: duration, timingFunction: timingFunction, removeOnComplet` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1437` | GalleryPageController.animate | `animateScaleY` | duration | timingFunction |  | `newView.layer?.animateScaleY(from: oldRect.height / newRect.height, to: 1, duration: duration, timingFunction: timingFunction, removeOnCompl` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1440` | GalleryPageController.animate | `animatePosition` | duration | timingFunction |  | `copyView.layer?.animatePosition(from: oldRect.origin, to: newRect.origin, duration: duration, timingFunction: timingFunction, removeOnComple` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1441` | GalleryPageController.animate | `animateScaleX` | duration | timingFunction |  | `copyView.layer?.animateScaleX(from: oldAlphaFrom == 0 ? oldRect.width / newRect.width : 1, to: oldAlphaFrom != 0 ? newRect.width / oldRect.w` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1442` | GalleryPageController.animate | `animateScaleY` | duration | timingFunction |  | `copyView.layer?.animateScaleY(from: oldAlphaFrom == 0 ? oldRect.height / newRect.height : 1, to: oldAlphaFrom != 0 ? newRect.height / oldRec` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1444` | GalleryPageController.animate | `animateAlpha` | duration | timingFunction |  | `copyView.layer?.animateAlpha(from: oldAlphaFrom , to: oldAlphaTo, duration: duration, timingFunction: timingFunction, removeOnCompletion: fa` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1460` | GalleryPageController.animateOut | `change` |  |  |  | `textScrollView.change(opacity: 0, animated: true)` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1499` | GalleryPageController.animateOut | `_change` |  |  |  | `view._change(opacity: 0, completion: { (_) in` |
| `packages/GalleryUI/Sources/GalleryUI/GalleryPageController.swift:1504` | GalleryPageController.animateOut | `_change` |  |  |  | `view._change(opacity: 0, completion: { (_) in` |
| `packages/GalleryUI/Sources/GalleryUI/PIPVideoWindow.swift:225` | ModernPictureInPictureVideoWindow.hide | `_change` | 0.1 | .linear |  | `contentView?._change(opacity: 0, animated: true, duration: 0.1, timingFunction: .linear)` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:532` | AdView.set | `change` |  |  |  | `counterView.change(size: dynamicResult.size, animated: animated)` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:533` | AdView.set | `change` |  |  |  | `counterView.change(pos: counterView.centerFrame().origin, animated: animated)` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:540` | AdView.set | `change` |  |  |  | `self?.progress.change(opacity: 0, animated: true)` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:545` | AdView.set | `change` |  |  |  | `self?.close.change(opacity: 1, animated: true)` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:1343` | SVideoView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:1514` | SVideoView.hideControls | `_change` | 0.2 | .linear |  | `controls._change(opacity: hide ? 0 : 1, animated: animated, duration: 0.2, timingFunction: .linear, completion: { [weak self] completed in` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:1523` | SVideoView.hideControls | `change` | 0.2 | .linear |  | `controls.change(opacity: hide ? 0 : 1, animated: animated, duration: 0.2, timingFunction: .linear, completion: { [weak self] completed in` |
| `packages/GalleryUI/Sources/GalleryUI/SVideoView.swift:1580` | SVideoView.setMode | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GalleryUI/Sources/GalleryUI/MGalleryItem.swift:686` | PublicPhoto.rewindForward | `animateContents` |  |  |  | `view.layer?.animateContents()` |

## GeneralRows (31)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/GeneralRows/Sources/GeneralRows/SliderContextMenuItem.swift:188` | SliderContextMenuRowView.set | `change` |  |  |  | `self.drawable?.change(opacity: item.volume > 0 ? 1 : 0, animated: animated)` |
| `packages/GeneralRows/Sources/GeneralRows/SliderContextMenuItem.swift:189` | SliderContextMenuRowView.set | `change` |  |  |  | `self.drawable_muted?.change(opacity: item.volume > 0 ? 0 : 1, animated: animated)` |
| `packages/GeneralRows/Sources/GeneralRows/SliderContextMenuItem.swift:195` | SliderContextMenuRowView.updateValue | `change` |  |  |  | `self.drawable?.change(opacity: value > 0 ? 1 : 0)` |
| `packages/GeneralRows/Sources/GeneralRows/SliderContextMenuItem.swift:196` | SliderContextMenuRowView.updateValue | `change` |  |  |  | `self.drawable_muted?.change(opacity: value > 0 ? 0 : 1)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:210` | PeerMediaDatePinnedView.updateIsVisible | `change` |  |  |  | `pillView.change(opacity: visible ? 1 : 0, animated: animated)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:232` | PeerMediaDatePinnedView.armHideTimer | `change` | 0.3 |  |  | `self.pillView.change(opacity: 0, animated: true, duration: 0.3)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:281` | PeerMediaDatePinnedView.morph | `animate` | duration | .easeOut | position | `incoming.layer?.animate(from: NSValue(point: NSMakePoint(0, offset)), to: NSValue(point: .zero), keyPath: "position", timingFunction: .easeO` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:282` | PeerMediaDatePinnedView.morph | `animateScaleSpring` | duration |  |  | `incoming.layer?.animateScaleSpring(from: scale, to: 1, duration: duration, bounce: false)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:283` | PeerMediaDatePinnedView.morph | `animateAlpha` | duration * |  |  | `incoming.layer?.animateAlpha(from: 0, to: 1, duration: duration * 0.6)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:287` | PeerMediaDatePinnedView.morph | `animate` | duration | .easeOut | position | `outgoing.layer?.animate(from: NSValue(point: .zero), to: NSValue(point: NSMakePoint(0, -offset)), keyPath: "position", timingFunction: .ease` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:288` | PeerMediaDatePinnedView.morph | `animateScaleSpring` | duration |  |  | `outgoing.layer?.animateScaleSpring(from: 1, to: scale, duration: duration, removeOnCompletion: false, bounce: false)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerMediaDateItem.swift:289` | PeerMediaDatePinnedView.morph | `animateAlpha` | duration * |  |  | `outgoing.layer?.animateAlpha(from: 1, to: 0, duration: duration * 0.4, removeOnCompletion: false, completion: { [weak self, weak outgoing] _` |
| `packages/GeneralRows/Sources/GeneralRows/PeerEmptyHolderItem.swift:105` | PeerEmptyHolderView.set | `change` |  |  |  | `self.containerView.change(size: contentRect.size, animated: animated, corners: item.viewType.corners)` |
| `packages/GeneralRows/Sources/GeneralRows/PeerEmptyHolderItem.swift:106` | PeerEmptyHolderView.set | `change` |  |  |  | `self.containerView.change(pos: contentRect.origin, animated: animated)` |
| `packages/GeneralRows/Sources/GeneralRows/SearchRowItem.swift:94` | SearchRowView.onInsert | `animateAlpha` | 0.2 | .easeOut |  | `self.searchView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeOut, completion: { [weak self] _ in` |
| `packages/GeneralRows/Sources/GeneralRows/LoadingTableItem.swift:97` | LoadingTableRowView.set | `change` |  |  |  | `self.containerView.change(size: contentRect.size, animated: animated, corners: item.viewType.corners)` |
| `packages/GeneralRows/Sources/GeneralRows/LoadingTableItem.swift:98` | LoadingTableRowView.set | `change` |  |  |  | `self.containerView.change(pos: contentRect.origin, animated: animated)` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:169` | GeneralRowContainerView.setCorners | `animate` | 0.18 | .easeOut | path | `self.maskLayer.animate(from: oldPath, to: newPath, keyPath: "path", timingFunction: .easeOut, duration: 0.18, removeOnCompletion: false, add` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:230` | GeneralRowContainerView.change | `change` | 0.18 |  |  | `open func change(size: NSSize, animated: Bool, corners: GeneralViewItemCorners) {` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:231` | GeneralRowContainerView.change | `_change` | 0.18 |  |  | `super._change(size: size, animated: animated, animated, duration: 0.18)` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:287` | GeneralRowView.set | `change` |  |  |  | `errorTextView!.change(pos: NSMakePoint(item.inset.left, frame.height - 6 - errorLayout.layoutSize.height), animated: posAnimated)` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:289` | GeneralRowView.set | `change` |  |  |  | `errorTextView!.change(pos: NSMakePoint(minX + insets.left, frame.height - 2 - errorLayout.layoutSize.height), animated: posAnimated)` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:292` | GeneralRowView.set | `animateAlpha` | 0.2 |  |  | `errorTextView!.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:298` | GeneralRowView.set | `animateAlpha` | 0.2 |  |  | `errorTextView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, completion: { [weak errorTextView] _ in` |
| `packages/GeneralRows/Sources/GeneralRows/FilterChipRowItem.swift:104` | FilterChipRowView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GeneralRows/Sources/GeneralRows/FilterChipRowItem.swift:105` | FilterChipRowView.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/GeneralRows/Sources/GeneralRows/ExternalUsernameRowItem.swift:162` | ExternalUsernameRowView.set | `animateBackground` |  |  |  | `imageView.layer?.animateBackground()` |
| `packages/GeneralRows/Sources/GeneralRows/ExternalUsernameRowItem.swift:163` | ExternalUsernameRowView.set | `animateContents` |  |  |  | `imageView.layer?.animateContents()` |
| `packages/GeneralRows/Sources/GeneralRows/ActionButton.swift:26` | ActionButton. | `change` |  |  |  | `control.change(opacity: 0.8, animated: true)` |
| `packages/GeneralRows/Sources/GeneralRows/ActionButton.swift:30` | ActionButton. | `change` |  |  |  | `control.change(opacity: 1.0, animated: true)` |
| `packages/GeneralRows/Sources/GeneralRows/ActionButton.swift:34` | ActionButton. | `change` |  |  |  | `control.change(opacity: 1.0, animated: true)` |

## GiftCraftingUI (18)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:812` | Style.startCubeAnimation | `animateAlpha` | duration |  |  | `sticker.animateAlpha(from: 1.0, to: 0.0, duration: duration, removeOnCompletion: false)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:813` | Style.startCubeAnimation | `animateScaleCenter` | duration |  |  | `sticker.animateScaleCenter(from: 1.0, to: 0.1, duration: duration, removeOnCompletion: false)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1049` | Style.showFailedState | `animateAlpha` | animationDuration | .easeOut |  | `descriptionView.layer?.animateAlpha(from: 1, to: 0, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1052` | Style.showFailedState | `animateAlpha` | animationDuration | .easeOut |  | `chanceIndicatorsContainer.layer?.animateAlpha(from: 1, to: 0, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1055` | Style.showFailedState | `animateAlpha` | animationDuration | .easeOut |  | `viewAllVariantsButton.layer?.animateAlpha(from: 1, to: 0, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1059` | Style.showFailedState | `animateAlpha` | animationDuration | .easeOut |  | `anvilPatternView.layer?.animateAlpha(from: 1, to: 0, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1114` | Style.showFailedState | `animateAlpha` | animationDuration | .easeOut |  | `container.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1116` | Style.showFailedState | `animatePosition` | animationDuration | .easeOut |  | `failedTitleView.layer?.animatePosition(from: NSMakePoint(0, 20), to: .zero, duration: animationDuration, timingFunction: .easeOut, additive:` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1117` | Style.showFailedState | `animatePosition` | animationDuration | .easeOut |  | `failedDescriptionView.layer?.animatePosition(from: NSMakePoint(0, 20), to: .zero, duration: animationDuration, timingFunction: .easeOut, add` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1118` | Style.showFailedState | `animatePosition` | animationDuration | .easeOut |  | `failedGiftsContainer.layer?.animatePosition(from: NSMakePoint(0, 20), to: .zero, duration: animationDuration, timingFunction: .easeOut, addi` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1121` | Style.showFailedState | `animateAlpha` | 0.2 | .easeOut |  | `giftView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1122` | Style.showFailedState | `animateScaleSpring` | 0.35 |  |  | `giftView.layer?.animateScaleSpring(from: 0.35, to: 1.0, duration: 0.35, bounce: false)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1148` | Style.hideFailedState | `animateAlpha` | animationDuration | .easeOut |  | `titleView.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1152` | Style.hideFailedState | `animateAlpha` | animationDuration | .easeOut |  | `descriptionView.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1156` | Style.hideFailedState | `animateAlpha` | animationDuration | .easeOut |  | `chanceIndicatorsContainer.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1160` | Style.hideFailedState | `animateAlpha` | animationDuration | .easeOut |  | `viewAllVariantsButton.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1164` | Style.hideFailedState | `animateAlpha` | animationDuration | .easeOut |  | `craftButton.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |
| `packages/GiftCraftingUI/Sources/GiftCraftingUI/GiftCraftingArea.swift:1168` | Style.hideFailedState | `animateAlpha` | animationDuration | .easeOut |  | `anvilPatternView.layer?.animateAlpha(from: 0, to: 1, duration: animationDuration, timingFunction: .easeOut)` |

## GraphUI (35)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:126` | Content.revealFromSkeleton | `animateAlpha` | 0.22 |  |  | `skeletonView.layer?.animateAlpha(from: 1, to: 0, duration: 0.22, removeOnCompletion: false, completion: { [weak skeletonView] _ in` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:140` | Content.revealFromSkeleton | `animateAlpha` | 0.3 |  |  | `self.titleView.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:142` | Content.revealFromSkeleton | `animateAlpha` | 0.3 |  |  | `self.pillView.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:143` | Content.revealFromSkeleton | `animateScaleSpring` | 0.45 |  |  | `self.pillView.layer?.animateScaleSpring(from: 0.7, to: 1, duration: 0.45, bounce: false)` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:168` | Content.update | `CABasicAnimation` |  |  | backgroundColor | `let animation = CABasicAnimation(keyPath: "backgroundColor")` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:171` | Content.update | `.duration =` | 0.25 |  |  | `animation.duration = 0.25` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:206` | Content.layoutContent | `_change` | 0.35 | .spring |  | `self.pillView._change(pos: pillFrame.origin, animated: true, duration: 0.35, timingFunction: .spring)` |
| `packages/GraphUI/Sources/Charts/views/ChartOverviewTileView.swift:207` | Content.layoutContent | `_change` | 0.35 | .spring |  | `self.pillView._change(size: pillFrame.size, animated: true, duration: 0.35, timingFunction: .spring)` |
| `packages/GraphUI/Sources/Charts/views/ChartSkeletonView.swift:83` | Shape.updateShine | `CABasicAnimation` |  |  | position.x | `let animation = CABasicAnimation(keyPath: "position.x")` |
| `packages/GraphUI/Sources/Charts/views/ChartSkeletonView.swift:86` | Shape.updateShine | `.duration =` | shineDuration |  |  | `animation.duration = shineDuration` |
| `packages/GraphUI/Sources/Charts/views/ChartVisibilityView.swift:24` | ChartVisibilityView.playReveal | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/GraphUI/Sources/Charts/views/ChartVisibilityView.swift:32` | ChartVisibilityView.playReveal | `CASpringAnimation` |  |  | position.y | `let move = CASpringAnimation(keyPath: "position.y")` |
| `packages/GraphUI/Sources/Charts/views/ChartVisibilityItemView.swift:88` | ChartVisibilityItemView.setPillColors | `CABasicAnimation` |  |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/GraphUI/Sources/Charts/views/ChartVisibilityItemView.swift:91` | ChartVisibilityItemView.setPillColors | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/GraphUI/Sources/Charts/views/ChartVisibilityItemView.swift:95` | ChartVisibilityItemView.setPillColors | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/GraphUI/Sources/Charts/views/ChartVisibilityItemView.swift:98` | ChartVisibilityItemView.setPillColors | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:18` | . | `CASpringAnimation` |  |  |  | `let animation = CASpringAnimation()` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:19` | . | `.mass =` |  |  |  | `animation.mass = 1` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:20` | . | `.stiffness =` |  |  |  | `animation.stiffness = springStiffness` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:21` | . | `.damping =` |  |  |  | `animation.damping = springDamping` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:23` | . | `settlingDuration` |  |  |  | `return animation.settlingDuration` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:587` | Change.spring | `CASpringAnimation` |  |  | keyPath | `let animation = CASpringAnimation(keyPath: keyPath)` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:590` | Change.spring | `.mass =` |  |  |  | `animation.mass = 1` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:591` | Change.spring | `.stiffness =` |  |  |  | `animation.stiffness = springStiffness` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:592` | Change.spring | `.damping =` | springSettlingDuration |  |  | `animation.damping = springDamping` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:594` | Change.spring | `.duration =` |  |  |  | `animation.duration = springSettlingDuration` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:604` | Change.fade | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/GraphUI/Sources/Charts/views/ChartMorphingTextView.swift:607` | Change.fade | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/GraphUI/Sources/Helpers/UIView+Extensions.swift:41` | NSView.perform | `NSAnimationContext.runAnimationGroup` |  |  |  | `NSAnimationContext.runAnimationGroup({ _ in` |
| `packages/GraphUI/Sources/Helpers/UIImageView+Utils.swift:9` | NSImageView.setImage | `CATransition` |  |  |  | `let animation = CATransition()` |
| `packages/GraphUI/Sources/Helpers/UIImageView+Utils.swift:12` | NSImageView.setImage | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/GraphUI/Sources/Helpers/UILabel+Utils.swift:9` | NSTextField.setTextColor | `CATransition` |  |  |  | `let animation = CATransition()` |
| `packages/GraphUI/Sources/Helpers/UILabel+Utils.swift:12` | NSTextField.setTextColor | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/GraphUI/Sources/Helpers/UILabel+Utils.swift:22` | NSTextField.setText | `CATransition` |  |  |  | `let animation = CATransition()` |
| `packages/GraphUI/Sources/Helpers/UILabel+Utils.swift:25` | NSTextField.setText | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |

## GroupCallScreenUI (122)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupVideoView.swift:147` | GroupVideoView.updateLayout | `CABasicAnimation` |  |  | sublayerTransform | `let animation = CABasicAnimation(keyPath: "sublayerTransform")` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupVideoView.swift:151` | GroupVideoView.updateLayout | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:550` | VideoContainer.set | `_change` |  |  |  | `photoView._change(opacity: item.isActivePeer ? 1.0 : 0.5, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:555` | VideoContainer.set | `change` |  |  |  | `speakingView.change(opacity: showSpeakingView ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:602` | VideoContainer.set | `animateAlpha` | 0.3 | .easeInEaseOut | cornerRadius | `videoContainer.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:604` | VideoContainer.set | `animate` | 0.2 | .easeInEaseOut | cornerRadius | `videoContainer.layer?.animate(from: NSNumber(value: from), to: NSNumber(value: 0), keyPath: "cornerRadius", timingFunction: .easeInEaseOut, ` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:606` | VideoContainer.set | `animateScaleCenter` | 0.2 |  |  | `videoContainer.layer?.animateScaleCenter(from: photoView.frame.height / videoContainer.frame.width, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:608` | VideoContainer.set | `animatePosition` | 0.2 |  |  | `videoContainer.layer?.animatePosition(from: NSMakePoint(0, -photoView.frame.minY - 10), to: videoContainer.frame.origin, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:615` | VideoContainer.set | `animateAlpha` | 0.2 |  |  | `first.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak first, weak self] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:622` | VideoContainer.set | `animate` | 0.2 | .easeInEaseOut | cornerRadius | `first.layer?.animate(from: NSNumber(value: 0), to: NSNumber(value: to), keyPath: "cornerRadius", timingFunction: .easeInEaseOut, duration: 0` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:624` | VideoContainer.set | `animateScaleCenter` | 0.3 |  |  | `first.layer?.animateScaleCenter(from: 1, to: photoView.frame.height / first.frame.width, duration: 0.3, removeOnCompletion: false)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:626` | VideoContainer.set | `animatePosition` | 0.2 |  |  | `first.layer?.animatePosition(from: first.frame.origin, to: NSMakePoint(0, -photoView.frame.minY - 10), duration: 0.2, removeOnCompletion: fa` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:826` | VideoContainer.set | `animateAlpha` | 0.2 |  |  | `videoView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:832` | VideoContainer.set | `animateAlpha` | 0.2 |  |  | `first.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak first, weak self] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:870` | VideoContainer.set | `_change` |  |  |  | `photoView._change(opacity: item.isActivePeer ? 1.0 : 0.5, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:900` | VideoContainer.set | `animateAlpha` | 0.2 |  |  | `statusView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak statusView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:903` | VideoContainer.set | `animatePosition` |  |  |  | `statusView.layer?.animatePosition(from: statusView.frame.origin, to: NSMakePoint(statusView.frame.minX, statusView.frame.minY + 10))` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:921` | VideoContainer.set | `animateAlpha` | 0.3 |  |  | `statusView.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:922` | VideoContainer.set | `animatePosition` |  |  |  | `statusView.layer?.animatePosition(from: NSMakePoint(statusViewPoint.x, statusViewPoint.y - 10), to: statusViewPoint)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:925` | VideoContainer.set | `change` |  |  |  | `statusView?.change(pos: statusViewPoint, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:949` | VideoContainer.set | `animateAlpha` | 0.3 |  |  | `volumeView.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:950` | VideoContainer.set | `animatePosition` |  |  |  | `volumeView.layer?.animatePosition(from: NSMakePoint(volumeView.frame.minX - volumeView.frame.width, volumeView.frame.minY), to: volumeView.f` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:953` | VideoContainer.set | `change` |  |  |  | `statusView.change(pos: statusViewPoint, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:960` | VideoContainer.set | `animateAlpha` | 0.3 |  |  | `volumeView.layer?.animateAlpha(from: 1, to: 0, duration: 0.3, removeOnCompletion: false, completion: { [weak volumeView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:963` | VideoContainer.set | `animatePosition` |  |  |  | `volumeView.layer?.animatePosition(from: volumeView.frame.origin, to: NSMakePoint(volumeView.frame.minX - volumeView.frame.width, volumeView.` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:968` | VideoContainer.set | `change` |  |  |  | `statusView.change(pos: statusViewPoint, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallParticipantRowItem.swift:1122` | GroupCallParticipantRowView.set | `animateAlpha` | 0.3 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:22` | GroupCallSpeakingView. | `CAKeyframeAnimation` |  |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:27` | GroupCallSpeakingView. | `.duration =` | 0.7 |  |  | `animation.duration = 0.7` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:43` | GroupCallSpeakingView.update | `change` |  |  |  | `self.change(size: NSMakeSize(animationView.frame.width + textView.frame.width, max(animationView.frame.height, textView.frame.height)), anim` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:77` | GroupCallRecordingView.layout | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:81` | GroupCallRecordingView.layout | `.duration =` | 1.0 |  |  | `animation.duration = 1.0` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:180` | Mode.updateMode | `animateBackground` |  |  |  | `backgroundView.layer?.animateBackground()` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:314` | Mode.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:325` | Mode.update | `animateAlpha` | 0.2 |  |  | `speakingView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak speakingView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:334` | Mode.update | `change` |  |  |  | `statusView.change(opacity: speakingView == nil ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:388` | Mode.update | `animateAlpha` | 0.2 |  |  | `recordingView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:400` | Mode.update | `animateAlpha` | 0.2 |  |  | `recordingView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false,completion: { [weak recordingView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:438` | Mode.update | `change` |  |  |  | `self.statusView.change(size: dynamicResult.size, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTitleView.swift:439` | Mode.update | `change` |  |  |  | `self.statusView.change(pos: NSMakePoint(floorToScreenPixels(backingScaleFactor, (frame.width - dynamicResult.size.width) / 2), frame.midY), ` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:62` | GroupCallScheduleTimerView.update | `change` |  |  |  | `counter.change(size: value.size, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:63` | GroupCallScheduleTimerView.update | `change` |  |  |  | `counter.change(pos: focus(value.size).origin, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:88` | GroupCallScheduleTimerView.update | `change` |  |  |  | `mask.change(pos: NSMakePoint(round((frame.width - value.size.width) / 2), focus(mask.frame.size).minY), animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:93` | GroupCallScheduleTimerView.update | `CABasicAnimation` |  |  | opacity | `let animation: CABasicAnimation = CABasicAnimation(keyPath: "opacity")` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:97` | GroupCallScheduleTimerView.update | `.duration =` | 1.0 |  |  | `animation.duration = 1.0` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:156` | GroupCallScheduleView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSchedule.swift:162` | GroupCallScheduleView.update | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSecureEmojiView.swift:46` | EmojiView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSecureEmojiView.swift:107` | EmojiView.update | `CABasicAnimation` | 4.2 |  | sublayerTransform.translation.y | `let animation = CABasicAnimation(keyPath: "sublayerTransform.translation.y")` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSecureEmojiView.swift:109` | EmojiView.update | `.duration =` | 0.7 |  |  | `animation.duration = 0.7` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSecureEmojiView.swift:231` | EmojiView.update | `change` |  |  |  | `self.textView.change(opacity: state.showConferenceKey ? 0 : 1, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:191` | Mode.updateMode | `change` |  |  |  | `self.speakText?.change(opacity: mode == .fullscreen \|\| callMode == .video ? 0 : 1, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:192` | Mode.updateMode | `_change` |  |  |  | `self.fullscreenBackgroundView._change(opacity: mode == .fullscreen ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:203` | Mode.updateMode | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:213` | Mode.updateMode | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:245` | Mode.updateMode | `animateAlpha` | 0.2 |  |  | `rightButton1.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:256` | Mode.updateMode | `animateAlpha` | 0.2 |  |  | `leftButton2.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:527` | Mode.update | `animateAlpha` | 0.3 |  |  | `speakText.layer?.animateAlpha(from: 1, to: 0, duration: 0.3, removeOnCompletion: false, completion: { [weak speakText] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:530` | Mode.update | `animateScaleSpring` | 0.5 |  |  | `speakText.layer?.animateScaleSpring(from: 1, to: 0.2, duration: 0.5)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:541` | Mode.update | `animateAlpha` | 0.3 |  |  | `speakText.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:542` | Mode.update | `animateScaleSpring` | 0.5 |  |  | `speakText.layer?.animateScaleSpring(from: 0.2, to: 1, duration: 0.5)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:574` | Mode.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallControlsView.swift:600` | Mode.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak current] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMessagesView.swift:186` | MessageItemView.onRemove | `animateScaleSpring` | 0.6 |  |  | `self.containerView.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.6, removeOnCompletion: false, bounce: false)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMessagesView.swift:192` | MessageItemView.onInsert | `animateScaleSpring` | 0.6 |  |  | `self.containerView.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.6, removeOnCompletion: false, bounce: false)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMessagesView.swift:215` | MessageItemView.set | `animateScaleSpring` | 0.2 |  |  | `containerView.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:163` | V.updateLayout | `change` |  |  |  | `self?.pinView?.change(opacity: self?.pinIsVisible == true ? 1 : 0, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:164` | V.updateLayout | `change` |  |  |  | `self?.backView?.change(opacity: self?.pinIsVisible == true ? 1 : 0, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:168` | V.updateLayout | `change` |  |  |  | `self?.pinView?.change(opacity: self?.pinIsVisible == true ? 1 : 0, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:169` | V.updateLayout | `change` |  |  |  | `self?.backView?.change(opacity: self?.pinIsVisible == true ? 1 : 0, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:173` | V.updateLayout | `change` |  |  |  | `self?.pinView?.change(opacity: 0, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:174` | V.updateLayout | `change` |  |  |  | `self?.backView?.change(opacity: 0, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:196` | V.updateMode | `change` |  |  |  | `shadowView.change(opacity: controlsMode == .normal ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:198` | V.updateMode | `change` |  |  |  | `nameView.change(opacity: controlsMode == .normal ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:199` | V.updateMode | `change` |  |  |  | `statusView.change(opacity: controlsMode == .normal ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:200` | V.updateMode | `change` |  |  |  | `self.pinView?.change(opacity: self.mouseInside() && self.pinIsVisible ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:201` | V.updateMode | `change` |  |  |  | `self.backView?.change(opacity: self.mouseInside() && self.pinIsVisible ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:245` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `currentPinView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:258` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:291` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `currentBackView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:299` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:311` | V.updatePeer | `change` |  |  |  | `self.pinView?.change(opacity: self.mouseInside() && pinIsVisible ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:312` | V.updatePeer | `change` |  |  |  | `self.backView?.change(opacity: self.mouseInside() && pinIsVisible ? 1 : 0, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:364` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:376` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:399` | V.updatePeer | `_change` |  |  |  | `videoView._change(opacity: isPaused ? 0 : 1, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:421` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `pausedTextView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:422` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `pausedImageView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:428` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `pausedTextView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak pausedTextView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallMainVideoContainer.swift:438` | V.updatePeer | `animateAlpha` | 0.2 |  |  | `pausedImageView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak pausedImageView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallIncomingView.swift:58` | ParticipantsView.update | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [we` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallIncomingView.swift:61` | ParticipantsView.update | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 1.0, to: 0.2, duration: duration)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallIncomingView.swift:76` | ParticipantsView.update | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: NSMakePoint(CGFloat(index) * (photoSize.width - 18), 0), to: control.frame.origin, timingFunction: timi` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallIncomingView.swift:78` | ParticipantsView.update | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallIncomingView.swift:79` | ParticipantsView.update | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallIncomingView.swift:88` | ParticipantsView.update | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, add` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:39` | NoStreamView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:387` | Content.updateMouse | `change` |  |  |  | `controlsContainer.change(opacity: mode == .invisible && isFullScreen && state?.controlsTooltip == nil ? 0 : 1, animated: animated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:410` | Content.idleHide | `change` |  |  |  | `controlsContainer.change(opacity: mode == .invisible && isFullScreen && state?.controlsTooltip == nil ? 0 : 1, animated: true)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:536` | Content.updateLayout | `change` |  |  |  | `view.change(opacity: isHidden ? 0 : 1, animated: transition.isAnimated)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:762` | Content.applyUpdates | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:765` | Content.applyUpdates | `animateScaleSpring` | 0.3 |  |  | `view.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.3)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:785` | Content.applyUpdates | `animateAlpha` | duration |  |  | `self.peersTable.layer?.animateAlpha(from: from, to: to, duration: duration, removeOnCompletion: false, completion: { [weak self] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:815` | Content.applyUpdates | `animateAlpha` | duration |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: duration)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:826` | Content.applyUpdates | `animateAlpha` | duration |  |  | `tileView.layer?.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false, completion: { [weak tileView] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:843` | Content.applyUpdates | `animateAlpha` | duration |  |  | `current.layer?.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false, completion: { [weak current] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:846` | Content.applyUpdates | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: current.frame.origin, to: current.frame.origin - NSMakePoint(0, 10), removeOnCompletion: false)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:861` | Content.applyUpdates | `animateAlpha` | duration |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: duration)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:877` | Content.applyUpdates | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: current.frame.origin - NSMakePoint(0, 10), to: current.frame.origin)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:924` | Content.applyUpdates | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:969` | Content.applyUpdates | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:970` | Content.applyUpdates | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:994` | Content.applyUpdates | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:995` | Content.applyUpdates | `animateScaleSpring` | 0.2 |  |  | `current.textContainer.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:1000` | Content.applyUpdates | `animateScaleSpring` | 0.2 |  |  | `view.textContainer.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallView.swift:1023` | Content.applyUpdates | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSendMessageView.swift:428` | InputState.makeReactions | `animateScaleSpring` | 0.2 |  |  | `view.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallSendMessageView.swift:429` | InputState.makeReactions | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTileView.swift:443` | Transition.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 2, duration: 0.2)` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTileView.swift:451` | Transition.update | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 2, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTileView.swift:485` | Transition.deleteItem | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] completion in` |
| `packages/GroupCallScreenUI/Sources/GroupCallScreenUI/GroupCallTileView.swift:512` | Transition.insertItem | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## ImageCanvasUI (15)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasView.swift:1270` | EditImageCanvasView.showColorPicker | `animateAlpha` | 0.15 |  |  | `picker.layer?.animateAlpha(from: 0, to: 1, duration: 0.15)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasView.swift:1271` | EditImageCanvasView.showColorPicker | `animateScaleSpring` | 0.3 |  |  | `picker.layer?.animateScaleSpring(from: 0.9, to: 1, duration: 0.3)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:151` | EditImageCutoutView.setProcessing | `change` |  |  |  | `photoView.change(opacity: processing ? 0.6 : 1.0, animated: true)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:163` | EditImageCutoutView.showSubject | `animateFrame` | 0.45 | .spring | shadowOpacity | `subjectLayer.animateFrame(from: start, to: target, duration: 0.45, timingFunction: .spring)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:165` | EditImageCutoutView.showSubject | `CAKeyframeAnimation` |  |  | shadowOpacity | `let glow = CAKeyframeAnimation(keyPath: "shadowOpacity")` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:171` | EditImageCutoutView.showSubject | `change` | 0.25 |  |  | `photoView.change(opacity: 0, animated: true, duration: 0.25)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:172` | EditImageCutoutView.showSubject | `change` | 0.25 |  |  | `checkerboard.change(opacity: 1, animated: true, duration: 0.25)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:179` | EditImageCutoutView.setSubjectImage | `animateScaleSpring` | 0.35 |  |  | `subjectLayer.animateScaleSpring(from: 0.94, to: 1, duration: 0.35, center: false)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:185` | EditImageCutoutView.hideSubject | `animateAlpha` | 0.2 |  |  | `subjectLayer.animateAlpha(from: 1, to: 0, duration: 0.2)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:186` | EditImageCutoutView.hideSubject | `change` | 0.25 |  |  | `photoView.change(opacity: 1, animated: true, duration: 0.25)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCutoutController.swift:187` | EditImageCutoutView.hideSubject | `change` | 0.25 |  |  | `checkerboard.change(opacity: 0, animated: true, duration: 0.25)` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasControls.swift:620` | EditImageCanvasToolsRow.layoutTools | `NSAnimationContext.runAnimationGroup` | 0.25 |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasControls.swift:621` | EditImageCanvasToolsRow.layoutTools | `.duration =` | 0.25 |  |  | `context.duration = 0.25` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasControls.swift:1030` | EditImageCanvasModeRow.layoutPill | `NSAnimationContext.runAnimationGroup` | 0.2 |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/ImageCanvasUI/Sources/ImageCanvasUI/EditImageCanvasControls.swift:1031` | EditImageCanvasModeRow.layoutPill | `.duration =` | 0.2 |  |  | `context.duration = 0.2` |

## InlineMediaGrid (12)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:400` | MediaCell.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:418` | MediaCell.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:437` | MediaCell.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:475` | MediaCell.updateSelectionState | `animateAlpha` | 0.2 |  |  | `selectionView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:476` | MediaCell.updateSelectionState | `animateScaleSpring` | 0.2 |  |  | `selectionView?.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.2)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:483` | MediaCell.updateSelectionState | `animateScaleSpring` | 0.2 |  |  | `selectionView.layer?.animateScaleSpring(from: 1.0, to: 0.1, duration: 0.2)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/MediaCell.swift:484` | MediaCell.updateSelectionState | `animateAlpha` | 0.2 |  |  | `selectionView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak selectionView] completion in` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/ChatMessageAccessoryView.swift:263` | ChatMessageAccessoryView.updateText | `change` |  |  |  | `change(size: newSize, animated: animated)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/ChatMessageAccessoryView.swift:264` | ChatMessageAccessoryView.updateText | `change` |  |  |  | `backgroundView.change(size: newSize, animated: animated)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/ChatMessageAccessoryView.swift:278` | ChatMessageAccessoryView.updateText | `change` |  |  |  | `textView.change(pos: rect.origin, animated: animated)` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/ChatMessageAccessoryView.swift:281` | ChatMessageAccessoryView.updateText | `CABasicAnimation` |  |  | cornerRadius | `let cornerAnimation = CABasicAnimation(keyPath: "cornerRadius")` |
| `packages/InlineMediaGrid/Sources/InlineMediaGrid/ChatMessageAccessoryView.swift:285` | ChatMessageAccessoryView.updateText | `.duration =` | 0.2 |  |  | `cornerAnimation.duration = 0.2` |

## InlineStickerLayer (5)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InlineStickerLayer/Sources/InlineStickerLayer/InlineStickerItemLayer.swift:442` | FetchMode.removePlaceholder | `animateAlpha` | 0.2 |  |  | `shimmer.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak shimmer] _ in` |
| `packages/InlineStickerLayer/Sources/InlineStickerLayer/InlineStickerItemLayer.swift:673` | Shimmer.set | `animateContents` |  |  |  | `layer?.animateContents()` |
| `packages/InlineStickerLayer/Sources/InlineStickerLayer/InlineStickerItemLayer.swift:942` | Shimmer.updateSize | `animateContents` |  |  |  | `self?.animateContents()` |
| `packages/InlineStickerLayer/Sources/InlineStickerLayer/PeerInfoSpawnEmojiView.swift:144` | PeerInfoSpawnEmojiView.animateIn | `animate` | 0.4 | .spring | position | `layer.animate(from: center, to: NSValue(point: layer.position), keyPath: "position", timingFunction: .spring, duration: 0.4, delay: delay)` |
| `packages/InlineStickerLayer/Sources/InlineStickerLayer/PeerInfoSpawnEmojiView.swift:146` | PeerInfoSpawnEmojiView.animateIn | `animate` | 0.01 | .linear | opacity | `avatarBackgroundPatternContainer.animate(from: NSNumber(value: 0), to: NSNumber(value: 1), keyPath: "opacity", timingFunction: .linear, dura` |

## InputDataUI (26)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:464` | InputDataRowView.changeSeparator | `animateBounds` | 0.2 | .easeOut |  | `separator.animateBounds(from: from, to: rect.size.bounds, duration: 0.2, timingFunction: .easeOut)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:476` | InputDataRowView.changeSeparator | `animatePosition` | 0.2 | .easeOut |  | `separator.animatePosition(from: from, to: rect.origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:881` | InputDataRowView.set | `change` |  |  |  | `containerView.change(size: containerRect.size, animated: animated, corners: item.viewType.corners)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:882` | InputDataRowView.set | `change` |  |  |  | `containerView.change(pos: containerRect.origin, animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:982` | InputDataRowView.set | `animateAlpha` | 0.2 |  |  | `placeholderAction!.layer?.animateAlpha(from: 0, to: 2, duration: 0.2)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:988` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(item.inset.left + item.textFieldLeftInset - 3, 6), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:992` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(textX, textView.frame.minY), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:994` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(textX, textView.frame.minY), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1015` | InputDataRowView.set | `animateAlpha` | 0.2 |  |  | `placeholderAction.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak placeholderAction] _ in` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1027` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(item.inset.left + item.textFieldLeftInset - 3, 6), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1031` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(textX, textView.frame.minY), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1033` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(textX, textView.frame.minY), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1043` | InputDataRowView.set | `animateAlpha` | 0.2 |  |  | `placeholderAction.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak placeholderAction] _ in` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1057` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(item.inset.left + item.textFieldLeftInset - 3, 6), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1061` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(textX, textView.frame.minY), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataRowItem.swift:1063` | InputDataRowView.set | `_change` |  |  |  | `textView._change(pos: NSMakePoint(textX, textView.frame.minY), animated: animated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:87` | InputDataModalController.push | `animatePosition` | 0.35 | .spring |  | `controller.view.layer?.animatePosition(from: NSMakePoint(width / 3 * 2, 0), to: NSZeroPoint, duration: 0.35, timingFunction: .spring)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:89` | InputDataModalController.push | `animatePosition` | 0.35 | .spring |  | `tableView.layer?.animatePosition(from: tableView.frame.origin, to: NSMakePoint(tableView.frame.minX - width / 3, tableView.frame.minY), dura` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:138` | InputDataModalController.pop | `ContainedViewLayoutTransition.animated` | 0.35 | .spring |  | `let transition = animated ? ContainedViewLayoutTransition.animated(duration: 0.35, curve: .spring) : .immediate` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:148` | InputDataModalController.pop | `animatePosition` | 0.35 | .spring |  | `tableView.layer?.animatePosition(from: NSMakePoint(tableView.frame.minX - width / 3, tableView.frame.minY), to: tableView.frame.origin, dura` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:423` | InputDataModalController.updateFrame | `change` |  |  |  | `controller.genericView.change(size: frame.size, animated: transition.isAnimated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:424` | InputDataModalController.updateFrame | `change` |  |  |  | `controller.genericView.change(pos: frame.origin, animated: transition.isAnimated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:426` | InputDataModalController.updateFrame | `change` |  |  |  | `current.genericView.change(size: frame.size, animated: transition.isAnimated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:427` | InputDataModalController.updateFrame | `change` |  |  |  | `current.genericView.change(pos: NSMakePoint(0, 0), animated: transition.isAnimated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:430` | InputDataModalController.updateFrame | `change` |  |  |  | `current.genericView.change(size: frame.size, animated: transition.isAnimated)` |
| `packages/InputDataUI/Sources/InputDataUI/InputDataController.swift:431` | InputDataModalController.updateFrame | `change` |  |  |  | `current.genericView.change(pos: frame.origin, animated: transition.isAnimated)` |

## InputTextView (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InputTextView/Sources/InputTextView/FoldingTextView.swift:980` | WrapperView.update | `animateContents` |  |  |  | `current.animateContents()` |
| `packages/InputTextView/Sources/InputTextView/FoldingTextView.swift:1191` | FoldingTextView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## InputView (3)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InputView/Sources/InputView/ChatInputTextView.swift:477` | ChatInputTextView.updatePlaceholder | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/InputView/Sources/InputView/ChatInputTextView.swift:478` | ChatInputTextView.updatePlaceholder | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: current.frame.origin.offsetBy(dx: 20, dy: 0), to: current.frame.origin)` |
| `packages/InputView/Sources/InputView/ChatInputTextView.swift:483` | ChatInputTextView.updatePlaceholder | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false)` |

## InstantPageUI (15)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:105` | HeaderView.updateTitle | `animateAlpha` | 0.2 | CAMediaTimingFunctionName.spring |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: CAMediaTimingFunctionName.spring, completion: { [weak self, weak vie` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:111` | HeaderView.updateTitle | `change` |  | CAMediaTimingFunctionName.spring |  | `titleView?.change(opacity: 0, timingFunction: CAMediaTimingFunctionName.spring)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:121` | HeaderView.updateBorder | `change` |  |  |  | `borderView.change(opacity: isVisible ? 1 : 0, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:125` | HeaderView.updateBackVisiblity | `change` |  |  |  | `back.change(opacity: isVisible ? 1 : 0, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:392` | InstantViewController.updateProgress | `change` |  |  |  | `self.genericView.loadingIndicatorView.change(opacity: 0, animated: animated, completion: { [weak self] completed in` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantViewWindow.swift:398` | InstantViewController.updateProgress | `change` |  |  |  | `self.genericView.loadingIndicatorView.change(opacity: 1, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageV2ThinkingView.swift:134` | InstantPageV2ThinkingView.setRevealed | `animateAlpha` |  |  |  | `layer.animateAlpha(` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageViewController.swift:733` | InstantPageViewController.updateVisibleItems | `_change` |  |  |  | `(itemView as! NSView)._change(size: itemFrame.size, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageViewController.swift:734` | InstantPageViewController.updateVisibleItems | `_change` |  |  |  | `(itemView as! NSView)._change(pos: itemFrame.origin, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageViewController.swift:768` | InstantPageViewController.updateVisibleItems | `_change` |  |  |  | `view._change(pos: tileFrame.origin, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageViewController.swift:769` | InstantPageViewController.updateVisibleItems | `_change` |  |  |  | `view._change(size: tileFrame.size, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageContentView.swift:218` | InstantPageContentView.updateVisibleItems | `_change` |  |  |  | `(itemView as! NSView)._change(size: itemFrame.size, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageContentView.swift:219` | InstantPageContentView.updateVisibleItems | `_change` |  |  |  | `(itemView as! NSView)._change(pos: itemFrame.origin, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageContentView.swift:254` | InstantPageContentView.updateVisibleItems | `_change` |  |  |  | `view._change(pos: tileFrame.origin, animated: animated)` |
| `packages/InstantPageUI/Sources/InstantPageUI/InstantPageContentView.swift:255` | InstantPageContentView.updateVisibleItems | `_change` |  |  |  | `view._change(size: tileFrame.size, animated: animated)` |

## InviteLinksUI (16)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationRowItem.swift:366` | ExportedInvitationRowView.set | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 1, to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completion: { [we` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationRowItem.swift:369` | ExportedInvitationRowView.set | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 1.0, to: 0.2, duration: duration, bounce: false)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationRowItem.swift:384` | ExportedInvitationRowView.set | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: NSMakePoint(CGFloat(index) * (avatarSize.width - 14), 0), to: control.frame.origin, timingFunction: tim` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationRowItem.swift:386` | ExportedInvitationRowView.set | `animateAlpha` | duration | timingFunction |  | `control.layer?.animateAlpha(from: 0, to: 1, duration: duration, timingFunction: timingFunction)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationRowItem.swift:387` | ExportedInvitationRowView.set | `animateScaleSpring` | duration |  |  | `control.layer?.animateScaleSpring(from: 0.2, to: 1.0, duration: duration, bounce: false)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/ExportedInvitationRowItem.swift:396` | ExportedInvitationRowView.set | `animatePosition` | duration | timingFunction |  | `control.layer?.animatePosition(from: control.frame.origin - updatedPoint, to: .zero, duration: duration, timingFunction: timingFunction, add` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/InviteLinkRowItem.swift:283` | InviteLinkTokenView.update | `change` |  |  |  | `actions.change(pos: actionsPoint, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/InviteLinkRowItem.swift:284` | InviteLinkTokenView.update | `change` |  |  |  | `progressView.change(pos: progressPoint, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/InviteLinkRowItem.swift:366` | InviteLinkTokenView.update | `change` |  |  |  | `self.titleView.change(pos: self.titlePoint, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/InviteLinkRowItem.swift:367` | InviteLinkTokenView.update | `change` |  |  |  | `self.countView.change(pos: self.countPoint, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/PeerRequestJoinRowItem.swift:248` | PeerRequestJoinRowView.set | `change` |  |  |  | `self.addButton.change(opacity: 1, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/PeerRequestJoinRowItem.swift:250` | PeerRequestJoinRowView.set | `change` |  |  |  | `self.addButton.change(opacity: 0, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/PeerRequestJoinRowItem.swift:253` | PeerRequestJoinRowView.set | `change` |  |  |  | `self.dismissButton.change(opacity: 1, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/PeerRequestJoinRowItem.swift:255` | PeerRequestJoinRowView.set | `change` |  |  |  | `self.dismissButton.change(opacity: 0, animated: animated)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/PeerRequestJoinRowItem.swift:273` | PeerRequestJoinRowView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/InviteLinksUI/Sources/InviteLinksUI/PeerRequestJoinRowItem.swift:303` | PeerRequestJoinRowView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## LocationUI (16)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:65` | LocationPinView.updateState | `change` | 0.3 | CAMediaTimingFunctionName.spring |  | `dotView.change(opacity: 0, animated: animated)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:66` | LocationPinView.updateState | `change` | 0.3 | CAMediaTimingFunctionName.spring |  | `locationPin.change(pos: NSMakePoint(locationPin.frame.minX, frame.height - dotView.frame.height - locationPin.frame.height - 6), animated: a` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:68` | LocationPinView.updateState | `change` | 0.3 | CAMediaTimingFunctionName.spring |  | `dotView.change(opacity: 1, animated: animated)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:69` | LocationPinView.updateState | `change` | 0.3 | CAMediaTimingFunctionName.spring |  | `locationPin.change(pos: NSMakePoint(locationPin.frame.minX, location == nil ? 0 : frame.height - dotView.frame.height - locationPin.frame.he` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:183` | LocationMapView.updateExpandState | `change` |  |  |  | `locationPinView.change(opacity: 1, animated: animated)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:187` | LocationMapView.updateExpandState | `change` | duration | CAMediaTimingFunctionName.spring |  | `tableView.change(size: NSMakeSize(frame.width, 60), animated: animated, timingFunction: CAMediaTimingFunctionName.spring)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:188` | LocationMapView.updateExpandState | `change` | duration | timingFunction |  | `tableView.change(pos: NSMakePoint(0, frame.height - 60 - (hasExpand ? expandContainer.frame.height : 0)), animated: animated, duration: dura` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:192` | LocationMapView.updateExpandState | `_change` |  |  |  | `zoomControl?._change(opacity: 1, animated: animated)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:195` | LocationMapView.updateExpandState | `_change` |  |  |  | `zoomControl?._change(opacity: 0, animated: animated, completion: { [weak self] completed in` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:201` | LocationMapView.updateExpandState | `change` |  |  |  | `locationPinView.change(opacity: 0, animated: animated)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:205` | LocationMapView.updateExpandState | `change` | duration | timingFunction |  | `tableView.change(size: NSMakeSize(frame.width, tableHeight), animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:206` | LocationMapView.updateExpandState | `change` | duration | timingFunction |  | `tableView.change(pos: NSMakePoint(0, frame.height - (hasExpand ? expandContainer.frame.height : 0) - tableHeight), animated: animated, durat` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:209` | LocationMapView.updateExpandState | `change` | duration | timingFunction |  | `expandContainer.change(pos: NSMakePoint(0, hasExpand ? frame.height - expandContainer.frame.height : frame.height), animated: animated, dura` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:211` | LocationMapView.updateExpandState | `_change` | duration | timingFunction |  | `zoomControl._change(pos: zoomControlOrigin(zoomControl), animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:216` | LocationMapView.updateExpandState | `_change` | duration | timingFunction |  | `mapView._change(pos: NSMakePoint(0, mapY), animated: animated, duration: duration, timingFunction: timingFunction)` |
| `packages/LocationUI/Sources/LocationUI/LocationModalController.swift:219` | LocationMapView.updateExpandState | `change` | 0.2 | CAMediaTimingFunctionName.linear |  | `locationPinView.change(pos: NSMakePoint(pinPoint.minX, pinPoint.midY - locationPinView.frame.height), animated: animated, duration: 0.2, tim` |

## MediaRecorderUI (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/MediaRecorderUI/Sources/MediaRecorderUI/VideoRecorderModalView.swift:116` | VideoRecorderModalView.fadeOutPausedPlayer | `animateAlpha` | 0.3 |  |  | `layer.animateAlpha(from: 1, to: 0, duration: 0.3, completion: { [weak layer] _ in` |
| `packages/MediaRecorderUI/Sources/MediaRecorderUI/VideoRecorderModalView.swift:236` | VideoRecorderModalView.updateForPreview | `animateAlpha` | 0.2 |  |  | `placeholderView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2)` |
| `packages/MediaRecorderUI/Sources/MediaRecorderUI/VideoRecorderModalView.swift:241` | VideoRecorderModalView.updateForPreview | `change` |  |  |  | `progressView.change(opacity: 0, removeOnCompletion: false) { [weak self] completed in` |
| `packages/MediaRecorderUI/Sources/MediaRecorderUI/VideoRecorderModalView.swift:256` | VideoRecorderModalView.didStartedRecording | `change` | 0.3 |  |  | `placeholderView.change(opacity: 0.0, duration: 0.3)` |

## MonetizationUI (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/MonetizationUI/Sources/MonetizationUI/FragmentMonetizationController.swift:1262` | WithdrawInput.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/MonetizationUI/Sources/MonetizationUI/FragmentMonetizationController.swift:1280` | WithdrawInput.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/MonetizationUI/Sources/MonetizationUI/FragmentStarMonetizationController.swift:918` | WithdrawInput.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/MonetizationUI/Sources/MonetizationUI/FragmentStarMonetizationController.swift:936` | WithdrawInput.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## PasscodeUI (5)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PasscodeUI/Sources/PasscodeUI/PasscodeLockController.swift:269` | PasscodeLockView.change | `_change` |  |  |  | `input._change(size: NSMakeSize(width, input.frame.height), animated: animated)` |
| `packages/PasscodeUI/Sources/PasscodeUI/PasscodeLockController.swift:270` | PasscodeLockView.change | `_change` |  |  |  | `input._change(pos: NSMakePoint(PasscodeLockView.textInset, input.frame.minY), animated: animated)` |
| `packages/PasscodeUI/Sources/PasscodeUI/PasscodeLockController.swift:271` | PasscodeLockView.change | `change` |  |  |  | `nextButton.change(opacity: 1, animated: animated)` |
| `packages/PasscodeUI/Sources/PasscodeUI/PasscodeLockController.swift:275` | PasscodeLockView.change | `_change` |  |  |  | `input._change(pos: NSMakePoint(f.minX, input.frame.minY), animated: animated)` |
| `packages/PasscodeUI/Sources/PasscodeUI/PasscodeLockController.swift:276` | PasscodeLockView.change | `change` |  |  |  | `nextButton.change(opacity: 0, animated: animated)` |

## PaymentsUI (6)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PaymentsUI/Sources/PaymentsUI/PaymentsTipsRowItem.swift:179` | PaymentsTipView.update | `animateBackground` |  |  |  | `layer?.animateBackground()` |
| `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutPriceItem.swift:152` | PaymentsCheckoutPriceView.set | `change` |  |  |  | `self.price.change(opacity: !input.string.isEmpty ? 0 : 1, animated: false)` |
| `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutPriceItem.swift:165` | PaymentsCheckoutPriceView.set | `change` |  |  |  | `self.price.change(opacity: !input.string.isEmpty ? 0 : 1, animated: false)` |
| `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutPriceItem.swift:199` | PaymentsCheckoutPriceView.textDidChange | `change` |  |  |  | `self.price.change(opacity: !text.isEmpty ? 0 : 1, animated: false)` |
| `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutRecurrentRowItem.swift:132` | PaymentsCheckoutRecurrentRowView.set | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PaymentsUI/Sources/PaymentsUI/PaymentsCheckoutRecurrentRowItem.swift:133` | PaymentsCheckoutRecurrentRowView.set | `animateScaleCenter` | 0.2 |  |  | `view.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |

## PeerInfoUI (55)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoController.swift:467` | PeerInfoView.updateScrollState | `change` |  |  |  | `self.navBgView.change(opacity: state == .pageIn ? 1 : 0, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoController.swift:873` | ScrollState.separateNumbers | `animateScale` | 0.2 |  |  | `layer.animateScale(from: 0.01, to: 1.0, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoController.swift:874` | ScrollState.separateNumbers | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 0, to: 1.0, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaTabsView.swift:58` | ItemView.update | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaTabsView.swift:59` | ItemView.update | `animateScaleCenter` | 0.2 |  |  | `view.layer?.animateScaleCenter(from: 0.01, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaTabsView.swift:66` | ItemView.update | `animateScaleCenter` | 0.25 |  |  | `view.layer?.animateScaleCenter(from: 1, to: 0.01, duration: 0.25, removeOnCompletion: false)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaTabsView.swift:183` | ItemView.update | `animateScaleCenter` | 0.25 |  |  | `view.layer?.animateScaleCenter(from: 1, to: 0.01, duration: 0.25, removeOnCompletion: false)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaTabsView.swift:207` | ItemView.update | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaTabsView.swift:208` | ItemView.update | `animateScaleCenter` | 0.3 |  |  | `view.layer?.animateScaleCenter(from: 0.01, to: 1, duration: 0.3)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:195` | PeerMediaContainerView.updateEmpty | `animateAlpha` | 0.2 |  |  | `self.emptyView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:213` | PeerMediaContainerView.changeState | `change` |  |  |  | `actionsPanelView.change(pos: NSMakePoint(0, frame.height - inset), animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:337` | PeerMediaControllerView.setHeaderPinned | `change` |  |  |  | `headerUnderlayView.change(opacity: pinned ? 1 : 0, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:338` | PeerMediaControllerView.setHeaderPinned | `change` |  |  |  | `headerEdgeView.change(opacity: pinned ? 1 : 0, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:443` | PeerMediaControllerView.cancelSwipe | `animatePosition` | 0.4 | .spring |  | `visibleNeighbor.layer?.animatePosition(from: visibleNeighbor.frame.origin, to: NSMakePoint(side * contentView.frame.width, visibleNeighbor.f` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:445` | PeerMediaControllerView.cancelSwipe | `_change` | 0.4 | .spring |  | `mainView?._change(pos: NSZeroPoint, animated: true, duration: 0.4, timingFunction: .spring, completion: { [weak self] completed in` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:590` | PeerMediaControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `previousMain.layer?.animatePosition(from: origin, to: NSMakePoint(origin.x - previousMain.frame.width, origin.y), duration: duration, timing` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:591` | PeerMediaControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `view.layer?.animatePosition(from: NSMakePoint(view.frame.width, origin.y), to: NSMakePoint(0, origin.y), duration: duration, timingFunction:` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:593` | PeerMediaControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `previousMain.layer?.animatePosition(from: origin, to: NSMakePoint(origin.x + previousMain.frame.width, origin.y), duration: duration, timing` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:594` | PeerMediaControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `view.layer?.animatePosition(from: NSMakePoint(-view.frame.width, origin.y), to: NSMakePoint(0, origin.y), duration: duration, timingFunction` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:597` | PeerMediaControllerView.updateMainView | `animatePosition` | duration | timingFunction |  | `previousMain.layer?.animatePosition(from: origin, to: NSMakePoint(exitX, origin.y), duration: duration, timingFunction: timingFunction, remo` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:598` | PeerMediaControllerView.updateMainView | `_change` | duration | timingFunction |  | `view._change(pos: NSZeroPoint, animated: true, duration: duration, timingFunction: timingFunction, completion: settle)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:623` | PeerMediaControllerView.updateSearchState | `animateAlpha` | 0.2 | .spring |  | `searchPanelView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:624` | PeerMediaControllerView.updateSearchState | `animatePosition` | 0.4 | .spring |  | `searchPanelView.layer?.animatePosition(from: NSMakePoint(searchPanelView.frame.minX, searchPanelView.frame.minY - 10), to: searchPanelView.f` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:632` | PeerMediaControllerView.updateSearchState | `_change` |  |  |  | `tabsView._change(opacity: 0, animated: state.animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:634` | PeerMediaControllerView.updateSearchState | `_change` |  |  |  | `tabsView._change(opacity: 1, animated: state.animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaController.swift:2450` | TabSwipeGesture.updateSearchBarVisibility | `change` |  |  |  | `stackedBar.change(opacity: visible ? 1 : 0, for: searchBtn, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PersonalChannelRowItem.swift:193` | LoadingView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaBlockRowItem.swift:225` | PeerMediaBlockRowView.set | `change` |  |  |  | `item.controller.genericView.change(pos: NSMakePoint(0, max(0, table.rectOf(item: item).minY)), animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerMediaBlockRowItem.swift:232` | PeerMediaBlockRowView.set | `change` |  |  |  | `item.controller.genericView.change(opacity: item.isMediaVisible ? 1 : 0, animated: animated, completion: { [weak item] _ in` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1281` | GiftIconLayer.startAnimations | `CABasicAnimation` | hoverDuration |  | transform.translation.y | `let hoverAnimation = CABasicAnimation(keyPath: "transform.translation.y")` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1282` | GiftIconLayer.startAnimations | `.duration =` | hoverDuration |  |  | `hoverAnimation.duration = hoverDuration` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1298` | GiftIconLayer.startAnimations | `CABasicAnimation` | wiggleDuration |  | transform.rotation.z | `let wiggleAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1299` | GiftIconLayer.startAnimations | `.duration =` | wiggleDuration |  |  | `wiggleAnimation.duration = wiggleDuration` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1313` | GiftIconLayer.startAnimations | `CABasicAnimation` | glowDuration |  | transform.scale | `let glowAnimation = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1314` | GiftIconLayer.startAnimations | `.duration =` | glowDuration |  |  | `glowAnimation.duration = glowDuration` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1512` | SpawnGiftsView.update | `animateAlpha` | 0.2 |  |  | `iconLayer.animateAlpha(from: 0.0, to: 1.0, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1513` | SpawnGiftsView.update | `animateScale` | 0.2 |  |  | `iconLayer.animateScale(from: 0.01, to: 1.0, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1549` | SpawnGiftsView.interpolatePosition | `animateScale` | 0.25 |  |  | `layer.animateScale(from: 1.0, to: 0.01, duration: 0.25, removeOnCompletion: false)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1550` | SpawnGiftsView.interpolatePosition | `animateAlpha` | 0.25 |  |  | `layer.animateAlpha(from: 1.0, to: 0.0, duration: 0.25, removeOnCompletion: false, completion: { _ in` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:1575` | SpawnGiftsView.animateIn | `animatePosition` | 0.4 | .spring |  | `layer.animatePosition(from: avatarCenter, to: layer.position, duration: 0.4, timingFunction: .spring)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2049` | PeerInfoHeadView.layoutActionItems | `change` |  |  |  | `actionsView.change(size: NSMakeSize(actionItemWidth * CGFloat(items.count) + CGFloat(items.count - 1) * actionItemInset, maxActionSize.heigh` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2063` | PeerInfoHeadView.layoutActionItems | `change` |  |  |  | `view.change(pos: NSMakePoint(x, 0), animated: false)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2082` | PeerInfoHeadView.set | `change` |  |  |  | `spawnGiftsView.change(opacity: item.editing ? 0 : 1, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2213` | PeerInfoHeadView.set | `change` | 0.2 | .easeOut |  | `current.change(size: current.smallSize, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2265` | PeerInfoHeadView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2299` | PeerInfoHeadView.set | `change` |  |  |  | `nameView.change(size: item.nameSize, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2303` | PeerInfoHeadView.set | `change` |  |  |  | `nameView.change(opacity: item.editing ? 0 : 1, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2304` | PeerInfoHeadView.set | `change` |  |  |  | `statusContainer.change(opacity: item.editing ? 0 : 1, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2306` | PeerInfoHeadView.set | `change` |  |  |  | `backgroundView.change(opacity: item.editing \|\| !item.colorfulProfile \|\| uniqueBackground != nil ? 0 : 1, animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2336` | PeerInfoHeadView.set | `animateAlpha` | 0.2 |  |  | `photoEditableView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2347` | PeerInfoHeadView.set | `animateAlpha` | 0.2 |  |  | `photoEditableView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak photoEditableView] _ in` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2363` | PeerInfoHeadView.set | `_change` |  |  |  | `self.photoVideoView?._change(size: NSMakeSize(item.photoDimension - 6, item.photoDimension - 6), animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2364` | PeerInfoHeadView.set | `_change` |  |  |  | `self.photoVideoView?._change(pos: NSMakePoint(3, 3), animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2367` | PeerInfoHeadView.set | `_change` |  |  |  | `self.photoVideoView?._change(size: NSMakeSize(item.photoDimension, item.photoDimension), animated: animated)` |
| `packages/PeerInfoUI/Sources/PeerInfoUI/PeerInfoHeadItem.swift:2368` | PeerInfoHeadView.set | `_change` |  |  |  | `self.photoVideoView?._change(pos: NSMakePoint(0, 0), animated: animated)` |

## PeerMediaUI (5)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaRowContent.swift:275` | PeerMediaRowView.updateSelectingMode | `animatePosition` |  |  |  | `self.borderView.animatePosition(from: present, to: borderOrigin)` |
| `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaRowContent.swift:281` | PeerMediaRowView.updateSelectingMode | `change` |  |  |  | `contentView.change(pos: to, animated: animated)` |
| `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaRowContent.swift:288` | PeerMediaRowView.updateSelectingMode | `change` |  |  |  | `selectingControl?.change(pos: NSMakePoint(item.viewType.innerInset.left, selectingControl!.frame.minY), animated: animated)` |
| `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaRowContent.swift:294` | PeerMediaRowView.updateSelectingMode | `change` |  |  |  | `selectingControl.change(pos: point, animated: animated, completion: { [weak selectingControl] _ in` |
| `packages/PeerMediaUI/Sources/PeerMediaUI/PeerMediaFileRowContent.swift:375` | PeerMediaFileRowView.set | `animateAlpha` | 0.2 |  |  | `downloadProgressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak downloadProgressView]` |

## PremiumStatusUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PremiumStatusUI/Sources/PremiumStatusUI/PremiumStatusControl.swift:333` | StatusConfiguration.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PremiumStatusUI/Sources/PremiumStatusUI/PremiumStatusControl.swift:334` | StatusConfiguration.set | `animateScale` | 0.2 |  |  | `current.animateScale(from: 0.1, to: 1, duration: 0.2)` |

## PremiumUI (20)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PremiumUI/Sources/PremiumUI/PremiumGiftRowItem.swift:140` | OptionView.update | `change` |  |  |  | `self.selected.change(opacity: selected ? 1.0 : 0.0, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumLimitController.swift:577` | AcceptView.playAppearanceAnimation | `animateScaleSpring` | 1.0 |  |  | `self.top.layer!.animateScaleSpring(from: 0.1, to: 1.0, duration: 1.0)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumLimitController.swift:584` | AcceptView.playAppearanceAnimation | `CABasicAnimation` |  |  | position.x | `let positionAnimation = CABasicAnimation(keyPath: "position.x")` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumLimitController.swift:589` | AcceptView.playAppearanceAnimation | `.duration =` | 0.2 |  |  | `positionAnimation.duration = 0.2` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumGiftController.swift:283` | HeaderView.update | `change` |  |  |  | `container.change(opacity: isHidden ? 0 : 1, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumGiftController.swift:345` | HeaderView.updateScroll | `change` |  |  |  | `bottomBorder.change(opacity: 0, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumGiftController.swift:348` | HeaderView.updateScroll | `animateBackground` |  |  |  | `bottomView.layer?.animateBackground()` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumGiftController.swift:351` | HeaderView.updateScroll | `change` |  |  |  | `bottomBorder.change(opacity: 1, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumGiftController.swift:354` | HeaderView.updateScroll | `animateBackground` |  |  |  | `bottomView.layer?.animateBackground()` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:946` | HeaderView.update | `change` |  |  |  | `container.change(opacity: isHidden ? 0 : 1, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1014` | HeaderView.updateScroll | `change` |  |  |  | `bottomBorder.change(opacity: 0, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1017` | HeaderView.updateScroll | `animateBackground` |  |  |  | `bottomView?.layer?.animateBackground()` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1020` | HeaderView.updateScroll | `change` |  |  |  | `bottomBorder.change(opacity: 1, animated: animated)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1023` | HeaderView.updateScroll | `animateBackground` |  |  |  | `bottomView?.layer?.animateBackground()` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1097` | HeaderView.update | `animateAlpha` | 0.2 |  |  | `bottomView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1161` | HeaderView.append | `animatePosition` | duration | .spring |  | `controller.view.layer?.animatePosition(from: NSMakePoint(frame.width, 0), to: .zero, duration: duration, timingFunction: .spring)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1162` | HeaderView.append | `animatePosition` | duration | .spring |  | `self.containerView.layer?.animatePosition(from: .zero, to: NSMakePoint(-30, 0), duration: duration, timingFunction: .spring)` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1177` | HeaderView.applyFade | `animateAlpha` | duration - |  |  | `fadeView.layer?.animateAlpha(from: from, to: to, duration: duration - 0.05, removeOnCompletion: false, completion: { [weak fadeView] _ in` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1184` | HeaderView.stackBack | `animatePosition` | duration | .spring |  | `controller.view.layer?.animatePosition(from: .zero, to: NSMakePoint(frame.width, 0), duration: duration, timingFunction: .spring, removeOnCo` |
| `packages/PremiumUI/Sources/PremiumUI/PremiumBoardingController.swift:1189` | HeaderView.stackBack | `animatePosition` | duration | .spring |  | `self.containerView.layer?.animatePosition(from: NSMakePoint(-30, 0), to: .zero, duration: duration, timingFunction: .spring)` |

## PrivateCallScreen (24)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/PrivateCallScreen/Sources/PeerCallStatusView.swift:192` | PeerCallStatusView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallStatusView.swift:193` | PeerCallStatusView.updateState | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.01, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallStatusView.swift:214` | PeerCallStatusView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallStatusView.swift:215` | PeerCallStatusView.updateState | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.01, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallTooltipStatusView.swift:128` | TooltipType.reveal | `animate` | 0.5 | .spring | path | `self.maskLayer.animate(from: maskLayer.path!, to: path, keyPath: "path", timingFunction: .spring, duration: 0.5, removeOnCompletion: false, ` |
| `packages/PrivateCallScreen/Sources/PeerCallTooltipStatusView.swift:132` | TooltipType.reveal | `animatePosition` | 0.5 | .spring |  | `self.layer?.animatePosition(from: NSMakePoint(self.frame.minX + (self.frame.width / 2) - self.imageOffset / 2, self.frame.minY), to: self.fr` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:611` | PeerCallScreenView.updateState | `animateAlpha` | transition.duration | transition.timingFunction |  | `largeVideo.layer?.animateAlpha(from: 0, to: 1, duration: transition.duration, timingFunction: transition.timingFunction)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:637` | PeerCallScreenView.updateState | `animateAlpha` | transition.duration | transition.timingFunction |  | `smallVideo.layer?.animateAlpha(from: 0, to: 1, duration: transition.duration, timingFunction: transition.timingFunction)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:722` | PeerCallScreenView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:723` | PeerCallScreenView.updateState | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.01, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:754` | PeerCallScreenView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:755` | PeerCallScreenView.updateState | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.01, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:840` | PeerCallScreenView.updateState | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: indicesAndItem.1.enabled ? 1.0 : 0.7, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:841` | PeerCallScreenView.updateState | `animateScaleSpring` | 0.2 |  |  | `view.layer?.animateScaleSpring(from: 0.01, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:891` | PeerCallScreenView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:892` | PeerCallScreenView.updateState | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.8, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:954` | PeerCallScreenView.updateState | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreenView.swift:955` | PeerCallScreenView.updateState | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.01, to: 1, duration: 0.2, bounce: false)` |
| `packages/PrivateCallScreen/Sources/PeerCallScreen.swift:452` | TooltipTuple.show | `NSAnimationContext.runAnimationGroup` |  |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/PrivateCallScreen/Sources/PeerCallAction.swift:11` | .addHeartbeatAnimation | `makeSpringAnimation` |  |  | transform.scale | `let animation = makeSpringAnimation("transform.scale")` |
| `packages/PrivateCallScreen/Sources/PeerCallAction.swift:16` | .addHeartbeatAnimation | `.duration =` | 1.3 |  |  | `animation.duration = 1.3` |
| `packages/PrivateCallScreen/Sources/PeerCallAction.swift:222` | PeerCallActionView.updateLoading | `animateAlpha` | 0.4 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.4)` |
| `packages/PrivateCallScreen/Sources/PeerCallAction.swift:249` | PeerCallActionView.updateEnabled | `change` |  |  |  | `change(opacity: enabled ? 1 : 0.7, animated: animated)` |
| `packages/PrivateCallScreen/Sources/PeerCallAction.swift:349` | PeerCallActionView.update | `animateContents` |  |  |  | `backgroundLayer.animateContents()` |

## QrStudioUI (60)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:386` | Texts.setPressed | `CASpringAnimation` |  |  | transform | `let animation = CASpringAnimation(keyPath: "transform")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:389` | Texts.setPressed | `.stiffness =` | 0.5 |  |  | `animation.stiffness = 438.0` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:390` | Texts.setPressed | `.damping =` | 0.5 |  |  | `animation.damping = 23.0` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:391` | Texts.setPressed | `.duration =` | 0.5 |  |  | `animation.duration = 0.5` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:401` | Texts.animatePourBump | `CAKeyframeAnimation` |  |  | transform | `let animation = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:406` | Texts.animatePourBump | `.duration =` | 0.74 |  |  | `animation.duration = 0.74` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:471` | Texts.setTaken | `animate` |  | .easeInEaseOut | opacity | `layer.animate(from: NSNumber(value: from), to: NSNumber(value: alpha), keyPath: "opacity", timingFunction: .easeInEaseOut, duration: isTaken` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:478` | Texts.update | `CATransition` | 0.45 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:496` | Texts.update | `CATransition` | 0.2 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodePillView.swift:503` | Texts.update | `CATransition` | 0.35 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioToastView.swift:229` | IconMode.showProgress | `CABasicAnimation` | 2.0 |  | transform.rotation.z | `let rotation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioToastView.swift:246` | IconMode.updateProgress | `animate` | 0.2 | .easeOut | strokeEnd | `self.progressLayer.animate(from: NSNumber(value: Double(from)), to: NSNumber(value: Double(target)), keyPath: "strokeEnd", timingFunction: .` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioToastView.swift:257` | IconMode.completeProgress | `animateAlpha` | 0.2 |  |  | `self.iconView.layer?.animateAlpha(from: 0.0, to: 1.0, duration: 0.2)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioToastView.swift:260` | IconMode.completeProgress | `CATransition` | 0.2 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioGlassButtonView.swift:53` | QrStudioGlass.crossfade | `CATransition` | 0.45 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioGlassButtonView.swift:125` | QrStudioGlassButtonView.update | `animateAlpha` | 0.45 |  |  | `layer.animateAlpha(from: 0.0, to: 1.0, duration: 0.45, completion: { [weak self] _ in` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:169` | QrStudioAshLayer.particleHash | `CAKeyframeAnimation` | life |  | position | `let position = CAKeyframeAnimation(keyPath: "position")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:172` | QrStudioAshLayer.particleHash | `CAKeyframeAnimation` | life |  | opacity | `let opacity = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:175` | QrStudioAshLayer.particleHash | `CAKeyframeAnimation` | life |  | transform.scale | `let scale = CAKeyframeAnimation(keyPath: "transform.scale")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:181` | QrStudioAshLayer.particleHash | `.duration =` | life |  |  | `group.duration = life` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:279` | QrStudioPlaneLayer.apply | `CAKeyframeAnimation` | sticker.period |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:281` | QrStudioPlaneLayer.apply | `.duration =` | sticker.period |  |  | `animation.duration = sticker.period` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:554` | QrStudioCodeView.animateLogoDip | `CABasicAnimation` |  |  | transform.scale | `let dip = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:560` | QrStudioCodeView.animateLogoDip | `CASpringAnimation` |  |  | transform.scale | `let spring = CASpringAnimation(keyPath: "transform.scale")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:563` | QrStudioCodeView.animateLogoDip | `.mass =` |  |  |  | `spring.mass = 1.0` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:564` | QrStudioCodeView.animateLogoDip | `.stiffness =` |  |  |  | `spring.stiffness = 195.0` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:565` | QrStudioCodeView.animateLogoDip | `.damping =` | 0.6 |  |  | `spring.damping = 15.36` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:567` | QrStudioCodeView.animateLogoDip | `.duration =` | 0.6 |  |  | `spring.duration = 0.6` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:571` | QrStudioCodeView.animateLogoDip | `.duration =` | 0.74 |  |  | `group.duration = 0.74` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:604` | QrStudioCodeView.update | `CAKeyframeAnimation` | 0.5 |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCodeView.swift:606` | QrStudioCodeView.update | `.duration =` | 0.5 |  |  | `animation.duration = 0.5` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioStickerFrames.swift:9` | .qrStudioCrossfadeContents | `CATransition` | 0.25 |  |  | `let transition = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioStickerFrames.swift:11` | .qrStudioCrossfadeContents | `.duration =` | 0.25 |  |  | `transition.duration = 0.25` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioStickerFrames.swift:164` | QrStudioPhasedAnimation.apply | `CAKeyframeAnimation` | frames.period |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioStickerFrames.swift:166` | QrStudioPhasedAnimation.apply | `.duration =` | frames.period |  |  | `animation.duration = frames.period` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioEmojiTabView.swift:217` | Slot.activate | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioEmojiTabView.swift:220` | Slot.activate | `.duration =` | 0.4 |  |  | `animation.duration = 0.4` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioAppearanceReveal.swift:10` | QrStudioAppearanceReveal.animation | `CAKeyframeAnimation` | QrStudioReveal.duration |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioAppearanceReveal.swift:12` | QrStudioAppearanceReveal.animation | `.duration =` | QrStudioReveal.duration |  |  | `animation.duration = QrStudioReveal.duration` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioSheetView.swift:283` | Layout.addAppearanceFade | `CATransition` | 0.4 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioSheetView.swift:315` | Layout.applyAppearance | `CATransition` | 0.35 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioSheetView.swift:423` | Layout.open | `ContainedViewLayoutTransition.animated` | 0.2 | .easeInOut |  | `let transition = ContainedViewLayoutTransition.animated(duration: 0.2, curve: .easeInOut)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:212` | State.animateBounce | `CABasicAnimation` |  |  | transform | `let dip = CABasicAnimation(keyPath: "transform")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:218` | State.animateBounce | `CASpringAnimation` |  |  | transform | `let spring = CASpringAnimation(keyPath: "transform")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:221` | State.animateBounce | `.mass =` |  |  |  | `spring.mass = 1.0` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:222` | State.animateBounce | `.stiffness =` |  |  |  | `spring.stiffness = 130.5` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:223` | State.animateBounce | `.damping =` | 0.7 |  |  | `spring.damping = 11.42` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:225` | State.animateBounce | `.duration =` | 0.7 |  |  | `spring.duration = 0.7` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:229` | State.animateBounce | `.duration =` | 0.82 |  |  | `group.duration = 0.82` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:263` | State.update | `CABasicAnimation` |  |  | shadowOpacity | `let animation = CABasicAnimation(keyPath: "shadowOpacity")` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:266` | State.update | `.duration =` | 0.45 |  |  | `animation.duration = 0.45` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioCardView.swift:402` | State.applyInk | `CATransition` | 0.5 |  |  | `let fade = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioGiftsTabView.swift:123` | QrStudioGiftTileView.update | `animate` | 0.2 | .easeInEaseOut | path | `self.trimMask.animate(from: previousTrimPath, to: trimPath, keyPath: "path", timingFunction: .easeInEaseOut, duration: 0.2)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioGiftsTabView.swift:126` | QrStudioGiftTileView.update | `animate` | 0.2 | .easeInEaseOut | path | `self.ring.animate(from: previousRingPath, to: ringPath, keyPath: "path", timingFunction: .easeInEaseOut, duration: 0.2)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioGiftsTabView.swift:128` | QrStudioGiftTileView.update | `animate` | 0.2 | .easeInEaseOut | lineWidth | `self.ring.animate(from: NSNumber(value: Double(previousRingLineWidth)), to: NSNumber(value: Double(ringLineWidth)), keyPath: "lineWidth", ti` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioColorsTabView.swift:115` | QrStudioPressRing.update | `animate` | QrStudioPressRing.duration | .easeInEaseOut | path | `self.layer.animate(from: previousPath, to: path, keyPath: "path", timingFunction: .easeInEaseOut, duration: QrStudioPressRing.duration)` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioColorsTabView.swift:117` | QrStudioPressRing.update | `animate` | QrStudioPressRing.duration | .easeInEaseOut | lineWidth | `self.layer.animate(from: NSNumber(value: Double(previousLineWidth)), to: NSNumber(value: Double(lineWidth)), keyPath: "lineWidth", timingFun` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioColorsTabView.swift:118` | QrStudioPressRing.update | `animate` | QrStudioPressRing.duration | .easeInEaseOut | transform.scale | `target?.animate(from: NSNumber(value: Double(previousScale)), to: NSNumber(value: Double(scale)), keyPath: "transform.scale", timingFunction` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioThemeBackgroundView.swift:78` | QrStudioThemeBackgroundView.setMode | `CATransition` | 0.25 |  |  | `let transition = CATransition()` |
| `packages/QrStudioUI/Sources/QrStudioUI/QrStudioThemeBackgroundView.swift:80` | QrStudioThemeBackgroundView.setMode | `.duration =` | 0.25 |  |  | `transition.duration = 0.25` |

## QuickSwitcher (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/QuickSwitcher/Sources/QuickSwitcher/QuickSwitcherModalController.swift:242` | QuickSwitcherView.appearForumTopics | `animatePosition` | 0.35 | .spring |  | `tableView.layer?.animatePosition(from: NSMakePoint(oneOfThird * 2, tableView.frame.minY), to: tableView.frame.origin, duration: 0.35, timing` |
| `packages/QuickSwitcher/Sources/QuickSwitcher/QuickSwitcherModalController.swift:243` | QuickSwitcherView.appearForumTopics | `animatePosition` | 0.35 | .spring |  | `self.tableView.layer?.animatePosition(from: tableView.frame.origin, to: NSMakePoint(-oneOfThird, tableView.frame.minY), duration: 0.35, timi` |
| `packages/QuickSwitcher/Sources/QuickSwitcher/QuickSwitcherModalController.swift:255` | QuickSwitcherView.cancelForum | `animatePosition` | 0.35 | .spring |  | `view.layer?.animatePosition(from: tableView.frame.origin, to: NSMakePoint(frame.width, view.frame.minY), duration: 0.35, timingFunction: .sp` |
| `packages/QuickSwitcher/Sources/QuickSwitcher/QuickSwitcherModalController.swift:258` | QuickSwitcherView.cancelForum | `animatePosition` | 0.35 | .spring |  | `self.tableView.layer?.animatePosition(from: NSMakePoint(-oneOfThird, tableView.frame.minY), to: tableView.frame.origin, duration: 0.35, timi` |

## RichTextEditorUI (1)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/RichTextEditorUI/Sources/RichTextEditorUI/Canvas/SpoilerEffectView.swift:37` | DefaultSpoilerEffectView.dissolve | `NSAnimationContext.runAnimationGroup` |  |  |  | `NSAnimationContext.runAnimationGroup({ ctx in ctx.duration = 0.3; animator().alphaValue = 0 },` |

## SceneEffects (90)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/SceneEffects/Sources/EmojiAnimationEffectView.swift:56` | Source.animateContentScale | `animateScaleSpring` | duration |  |  | `player.layer?.animateScaleSpring(from: from, to: to, duration: duration, removeOnCompletion: false, bounce: false, completion: completion)` |
| `packages/SceneEffects/Sources/EmojiAnimationEffectView.swift:58` | Source.animateContentScale | `animateScaleCenter` | duration |  |  | `player.layer?.animateScaleCenter(from: from, to: to, duration: duration, removeOnCompletion: false, completion: completion)` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:40` | FasterStarsView.setVisible | `_change` |  |  |  | `self._change(opacity: visible ? 0.4 : 0.0, animated: true, completion: { [weak self] finished in` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:54` | FasterStarsView.startAnimation | `CABasicAnimation` |  |  | speedFactor | `let speedAnimation = CABasicAnimation(keyPath: "speedFactor")` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:57` | FasterStarsView.startAnimation | `.duration =` | 0.8 |  |  | `speedAnimation.duration = 0.8` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:63` | FasterStarsView.startAnimation | `CABasicAnimation` |  |  | stretchFactor | `let stretchAnimation = CABasicAnimation(keyPath: "stretchFactor")` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:66` | FasterStarsView.startAnimation | `.duration =` | 0.8 |  |  | `stretchAnimation.duration = 0.8` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:79` | FasterStarsView.resetAnimation | `CABasicAnimation` |  |  | speedFactor | `let speedAnimation = CABasicAnimation(keyPath: "speedFactor")` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:82` | FasterStarsView.resetAnimation | `.duration =` | 0.35 |  |  | `speedAnimation.duration = 0.35` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:88` | FasterStarsView.resetAnimation | `CABasicAnimation` |  |  | stretchFactor | `let stretchAnimation = CABasicAnimation(keyPath: "stretchFactor")` |
| `packages/SceneEffects/Sources/FasterStarsView.swift:91` | FasterStarsView.resetAnimation | `.duration =` | 0.35 |  |  | `stretchAnimation.duration = 0.35` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:81` | PremiumGiftStarSceneView.handleTap | `CASpringAnimation` |  |  | rotation | `let animation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:84` | PremiumGiftStarSceneView.handleTap | `.duration =` | 0.25 |  |  | `animation.duration = 0.25` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:93` | PremiumGiftStarSceneView.handleTap | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:96` | PremiumGiftStarSceneView.handleTap | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:97` | PremiumGiftStarSceneView.handleTap | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:98` | PremiumGiftStarSceneView.handleTap | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:99` | PremiumGiftStarSceneView.handleTap | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.8` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:195` | PremiumGiftStarSceneView.setupGradientAnimation | `CABasicAnimation` | 4.5 |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:196` | PremiumGiftStarSceneView.setupGradientAnimation | `.duration =` | 4.5 |  |  | `animation.duration = 4.5` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:214` | PremiumGiftStarSceneView.setupShineAnimation | `CABasicAnimation` |  |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:220` | PremiumGiftStarSceneView.setupShineAnimation | `.duration =` | 0.9 |  |  | `animation.duration = 0.9` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:225` | PremiumGiftStarSceneView.setupShineAnimation | `.duration =` | 3.0 |  |  | `group.duration = 3.0` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:265` | PremiumGiftStarSceneView.playAppearanceAnimation | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:268` | PremiumGiftStarSceneView.playAppearanceAnimation | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:269` | PremiumGiftStarSceneView.playAppearanceAnimation | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:270` | PremiumGiftStarSceneView.playAppearanceAnimation | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/PremiumGiftStarSceneView.swift:271` | PremiumGiftStarSceneView.playAppearanceAnimation | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.75` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:86` | Mode.handleTap | `CASpringAnimation` |  |  | rotation | `let animation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:89` | Mode.handleTap | `.duration =` | 0.25 |  |  | `animation.duration = 0.25` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:98` | Mode.handleTap | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:101` | Mode.handleTap | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:102` | Mode.handleTap | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:103` | Mode.handleTap | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:104` | Mode.handleTap | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.8` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:208` | Mode.setupGradientAnimation | `CABasicAnimation` | 4.5 |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:209` | Mode.setupGradientAnimation | `.duration =` | 4.5 |  |  | `animation.duration = 4.5` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:237` | Mode.setupShineAnimation | `CABasicAnimation` |  |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:243` | Mode.setupShineAnimation | `.duration =` | 0.9 |  |  | `animation.duration = 0.9` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:248` | Mode.setupShineAnimation | `.duration =` | 4.0 |  |  | `group.duration = 4.0` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:324` | Mode.playAppearanceAnimation | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:327` | Mode.playAppearanceAnimation | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:328` | Mode.playAppearanceAnimation | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:329` | Mode.playAppearanceAnimation | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/PremiumCoinSceneView.swift:330` | Mode.playAppearanceAnimation | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.75` |
| `packages/SceneEffects/Sources/SwirlStarsView.swift:49` | SwirlStarsView.setVisible | `_change` |  |  |  | `self._change(opacity: visible ? 0.6 : 0.0, animated: true, completion: { [weak self] finished in` |
| `packages/SceneEffects/Sources/SwirlStarsView.swift:68` | SwirlStarsView.setupAnimations | `CABasicAnimation` |  |  | eulerAngles | `let animation = CABasicAnimation(keyPath: "eulerAngles")` |
| `packages/SceneEffects/Sources/SwirlStarsView.swift:71` | SwirlStarsView.setupAnimations | `.duration =` | 1.5 |  |  | `animation.duration = 1.5` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:86` | PremiumStarSceneView.handleTap | `CASpringAnimation` |  |  | rotation | `let animation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:89` | PremiumStarSceneView.handleTap | `.duration =` | 0.25 |  |  | `animation.duration = 0.25` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:98` | PremiumStarSceneView.handleTap | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:101` | PremiumStarSceneView.handleTap | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:102` | PremiumStarSceneView.handleTap | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:103` | PremiumStarSceneView.handleTap | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:104` | PremiumStarSceneView.handleTap | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.8` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:210` | PremiumStarSceneView.setupGradientAnimation | `CABasicAnimation` | 4.5 |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:211` | PremiumStarSceneView.setupGradientAnimation | `.duration =` | 4.5 |  |  | `animation.duration = 4.5` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:229` | PremiumStarSceneView.setupShineAnimation | `CABasicAnimation` |  |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:235` | PremiumStarSceneView.setupShineAnimation | `.duration =` | 0.9 |  |  | `animation.duration = 0.9` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:240` | PremiumStarSceneView.setupShineAnimation | `.duration =` | 3.0 |  |  | `group.duration = 3.0` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:298` | PremiumStarSceneView.playAppearanceAnimation | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:301` | PremiumStarSceneView.playAppearanceAnimation | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:302` | PremiumStarSceneView.playAppearanceAnimation | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:303` | PremiumStarSceneView.playAppearanceAnimation | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/PremiumStarSceneView.swift:304` | PremiumStarSceneView.playAppearanceAnimation | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.75` |
| `packages/SceneEffects/Sources/BadgeStarsView.swift:39` | BadgeStarsView.setVisible | `_change` |  |  |  | `self._change(opacity: visible ? 0.6 : 0.0, animated: true, completion: { [weak self] finished in` |
| `packages/SceneEffects/Sources/HelloView.swift:136` | HelloView.spawnPhrase | `animateScale` | duration |  |  | `view.animateScale(from: CGFloat.random(in: 0.4 ..< 0.6), to: CGFloat.random(in: 0.9 ..< 1.2), duration: duration, removeOnCompletion: false)` |
| `packages/SceneEffects/Sources/DataRainView.swift:118` | DataRainView.setVisible | `_change` |  |  |  | `self._change(opacity: visible ? 0.6 : 0.0, animated: true, completion: { [weak self] finished in` |
| `packages/SceneEffects/Sources/Confetti.swift:422` | Style.playPattern | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/SceneEffects/Sources/Confetti.swift:425` | Style.playPattern | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/SceneEffects/Sources/Confetti.swift:470` | Style.playStrikeAnimation | `animateScale` | 0.1 |  |  | `particle.animateScale(from: 0.1, to: 1, duration: 0.1)` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:91` | GoldenStarSceneView.handleTap | `CASpringAnimation` |  |  | rotation | `let animation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:94` | GoldenStarSceneView.handleTap | `.duration =` | 0.25 |  |  | `animation.duration = 0.25` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:103` | GoldenStarSceneView.handleTap | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:106` | GoldenStarSceneView.handleTap | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:107` | GoldenStarSceneView.handleTap | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:108` | GoldenStarSceneView.handleTap | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:109` | GoldenStarSceneView.handleTap | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.8` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:214` | GoldenStarSceneView.setup | `CAKeyframeAnimation` |  |  |  | `let animation = CAKeyframeAnimation()` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:238` | GoldenStarSceneView.setup | `CAKeyframeAnimation` |  |  |  | `let animation = CAKeyframeAnimation()` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:290` | GoldenStarSceneView.setupGradientAnimation | `CABasicAnimation` | 4.5 |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:291` | GoldenStarSceneView.setupGradientAnimation | `.duration =` | 4.5 |  |  | `animation.duration = 4.5` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:309` | GoldenStarSceneView.setupShineAnimation | `CABasicAnimation` |  |  | contentsTransform | `let animation = CABasicAnimation(keyPath: "contentsTransform")` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:315` | GoldenStarSceneView.setupShineAnimation | `.duration =` | 0.9 |  |  | `animation.duration = 0.9` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:320` | GoldenStarSceneView.setupShineAnimation | `.duration =` | 3.0 |  |  | `group.duration = 3.0` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:378` | GoldenStarSceneView.playAppearanceAnimation | `CASpringAnimation` |  |  | rotation | `let springAnimation = CASpringAnimation(keyPath: "rotation")` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:381` | GoldenStarSceneView.playAppearanceAnimation | `.mass =` |  |  |  | `springAnimation.mass = 1.0` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:382` | GoldenStarSceneView.playAppearanceAnimation | `.stiffness =` | springAnimation.settlingDuration * |  |  | `springAnimation.stiffness = 21.0` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:383` | GoldenStarSceneView.playAppearanceAnimation | `.damping =` | springAnimation.settlingDuration * |  |  | `springAnimation.damping = 5.8` |
| `packages/SceneEffects/Sources/Star_GoldenStar.swift:384` | GoldenStarSceneView.playAppearanceAnimation | `.duration =` | springAnimation.settlingDuration * |  |  | `springAnimation.duration = springAnimation.settlingDuration * 0.75` |

## SelectColorUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/SelectColorUI/Sources/SelectColorUI/SelectColorController.swift:426` | ProfilePreviewRowView.set | `animateBackground` |  |  |  | `backgroundView.layer?.animateBackground()` |
| `packages/SelectColorUI/Sources/SelectColorUI/SelectColorController.swift:2763` | SelectColorControllerCollectData.backgroundIcon | `animateAlpha` | 0.2 |  |  | `panel.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## SelectPeersUI (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/SelectPeersUI/Sources/SelectPeersUI/SelectPeersController.swift:1478` | SelectPeersControllerView.tokenizedViewDidChangedHeight | `_change` |  |  |  | `tokenView._change(pos: NSMakePoint(tokenView.frame.minX, 10), animated: animated)` |
| `packages/SelectPeersUI/Sources/SelectPeersUI/SelectPeersController.swift:1479` | SelectPeersControllerView.tokenizedViewDidChangedHeight | `change` |  |  |  | `tableView.change(size: NSMakeSize(containerView.frame.width, max(0, containerView.frame.height - height - 20)), animated: animated)` |
| `packages/SelectPeersUI/Sources/SelectPeersUI/SelectPeersController.swift:1480` | SelectPeersControllerView.tokenizedViewDidChangedHeight | `change` |  |  |  | `tableView.change(pos: NSMakePoint(0, height + 20), animated: animated)` |
| `packages/SelectPeersUI/Sources/SelectPeersUI/SelectPeersController.swift:1481` | SelectPeersControllerView.tokenizedViewDidChangedHeight | `change` |  |  |  | `separatorView.change(pos: NSMakePoint(0, tokenView.frame.maxY + 10), animated: animated)` |

## SettingsUI (24)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/SettingsUI/Sources/SettingsUI/DockIconRowItem.swift:264` | Indicator.updateSelection | `animateAlpha` | 0.18 |  |  | `selected.animateAlpha(from: CGFloat(previousOpacity), to: CGFloat(opacity), duration: 0.18)` |
| `packages/SettingsUI/Sources/SettingsUI/DockIconRowItem.swift:265` | Indicator.updateSelection | `animateAlpha` | 0.18 | .easeOut |  | `selectionOutline.animateAlpha(from: CGFloat(previousOpacity), to: CGFloat(opacity), duration: 0.18)` |
| `packages/SettingsUI/Sources/SettingsUI/DockIconRowItem.swift:267` | Indicator.updateSelection | `animateScale` | 0.2 | .easeOut |  | `selectionOutline.animateScale(from: 0.94, to: 1, duration: 0.2, timingFunction: .easeOut)` |
| `packages/SettingsUI/Sources/SettingsUI/DockIconRowItem.swift:326` | Indicator.updateItem | `animateContents` |  |  |  | `self.content.animateContents()` |
| `packages/SettingsUI/Sources/SettingsUI/DockIconRowItem.swift:332` | Indicator.updateItem | `animateContents` |  |  |  | `self.content.animateContents()` |
| `packages/SettingsUI/Sources/SettingsUI/EditAccountInfoItem.swift:182` | EditAccountInfoItemView.set | `change` |  |  |  | `progressView.change(opacity: 1, animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/EditAccountInfoItem.swift:193` | EditAccountInfoItemView.set | `animateAlpha` | 0.2 |  |  | `self.tempImageView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/SettingsUI/Sources/SettingsUI/EditAccountInfoItem.swift:200` | EditAccountInfoItemView.set | `change` |  |  |  | `progressView.change(opacity: 0, animated: animated, removeOnCompletion: false, completion: { [weak self] complete in` |
| `packages/SettingsUI/Sources/SettingsUI/EditAccountInfoItem.swift:214` | EditAccountInfoItemView.set | `animateAlpha` | 0.2 |  |  | `tempImageView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak tempImageView] _ in` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:302` | AccountInfoView.playAnimation | `animateScaleSpring` | 0.3 |  |  | `control.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3, bounce: true)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:451` | AccountInfoView.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:452` | AccountInfoView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:454` | AccountInfoView.set | `_change` |  |  |  | `self.avatarView._change(size: NSMakeSize(54, 54), animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:455` | AccountInfoView.set | `_change` |  |  |  | `self.photoVideoView?._change(size: NSMakeSize(54, 54), animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:462` | AccountInfoView.set | `_change` |  |  |  | `self.avatarView._change(pos: NSMakePoint(3, 3), animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:463` | AccountInfoView.set | `_change` |  |  |  | `self.photoVideoView?._change(pos: NSMakePoint(3, 3), animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:470` | AccountInfoView.set | `_change` |  |  |  | `self.avatarView._change(size: NSMakeSize(60, 60), animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:471` | AccountInfoView.set | `_change` |  |  |  | `self.photoVideoView?._change(size: NSMakeSize(60, 60), animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:473` | AccountInfoView.set | `_change` |  |  |  | `self.avatarView._change(pos: .zero, animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountInfoItem.swift:474` | AccountInfoView.set | `_change` |  |  |  | `self.photoVideoView?._change(pos: .zero, animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountViewController.swift:858` | AccountViewController.showSearchController | `animateAlpha` | 0.25 |  |  | `searchController.view.layer?.animateAlpha(from: 0.0, to: 1.0, duration: 0.25)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountViewController.swift:866` | AccountViewController.showSearchController | `change` |  |  |  | `tableView.change(opacity: 0, animated: animated)` |
| `packages/SettingsUI/Sources/SettingsUI/AccountViewController.swift:880` | AccountViewController.hideSearchController | `_change` | 0.25 | CAMediaTimingFunctionName.spring |  | `searchController.view._change(opacity: 0, animated: animated, duration: 0.25, timingFunction: CAMediaTimingFunctionName.spring, completion: ` |
| `packages/SettingsUI/Sources/SettingsUI/AccountViewController.swift:884` | AccountViewController.hideSearchController | `change` |  |  |  | `tableView.change(opacity: 1, animated: animated)` |

## ShareUI (21)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:215` | ShareModalView.updateLocalizationAndTheme | `animateAlpha` | 0.2 |  |  | `textContainerView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:216` | ShareModalView.updateLocalizationAndTheme | `animateAlpha` | 0.2 |  |  | `actionsContainerView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:217` | ShareModalView.updateLocalizationAndTheme | `animateAlpha` | 0.2 |  |  | `bottomSeparator.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:218` | ShareModalView.updateLocalizationAndTheme | `animateAlpha` | 0.2 |  |  | `basicSearchView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:219` | ShareModalView.updateLocalizationAndTheme | `animateAlpha` | 0.2 |  |  | `tokenizedView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:220` | ShareModalView.updateLocalizationAndTheme | `animateAlpha` | 0.2 |  |  | `dismiss.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:250` | ShareModalView.applyTransition | `change` |  |  |  | `self.topSeparator.change(opacity: item != nil ? 0 : 1, animated: transition.animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:355` | ForumTopicItem.appearForumTopics | `animatePosition` | 0.35 | .spring |  | `tableView.layer?.animatePosition(from: NSMakePoint(oneOfThird * 2, tableView.frame.minY), to: tableView.frame.origin, duration: 0.35, timing` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:356` | ForumTopicItem.appearForumTopics | `animatePosition` | 0.35 | .spring |  | `sourceView.layer?.animatePosition(from: sourceView.frame.origin, to: NSMakePoint(-oneOfThird, sourceView.frame.minY), duration: 0.35, timing` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:399` | ForumTopicItem.appearCommunityChats | `animatePosition` | 0.35 | .spring |  | `tableView.layer?.animatePosition(from: NSMakePoint(oneOfThird * 2, tableView.frame.minY), to: tableView.frame.origin, duration: 0.35, timing` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:400` | ForumTopicItem.appearCommunityChats | `animatePosition` | 0.35 | .spring |  | `sourceView.layer?.animatePosition(from: sourceView.frame.origin, to: NSMakePoint(-oneOfThird, sourceView.frame.minY), duration: 0.35, timing` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:410` | ForumTopicItem.pop | `animatePosition` | 0.35 | .spring |  | `view.layer?.animatePosition(from: tableView.frame.origin, to: NSMakePoint(frame.width, view.frame.minY), duration: 0.35, timingFunction: .sp` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:413` | ForumTopicItem.pop | `animatePosition` | 0.35 | .spring |  | `sourceView.layer?.animatePosition(from: NSMakePoint(-oneOfThird, sourceView.frame.minY), to: sourceView.frame.origin, duration: 0.35, timing` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:442` | ForumTopicItem.tokenizedViewDidChangedHeight | `_change` |  |  |  | `searchView._change(pos: NSMakePoint(10 + (!dismiss.isHidden ? 40 : 0), 10), animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:445` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `tableView.change(size: tableSize, animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:446` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `tableView.change(pos: tablePosition, animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:447` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `communityChatsView?.change(size: tableSize, animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:448` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `communityChatsView?.change(pos: tablePosition, animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:449` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `forumTopicsView?.change(size: tableSize, animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:450` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `forumTopicsView?.change(pos: tablePosition, animated: animated)` |
| `packages/ShareUI/Sources/ShareUI/ShareModalController.swift:451` | ForumTopicItem.tokenizedViewDidChangedHeight | `change` |  |  |  | `topSeparator.change(pos: NSMakePoint(0, searchView.frame.maxY + 10), animated: animated)` |

## ShortPeerRow (36)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ChatActivitiesModel.swift:153` | Shape.add | `CAKeyframeAnimation` | self.loopDuration |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ChatActivitiesModel.swift:155` | Shape.add | `.duration =` | self.loopDuration |  |  | `animation.duration = self.loopDuration` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:308` | ShortPeerRowView.changeSeparator | `animateBounds` | 0.2 | .easeOut |  | `separator.animateBounds(from: from, to: rect.size.bounds, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:320` | ShortPeerRowView.changeSeparator | `animatePosition` | 0.2 | .easeOut |  | `separator.animatePosition(from: from, to: rect.origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:612` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `contextLabel.change(pos: rect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:616` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `bg.change(pos: bgFrame.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:617` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `bg.change(size: bgFrame.size, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:624` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `switchView.change(pos: rect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:629` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `choiceControl.change(pos: rect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:636` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `self.container.change(size: containerRect.size, animated: false)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:637` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `self.container.change(pos: containerRect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:668` | ShortPeerRowView.updateInteractionType | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:669` | ShortPeerRowView.updateInteractionType | `animateScaleSpring` | 0.3 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:705` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `deleteControl?.change(opacity: 1, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:706` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `deleteControl?.change(pos: NSMakePoint(item.deleteInset, deleteControl!.frame.minY), animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:1133` | ShortPeerRowView.set | `_change` |  |  |  | `self.image._change(opacity: item.enabled ? 1 : 0.8, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:1269` | ShortPeerRowView.updatePresentation | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShortPeerRow/Sources/ShortPeerRowShare/ShortPeerRowView.swift:1270` | ShortPeerRowView.updatePresentation | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ChatActivitiesModel.swift:153` | Shape.add | `CAKeyframeAnimation` | self.loopDuration |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ChatActivitiesModel.swift:155` | Shape.add | `.duration =` | self.loopDuration |  |  | `animation.duration = self.loopDuration` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:308` | ShortPeerRowView.changeSeparator | `animateBounds` | 0.2 | .easeOut |  | `separator.animateBounds(from: from, to: rect.size.bounds, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:320` | ShortPeerRowView.changeSeparator | `animatePosition` | 0.2 | .easeOut |  | `separator.animatePosition(from: from, to: rect.origin, duration: 0.2, timingFunction: .easeOut)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:612` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `contextLabel.change(pos: rect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:616` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `bg.change(pos: bgFrame.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:617` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `bg.change(size: bgFrame.size, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:624` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `switchView.change(pos: rect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:629` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `choiceControl.change(pos: rect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:636` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `self.container.change(size: containerRect.size, animated: false)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:637` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `self.container.change(pos: containerRect.origin, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:668` | ShortPeerRowView.updateInteractionType | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:669` | ShortPeerRowView.updateInteractionType | `animateScaleSpring` | 0.3 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:705` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `deleteControl?.change(opacity: 1, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:706` | ShortPeerRowView.updateInteractionType | `change` |  |  |  | `deleteControl?.change(pos: NSMakePoint(item.deleteInset, deleteControl!.frame.minY), animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:1133` | ShortPeerRowView.set | `_change` |  |  |  | `self.image._change(opacity: item.enabled ? 1 : 0.8, animated: animated)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:1269` | ShortPeerRowView.updatePresentation | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowView.swift:1270` | ShortPeerRowView.updatePresentation | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |

## SidebarUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/SidebarUI/Sources/SidebarUI/LeftSidebarFolderItem.swift:203` | LeftSidebarFolderView.updateHighlight | `change` |  |  |  | `self.imageView.change(opacity: 1.0, animated: animated)` |
| `packages/SidebarUI/Sources/SidebarUI/LeftSidebarFolderItem.swift:204` | LeftSidebarFolderView.updateHighlight | `change` |  |  |  | `self.textView.change(opacity: 1.0, animated: animated)` |

## StarsUI (34)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/StarsUI/Sources/StarsUI/PremiumGiftingController.swift:240` | HeaderStarRowItemView.set | `change` |  |  |  | `self.avatars.change(opacity: 0, animated: animated)` |
| `packages/StarsUI/Sources/StarsUI/PremiumGiftingController.swift:243` | HeaderStarRowItemView.set | `change` |  |  |  | `self.avatars.change(opacity: 1, animated: animated)` |
| `packages/StarsUI/Sources/StarsUI/PremiumGiftingController.swift:784` | Tuple.PremiumGiftingController | `animatePosition` | 0.2 | .spring |  | `features.view.layer?.animatePosition(from: NSMakePoint(0, controller.bounds.maxY), to: NSMakePoint(0, features._frameRect.minY), duration: 0` |
| `packages/StarsUI/Sources/StarsUI/PremiumGiftingController.swift:785` | Tuple.PremiumGiftingController | `animateAlpha` | 0.2 |  |  | `features.view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/PremiumGiftingController.swift:791` | Tuple.PremiumGiftingController | `animateAlpha` | 0.2 |  |  | `background.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/GiftButtonStarsView.swift:98` | GiftButtonStarsView.seed | `animateScaleCenter` | duration |  |  | `layer.animateScaleCenter(from: 0.001, to: scale, duration: duration, removeOnCompletion: false, completion: { [weak self, weak layer] _ in` |
| `packages/StarsUI/Sources/StarsUI/GiftButtonStarsView.swift:103` | GiftButtonStarsView.seed | `animateAlpha` | Double(CGFloat.random(in: 0.3 ..< 0.35) |  |  | `layer.animateAlpha(from: 1, to: 0, duration: Double(CGFloat.random(in: 0.3 ..< 0.35)), removeOnCompletion: false, completion: { [weak self, ` |
| `packages/StarsUI/Sources/StarsUI/GiftOptionsRowItem.swift:1031` | StarPriceView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/GiftOptionsRowItem.swift:1227` | StarPriceView.set | `animateScaleSpring` | 0.35 |  |  | `view?.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.35)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_MarketplaceController.swift:483` | AttributeItemView.updateBorder | `change` |  |  |  | `separatorView.change(opacity: visible ? 1 : 0)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_MarketplaceController.swift:1035` | AttributeItemView.updateIsVisible | `change` |  |  |  | `containerView.change(opacity: 1, animated: animated)` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:20` | GiftBuilderMotion.updateText | `animateAlpha` | 0.2 |  |  | `previous.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak previous] _ in` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:23` | GiftBuilderMotion.updateText | `animateAlpha` | 0.25 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.25)` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:29` | GiftBuilderMotion.fade | `CATransition` |  |  |  | `let transition = CATransition()` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:31` | GiftBuilderMotion.fade | `.duration =` |  |  |  | `transition.duration = reduceMotion ? 0.15 : 0.25` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:98` | GiftBuilderAppearanceReveal.makeMask | `CAKeyframeAnimation` |  |  | bounds | `let animation = CAKeyframeAnimation(keyPath: "bounds")` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:104` | GiftBuilderAppearanceReveal.makeMask | `.duration =` | Self.duration |  |  | `animation.duration = Self.duration` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:149` | GiftBuilderGlassView.update | `animateAlpha` | 0.2 |  |  | `visual.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, completion: { [weak self, weak visual] _ in` |
| `packages/StarsUI/Sources/StarsUI/GiftBuilderMotion.swift:264` | GiftBuilderBackgroundView.reveal | `animateAlpha` | 0.25 |  |  | `layer.animateAlpha(from: 0, to: 1, duration: 0.25, completion: { [weak self, weak background] _ in` |
| `packages/StarsUI/Sources/StarsUI/StarGift_Nft_Controller.swift:1441` | ActionView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/Star_AuctionBidController.swift:160` | TitleRowView.updateBorder | `change` |  |  |  | `separatorView.change(opacity: visible ? 1 : 0)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:200` | OptionView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:934` | ActionView.showGift | `animateAlpha` | 0.22 |  |  | `old.layer?.animateAlpha(from: CGFloat(old.layer?.presentation()?.opacity ?? 1), to: 0, duration: 0.22, removeOnCompletion: false, completion` |
| `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:938` | ActionView.showGift | `animateAlpha` | 0.3 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.3)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:940` | ActionView.showGift | `animateScaleCenter` | 0.22 | .spring |  | `old.layer?.animateScaleCenter(from: old.layer?.presentation()?.transform.m11 ?? 1, to: 0.86, duration: 0.22, removeOnCompletion: false)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:941` | ActionView.showGift | `animateScaleSpring` | 0.6 | .spring |  | `current.layer?.animateScaleSpring(from: 0.8, to: 1, duration: 0.6)` |
| `packages/StarsUI/Sources/StarsUI/StarGift_ModelBuilderController.swift:942` | ActionView.showGift | `animatePosition` | 0.5 | .spring |  | `current.layer?.animatePosition(from: NSMakePoint(0, 12), to: .zero, duration: 0.5, timingFunction: .spring, additive: true)` |
| `packages/StarsUI/Sources/StarsUI/GiftingController.swift:151` | HeaderTextRowView.set | `animateAlpha` | 0.2 |  |  | `infoView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/GiftingController.swift:227` | HeaderRowView.set | `change` |  |  |  | `self.avatars.change(opacity: 1, animated: animated)` |
| `packages/StarsUI/Sources/StarsUI/GiftingController.swift:355` | FilterRowView.set | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/GiftingController.swift:356` | FilterRowView.set | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StarsUI/Sources/StarsUI/Star_ListScreen.swift:205` | FloatingHeaderView.updateScrolled | `change` |  |  |  | `blurView.change(opacity: scrolled ? 1 : 0, animated: animated)` |
| `packages/StarsUI/Sources/StarsUI/Star_ListScreen.swift:206` | FloatingHeaderView.updateScrolled | `change` |  |  |  | `textView.change(opacity: scrolled ? 1 : 0, animated: animated)` |
| `packages/StarsUI/Sources/StarsUI/PeerMediaGiftsController.swift:1193` | PeerMediaGiftsExternalArguments.PeerMediaGiftsController | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: NSMakePoint(0, parent.frame.height), to: current.frame.origin)` |

## StatisticsUI (15)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:317` | StatisticRowView.set | `animateAlpha` | 0.14 |  |  | `skeletonView.layer?.animateAlpha(from: 1, to: 0, duration: 0.14, removeOnCompletion: false, completion: { [weak skeletonView] _ in` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:320` | StatisticRowView.set | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:438` | StatisticLoadingRowView.set | `animateAlpha` | 0.2 |  |  | `self.errorView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:444` | StatisticLoadingRowView.set | `animateAlpha` | 0.2 |  |  | `progress.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak progress] _ in` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:459` | StatisticLoadingRowView.set | `animateAlpha` | 0.2 |  |  | `self.progressIndicator?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:463` | StatisticLoadingRowView.set | `animateAlpha` | 0.2 |  |  | `self.progressIndicator?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticRowItem.swift:466` | StatisticLoadingRowView.set | `animateAlpha` | 0.2 |  |  | `errorView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak errorView] _ in` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticsLoadingRowItem.swift:96` | StatisticsLoadingRowView.viewClass | `change` |  |  |  | `self.imageView.change(opacity: 0, animated: false)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticsLoadingRowItem.swift:97` | StatisticsLoadingRowView.viewClass | `change` |  |  |  | `self.textView.change(opacity: 0, animated: false)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticsLoadingRowItem.swift:98` | StatisticsLoadingRowView.viewClass | `change` |  |  |  | `self.progressIndicator.change(opacity: 1, animated: false)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticsLoadingRowItem.swift:103` | StatisticsLoadingRowView.viewClass | `change` |  |  |  | `self?.imageView.change(opacity: 1, animated: true)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticsLoadingRowItem.swift:104` | StatisticsLoadingRowView.viewClass | `change` |  |  |  | `self?.textView.change(opacity: 1, animated: true)` |
| `packages/StatisticsUI/Sources/StatisticsUI/StatisticsLoadingRowItem.swift:105` | StatisticsLoadingRowView.viewClass | `change` |  |  |  | `self?.progressIndicator.change(opacity: 0, animated: true)` |
| `packages/StatisticsUI/Sources/StatisticsUI/ChannelBoostStatsController.swift:480` | LineView.layoutActionItems | `change` |  |  |  | `actionsView.change(size: NSMakeSize(actionItemWidth * CGFloat(items.count) + CGFloat(items.count - 1) * actionItemInset, maxActionSize.heigh` |
| `packages/StatisticsUI/Sources/StatisticsUI/ChannelBoostStatsController.swift:488` | LineView.layoutActionItems | `change` |  |  |  | `view.change(pos: NSMakePoint(x, 0), animated: false)` |

## StickerSettingsUI (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/StickerSettingsUI/Sources/StickerSettingsUI/QuickReactionRowItem.swift:154` | QuickReactionRowView.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StickerSettingsUI/Sources/StickerSettingsUI/QuickReactionRowItem.swift:155` | QuickReactionRowView.set | `animateScale` | 0.2 |  |  | `current.animateScale(from: 0.1, to: 1, duration: 0.2)` |

## StoriesUI (102)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/StoriesUI/Sources/StoriesUI/StoryChannelInputView.swift:182` | StoryChannelInputView.updateState | `change` |  |  |  | `current.change(size: text.size, animated: animated && !isNew)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChannelInputView.swift:205` | StoryChannelInputView.updateState | `change` |  |  |  | `current.change(size: text.size, animated: animated && !isNew)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:58` | LockControl.updatePercent | `change` |  |  |  | `arrow.change(opacity: percent, animated: true)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:139` | StoryRecorderOverlayView.updateInside | `CABasicAnimation` | 0.1 |  | backgroundColor | `let animation = CABasicAnimation(keyPath: "backgroundColor")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:140` | StoryRecorderOverlayView.updateInside | `.duration =` | 0.1 |  |  | `animation.duration = 0.1` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:277` | StoryRecorderOverlayWindowController.hold | `change` |  |  |  | `lockControl.change(opacity: 0, animated: animated) { [weak self] _ in` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:314` | StoryRecorderOverlayWindowController.show | `animateScaleSpring` | 0.4 |  |  | `view.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.4)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:315` | StoryRecorderOverlayWindowController.show | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:358` | StoryRecorderOverlayWindowController.hide | `_change` | 0.2 |  |  | `lockWindow.contentView?._change(opacity: 0, animated: true)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:360` | StoryRecorderOverlayWindowController.hide | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 1.0, to: 0, duration: 0.2, removeOnCompletion: false, completion: { complete in` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:447` | StoryRecordingView.viewWillMove | `CABasicAnimation` |  |  | opacity | `let animate = CABasicAnimation(keyPath: "opacity")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:451` | StoryRecordingView.viewWillMove | `.duration =` | 1.5 |  |  | `animate.duration = 1.5` |
| `packages/StoriesUI/Sources/StoriesUI/StoryRecordingView.swift:533` | StoryRecordingView.updateStoryRecordingView | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMorphTransition.swift:145` | Entry.release | `CABasicAnimation` |  |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMorphTransition.swift:148` | Entry.release | `.duration =` | fadeDuration |  |  | `animation.duration = fadeDuration` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMorphTransition.swift:517` | Phase.add | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMorphTransition.swift:520` | Phase.add | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMorphTransition.swift:596` | Phase.syncChrome | `CAKeyframeAnimation` |  |  | opacity | `let animation = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMorphTransition.swift:599` | Phase.syncChrome | `.duration =` | timeline.plan.duration |  |  | `animation.duration = timeline.plan.duration` |
| `packages/StoriesUI/Sources/StoriesUI/StoryLayoutView.swift:208` | State.updateStatus | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMediaController.swift:781` | FolderPanel.updateState | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: NSMakePoint(0, frame.height), to: current.frame.origin)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryMediaController.swift:803` | FolderPanel.updateState | `animatePosition` |  |  |  | `current.layer?.animatePosition(from: NSMakePoint(0, frame.height), to: current.frame.origin)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:533` | Container.apply | `change` |  |  |  | `current.change(size: text.size, animated: animated && !isNew)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:536` | Container.apply | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:537` | Container.apply | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1105` | State.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1124` | State.update | `animateAlpha` | 0.2 |  |  | `textView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1176` | State.update | `animateBackground` |  |  |  | `self.shadowView.layer?.animateBackground()` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1181` | State.update | `animateBackground` |  |  |  | `self.shadowView.layer?.animateBackground()` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1638` | State.updateSides | `change` |  |  |  | `self.prevStoryView?.change(opacity: isPrev ? 1 : 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1639` | State.updateSides | `change` |  |  |  | `self.nextStoryView?.change(opacity: !isPrev ? 1 : 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1641` | State.updateSides | `change` |  |  |  | `self.prevStoryView?.change(opacity: 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1642` | State.updateSides | `change` |  |  |  | `self.nextStoryView?.change(opacity: 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1743` | State.notify | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1760` | State.notify | `change` |  |  |  | `self.controls.change(opacity: isControlHid ? 0 : 1, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1761` | State.notify | `change` |  |  |  | `self.navigator.change(opacity: isControlHid ? 0 : 1, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1763` | State.notify | `change` |  |  |  | `self.text?.change(opacity: isControlHid \|\| value.wideInput ? 0 : 1, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:1937` | State.animateAppearingWithoutSource | `animateScaleSpring` | 0.4 |  |  | `self.container.layer?.animateScaleSpring(from: 0.94, to: 1, duration: 0.4, bounce: true)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2555` | TranslateDirection.translate | `.duration =` | duration |  |  | `group.duration = duration` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2562` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.translation.x | `translation = CABasicAnimation(keyPath: "sublayerTransform.translation.x")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2565` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.rotation.y | `rotation = CABasicAnimation(keyPath: "sublayerTransform.rotation.y")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2568` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.translation.z | `translationZ = CABasicAnimation(keyPath: "sublayerTransform.translation.z")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2572` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.translation.x | `translation = CABasicAnimation(keyPath: "sublayerTransform.translation.x")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2575` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.rotation.y | `rotation = CABasicAnimation(keyPath: "sublayerTransform.rotation.y")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2578` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.translation.z | `translationZ = CABasicAnimation(keyPath: "sublayerTransform.translation.z")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2581` | TranslateDirection.translate | `_change` | duration | .easeOut |  | `view2._change(opacity: 1, duration: duration, timingFunction: .easeOut)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2582` | TranslateDirection.translate | `_change` | duration | .easeOut | sublayerTransform.translation.x | `view1._change(opacity: 0, duration: duration, timingFunction: .easeOut)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2584` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.translation.x | `translation = CABasicAnimation(keyPath: "sublayerTransform.translation.x")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2587` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.rotation.y | `rotation = CABasicAnimation(keyPath: "sublayerTransform.rotation.y")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2590` | TranslateDirection.translate | `CABasicAnimation` |  |  | sublayerTransform.translation.z | `translationZ = CABasicAnimation(keyPath: "sublayerTransform.translation.z")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2593` | TranslateDirection.translate | `_change` | duration | .easeOut |  | `view2._change(opacity: 0, duration: duration, timingFunction: .easeOut)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryListView.swift:2594` | TranslateDirection.translate | `_change` | duration | .easeOut |  | `view1._change(opacity: 1, duration: duration, timingFunction: .easeOut)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:378` | PositionView.onInsert | `animateScaleSpring` | 0.6 |  |  | `self.containerView.layer?.animateScaleSpring(from: 0.01, to: 1.0, duration: 0.6, delay: item.insertDelay ?? 0, removeOnCompletion: false, bo` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:530` | PositionView.set | `animateScaleSpring` | 0.2 |  |  | `containerView.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:629` | PositionView.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let fadeDown = makeSpringAnimation("opacity")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:636` | PositionView.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let fadeUp = makeSpringAnimation("opacity")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:807` | FixedMessageItemView.onInsert | `animateScaleSpring` | 0.6 |  |  | `self.containerView.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.6, removeOnCompletion: false, bounce: false)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:857` | FixedMessageItemView.set | `animateScaleSpring` | 0.2 |  |  | `containerView.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:1003` | Item.animate | `animateScale` | 0.3 | .easeInEaseOut |  | `l.animateScale(from: 0.1, to: 1, duration: 0.3, timingFunction: .easeInEaseOut)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:1009` | Item.animate | `CAKeyframeAnimation` | duration |  | position | `let pos = CAKeyframeAnimation(keyPath: "position")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:1016` | Item.animate | `CAKeyframeAnimation` |  |  | opacity | `let op = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:1022` | Item.animate | `CAKeyframeAnimation` |  |  | transform.scale | `let sc = CAKeyframeAnimation(keyPath: "transform.scale")` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:1029` | Item.animate | `.duration =` | duration |  |  | `group.duration = duration` |
| `packages/StoriesUI/Sources/StoriesUI/StoryStreamMessagesView.swift:1364` | StoryStreamMessagesView.update | `change` | 0.2 | .easeOut |  | `tableView.change(opacity: lastHideMessageId != nil ? 0 : 1, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:776` | Preview.updateVisibility | `_change` |  |  |  | `preview._change(opacity: preview._mouseInside() ? 1.0 : 0.0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:779` | Preview.updateVisibility | `change` |  |  |  | `button.change(opacity: 1.0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:781` | Preview.updateVisibility | `change` |  |  |  | `button.change(opacity: 0.8, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:816` | Preview.update | `animateAlpha` | 0.25 |  |  | `preview.layer?.animateAlpha(from: 0, to: 1, duration: 0.25)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:817` | Preview.update | `animateScaleSpring` | 0.25 |  |  | `preview.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.25, bounce: false)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1287` | Source.updatePrevNextControls | `change` |  |  |  | `self.prev_button.change(opacity: hasPrevGroup ? 1 : 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1288` | Source.updatePrevNextControls | `change` |  |  |  | `self.next_button.change(opacity: 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1290` | Source.updatePrevNextControls | `change` |  |  |  | `self.prev_button.change(opacity: 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1294` | Source.updatePrevNextControls | `change` |  |  |  | `self.next_button.change(opacity: hasNextGroup ? 1 : 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1295` | Source.updatePrevNextControls | `change` |  |  |  | `self.prev_button.change(opacity: 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1297` | Source.updatePrevNextControls | `change` |  |  |  | `self.next_button.change(opacity: 0, animated: animated)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1814` | Source.playReaction | `animateScale` | 0.25 |  |  | `layer.animateScale(from: 0.1, to: 1, duration: 0.25)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1865` | Source.showReactions | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1866` | Source.showReactions | `animateScaleSpring` | 0.2 |  |  | `view.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1896` | Source.showLikePanel | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1897` | Source.showLikePanel | `animateScaleSpring` | 0.2 |  |  | `view.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1957` | Source.showTooltip | `animateAlpha` | 0.2 |  |  | `tooltip.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:1958` | Source.showTooltip | `animatePosition` |  |  |  | `tooltip.layer?.animatePosition(from: tooltip.frame.origin.offsetBy(dx: 0, dy: 20), to: tooltip.frame.origin)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:2096` | Source.scrollWheel | `change` |  |  |  | `current.change(pos: NSMakePoint(current.frame.minX, 0), animated: true)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:2098` | Source.scrollWheel | `_change` |  |  |  | `overlay._change(pos: NSMakePoint(overlay.frame.minX, current.storyRect.maxY - overlay.frame.height + 15), animated: true)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:4083` | StoryModalController.ShowStories | `animateBackground` |  |  |  | `showModal(with: StoryModalController(context: context, stories: storyContent, initialId: initialId), for: context.window, animationType: .an` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:4140` | StoryModalController.ShowSingleStory | `animateBackground` |  |  |  | `showModal(with: StoryModalController(context: context, stories: storyContent, initialId: initialId), for: context.window, animationType: .an` |
| `packages/StoriesUI/Sources/StoriesUI/StoryModalController.swift:4156` | StoryModalController.ShowListStory | `animateBackground` |  |  |  | `showModal(with: StoryModalController(context: context, stories: storyContent, initialId: initialId), for: context.window, animationType: .an` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:476` | StoryListContainer.set | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:477` | StoryListContainer.set | `animateScaleCenter` | 0.2 |  |  | `view.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:479` | StoryListContainer.set | `animateAlpha` | 0.2 |  |  | `component.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:480` | StoryListContainer.set | `animateScaleCenter` | 0.2 |  |  | `component.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:690` | StoryListContainer.updateLayout | `_change` | transition.duration | transition.timingFunction |  | `scrollView.contentView._change(size: CGSize(width: scrollView.contentView.bounds.width, height: size.height), animated: transition.isAnimate` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:1287` | ItemView.updateLayout | `animateCornerRadius` | transition.duration | transition.timingFunction |  | `backgroundView.animateCornerRadius(duration: transition.duration, timingFunction: transition.timingFunction)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryChatListView.swift:1293` | ItemView.updateLayout | `animateCornerRadius` | transition.duration | transition.timingFunction |  | `imageView.layer?.animateCornerRadius(duration: transition.duration, timingFunction: transition.timingFunction)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:145` | StoryLikeActionButton.react | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:146` | StoryLikeActionButton.react | `animateScale` | 0.2 |  |  | `layer.animateScale(from: 0.1, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:280` | StoryLikeActionButton.update | `animateAlpha` | 0.2 | .spring |  | `layer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:281` | StoryLikeActionButton.update | `animateScale` | 0.35 | .spring |  | `layer.animateScale(from: 0.1, to: 1, duration: 0.35, timingFunction: .spring)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:378` | State.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:379` | State.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:498` | State.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/StoriesUI/Sources/StoriesUI/StoryInputView.swift:499` | State.update | `animateScaleSpring` | 0.2 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2, bounce: false)` |

## TGUIKit (488)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/TGUIKit/Sources/ModalMorphTransition.swift:618` | Segment.keyframe | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/ModalMorphTransition.swift:621` | Segment.keyframe | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/ModalMorphTransition.swift:674` | Segment.fadeOutAndFinish | `animateAlpha` | duration |  |  | `layer.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/ModalMorphTransition.swift:677` | Segment.fadeOutAndFinish | `animateAlpha` | duration |  |  | `shadow.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/SoftwareGradientBackground.swift:381` | CloneView.updateLayout | `CAKeyframeAnimation` | duration |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/TGUIKit/Sources/SoftwareGradientBackground.swift:383` | CloneView.updateLayout | `.duration =` |  |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/SoftwareGradientBackground.swift:399` | CloneView.updateLayout | `CAKeyframeAnimation` | duration |  | contents | `let animation = CAKeyframeAnimation(keyPath: "contents")` |
| `packages/TGUIKit/Sources/SoftwareGradientBackground.swift:401` | CloneView.updateLayout | `.duration =` |  |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:265` | NumericAnimation.update | `animateAlpha` | Self.duration - | Self.timingFunction |  | `textView.layer?.animateAlpha(from: 1, to: 0, duration: Self.duration - 0.1, timingFunction: Self.timingFunction, removeOnCompletion: false, ` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:271` | NumericAnimation.update | `animatePosition` |  | Self.timingFunction |  | `textView.layer?.animatePosition(from: textView.frame.origin, to: NSMakePoint(textView.frame.minX, textView.frame.maxY), timingFunction: Self` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:273` | NumericAnimation.update | `animatePosition` |  | Self.timingFunction |  | `textView.layer?.animatePosition(from: textView.frame.origin, to: NSMakePoint(textView.frame.minX, textView.frame.minY - textView.frame.heigh` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:290` | NumericAnimation.update | `animatePosition` |  | Self.timingFunction |  | `view.layer?.animatePosition(from: NSMakePoint(from.x - pos.x, from.y - pos.y), to: .zero, timingFunction: Self.timingFunction, removeOnCompl` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:304` | NumericAnimation.update | `animatePosition` |  | Self.timingFunction |  | `current.layer?.animatePosition(from: NSMakePoint(pos.x, pos.y - layout.0.layoutSize.height), to: pos, timingFunction: Self.timingFunction)` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:306` | NumericAnimation.update | `animatePosition` |  | Self.timingFunction |  | `current.layer?.animatePosition(from: NSMakePoint(pos.x, pos.y + layout.0.layoutSize.height), to: pos, timingFunction: Self.timingFunction)` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:309` | NumericAnimation.update | `animateAlpha` | Self.duration |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: Self.duration)` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:342` | NumericAnimation.updateRegularLayouts | `animatePosition` |  | Self.timingFunction |  | `view.layer?.animatePosition(from: NSMakePoint(from.x - origin.x, from.y - origin.y), to: .zero, timingFunction: Self.timingFunction, removeO` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:361` | NumericAnimation.animateRollingBlur | `animate` | duration | .easeInEaseOut | filters.gaussianBlur.inputRadius | `layer.animate(from: NSNumber(value: Double(from)), to: NSNumber(value: Double(to)), keyPath: "filters.gaussianBlur.inputRadius", timingFunct` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:390` | NumericAnimation.updateRolling | `animate` | DynamicCounterTextView.rollingMotionDuration | .spring | position | `layer.animate(from: NSValue(point: .zero), to: NSValue(point: NSMakePoint(0, -shift)), keyPath: "position", timingFunction: .spring, duratio` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:391` | NumericAnimation.updateRolling | `animate` | DynamicCounterTextView.rollingMotionDuration | .spring | transform.scale | `layer.animate(from: NSNumber(value: 1.0), to: NSNumber(value: 0.01), keyPath: "transform.scale", timingFunction: .spring, duration: DynamicC` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:393` | NumericAnimation.updateRolling | `animate` | DynamicCounterTextView.rollingAlphaDuration | .easeInEaseOut | opacity | `layer.animate(from: NSNumber(value: 1.0), to: NSNumber(value: 0.0), keyPath: "opacity", timingFunction: .easeInEaseOut, duration: DynamicCou` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:410` | NumericAnimation.updateRolling | `animatePosition` | DynamicCounterTextView.rollingMotionDuration | .spring |  | `view.layer?.animatePosition(from: NSMakePoint(from.x - origin.x, from.y - origin.y), to: .zero, duration: DynamicCounterTextView.rollingMoti` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:428` | NumericAnimation.updateRolling | `animate` | DynamicCounterTextView.rollingMotionDuration | .spring | transform.scale | `layer.animate(from: NSNumber(value: 0.001), to: NSNumber(value: 1.0), keyPath: "transform.scale", timingFunction: .spring, duration: Dynamic` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:429` | NumericAnimation.updateRolling | `animate` | DynamicCounterTextView.rollingMotionDuration | .spring | position | `layer.animate(from: NSValue(point: NSMakePoint(0, shift)), to: NSValue(point: .zero), keyPath: "position", timingFunction: .spring, duration` |
| `packages/TGUIKit/Sources/DynamicCounterTextView.swift:431` | NumericAnimation.updateRolling | `animate` | DynamicCounterTextView.rollingAlphaDuration | .easeInEaseOut | opacity | `layer.animate(from: NSNumber(value: 0.0), to: NSNumber(value: 1.0), keyPath: "opacity", timingFunction: .easeInEaseOut, duration: DynamicCou` |
| `packages/TGUIKit/Sources/ViewController.swift:262` | TileControl.change | `change` | duration | CAMediaTimingFunctionName |  | `open override func change(size: NSSize, animated: Bool, _ save: Bool = true, removeOnCompletion: Bool = true, duration: Double = 0.2, timing` |
| `packages/TGUIKit/Sources/ViewController.swift:263` | TileControl.change | `change` | duration | timingFunction |  | `super.change(size: size, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFunctio` |
| `packages/TGUIKit/Sources/View.swift:461` | View.change | `change` | duration | CAMediaTimingFunctionName |  | `open func change(pos position: NSPoint, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFu` |
| `packages/TGUIKit/Sources/View.swift:462` | View.change | `_change` | duration | timingFunction |  | `super._change(pos: position, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFun` |
| `packages/TGUIKit/Sources/View.swift:465` | View.change | `change` | duration | CAMediaTimingFunctionName |  | `open func change(size: NSSize, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFunction: C` |
| `packages/TGUIKit/Sources/View.swift:466` | View.change | `_change` | duration | timingFunction |  | `super._change(size: size, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFuncti` |
| `packages/TGUIKit/Sources/View.swift:468` | View.change | `change` | duration | CAMediaTimingFunctionName |  | `open func change(opacity to: CGFloat, animated: Bool = true, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, tim` |
| `packages/TGUIKit/Sources/View.swift:469` | View.change | `_change` | duration | timingFunction |  | `super._change(opacity: to, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFunct` |
| `packages/TGUIKit/Sources/RadialProgressView.swift:750` | RadialProgressView.updateRotation | `CABasicAnimation` |  |  | transform.rotation.z | `let animation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/TGUIKit/Sources/RadialProgressView.swift:753` | RadialProgressView.updateRotation | `.duration =` | Double(2.0 * CGFloat.pi / RadialProgressView.rotationSpeed) |  |  | `animation.duration = Double(2.0 * CGFloat.pi / RadialProgressView.rotationSpeed)` |
| `packages/TGUIKit/Sources/Popover.swift:291` | AnimationMode.show | `animateScaleSpringFrom` | 0.4 |  |  | `strongSelf.background.layer?.animateScaleSpringFrom(anchor: anchor, from: 0.1, to: 1.0, duration: 0.4, bounce: false)` |
| `packages/TGUIKit/Sources/Popover.swift:292` | AnimationMode.show | `animateAlpha` | 0.2 |  |  | `strongSelf.background.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, completion: completion)` |
| `packages/TGUIKit/Sources/Popover.swift:300` | AnimationMode.show | `animateBounds` | 0.25 | .spring |  | `strongSelf.overlay.layer?.animateBounds(from: from.offsetBy(dx: point.x, dy: point.y), to: to, duration: 0.25, timingFunction: .spring, comp` |
| `packages/TGUIKit/Sources/Popover.swift:301` | AnimationMode.show | `animatePosition` | 0.25 | .spring |  | `strongSelf.overlay.layer?.animatePosition(from: point, to: strongSelf.overlay.frame.origin, duration: 0.25, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Popover.swift:451` | AnimationMode.hide | `change` | 0.15 |  |  | `background.change(opacity: 0, animated: animates, duration: 0.15, completion: { [weak self] complete in` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:105` | InvisibleInkDustView.update | `ContainedViewLayoutTransition.animated` | 0.3 | .linear |  | `let transition = ContainedViewLayoutTransition.animated(duration: 0.3, curve: .linear)` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:117` | InvisibleInkDustView.update | `ContainedViewLayoutTransition.animated` | 0.4 | .linear |  | `let transition = ContainedViewLayoutTransition.animated(duration: 0.4, curve: .linear)` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:308` | MediaDustView.update | `ContainedViewLayoutTransition.animated` | 0.3 | .linear |  | `let transition = ContainedViewLayoutTransition.animated(duration: 0.3, curve: .linear)` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:320` | MediaDustView.update | `ContainedViewLayoutTransition.animated` | 0.4 | .linear |  | `let transition = ContainedViewLayoutTransition.animated(duration: 0.4, curve: .linear)` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:347` | MediaDustView.setupRandomAnimations | `CABasicAnimation` |  |  | emitterBehaviors.randomAttractor0.falloff | `let falloffAnimation1 = CABasicAnimation(keyPath: "emitterBehaviors.randomAttractor0.falloff")` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:353` | MediaDustView.setupRandomAnimations | `.duration =` | 2.0 |  |  | `falloffAnimation1.duration = 2.0` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:359` | MediaDustView.setupRandomAnimations | `CAKeyframeAnimation` |  |  | emitterBehaviors.randomAttractor0.position | `let positionAnimation1 = CAKeyframeAnimation(keyPath: "emitterBehaviors.randomAttractor0.position")` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:365` | MediaDustView.setupRandomAnimations | `.duration =` | 3.0 |  |  | `positionAnimation1.duration = 3.0` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:378` | MediaDustView.setupRandomAnimations | `CABasicAnimation` |  |  | emitterBehaviors.randomAttractor1.falloff | `let falloffAnimation2 = CABasicAnimation(keyPath: "emitterBehaviors.randomAttractor1.falloff")` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:384` | MediaDustView.setupRandomAnimations | `.duration =` | 2.0 |  |  | `falloffAnimation2.duration = 2.0` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:390` | MediaDustView.setupRandomAnimations | `CAKeyframeAnimation` |  |  | emitterBehaviors.randomAttractor1.position | `let positionAnimation2 = CAKeyframeAnimation(keyPath: "emitterBehaviors.randomAttractor1.position")` |
| `packages/TGUIKit/Sources/InvisibleInkDustView.swift:396` | MediaDustView.setupRandomAnimations | `.duration =` | 3.0 |  |  | `positionAnimation2.duration = 3.0` |
| `packages/TGUIKit/Sources/Control.swift:249` | Control.apply | `animateBackground` |  |  |  | `layer.animateBackground()` |
| `packages/TGUIKit/Sources/Control.swift:266` | Control.stateDidUpdate | `animateScaleSpring` | 0.3 |  |  | `self.layer?.animateScaleSpring(from: 1, to: pressed, duration: 0.3, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/Control.swift:268` | Control.stateDidUpdate | `animateScaleSpring` | 0.3 |  |  | `self.layer?.animateScaleSpring(from: pressed, to: 1.0, duration: 0.3)` |
| `packages/TGUIKit/Sources/Control.swift:338` | Control.viewDidMoveToSuperview | `animateAlpha` | 0.2 |  |  | `self.layer?.animateAlpha(from: newValue ? 1.0 : 0.0, to: newValue ? 0.0 : 1.0, duration: 0.2, completion:{ [weak self] completed in` |
| `packages/TGUIKit/Sources/Control.swift:829` | Control.apply | `animateBackground` |  |  |  | `self.layer?.animateBackground()` |
| `packages/TGUIKit/Sources/ShimmerLayer.swift:495` | SilhouetteShimmerLayer.makeAnimation | `CAKeyframeAnimation` |  |  | opacity | `let animation = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/TGUIKit/Sources/ShimmerLayer.swift:499` | SilhouetteShimmerLayer.makeAnimation | `.duration =` | 1.5 |  |  | `animation.duration = 1.5` |
| `packages/TGUIKit/Sources/TableRowView.swift:586` | TableRowView.focusAnimation | `makeSpringAnimation` |  |  | opacity | `let animation: CABasicAnimation = makeSpringAnimation("opacity")` |
| `packages/TGUIKit/Sources/SearchView.swift:157` | TagInfo.updateTags | `animateScaleSpring` | 0.2 |  |  | `tag.layer?.animateScaleSpring(from: 1.0, to: 0.3, duration: 0.2)` |
| `packages/TGUIKit/Sources/SearchView.swift:158` | TagInfo.updateTags | `animateAlpha` | 0.2 |  |  | `tag.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak tag] _ in` |
| `packages/TGUIKit/Sources/SearchView.swift:218` | TagInfo.updateTags | `animateAlpha` | 0.2 |  |  | `tagView.layer?.animateAlpha(from: 0, to: 1.0, duration: 0.2)` |
| `packages/TGUIKit/Sources/SearchView.swift:225` | TagInfo.updateTags | `_change` |  |  |  | `inputContainer._change(pos: NSMakePoint(placeholderTextInset + 8, inputContainer.frame.minY), animated: true)` |
| `packages/TGUIKit/Sources/SearchView.swift:627` | TagInfo.change | `animate` | animationStyle.duration | animationStyle.function | opacity | `clear.layer?.animate(from: 0.0 as NSNumber, to: 1.0 as NSNumber, keyPath: "opacity", timingFunction: animationStyle.function, duration: anim` |
| `packages/TGUIKit/Sources/SearchView.swift:647` | TagInfo.change | `animate` | animationStyle.duration | animationStyle.function | opacity | `clear.layer?.animate(from: 1.0 as NSNumber, to: 0.0 as NSNumber, keyPath: "opacity", timingFunction: animationStyle.function, duration: anim` |
| `packages/TGUIKit/Sources/SearchView.swift:815` | TagInfo.change | `change` | duration | CAMediaTimingFunctionName |  | `open override func change(size: NSSize, animated: Bool = true, _ save: Bool = true, removeOnCompletion: Bool = false, duration: Double = 0.2` |
| `packages/TGUIKit/Sources/SearchView.swift:816` | TagInfo.change | `change` | duration | timingFunction |  | `super.change(size: size, animated: animated, save, duration: duration, timingFunction: timingFunction)` |
| `packages/TGUIKit/Sources/SearchView.swift:817` | TagInfo.change | `change` |  |  |  | `clear.change(pos: NSMakePoint(frame.width - inset - clear.frame.width, clear.frame.minY), animated: animated)` |
| `packages/TGUIKit/Sources/VerticalParticleListControl.swift:120` | VerticalParticleListControl.update | `animatePosition` | 0.4 | .spring |  | `self.unselected.layer?.animatePosition(from: self.unselected.frame.origin - pos, to: .zero, duration: 0.4, timingFunction: .spring, additive` |
| `packages/TGUIKit/Sources/VerticalParticleListControl.swift:121` | VerticalParticleListControl.update | `animatePosition` | 0.4 | .spring |  | `self.unselectedMask.layer?.animatePosition(from: self.unselectedMask.frame.origin - pos, to: .zero, duration: 0.4, timingFunction: .spring, ` |
| `packages/TGUIKit/Sources/VerticalParticleListControl.swift:122` | VerticalParticleListControl.update | `animatePosition` | 0.4 | .spring |  | `self.selected.layer?.animatePosition(from: self.selected.frame.origin - selectedPoint, to: .zero, duration: 0.4, timingFunction: .spring, ad` |
| `packages/TGUIKit/Sources/DatePicker.swift:90` | DatePicker.updateSelected | `change` |  |  |  | `self.borderView.change(opacity: 0, animated: animated)` |
| `packages/TGUIKit/Sources/DatePicker.swift:91` | DatePicker.updateSelected | `change` |  |  |  | `self.activeBorderView.change(opacity: 1, animated: animated)` |
| `packages/TGUIKit/Sources/DatePicker.swift:93` | DatePicker.updateSelected | `change` |  |  |  | `self.borderView.change(opacity: 1, animated: animated)` |
| `packages/TGUIKit/Sources/DatePicker.swift:94` | DatePicker.updateSelected | `change` |  |  |  | `self.activeBorderView.change(opacity: 0, animated: animated)` |
| `packages/TGUIKit/Sources/EdgeEffectView.swift:124` | AppliedGradient.update | `CABasicAnimation` |  |  | colors | `let colorAnim = CABasicAnimation(keyPath: "colors")` |
| `packages/TGUIKit/Sources/EdgeEffectView.swift:127` | AppliedGradient.update | `.duration =` | duration |  |  | `colorAnim.duration = duration` |
| `packages/TGUIKit/Sources/EdgeEffectView.swift:133` | AppliedGradient.update | `CABasicAnimation` |  |  | locations | `let locAnim = CABasicAnimation(keyPath: "locations")` |
| `packages/TGUIKit/Sources/EdgeEffectView.swift:136` | AppliedGradient.update | `.duration =` | duration |  |  | `locAnim.duration = duration` |
| `packages/TGUIKit/Sources/BlurEdgeView.swift:122` | Edge.change | `change` | duration | CAMediaTimingFunctionName |  | `public func change(opacity to: CGFloat, animated: Bool = true, _ save: Bool = true, removeOnCompletion: Bool = true, duration: Double = 0.2,` |
| `packages/TGUIKit/Sources/BlurEdgeView.swift:123` | Edge.change | `_change` | duration | timingFunction |  | `self._change(opacity: to, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFuncti` |
| `packages/TGUIKit/Sources/ColorSwatchView.swift:35` | ColorSwatchView.update | `animateScale` |  |  |  | `self.fillView.animateScale(from: 1, to: 0.8, duration: animated ? 0.2 : 0, removeOnCompletion: true)` |
| `packages/TGUIKit/Sources/ColorSwatchView.swift:40` | ColorSwatchView.update | `animateScale` |  |  |  | `self.fillView.animateScale(from: 0.8, to: 1, duration: animated ? 0.2 : 0, removeOnCompletion: true)` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:49` | NavigationBarView.setEdgeEffectOpacity | `change` |  |  |  | `edge.change(opacity: clamped, animated: true)` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:288` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `pLeft.change(opacity: 0.0, duration: animationStyle.duration, timingFunction: animationStyle.function, completion:{ [weak pLeft] completed i` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:293` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `pLeft.change(pos: NSMakePoint(pLeft_to, pLeft.frame.minY), animated: true, duration: animationStyle.duration, timingFunction: animationStyle` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:295` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `pCenter.change(opacity: 0.0, duration: animationStyle.duration, timingFunction: animationStyle.function, completion:{ [weak pCenter] complet` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:303` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `pRight.change(opacity: 0.0, duration: animationStyle.duration, timingFunction: animationStyle.function, completion:{ [weak pRight] completed` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:308` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `pRight.change(pos: NSMakePoint(pRight_to, pRight.frame.minY), animated: true, duration: animationStyle.duration, timingFunction: animationSt` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:312` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `left.change(opacity: 1.0, duration: animationStyle.duration, timingFunction: animationStyle.function)` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:314` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `left.change(pos: NSMakePoint(nLeft_to, left.frame.minY), animated: true, duration: animationStyle.duration, timingFunction: animationStyle.f` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:318` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `center.change(opacity: 1.0, duration: animationStyle.duration, timingFunction: animationStyle.function)` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:321` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `center.change(pos: NSMakePoint(nCenter_to, center.frame.minY), animated: true, duration: animationStyle.duration, timingFunction: animationS` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:325` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `right.change(opacity: 1.0, duration: animationStyle.duration, timingFunction: animationStyle.function)` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:327` | NavigationBarView.switchViews | `change` | animationStyle.duration | animationStyle.function |  | `right.change(pos: NSMakePoint(nRight_to, right.frame.minY), animated: true, duration: animationStyle.duration, timingFunction: animationStyl` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:377` | NavigationBarView.applyAnimation | `animateAlpha` | 0.2 |  |  | `toView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/NavigationBarView.swift:378` | NavigationBarView.applyAnimation | `animateAlpha` | 0.2 |  |  | `fromView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak fromView] completed in` |
| `packages/TGUIKit/Sources/Modal.swift:695` | Side.update | `animateAlpha` | 0.2 |  |  | `titleView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:696` | Side.update | `animateAlpha` | 0.2 |  |  | `subtitleView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:744` | Side.updateBackground | `change` |  |  |  | `self.titleView.change(opacity: state == .normal ? 0 : 1, animated: animated)` |
| `packages/TGUIKit/Sources/Modal.swift:746` | Side.updateBackground | `change` |  |  |  | `self.titleView.change(opacity: 1, animated: animated)` |
| `packages/TGUIKit/Sources/Modal.swift:749` | Side.updateBackground | `change` |  |  |  | `shadowEdgeView.change(opacity: edgeOpacity, animated: animated)` |
| `packages/TGUIKit/Sources/Modal.swift:750` | Side.updateBackground | `change` |  |  |  | `contentBlurView.change(opacity: edgeOpacity, animated: animated)` |
| `packages/TGUIKit/Sources/Modal.swift:1292` | Modal.setDim | `CAKeyframeAnimation` |  |  | backgroundColor | `let animation = CAKeyframeAnimation(keyPath: "backgroundColor")` |
| `packages/TGUIKit/Sources/Modal.swift:1299` | Modal.setDim | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/Modal.swift:1340` | Modal.resize | `change` |  |  |  | `interactionsView?.change(pos: NSMakePoint(0, size.height + headerOffset), animated: animated)` |
| `packages/TGUIKit/Sources/Modal.swift:1414` | Modal.updateContentMask | `animate` | 0.2 | .easeOut | locations | `mask.animate(from: from as NSArray, to: locations as NSArray, keyPath: "locations", timingFunction: .easeOut, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:1487` | Modal.close | `animateBackground` |  |  |  | `let animateBackground = !unhideModalIfNeeded() \|\| self.controller?.containerBackground == .clear \|\| animationType == .animateBackground` |
| `packages/TGUIKit/Sources/Modal.swift:1524` | Modal.close | `CABasicAnimation` |  |  | backgroundColor | `let dim = CABasicAnimation(keyPath: "backgroundColor")` |
| `packages/TGUIKit/Sources/Modal.swift:1554` | Modal.close | `animateAlpha` | 0.15 |  |  | `background?.layer?.animateAlpha(from: 1, to: 0, duration: 0.15, removeOnCompletion: false, completion: { [weak background] _ in` |
| `packages/TGUIKit/Sources/Modal.swift:1576` | Modal.close | `animateBackground` | 0.25 | .spring |  | `if let controller = controller, controller.contentBelowBackground, !animateBackground {` |
| `packages/TGUIKit/Sources/Modal.swift:1577` | Modal.close | `_change` | 0.25 | .spring |  | `controller.view._change(opacity: 0, animated: true, removeOnCompletion: false, duration: 0.25, timingFunction: .spring, completion: { [weak ` |
| `packages/TGUIKit/Sources/Modal.swift:1586` | Modal.close | `animateBackground` | 0.25 |  |  | `} else if animateBackground {` |
| `packages/TGUIKit/Sources/Modal.swift:1587` | Modal.close | `animateAlpha` | 0.25 |  |  | `background.layer?.animateAlpha(from: 1.0, to: 0.0, duration: 0.25, removeOnCompletion: false, completion: {[weak self, weak background] comp` |
| `packages/TGUIKit/Sources/Modal.swift:1602` | Modal.close | `animateAlpha` | 0.2 |  |  | `lastActive.containerView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:1610` | Modal.close | `animateBackground` |  |  |  | `case .common, .noMorph, .noneDelayed, .animateBackground:` |
| `packages/TGUIKit/Sources/Modal.swift:1615` | Modal.close | `animatePosition` | 0.25 | .spring |  | `contentView.layer?.animatePosition(from: oldRect.origin, to: newRect.origin, duration: 0.25, timingFunction: .spring, removeOnCompletion: fa` |
| `packages/TGUIKit/Sources/Modal.swift:1616` | Modal.close | `animateScaleX` | 0.25 | .spring |  | `contentView.layer?.animateScaleX(from: 1, to: newRect.width / oldRect.width, duration: 0.25, timingFunction: .spring, removeOnCompletion: fa` |
| `packages/TGUIKit/Sources/Modal.swift:1617` | Modal.close | `animateScaleY` | 0.25 | .spring |  | `contentView.layer?.animateScaleY(from: 1, to: newRect.height / oldRect.height, duration: 0.25, timingFunction: .spring, removeOnCompletion: ` |
| `packages/TGUIKit/Sources/Modal.swift:1638` | Modal.addSubview | `animateAlpha` | 0.2 |  |  | `subview.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak subview] _ in` |
| `packages/TGUIKit/Sources/Modal.swift:1649` | Modal.addSubview | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:1699` | Modal.show | `animateAlpha` | 0.4 | .spring |  | `controller.view.layer?.animateAlpha(from: 0.1, to: 1, duration: 0.4, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1725` | Modal.show | `animateBackground` | 0.25 | .spring |  | `} else if case .animateBackground = strongSelf.animationType {` |
| `packages/TGUIKit/Sources/Modal.swift:1727` | Modal.show | `animateAlpha` | 0.25 | .spring |  | `strongSelf.container.layer?.animateAlpha(from: 0.1, to: 1.0, duration: 0.25, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1733` | Modal.show | `animatePosition` | 0.35 | .spring |  | `strongSelf.container.layer?.animatePosition(from: NSMakePoint(origin.x, origin.y + 100), to: origin, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1735` | Modal.show | `animateScaleSpring` | 0.35 |  |  | `strongSelf.container.layer?.animateScaleSpring(from: 0.5, to: 1.0, duration: 0.35, bounce: true)` |
| `packages/TGUIKit/Sources/Modal.swift:1739` | Modal.show | `animateAlpha` | 0.15 | .spring |  | `view.layer?.animateAlpha(from: 0.1, to: 1.0, duration: 0.15, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1740` | Modal.show | `animatePosition` | 0.3 | .spring |  | `view.layer?.animatePosition(from: oldRect.origin, to: newRect.origin, duration: 0.3, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1741` | Modal.show | `animateScaleX` | 0.3 | .spring |  | `view.layer?.animateScaleX(from: oldRect.width / newRect.width, to: 1, duration: 0.3, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1742` | Modal.show | `animateScaleY` | 0.3 | .spring |  | `view.layer?.animateScaleY(from: oldRect.height / newRect.height, to: 1, duration: 0.3, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1744` | Modal.show | `animateAlpha` | 0.15 | .spring |  | `view.layer?.animateAlpha(from: 1.0, to: 1.0, duration: 0.15, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1745` | Modal.show | `animateBackground` | 0.2 |  |  | `case .animateBackground:` |
| `packages/TGUIKit/Sources/Modal.swift:1746` | Modal.show | `animateAlpha` | 0.2 |  |  | `strongSelf.visualEffectView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:1760` | Modal.show | `animateBackground` | 0.2 |  |  | `if case .animateBackground = strongSelf.animationType {` |
| `packages/TGUIKit/Sources/Modal.swift:1761` | Modal.show | `animateAlpha` | 0.2 |  |  | `strongSelf.visualEffectView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/Modal.swift:1829` | Modal.show | `animateAlpha` | 0.4 | .spring |  | `controller.view.layer?.animateAlpha(from: 0.1, to: 1, duration: 0.4, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/Modal.swift:1845` | Modal.show | `animateAlpha` | 0.15 |  |  | `strongSelf.background.layer?.animateAlpha(from: 0, to: 1, duration: 0.15, completion:{[weak strongSelf] (completed) in` |
| `packages/TGUIKit/Sources/Modal.swift:1918` | ModalAnimationType.findModal | `animateBackground` |  |  |  | `case animateBackground` |
| `packages/TGUIKit/Sources/Modal.swift:1926` | ModalAnimationCloseBehaviour.findModal | `animateBackground` |  |  |  | `case animateBackground` |
| `packages/TGUIKit/Sources/NavigationModalView.swift:73` | NavigationModalView.close | `animateAlpha` | 0.2 |  |  | `self.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion:false, completion:{[weak self] (completed) in` |
| `packages/TGUIKit/Sources/NavigationModalView.swift:85` | NavigationModalView.viewDidMoveToWindow | `animateAlpha` | 0.2 |  |  | `self.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:98` | InfiniteProgressView.updateProgressAnimation | `CABasicAnimation` |  |  | strokeEnd | `let animation = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:101` | InfiniteProgressView.updateProgressAnimation | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:122` | InfiniteProgressView.updateProgressAnimation | `CABasicAnimation` |  |  | strokeEnd | `let grow = CABasicAnimation(keyPath: "strokeEnd")` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:128` | InfiniteProgressView.updateProgressAnimation | `CABasicAnimation` |  |  | strokeStart | `let shrink = CABasicAnimation(keyPath: "strokeStart")` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:136` | InfiniteProgressView.updateProgressAnimation | `.duration =` | 2.5 |  |  | `group.duration = 2.5` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:147` | InfiniteProgressView.viewDidMoveToWindow | `CABasicAnimation` | 1.5 var |  | transform.rotation.z | `let basicAnimation = CABasicAnimation(keyPath: "transform.rotation.z")` |
| `packages/TGUIKit/Sources/InfiniteProgressView.swift:148` | InfiniteProgressView.viewDidMoveToWindow | `.duration =` | 1.5 var |  |  | `basicAnimation.duration = 1.5` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:192` | SegmentItemView.updateHandlers | `change` |  |  |  | `self?.textView?.change(opacity: 0.8, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:193` | SegmentItemView.updateHandlers | `_change` |  |  |  | `self?.customTextView?._change(opacity: 0.8, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:194` | SegmentItemView.updateHandlers | `change` |  |  |  | `self?.imageView?.change(opacity: 0.8, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:199` | SegmentItemView.updateHandlers | `change` |  |  |  | `self?.textView?.change(opacity: 1.0, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:200` | SegmentItemView.updateHandlers | `_change` |  |  |  | `self?.customTextView?._change(opacity: 1.0, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:201` | SegmentItemView.updateHandlers | `change` |  |  |  | `self?.imageView?.change(opacity: 1.0, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:205` | SegmentItemView.updateHandlers | `change` |  |  |  | `self?.textView?.change(opacity: 1.0, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:206` | SegmentItemView.updateHandlers | `_change` |  |  |  | `self?.customTextView?._change(opacity: 1.0, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:207` | SegmentItemView.updateHandlers | `change` |  |  |  | `self?.imageView?.change(opacity: 1.0, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:357` | SegmentItemView.updateItem | `change` | duration |  |  | `change(size: size, animated: animated, duration: duration)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:563` | ScrollableSegmentView.moveSelector | `change` |  |  |  | `self.selectorView.change(pos: selectorFrame.origin, animated: animated)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:564` | ScrollableSegmentView.moveSelector | `change` |  |  |  | `self.selectorView.change(size: selectorFrame.size, animated: animated)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:648` | ScrollableSegmentView.removeItem | `animateAlpha` | duration |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false, completion: { [weak view] _ in` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:756` | ScrollableSegmentView.applyLiveResort | `change` |  |  |  | `view.change(pos: NSMakePoint(x, view.frame.minY), animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:764` | ScrollableSegmentView.applyLiveResort | `change` |  |  |  | `selectorView.change(pos: selectorFrame.origin, animated: true)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:786` | ScrollableSegmentView.layoutItems | `_change` |  |  |  | `view._change(pos: NSMakePoint(x, 0), animated: animated, completion: { [weak self] completed in` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:795` | ScrollableSegmentView.layoutItems | `change` |  |  |  | `documentView.change(size: NSMakeSize(max(x, frame.width), frame.height), animated: animated)` |
| `packages/TGUIKit/Sources/ScrollableSegmentView.swift:796` | ScrollableSegmentView.layoutItems | `change` |  |  |  | `selectorView.change(pos: selectorFrame.origin, animated: animated)` |
| `packages/TGUIKit/Sources/CatalinaStyledSegmentController.swift:89` | CatalinaSegmentItemView.set | `change` |  |  |  | `separatorView.change(opacity: hasSepator ? 0.4 : 0, animated: animated)` |
| `packages/TGUIKit/Sources/CatalinaStyledSegmentController.swift:90` | CatalinaSegmentItemView.set | `change` |  |  |  | `activeTextView.change(opacity: selected ? 1 : 0, animated: animated)` |
| `packages/TGUIKit/Sources/CatalinaStyledSegmentController.swift:91` | CatalinaSegmentItemView.set | `change` |  |  |  | `inactiveTextView.change(opacity: !selected ? 1 : 0, animated: animated)` |
| `packages/TGUIKit/Sources/CatalinaStyledSegmentController.swift:220` | CatalinaSegmentedControlView.set | `change` |  |  |  | `button.change(pos: NSMakePoint(max(2, min(subview.frame.minX + 2, frame.width - subview.frame.width - 2)), 2), animated: animated)` |
| `packages/TGUIKit/Sources/TabBarView.swift:495` | SelectionGesture.updateSelection | `animate` | 0.4 | .spring | transform | `layer.animate(from: NSValue(caTransform3D: previous), to: NSValue(caTransform3D: transform), keyPath: "transform", timingFunction: .spring, ` |
| `packages/TGUIKit/Sources/TabBarView.swift:600` | SelectionGesture.updateSelectionFrame | `animatePosition` | duration | curve.timingFunction |  | `layer.animatePosition(from: previousPosition, to: layer.position, duration: duration, timingFunction: curve.timingFunction)` |
| `packages/TGUIKit/Sources/TabBarView.swift:601` | SelectionGesture.updateSelectionFrame | `animateBounds` | duration | curve.timingFunction |  | `layer.animateBounds(from: previousBounds, to: layer.bounds, duration: duration, timingFunction: curve.timingFunction)` |
| `packages/TGUIKit/Sources/Extensions.swift:504` | CALayer.animateBackground | `animateBackground` |  |  |  | `func animateBackground(duration: Double = 0.2, function: CAMediaTimingFunctionName = .easeOut) ->Void {` |
| `packages/TGUIKit/Sources/Extensions.swift:507` | CALayer.animateBackground | `makeSpringAnimation` |  |  | backgroundColor | `animation = makeSpringAnimation("backgroundColor")` |
| `packages/TGUIKit/Sources/Extensions.swift:509` | CALayer.animateBackground | `CABasicAnimation` |  |  | backgroundColor | `animation = CABasicAnimation(keyPath: "backgroundColor")` |
| `packages/TGUIKit/Sources/Extensions.swift:514` | CALayer.animateTransform | `animateTransform` | 0.2 |  | transform | `func animateTransform() ->Void {` |
| `packages/TGUIKit/Sources/Extensions.swift:515` | CALayer.animateTransform | `CABasicAnimation` | 0.2 |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/Extensions.swift:516` | CALayer.animateTransform | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:523` | CALayer.animatePath | `makeSpringAnimation` |  |  | path | `animation = makeSpringAnimation("path")` |
| `packages/TGUIKit/Sources/Extensions.swift:525` | CALayer.animatePath | `CABasicAnimation` |  |  | path | `animation = CABasicAnimation(keyPath: "path")` |
| `packages/TGUIKit/Sources/Extensions.swift:528` | CALayer.animatePath | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/Extensions.swift:531` | CALayer.animateShadow | `animateShadow` | 0.2 |  | shadowPath | `func animateShadow() {` |
| `packages/TGUIKit/Sources/Extensions.swift:532` | CALayer.animateShadow | `CABasicAnimation` | 0.2 |  | shadowPath | `let animation = CABasicAnimation(keyPath: "shadowPath")` |
| `packages/TGUIKit/Sources/Extensions.swift:533` | CALayer.animateShadow | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:536` | CALayer.animateFrameFast | `animateFrame` | 0.2 |  | frame | `func animateFrameFast() {` |
| `packages/TGUIKit/Sources/Extensions.swift:537` | CALayer.animateFrameFast | `CABasicAnimation` | 0.2 |  | frame | `let animation = CABasicAnimation(keyPath: "frame")` |
| `packages/TGUIKit/Sources/Extensions.swift:538` | CALayer.animateFrameFast | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:542` | CALayer.animateBorder | `animateBorder` | 0.2 |  | borderWidth | `func animateBorder() ->Void {` |
| `packages/TGUIKit/Sources/Extensions.swift:543` | CALayer.animateBorder | `CABasicAnimation` | 0.2 |  | borderWidth | `let animation = CABasicAnimation(keyPath: "borderWidth")` |
| `packages/TGUIKit/Sources/Extensions.swift:544` | CALayer.animateBorder | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:548` | CALayer.animateOpacity | `CABasicAnimation` | 0.2 |  | opacity | `let animation = CABasicAnimation(keyPath: "opacity")` |
| `packages/TGUIKit/Sources/Extensions.swift:549` | CALayer.animateOpacity | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:553` | CALayer.animateBorderColor | `animateBorder` | 0.2 |  | borderColor | `func animateBorderColor() ->Void {` |
| `packages/TGUIKit/Sources/Extensions.swift:554` | CALayer.animateBorderColor | `CABasicAnimation` | 0.2 |  | borderColor | `let animation = CABasicAnimation(keyPath: "borderColor")` |
| `packages/TGUIKit/Sources/Extensions.swift:555` | CALayer.animateBorderColor | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:559` | CALayer.animateGradientColors | `CABasicAnimation` | 0.2 |  | colors | `let animation = CABasicAnimation(keyPath: "colors")` |
| `packages/TGUIKit/Sources/Extensions.swift:560` | CALayer.animateGradientColors | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:563` | CALayer.animateCornerRadius | `animateCornerRadius` |  | CAMediaTimingFunctionName |  | `func animateCornerRadius(duration: Double = 0.2, timingFunction: CAMediaTimingFunctionName = .easeOut) ->Void {` |
| `packages/TGUIKit/Sources/Extensions.swift:566` | CALayer.animateCornerRadius | `makeSpringAnimation` |  |  | cornerRadius | `animation = makeSpringAnimation("cornerRadius")` |
| `packages/TGUIKit/Sources/Extensions.swift:568` | CALayer.animateCornerRadius | `CABasicAnimation` |  |  | cornerRadius | `animation = CABasicAnimation(keyPath: "cornerRadius")` |
| `packages/TGUIKit/Sources/Extensions.swift:571` | CALayer.animateCornerRadius | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/Extensions.swift:575` | CALayer.animateContents | `animateContents` | 0.2 |  | contents | `func animateContents() ->Void {` |
| `packages/TGUIKit/Sources/Extensions.swift:576` | CALayer.animateContents | `CABasicAnimation` | 0.2 |  | contents | `let animation = CABasicAnimation(keyPath: "contents")` |
| `packages/TGUIKit/Sources/Extensions.swift:577` | CALayer.animateContents | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/Extensions.swift:852` | NSView._change | `_change` |  | CAMediaTimingFunctionName |  | `func _change(pos position: NSPoint, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFuncti` |
| `packages/TGUIKit/Sources/Extensions.swift:872` | NSView._change | `animatePosition` | duration | timingFunction |  | `layer.animatePosition(from: NSMakePoint(presentX, presentY), to: position, duration: duration, timingFunction: timingFunction, removeOnCompl` |
| `packages/TGUIKit/Sources/Extensions.swift:889` | NSView._change | `animatePosition` | duration | timingFunction |  | `self.layer?.animatePosition(from: NSMakePoint(presentX, presentY), to: position, duration: duration, timingFunction: timingFunction, removeO` |
| `packages/TGUIKit/Sources/Extensions.swift:915` | NSView._change | `_change` |  | CAMediaTimingFunctionName |  | `func _change(size: NSSize, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFunction: CAMed` |
| `packages/TGUIKit/Sources/Extensions.swift:930` | NSView.animate | `animateBounds` | duration | timingFunction |  | `layer.animateBounds(from: presentBounds, to: NSMakeRect(0, 0, size.width, size.height), duration: duration, timingFunction: timingFunction, ` |
| `packages/TGUIKit/Sources/Extensions.swift:962` | NSView._changeBounds | `animateBounds` | duration | timingFunction |  | `layer.animateBounds(from: from, to: to, duration: duration, timingFunction: timingFunction, removeOnCompletion: removeOnCompletion, completi` |
| `packages/TGUIKit/Sources/Extensions.swift:971` | NSView._changeBounds | `animateBounds` | duration | timingFunction |  | `self.layer?.animateBounds(from: from, to: to, duration: duration, timingFunction: timingFunction, removeOnCompletion: removeOnCompletion, co` |
| `packages/TGUIKit/Sources/Extensions.swift:982` | NSView._change | `_change` |  | CAMediaTimingFunctionName |  | `func _change(opacity to: CGFloat, animated: Bool = true, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingF` |
| `packages/TGUIKit/Sources/Extensions.swift:995` | NSView._change | `animateAlpha` | duration | timingFunction |  | `layer.animateAlpha(from: opacity, to: to, duration:duration, timingFunction: timingFunction, removeOnCompletion: removeOnCompletion, complet` |
| `packages/TGUIKit/Sources/Extensions.swift:2380` | NSEdgeInsets.performSubviewRemoval | `animateAlpha` | duration | timingFunction |  | `view.layer?.animateAlpha(from: CGFloat(from), to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, completi` |
| `packages/TGUIKit/Sources/Extensions.swift:2391` | NSEdgeInsets.performSubviewRemoval | `animateScaleCenter` | duration | timingFunction |  | `view.layer?.animateScaleCenter(from: 1, to: 0.01, duration: duration, removeOnCompletion: false, timingFunction: timingFunction)` |
| `packages/TGUIKit/Sources/Extensions.swift:2393` | NSEdgeInsets.performSubviewRemoval | `animateScaleXCenter` | duration | timingFunction |  | `view.layer?.animateScaleXCenter(from: 1, to: 0.01, duration: duration, removeOnCompletion: false, timingFunction: timingFunction)` |
| `packages/TGUIKit/Sources/Extensions.swift:2395` | NSEdgeInsets.performSubviewRemoval | `animateScaleYCenter` | duration | timingFunction |  | `view.layer?.animateScaleYCenter(from: 1, to: 0.01, duration: duration, removeOnCompletion: false, timingFunction: timingFunction)` |
| `packages/TGUIKit/Sources/Extensions.swift:2397` | NSEdgeInsets.performSubviewRemoval | `animateScaleCenter` | duration | timingFunction |  | `view.layer?.animateScaleCenter(from: 1, to: scaleTo, duration: duration, removeOnCompletion: false, timingFunction: timingFunction)` |
| `packages/TGUIKit/Sources/Extensions.swift:2406` | NSEdgeInsets.performSublayerRemoval | `animateAlpha` | duration | timingFunction |  | `view.animateAlpha(from: CGFloat(view.opacity), to: 0, duration: duration, timingFunction: timingFunction, removeOnCompletion: false, complet` |
| `packages/TGUIKit/Sources/Extensions.swift:2417` | NSEdgeInsets.performSublayerRemoval | `animateScale` | duration | timingFunction |  | `view.animateScale(from: 1, to: 0.01, duration: duration, timingFunction: timingFunction, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/Extensions.swift:2419` | NSEdgeInsets.performSublayerRemoval | `animateScale` | duration | timingFunction |  | `view.animateScale(from: 1, to: scaleTo, duration: duration, timingFunction: timingFunction, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/Extensions.swift:2428` | NSEdgeInsets.performSubviewPosRemoval | `animatePosition` | duration | timingFunction |  | `view.layer?.animatePosition(from: view.frame.origin, to: pos, duration: duration, timingFunction: timingFunction, removeOnCompletion: false,` |
| `packages/TGUIKit/Sources/ImageButton.swift:16` | ImageButtonAnimationPolicy. | `animateContents` |  |  |  | `case animateContents` |
| `packages/TGUIKit/Sources/ImageButton.swift:300` | ImageButton.apply | `animateScaleSpring` | 0.35 |  |  | `additionBackgroundView.layer?.animateScaleSpring(from: current, to: value, duration: 0.35, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/ImageButton.swift:336` | ImageButton.applyAnimation | `animateContents` |  |  |  | `case .animateContents:` |
| `packages/TGUIKit/Sources/ImageButton.swift:349` | ImageButton.applyAnimation | `animateScaleCenter` | 0.25 |  |  | `imageView.layer?.animateScaleCenter(from: 1, to: 0.1, duration: 0.25, removeOnCompletion: false, completion: { [weak imageView] _ in` |
| `packages/TGUIKit/Sources/ImageButton.swift:352` | ImageButton.applyAnimation | `animateAlpha` | 0.2 |  |  | `imageView.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/ImageButton.swift:354` | ImageButton.applyAnimation | `animateScaleCenter` | 0.25 |  |  | `newImageView.layer?.animateScaleCenter(from: 0.1, to: 1, duration: 0.25, removeOnCompletion: true)` |
| `packages/TGUIKit/Sources/CodeEntryControl.swift:109` | CodeEntryElement.inputKey | `animateAlpha` | 0.2 |  |  | `textView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/CodeEntryControl.swift:110` | CodeEntryElement.inputKey | `animatePosition` | 0.2 |  |  | `textView.layer?.animatePosition(from: NSMakePoint(textView.frame.minX, textView.frame.minY + 5), to: textView.frame.origin)` |
| `packages/TGUIKit/Sources/CodeEntryControl.swift:111` | CodeEntryElement.inputKey | `animateScaleSpring` | 0.2 |  |  | `textView.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/CodeEntryControl.swift:146` | CodeEntryElement.updateResponder | `animateBorder` |  |  |  | `layer?.animateBorder()` |
| `packages/TGUIKit/Sources/ScrollView.swift:259` | ScrollView.change | `change` | duration | CAMediaTimingFunctionName |  | `public func change(pos position: NSPoint, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timing` |
| `packages/TGUIKit/Sources/ScrollView.swift:260` | ScrollView.change | `_change` | duration | timingFunction |  | `super._change(pos: position, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFun` |
| `packages/TGUIKit/Sources/ScrollView.swift:263` | ScrollView.change | `change` | duration | CAMediaTimingFunctionName |  | `public func change(size: NSSize, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFunction:` |
| `packages/TGUIKit/Sources/ScrollView.swift:264` | ScrollView.change | `_change` | duration | timingFunction |  | `super._change(size: size, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFuncti` |
| `packages/TGUIKit/Sources/ScrollView.swift:266` | ScrollView.change | `change` | duration | CAMediaTimingFunctionName |  | `public func change(opacity to: CGFloat, animated: Bool = true, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, t` |
| `packages/TGUIKit/Sources/ScrollView.swift:267` | ScrollView.change | `_change` | duration | timingFunction |  | `super._change(opacity: to, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFunct` |
| `packages/TGUIKit/Sources/DraggingView.swift:140` | DraggingView.updateItems | `animateBorder` |  |  |  | `itemView.layer?.animateBorder()` |
| `packages/TGUIKit/Sources/DraggingView.swift:143` | DraggingView.updateItems | `animateBorder` |  |  |  | `itemView.layer?.animateBorder()` |
| `packages/TGUIKit/Sources/DraggingView.swift:173` | DraggingView.draggingEntered | `animateAlpha` | 0.25 |  |  | `container.layer?.animateAlpha(from: 0.0, to: 1.0, duration: 0.25)` |
| `packages/TGUIKit/Sources/DraggingView.swift:186` | DraggingView.draggingExited | `animateAlpha` | 0.25 |  |  | `container.layer?.animateAlpha(from: 1.0, to: 0.0, duration: 0.25, removeOnCompletion:false, completion:{[weak self] (completed) in` |
| `packages/TGUIKit/Sources/ShimmerTooltipView.swift:60` | ShimmerTooltipView.show | `animateAlpha` | 0.2 |  |  | `layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/ShimmerTooltipView.swift:61` | ShimmerTooltipView.show | `animateScaleSpringFrom` | 0.4 |  |  | `layer?.animateScaleSpringFrom(anchor: NSMakePoint(arrowX, frame.height), from: 0.01, to: 1, duration: 0.4, bounce: false)` |
| `packages/TGUIKit/Sources/ShimmerTooltipView.swift:117` | ShimmerTooltipView.layout | `CABasicAnimation` |  |  | position.x | `let animation = CABasicAnimation(keyPath: "position.x")` |
| `packages/TGUIKit/Sources/ShimmerTooltipView.swift:120` | ShimmerTooltipView.layout | `.duration =` | 2.2 |  |  | `animation.duration = 2.2` |
| `packages/TGUIKit/Sources/GlassContainerView.swift:70` | GlassContainerView.setGhostFrame | `NSAnimationContext.runAnimationGroup` | duration if |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/TGUIKit/Sources/GlassContainerView.swift:71` | GlassContainerView.setGhostFrame | `.duration =` | duration if |  |  | `context.duration = duration` |
| `packages/TGUIKit/Sources/TableView.swift:1822` | TableView.updatePrimaryStickAfterScroll | `_change` |  |  |  | `stickView._change(pos: updatedPoint, animated: animated \|\| maybeAnimated)` |
| `packages/TGUIKit/Sources/TableView.swift:1879` | TableView.updatePrimaryStickAfterScroll | `_change` |  |  |  | `stickView._change(pos: NSMakePoint(0, -stickView.frame.height), animated: animated, removeOnCompletion: false, completion: { [weak stickView` |
| `packages/TGUIKit/Sources/TableView.swift:1967` | TableView.updateSecondaryStickAfterScroll | `_change` |  |  |  | `secondaryStickView._change(pos: updatedPoint, animated: animated)` |
| `packages/TGUIKit/Sources/TableView.swift:2033` | TableView.updateSecondaryStickAfterScroll | `_change` |  |  |  | `secondaryStickView._change(pos: NSMakePoint(0, -secondaryStickView.frame.height), animated: animated, removeOnCompletion: false, completion:` |
| `packages/TGUIKit/Sources/TableView.swift:2346` | TableView.startResorting | `animatePosition` | duration | .spring |  | `view.layer?.animatePosition(from: NSMakePoint(0, view.frame.minY - newPoint.y), to: .zero, duration: duration, timingFunction: .spring, remo` |
| `packages/TGUIKit/Sources/TableView.swift:2366` | TableView.stopResorting | `NSAnimationContext.runAnimationGroup` |  |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/TGUIKit/Sources/TableView.swift:3780` | TableView.saveVisible | `change` |  |  |  | `searchView.change(pos: NSMakePoint(0, -searchView.frame.height), animated: true)` |
| `packages/TGUIKit/Sources/TableView.swift:3792` | TableView.saveVisible | `change` |  |  |  | `searchView.change(pos: NSZeroPoint, animated: true)` |
| `packages/TGUIKit/Sources/TableView.swift:3972` | PendingResizeAnchor.apply | `CABasicAnimation` |  |  | bounds | `let bounds = CABasicAnimation(keyPath: "bounds")` |
| `packages/TGUIKit/Sources/TableView.swift:3984` | PendingResizeAnchor.apply | `CABasicAnimation` |  |  | position | `let animation = CABasicAnimation(keyPath: "position")` |
| `packages/TGUIKit/Sources/TableView.swift:3988` | PendingResizeAnchor.apply | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/TableView.swift:4015` | PendingResizeAnchor.updateEmpties | `animateAlpha` | duration |  |  | `emptyView.layer?.animateAlpha(from: 0, to: 1, duration: duration)` |
| `packages/TGUIKit/Sources/TableView.swift:4028` | PendingResizeAnchor.updateEmpties | `animatePosition` |  |  |  | `emptyView.layer?.animatePosition(from: emptyView.frame.origin.offsetBy(dx: 0, dy: 25), to: emptyView.frame.origin)` |
| `packages/TGUIKit/Sources/TableView.swift:4036` | PendingResizeAnchor.updateEmpties | `_change` |  |  |  | `tableView._change(opacity: 0, animated: animated)` |
| `packages/TGUIKit/Sources/TableView.swift:4041` | PendingResizeAnchor.updateEmpties | `animateAlpha` | duration |  |  | `emptyView.layer?.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false, completion: { [weak emptyView] completed in` |
| `packages/TGUIKit/Sources/TableView.swift:4045` | PendingResizeAnchor.updateEmpties | `animatePosition` |  |  |  | `emptyView.layer?.animatePosition(from: emptyView.frame.origin, to: emptyView.frame.origin.offsetBy(dx: 0, dy: 25), removeOnCompletion: false` |
| `packages/TGUIKit/Sources/TableView.swift:4051` | PendingResizeAnchor.updateEmpties | `_change` |  |  |  | `tableView._change(opacity: 1, animated: animated)` |
| `packages/TGUIKit/Sources/TableView.swift:4196` | PendingResizeAnchor.change | `change` |  | CAMediaTimingFunctionName |  | `public override func change(size: NSSize, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timing` |
| `packages/TGUIKit/Sources/TableView.swift:4207` | PendingResizeAnchor.change | `animateBoundsOriginYAdditive` | duration |  |  | `self.layer?.animateBoundsOriginYAdditive(from: -y, to: 0, duration: duration)` |
| `packages/TGUIKit/Sources/TableView.swift:4221` | PendingResizeAnchor.change | `change` | duration | timingFunction |  | `super.change(size: size, animated: animated, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFunction, com` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:51` | CAAnimation.makeSpringAnimation | `makeSpringAnimation` |  |  | path | `public func makeSpringAnimation(_ path:String) -> CABasicAnimation {` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:52` | CAAnimation.makeSpringAnimation | `CASpringAnimation` |  |  | path | `let springAnimation:CASpringAnimation = CASpringAnimation(keyPath: path)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:53` | CAAnimation.makeSpringAnimation | `.mass =` |  |  |  | `springAnimation.mass = 3.0;` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:54` | CAAnimation.makeSpringAnimation | `.stiffness =` |  |  |  | `springAnimation.stiffness = 1000.0;` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:55` | CAAnimation.makeSpringAnimation | `.damping =` |  |  |  | `springAnimation.damping = 500.0;` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:57` | CAAnimation.makeSpringAnimation | `.duration =` |  |  |  | `springAnimation.duration = 0.5;//springAnimation.settlingDuration;` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:62` | CAAnimation.makeSpringBounceAnimation | `makeSpringBounceAnimation` |  |  | path | `public func makeSpringBounceAnimation(_ path:String, _ initialVelocity:CGFloat, _ damping: CGFloat = 88.0) -> CABasicAnimation {` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:63` | CAAnimation.makeSpringBounceAnimation | `CASpringAnimation` |  |  | path | `let springAnimation:CASpringAnimation = CASpringAnimation(keyPath: path)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:64` | CAAnimation.makeSpringBounceAnimation | `.mass =` |  |  |  | `springAnimation.mass = 5.0` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:65` | CAAnimation.makeSpringBounceAnimation | `.stiffness =` |  |  |  | `springAnimation.stiffness = 900.0` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:66` | CAAnimation.makeSpringBounceAnimation | `.damping =` | springAnimation.settlingDuration |  |  | `springAnimation.damping = damping` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:68` | CAAnimation.makeSpringBounceAnimation | `.duration =` | springAnimation.settlingDuration |  |  | `springAnimation.duration = springAnimation.settlingDuration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:78` | CALayer.makeAnimation | `makeSpringAnimation` |  |  |  | `let animation = makeSpringAnimation(keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:109` | CALayer.makeAnimation | `CABasicAnimation` |  |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:112` | CALayer.makeAnimation | `.duration =` | duration if let |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:136` | CALayer.animate | `animate` | Double | CAMediaTimingFunctionName | String | `func animate(from: AnyObject, to: AnyObject, keyPath: String, timingFunction: CAMediaTimingFunctionName, duration: Double, delay: Double = 0` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:138` | CALayer.animate | `makeSpringAnimation` |  |  |  | `let animation = makeSpringAnimation(keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:167` | CALayer.animate | `CABasicAnimation` |  |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:170` | CALayer.animate | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:188` | CALayer.animateAdditive | `animateAdditive` | Double | CAMediaTimingFunctionName | String | `func animateAdditive(from: NSValue, to: NSValue, keyPath: String, key: String, timingFunction: CAMediaTimingFunctionName, duration: Double, ` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:195` | CALayer.animateAdditive | `CABasicAnimation` |  |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:198` | CALayer.animateAdditive | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:211` | CALayer.animateScaleSpring | `animateScaleSpring` | Double |  | transform | `func animateScaleSpring(from: CGFloat, to: CGFloat, duration: Double, delay: Double = 0, initialVelocity: CGFloat = 0.0, removeOnCompletion:` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:212` | CALayer.animateScaleSpring | `makeSpringBounceAnimation` |  |  | transform | `let animation = bounce ? makeSpringBounceAnimation("transform", initialVelocity) : makeSpringAnimation("transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:255` | CALayer.animateScaleSpringFrom | `animateScaleSpringFrom` | Double |  | transform | `func animateScaleSpringFrom(anchor: NSPoint, from: CGFloat, to: CGFloat, duration: Double, initialVelocity: CGFloat = 0.0, removeOnCompletio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:256` | CALayer.animateScaleSpringFrom | `makeSpringBounceAnimation` |  |  | transform | `let animation = bounce ? makeSpringBounceAnimation("transform", initialVelocity) : makeSpringAnimation("transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:291` | CALayer.animateScaleXCenter | `animateScaleXCenter` | Double | CAMediaTimingFunctionName | transform | `func animateScaleXCenter(from: CGFloat, to: CGFloat, duration: Double, removeOnCompletion: Bool = true, timingFunction: CAMediaTimingFunctio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:292` | CALayer.animateScaleXCenter | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:312` | CALayer.animateScaleXCenter | `.duration =` | duration if let |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:319` | CALayer.animateScaleYCenter | `animateScaleYCenter` | Double | CAMediaTimingFunctionName | transform | `func animateScaleYCenter(from: CGFloat, to: CGFloat, duration: Double, removeOnCompletion: Bool = true, timingFunction: CAMediaTimingFunctio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:320` | CALayer.animateScaleYCenter | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:340` | CALayer.animateScaleYCenter | `.duration =` | duration if let |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:347` | CALayer.animateScaleCenter | `animateScaleCenter` | Double | CAMediaTimingFunctionName | transform | `func animateScaleCenter(from: CGFloat, to: CGFloat, duration: Double, removeOnCompletion: Bool = true, timingFunction: CAMediaTimingFunction` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:348` | CALayer.animateScaleCenter | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:366` | CALayer.animateScaleCenter | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:379` | CALayer.animateScaleCenter | `animateScaleCenter` | Double | CAMediaTimingFunctionName | transform | `func animateScaleCenter(fromX: CGFloat, fromY: CGFloat, to: CGFloat, anchor: NSPoint, duration: Double, removeOnCompletion: Bool = true, tim` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:380` | CALayer.animateScaleCenter | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:398` | CALayer.animateScaleCenter | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:412` | CALayer.animateScaleXCenter | `animateScaleXCenter` | Double | CAMediaTimingFunctionName | transform | `func animateScaleXCenter(from: CGFloat, to: CGFloat, duration: Double, removeOnCompletion: Bool = true, timingFunction: CAMediaTimingFunctio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:413` | CALayer.animateScaleXCenter | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:431` | CALayer.animateScaleXCenter | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:444` | CALayer.animateScaleYCenter | `animateScaleYCenter` | Double | CAMediaTimingFunctionName | transform | `func animateScaleYCenter(from: CGFloat, to: CGFloat, duration: Double, removeOnCompletion: Bool = true, timingFunction: CAMediaTimingFunctio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:445` | CALayer.animateScaleYCenter | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:463` | CALayer.animateScaleYCenter | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:478` | CALayer.animateAlpha | `animateAlpha` | Double | CAMediaTimingFunctionName | opacity | `func animateAlpha(from: CGFloat, to: CGFloat, duration: Double, timingFunction: CAMediaTimingFunctionName = CAMediaTimingFunctionName.easeOu` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:479` | CALayer.animateAlpha | `animate` | duration | timingFunction | opacity | `self.animate(from: NSNumber(value: Float(from)), to: NSNumber(value: Float(to)), keyPath: "opacity", timingFunction: timingFunction, duratio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:482` | CALayer.animateSpring | `animateSpring` | Double |  | String | `func animateSpring(from: AnyObject, to: AnyObject, keyPath: String, duration: Double, initialVelocity: CGFloat = 0.0, damping: CGFloat = 88.` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:485` | CALayer.animateSpring | `makeSpringBounceAnimation` |  |  |  | `animation = makeSpringBounceAnimation(keyPath, initialVelocity, damping)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:487` | CALayer.animateSpring | `makeSpringAnimation` |  |  |  | `animation = makeSpringAnimation(keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:510` | CALayer.animateScale | `animateScale` | Double | CAMediaTimingFunctionName | transform.scale | `func animateScale(from: CGFloat, to: CGFloat, duration: Double, timingFunction: CAMediaTimingFunctionName = CAMediaTimingFunctionName.easeIn` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:511` | CALayer.animateScale | `animate` | duration | timingFunction | transform.scale | `self.animate(from: NSNumber(value: Float(from)), to: NSNumber(value: Float(to)), keyPath: "transform.scale", timingFunction: timingFunction,` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:514` | CALayer.animateScaleX | `animateScaleX` | Double | CAMediaTimingFunctionName | transform.scale.x | `func animateScaleX(from: CGFloat, to: CGFloat, duration: Double, timingFunction: CAMediaTimingFunctionName = CAMediaTimingFunctionName.easeI` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:515` | CALayer.animateScaleX | `animate` | duration | timingFunction | transform.scale.x | `self.animate(from: NSNumber(value: Float(from)), to: NSNumber(value: Float(to)), keyPath: "transform.scale.x", timingFunction: timingFunctio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:518` | CALayer.animateScaleY | `animateScaleY` | Double | CAMediaTimingFunctionName | transform.scale.y | `func animateScaleY(from: CGFloat, to: CGFloat, duration: Double, timingFunction: CAMediaTimingFunctionName = CAMediaTimingFunctionName.easeI` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:519` | CALayer.animateScaleY | `animate` | duration | timingFunction | transform.scale.y | `self.animate(from: NSNumber(value: Float(from)), to: NSNumber(value: Float(to)), keyPath: "transform.scale.y", timingFunction: timingFunctio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:522` | CALayer.animatePosition | `animatePosition` |  | CAMediaTimingFunctionName |  | `func animatePosition(from: NSPoint, to: NSPoint, duration: Double = 0.2, timingFunction: CAMediaTimingFunctionName = CAMediaTimingFunctionNa` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:529` | CALayer.animatePosition | `animate` | duration | timingFunction | position | `self.animate(from: NSValue(point: from), to: NSValue(point: to), keyPath: "position", timingFunction: timingFunction, duration: duration, re` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:532` | CALayer.animateBounds | `animateBounds` |  | CAMediaTimingFunctionName |  | `func animateBounds(from: NSRect, to: NSRect, duration: Double = 0.2, timingFunction: CAMediaTimingFunctionName = CAMediaTimingFunctionName.e` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:539` | CALayer.animateBounds | `animate` | duration | timingFunction | bounds | `self.animate(from: NSValue(rect: from), to: NSValue(rect: to), keyPath: "bounds", timingFunction: timingFunction, duration: duration, remove` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:542` | CALayer.animateBoundsOriginYAdditive | `animateBoundsOriginYAdditive` | Double | CAMediaTimingFunctionName.easeOut | bounds.origin.y | `func animateBoundsOriginYAdditive(from: CGFloat, to: CGFloat, duration: Double, completion: ((Bool) -> Void)? = nil) {` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:543` | CALayer.animateBoundsOriginYAdditive | `animateAdditive` | duration | CAMediaTimingFunctionName.easeOut | bounds.origin.y | `self.animateAdditive(from: from as NSNumber, to: to as NSNumber, keyPath: "bounds.origin.y", key: "boundsOriginYAdditive", timingFunction: C` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:546` | CALayer.animateFrame | `animateFrame` | Double | CAMediaTimingFunctionName |  | `func animateFrame(from: CGRect, to: CGRect, duration: Double, timingFunction: CAMediaTimingFunctionName, removeOnCompletion: Bool = true, ad` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:553` | CALayer.animateFrame | `animatePosition` | duration | timingFunction |  | `self.animatePosition(from: CGPoint(x: from.midX, y: from.midY), to: CGPoint(x: to.midX, y: to.midY), duration: duration, timingFunction: tim` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:554` | CALayer.animateFrame | `animateBounds` | duration | timingFunction |  | `self.animateBounds(from: CGRect(origin: self.bounds.origin, size: from.size), to: CGRect(origin: self.bounds.origin, size: to.size), duratio` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:558` | CALayer.shake | `CABasicAnimation` |  |  | position | `let animation = CABasicAnimation(keyPath: "position")` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:559` | CALayer.shake | `.duration =` |  |  |  | `animation.duration = duration;` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:577` | CALayer.animateKeyframes | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:591` | CALayer.animateKeyframes | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/CAAnimationUtils.swift:613` | CALayer.animateKeyframes | `.duration =` |  |  |  | `animation.duration = duration;` |
| `packages/TGUIKit/Sources/TransformImageView.swift:156` | TransformImageRenderer.setSignal | `animateAlpha` | 0.2 |  |  | `host.transformImageHostLayer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/TransformImageView.swift:158` | TransformImageRenderer.setSignal | `animateContents` |  |  |  | `host.transformImageHostLayer?.animateContents()` |
| `packages/TGUIKit/Sources/TransformImageView.swift:204` | TransformImageRenderer.setSignal | `animateContents` |  |  |  | `let animateContents = !self.first && animate` |
| `packages/TGUIKit/Sources/TransformImageView.swift:209` | TransformImageRenderer.setSignal | `animateAlpha` | 0.2 |  |  | `host.transformImageHostLayer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/TransformImageView.swift:211` | TransformImageRenderer.setSignal | `animateContents` |  |  |  | `if animateContents {` |
| `packages/TGUIKit/Sources/TransformImageView.swift:212` | TransformImageRenderer.setSignal | `animateContents` |  |  |  | `host.transformImageHostLayer?.animateContents()` |
| `packages/TGUIKit/Sources/AppMenuRowItem.swift:698` | AppMenuRowView.set | `_change` |  |  |  | `currentTextView?._change(opacity: item.item.title.isEmpty ? 0 : 1, animated: animated)` |
| `packages/TGUIKit/Sources/SliderView.swift:122` | SliderView._prepareTransition | `CATransition` | duration |  |  | `let transition = CATransition()` |
| `packages/TGUIKit/Sources/SliderView.swift:123` | SliderView._prepareTransition | `.duration =` | duration |  |  | `transition.duration = duration` |
| `packages/TGUIKit/Sources/SliderView.swift:396` | SliderDotsControl.slideDots | `NSAnimationContext.runAnimationGroup` | min(0.2 + Double(count - 1) * |  |  | `NSAnimationContext.runAnimationGroup({ context in` |
| `packages/TGUIKit/Sources/SliderView.swift:397` | SliderDotsControl.slideDots | `.duration =` | min(0.2 + Double(count - 1) * |  |  | `context.duration = min(0.2 + Double(count - 1) * 0.03, 0.35)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1188` | ControllerContainer.show | `_change` | scaledDuration / 3 | .spring |  | `controllerContainer.backdropView._change(opacity: 1, animated: true, duration: scaledDuration / 3, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1191` | ControllerContainer.show | `_change` | scaledDuration | .spring |  | `previousContainer._change(pos: NSMakePoint(pto, previousContainer.frame.minY), animated: true, duration: scaledDuration, timingFunction: .sp` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1217` | ControllerContainer.show | `_change` | scaledDuration | .spring |  | `controllerContainer._change(pos: NSMakePoint(nto, controllerContainer.frame.minY), animated: true, duration: scaledDuration, timingFunction:` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1230` | ControllerContainer.show | `_change` | scaledDuration / 3 | .spring |  | `previousContainer.backdropView._change(opacity: 0, animated: true, duration: scaledDuration / 3, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1510` | ControllerContainer.viewDidAppear | `_change` |  |  |  | `activeContainer._change(pos: NSMakePoint(nPosition, activeContainer.frame.minY), animated: false)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1522` | ControllerContainer.viewDidAppear | `_change` |  |  |  | `previousContainer._change(pos: NSMakePoint(min(previousStart + max(delta, 0) / parallaxDivisor + previousInsetLeft, previousInsetLeft), prev` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1550` | ControllerContainer.viewDidAppear | `_change` | scaledDuration | animationStyle.function |  | `activeContainer._change(pos: NSMakePoint(keepLeft + activeInsetLeft, activeContainer.frame.minY), animated: animated, duration: scaledDurati` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1561` | ControllerContainer.viewDidAppear | `_change` | scaledDuration / 2 | animationStyle.function |  | `activeContainer._change(opacity: 1, animated: animated, duration: scaledDuration / 2, timingFunction: animationStyle.function)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1562` | ControllerContainer.viewDidAppear | `_change` | scaledDuration | animationStyle.function |  | `previousContainer._change(pos: NSMakePoint(previousStart + previousInsetLeft, previousContainer.frame.minY), animated: animated, duration: s` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1618` | ControllerContainer.viewDidAppear | `_change` |  |  |  | `newContainer._change(pos: NSMakePoint(nPosition, newContainer.frame.minY), animated: false)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1620` | ControllerContainer.viewDidAppear | `_change` |  |  |  | `activeContainer._change(pos: NSMakePoint(min(-delta / 3.0 + activeInsetLeft, activeInsetLeft), activeContainer.frame.minY), animated: false)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1646` | ControllerContainer.viewDidAppear | `_change` | scaledDuration | animationStyle.function |  | `newContainer._change(pos: NSMakePoint(self.containerView.frame.width, newContainer.frame.minY), animated: animated, duration: scaledDuration` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1647` | ControllerContainer.viewDidAppear | `_change` | scaledDuration / 3 | animationStyle.function |  | `newContainer.backdropView._change(opacity: 0, animated: animated, duration: scaledDuration / 3, timingFunction: animationStyle.function)` |
| `packages/TGUIKit/Sources/NavigationViewController.swift:1648` | ControllerContainer.viewDidAppear | `_change` | scaledDuration | animationStyle.function |  | `activeContainer._change(pos: NSMakePoint(activeInsetLeft, activeContainer.frame.minY), animated: animated, duration: scaledDuration, timingF` |
| `packages/TGUIKit/Sources/TitleButton.swift:213` | TextLayoutCache.apply | `animateAlpha` | textButtonSubtextDuration | .easeInEaseOut |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: textButtonSubtextDuration, timingFunction: .easeInEaseOut)` |
| `packages/TGUIKit/Sources/TextView.swift:3301` | EmbeddedMaskSnapshot.updateInks | `animateAlpha` | 0.2 | .easeInEaseOut |  | `fake.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeInEaseOut, removeOnCompletion: false, completion: { [weak fake,` |
| `packages/TGUIKit/Sources/TextView.swift:4081` | TextView.setIsShimmering | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/ContainableController.swift:204` | ContainedViewLayoutTransition.updateFrame | `NSAnimationContext.runAnimationGroup` | duration if |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/TGUIKit/Sources/ContainableController.swift:205` | ContainedViewLayoutTransition.updateFrame | `.duration =` | duration if |  |  | `ctx.duration = duration` |
| `packages/TGUIKit/Sources/ContainableController.swift:225` | ContainedViewLayoutTransition.updateFrame | `NSAnimationContext.runAnimationGroup` | duration if |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/TGUIKit/Sources/ContainableController.swift:226` | ContainedViewLayoutTransition.updateFrame | `.duration =` | duration if |  |  | `ctx.duration = duration` |
| `packages/TGUIKit/Sources/ContainableController.swift:250` | ContainedViewLayoutTransition.updateFrame | `NSAnimationContext.runAnimationGroup` | duration if |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/TGUIKit/Sources/ContainableController.swift:251` | ContainedViewLayoutTransition.updateFrame | `.duration =` | duration if |  |  | `ctx.duration = duration` |
| `packages/TGUIKit/Sources/ContainableController.swift:264` | ContainedViewLayoutTransition.updateFrame | `change` | duration | curve.timingFunction |  | `view.change(size: frame.size, animated: true, duration: duration, timingFunction: curve.timingFunction, completion: { completed in` |
| `packages/TGUIKit/Sources/ContainableController.swift:284` | ContainedViewLayoutTransition.updateFrame | `_change` | duration | curve.timingFunction |  | `view._change(size: frame.size, animated: true, duration: duration, timingFunction: curve.timingFunction, completion: { completed in` |
| `packages/TGUIKit/Sources/ContainableController.swift:289` | ContainedViewLayoutTransition.updateFrame | `_change` | duration | curve.timingFunction |  | `view._change(pos: frame.origin, animated: true, duration: duration, timingFunction: curve.timingFunction, completion: { completed in` |
| `packages/TGUIKit/Sources/ContainableController.swift:316` | ContainedViewLayoutTransition.animateSize | `animateBounds` | duration | timingFunction |  | `layer.animateBounds(from: presentBounds, to: frame.size.bounds, duration: duration, timingFunction: timingFunction, completion: completion)` |
| `packages/TGUIKit/Sources/ContainableController.swift:325` | ContainedViewLayoutTransition.animatePos | `animatePosition` | duration | timingFunction |  | `layer.animatePosition(from: presentRect, to: frame.origin, duration: duration, timingFunction: timingFunction, completion: completion)` |
| `packages/TGUIKit/Sources/ContainableController.swift:369` | ContainedViewLayoutTransition.updateTransformScale | `animateScaleSpring` | duration |  |  | `layer.animateScaleSpring(from: previousScale, to: scale, duration: duration, bounce: false, completion: { result in` |
| `packages/TGUIKit/Sources/ContainableController.swift:401` | ContainedViewLayoutTransition.updateAlpha | `NSAnimationContext.runAnimationGroup` | duration if |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/TGUIKit/Sources/ContainableController.swift:402` | ContainedViewLayoutTransition.updateAlpha | `.duration =` | duration if |  |  | `ctx.duration = duration` |
| `packages/TGUIKit/Sources/ContainableController.swift:421` | ContainedViewLayoutTransition.updateAlpha | `animateAlpha` | duration | curve.timingFunction |  | `view.layer?.animateAlpha(from: CGFloat(previousAlpha), to: alpha, duration: duration, timingFunction: curve.timingFunction, completion: { re` |
| `packages/TGUIKit/Sources/ContainableController.swift:447` | ContainedViewLayoutTransition.updateAlpha | `animateAlpha` | duration | curve.timingFunction |  | `layer.animateAlpha(from: CGFloat(previousAlpha), to: alpha, duration: duration, timingFunction: curve.timingFunction, completion: { result i` |
| `packages/TGUIKit/Sources/ContainableController.swift:474` | ContainedViewLayoutTransition.animatePositionWithKeyframes | `animatePositionWithKeyframes` |  |  |  | `func animatePositionWithKeyframes(layer: CALayer, keyframes: [CGPoint], removeOnCompletion: Bool = true, additive: Bool = false, completion:` |
| `packages/TGUIKit/Sources/ParabollicAnimation.swift:16` | .parabollicReactionAnimation | `ContainedViewLayoutTransition.animated` | duration | .linear |  | `let transition = ContainedViewLayoutTransition.animated(duration: duration, curve: .linear)` |
| `packages/TGUIKit/Sources/ParabollicAnimation.swift:20` | .parabollicReactionAnimation | `CABasicAnimation` |  |  | transform.scale | `let animation = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/TGUIKit/Sources/ParabollicAnimation.swift:23` | .parabollicReactionAnimation | `.duration =` | transition.duration / 2 |  |  | `animation.duration = transition.duration / 2` |
| `packages/TGUIKit/Sources/ParabollicAnimation.swift:33` | .parabollicReactionAnimation | `animatePositionWithKeyframes` |  |  |  | `transition.animatePositionWithKeyframes(layer: layer, keyframes: keyFrames, removeOnCompletion: true, completion: { [weak view] completed in` |
| `packages/TGUIKit/Sources/TableAnimationInterface.swift:105` | AnimateItem.animate | `animatePosition` | 0.2 | .easeOut |  | `layer.animatePosition(from: from, to: to, duration: 0.2, timingFunction: .easeOut)` |
| `packages/TGUIKit/Sources/TableAnimationInterface.swift:112` | AnimateItem.animate | `animatePosition` | 0.2 | .easeOut |  | `layer.animatePosition(from: NSMakePoint(0, -height), to: NSZeroPoint, duration: 0.2, timingFunction: .easeOut, additive: true)` |
| `packages/TGUIKit/Sources/TableAnimationInterface.swift:118` | AnimateItem.animate | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/TableAnimationInterface.swift:138` | AnimateItem.scroll | `animateBounds` | 0.2 | CAMediaTimingFunctionName.easeOut |  | `table.contentView.layer?.animateBounds(from: from, to: to, duration: 0.2, timingFunction: CAMediaTimingFunctionName.easeOut)` |
| `packages/TGUIKit/Sources/PieChart.swift:592` | Value.update | `change` |  |  |  | `totalTextView.change(size: value.size, animated: animated)` |
| `packages/TGUIKit/Sources/PieChart.swift:593` | Value.update | `change` |  |  |  | `totalTextView.change(pos: focus(value.size).origin, animated: animated)` |
| `packages/TGUIKit/Sources/PieChart.swift:825` | Value.updateTooltip | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/LinearProgressControl.swift:301` | LinearProgressControl.preparedAnimation | `CABasicAnimation` |  |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/LinearProgressControl.swift:304` | LinearProgressControl.preparedAnimation | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/LinearProgressControl.swift:414` | AppliedPlaybackAnimation.set | `change` |  | timingFunction |  | `scrubber.change(pos: NSMakePoint(max(0, min(containerView.frame.minX + size.width - scrubber.frame.width / 2, containerView.frame.maxX - scr` |
| `packages/TGUIKit/Sources/VoiceBlobView.swift:111` | VoiceBlobView.startAnimating | `animateScaleSpring` | 0.6 |  |  | `mediumBlob.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.6)` |
| `packages/TGUIKit/Sources/VoiceBlobView.swift:112` | VoiceBlobView.startAnimating | `animateScaleSpring` | 0.6 |  |  | `bigBlob.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.6)` |
| `packages/TGUIKit/Sources/VoiceBlobView.swift:123` | VoiceBlobView.stopAnimating | `animateScaleSpring` | 0.6 |  |  | `mediumBlob.layer?.animateScaleSpring(from: 1.0, to: 0.1, duration: 0.6, removeOnCompletion: false, bounce: false)` |
| `packages/TGUIKit/Sources/VoiceBlobView.swift:124` | VoiceBlobView.stopAnimating | `animateScaleSpring` | 0.6 |  |  | `bigBlob.layer?.animateScaleSpring(from: 1.0, to: 0.1, duration: 0.6, removeOnCompletion: false, bounce: false)` |
| `packages/TGUIKit/Sources/ImageView.swift:23` | ImageView. | `animateAlpha` | 0.2 |  |  | `self.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/ImageView.swift:39` | ImageView. | `animateAlpha` | 0.2 |  |  | `self.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/ImageView.swift:118` | ImageView.animate | `CABasicAnimation` | 0.2 |  | contents | `let  animation = CABasicAnimation(keyPath: "contents")` |
| `packages/TGUIKit/Sources/ImageView.swift:119` | ImageView.animate | `.duration =` | 0.2 |  |  | `animation.duration = 0.2` |
| `packages/TGUIKit/Sources/ImageView.swift:128` | ImageView.change | `change` | duration | CAMediaTimingFunctionName |  | `open func change(pos position: NSPoint, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFu` |
| `packages/TGUIKit/Sources/ImageView.swift:129` | ImageView.change | `_change` | duration | timingFunction |  | `super._change(pos: position, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFun` |
| `packages/TGUIKit/Sources/ImageView.swift:132` | ImageView.change | `change` | duration | CAMediaTimingFunctionName |  | `open func change(size: NSSize, animated: Bool, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, timingFunction: C` |
| `packages/TGUIKit/Sources/ImageView.swift:133` | ImageView.change | `_change` | duration | timingFunction |  | `super._change(size: size, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFuncti` |
| `packages/TGUIKit/Sources/ImageView.swift:135` | ImageView.change | `change` | duration | CAMediaTimingFunctionName |  | `open func change(opacity to: CGFloat, animated: Bool = true, _ save:Bool = true, removeOnCompletion: Bool = true, duration:Double = 0.2, tim` |
| `packages/TGUIKit/Sources/ImageView.swift:136` | ImageView.change | `_change` | duration | timingFunction |  | `super._change(opacity: to, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFunct` |
| `packages/TGUIKit/Sources/PeerMediaPlayerAnimationView.swift:69` | PeerMediaPlayerAnimationView.animateToPlaying | `CABasicAnimation` |  |  | transform.scale.y | `let animation = CABasicAnimation(keyPath: "transform.scale.y")` |
| `packages/TGUIKit/Sources/PeerMediaPlayerAnimationView.swift:72` | PeerMediaPlayerAnimationView.animateToPlaying | `.duration =` | 0.25 + |  |  | `animation.duration = 0.25 + 0.25 * randDurationMul` |
| `packages/TGUIKit/Sources/PeerMediaPlayerAnimationView.swift:84` | PeerMediaPlayerAnimationView.animateToPaused | `CABasicAnimation` |  |  | transform.scale.y | `let animation = CABasicAnimation(keyPath: "transform.scale.y")` |
| `packages/TGUIKit/Sources/PeerMediaPlayerAnimationView.swift:87` | PeerMediaPlayerAnimationView.animateToPaused | `.duration =` | 0.25 |  |  | `animation.duration = 0.25` |
| `packages/TGUIKit/Sources/TGClipView.swift:211` | TGClipView.scroll | `NSAnimationContext.runAnimationGroup` | 0.35 let |  |  | `NSAnimationContext.runAnimationGroup({ ctx in` |
| `packages/TGUIKit/Sources/TGClipView.swift:212` | TGClipView.scroll | `.duration =` | 0.35 let |  |  | `ctx.duration = 0.35` |
| `packages/TGUIKit/Sources/SwitchView.swift:56` | SwitchMotion.thumb | `settlingDuration` |  |  |  | `static let settlingDuration = 0.9879858824571184` |
| `packages/TGUIKit/Sources/SwitchView.swift:60` | SwitchMotion.spring | `CASpringAnimation` |  |  | keyPath | `let animation = CASpringAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/SwitchView.swift:62` | SwitchMotion.spring | `.mass =` |  |  |  | `animation.mass = 1` |
| `packages/TGUIKit/Sources/SwitchView.swift:63` | SwitchMotion.spring | `.stiffness =` | settlingDuration |  |  | `animation.stiffness = frequency * frequency` |
| `packages/TGUIKit/Sources/SwitchView.swift:64` | SwitchMotion.spring | `.damping =` | settlingDuration |  |  | `animation.damping = 2 * dampingFraction * frequency` |
| `packages/TGUIKit/Sources/SwitchView.swift:65` | SwitchMotion.spring | `.duration =` | settlingDuration |  |  | `animation.duration = settlingDuration` |
| `packages/TGUIKit/Sources/SwitchView.swift:73` | SwitchMotion.interaction | `CABasicAnimation` | interactionDuration |  | keyPath | `let animation = CABasicAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/SwitchView.swift:74` | SwitchMotion.interaction | `.duration =` | interactionDuration |  |  | `animation.duration = interactionDuration` |
| `packages/TGUIKit/Sources/SwitchView.swift:409` | PendingChange.render | `.duration =` | SwitchMotion.interactionDuration |  | position | `animation.duration = SwitchMotion.interactionDuration` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:229` | State.applyCenterComposedTransform | `CASpringAnimation` |  |  | transform | `let animation = CASpringAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:232` | State.applyCenterComposedTransform | `.mass =` |  |  |  | `animation.mass = spring.mass` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:233` | State.applyCenterComposedTransform | `.stiffness =` |  |  |  | `animation.stiffness = spring.stiffness` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:234` | State.applyCenterComposedTransform | `.damping =` | animation.settlingDuration |  |  | `animation.damping = spring.damping` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:236` | State.applyCenterComposedTransform | `.duration =` | animation.settlingDuration |  |  | `animation.duration = animation.settlingDuration` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:252` | State.applyTransform | `CASpringAnimation` |  |  | transform | `let animation = CASpringAnimation(keyPath: "transform")` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:255` | State.applyTransform | `.mass =` |  |  |  | `animation.mass = spring.mass` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:256` | State.applyTransform | `.stiffness =` |  |  |  | `animation.stiffness = spring.stiffness` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:257` | State.applyTransform | `.damping =` | animation.settlingDuration |  |  | `animation.damping = spring.damping` |
| `packages/TGUIKit/Sources/GlassTouchEffect.swift:259` | State.applyTransform | `.duration =` | animation.settlingDuration |  |  | `animation.duration = animation.settlingDuration` |
| `packages/TGUIKit/Sources/TooltipController.swift:60` | TooltipView.move | `change` |  |  |  | `cornerView.change(pos: point, animated: animated)` |
| `packages/TGUIKit/Sources/TooltipController.swift:115` | TooltipView.update | `animate` | 0.2 | .easeOut | cornerRadius | `layer.animate(from: NSNumber(value: Float(layer.cornerRadius)), to: NSNumber(value: Float(radius)), keyPath: "cornerRadius", timingFunction:` |
| `packages/TGUIKit/Sources/TooltipController.swift:118` | TooltipView.update | `change` |  |  |  | `textContainer.change(size: containerSize, animated: animated)` |
| `packages/TGUIKit/Sources/TooltipController.swift:119` | TooltipView.update | `change` |  |  |  | `change(size: NSMakeSize(textContainer.frame.width, textContainer.frame.height + 14), animated: animated)` |
| `packages/TGUIKit/Sources/TooltipController.swift:228` | TooltipController.tooltip | `change` |  |  |  | `tooltip.change(pos: pos, animated: isExists \|\| animated)` |
| `packages/TGUIKit/Sources/TooltipController.swift:258` | TooltipController.tooltip | `animateAlpha` | 0.2 |  |  | `tooltip.layer?.animateAlpha(from: 0.3, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/TooltipController.swift:259` | TooltipController.tooltip | `animatePosition` |  |  |  | `tooltip.layer?.animatePosition(from: NSMakePoint(tooltip.frame.minX, tooltip.frame.minY - 5), to: tooltip.frame.origin)` |
| `packages/TGUIKit/Sources/TooltipController.swift:267` | TooltipController.tooltip | `animatePosition` | 0.2 |  |  | `tooltip.layer?.animatePosition(from: tooltip.frame.origin, to: NSMakePoint(tooltip.frame.minX, tooltip.frame.minY - 5), removeOnCompletion: ` |
| `packages/TGUIKit/Sources/TooltipController.swift:269` | TooltipController.tooltip | `animateAlpha` | 0.2 |  |  | `tooltip.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak tooltip, weak window] _ in` |
| `packages/TGUIKit/Sources/VisualEffectView.swift:105` | VisualEffect.change | `change` | duration | CAMediaTimingFunctionName |  | `public func change(size: NSSize, animated: Bool, _ save: Bool = true, removeOnCompletion: Bool = true, duration: Double = 0.2, timingFunctio` |
| `packages/TGUIKit/Sources/VisualEffectView.swift:107` | VisualEffect.change | `_change` | duration | timingFunction |  | `self._change(size: size, animated: animated, save, removeOnCompletion: removeOnCompletion, duration: duration, timingFunction: timingFunctio` |
| `packages/TGUIKit/Sources/VisualEffectView.swift:118` | VisualEffect.animate | `animateBounds` | duration | timingFunction |  | `layer.animateBounds(from: presentBounds, to: NSMakeRect(0, 0, size.width, size.height), duration: duration, timingFunction: timingFunction, ` |
| `packages/TGUIKit/Sources/SelectingControl.swift:70` | SelectingControl.set | `animateAlpha` | 0.2 |  |  | `selectedLayer.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/SelectingControl.swift:71` | SelectingControl.set | `animateScaleSpring` | 0.3 |  |  | `selectedLayer.animateScaleSpring(from: 0.2, to: 1.0, duration: 0.3)` |
| `packages/TGUIKit/Sources/SelectingControl.swift:76` | SelectingControl.set | `animateScaleSpring` | 0.3 |  |  | `selectedLayer.animateScaleSpring(from: 1, to: 0.2, duration: 0.3, removeOnCompletion: false)` |
| `packages/TGUIKit/Sources/SelectingControl.swift:77` | SelectingControl.set | `animateAlpha` | 0.2 |  |  | `selectedLayer.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak selectedLayer] _ in` |
| `packages/TGUIKit/Sources/StackedBarView.swift:105` | StackedBarView.change | `change` |  |  |  | `public func change(opacity: CGFloat, for button: ImageButton, animated: Bool = true) {` |
| `packages/TGUIKit/Sources/StackedBarView.swift:106` | StackedBarView.change | `change` |  |  |  | `button.change(opacity: opacity, animated: animated)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:70` | TokenView.change | `change` |  | CAMediaTimingFunctionName |  | `override func change(size: NSSize, animated: Bool = true, _ save: Bool = true, removeOnCompletion: Bool = false, duration: Double = 0.2, tim` |
| `packages/TGUIKit/Sources/TokenizedView.swift:75` | TokenView.change | `change` | duration | timingFunction |  | `super.change(size: size, animated: animated, save, duration: duration, timingFunction: timingFunction)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:78` | TokenView.change | `change` |  |  |  | `dismiss.change(pos: NSMakePoint(frame.width - 5 - dismiss.frame.width, point.minY), animated: animated)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:234` | Theme.removeTokens | `change` |  |  |  | `view.change(opacity: 0, animated: animated, completion: { [weak view] completed in` |
| `packages/TGUIKit/Sources/TokenizedView.swift:264` | Theme.layoutContainer | `change` | 0.2 |  |  | `token.change(pos: point, animated: token.immediatlyPaste ? false : animated)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:266` | Theme.layoutContainer | `animateAlpha` | 0.2 |  |  | `token.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:285` | Theme.layoutContainer | `change` |  |  |  | `placeholder.change(pos: NSMakePoint(point.x + 6, point.y + 3), animated: animated)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:286` | Theme.layoutContainer | `change` |  |  |  | `placeholder.change(opacity: tokens.isEmpty ? 1.0 : 0.0, animated: animated)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:289` | Theme.layoutContainer | `change` |  |  |  | `container.change(size: NSMakeSize(container.frame.width, contentHeight), animated: animated)` |
| `packages/TGUIKit/Sources/TokenizedView.swift:294` | Theme.layoutContainer | `_change` |  |  |  | `_change(size: NSMakeSize(mainw, height), animated: animated)` |
| `packages/TGUIKit/Sources/TableRowResizeAnchor.swift:67` | TableRowResizeAnchor.pin | `animatePosition` | duration | curve.timingFunction |  | `layer.animatePosition(from: NSMakePoint(0, shift), to: .zero, duration: duration, timingFunction: curve.timingFunction, additive: true)` |
| `packages/TGUIKit/Sources/TableRowResizeAnchor.swift:75` | TableRowResizeAnchor.pin | `CABasicAnimation` |  |  | position | `let animation = CABasicAnimation(keyPath: "position")` |
| `packages/TGUIKit/Sources/TableRowResizeAnchor.swift:79` | TableRowResizeAnchor.pin | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/TabBarController.swift:120` | TabBarController.didChange | `animateAlpha` | 0.15 |  |  | `current.view.layer?.animateAlpha(from: 1, to: 0, duration: 0.15, removeOnCompletion: false, completion: { [weak self, weak current] _ in` |
| `packages/TGUIKit/Sources/TabBarController.swift:137` | TabBarController.didChange | `animateAlpha` | 0.15 |  |  | `item.controller.view.layer?.animateAlpha(from: 0, to: 1, duration: 0.15)` |
| `packages/TGUIKit/Sources/AppMenuController.swift:200` | Entry.bubbleKeyframe | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/TGUIKit/Sources/AppMenuController.swift:203` | Entry.bubbleKeyframe | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/AppMenuController.swift:645` | Key.close | `animateAlpha` | duration |  |  | `panel?.view.layer?.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false, completion: { _ in` |
| `packages/TGUIKit/Sources/AppMenuController.swift:660` | Key.close | `animateAlpha` | duration |  |  | `view.layer?.animateAlpha(from: 1, to: 0, duration: duration, removeOnCompletion: false, completion: { [weak view, weak window] completed in` |
| `packages/TGUIKit/Sources/AppMenuController.swift:807` | Key.cancelSubmenuNow | `animateAlpha` | 0.2 |  |  | `submenu.view.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak submenu] _ in` |
| `packages/TGUIKit/Sources/AppMenuController.swift:947` | Key.activate | `animateAlpha` | 0.2 |  |  | `view.view.layer?.animateAlpha(from: 0.1, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/AppMenuController.swift:966` | Key.activate | `animateAlpha` | 0.2 |  |  | `window.contentView?.layer?.animateAlpha(from: 0.1, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/AppMenuController.swift:967` | Key.activate | `animateScaleSpringFrom` | 0.28 |  |  | `window.contentView?.layer?.animateScaleSpringFrom(anchor: NSMakePoint(anchor.x, rect.height / 2), from: 0.2, to: 1, duration: 0.28, bounce: ` |
| `packages/TGUIKit/Sources/SectionViewController.swift:335` | Gesture.settle | `_change` | duration | .spring |  | `sections[index].controller.view._change(pos: pageFrame(index).origin, animated: true, duration: duration, timingFunction: .spring)` |
| `packages/TGUIKit/Sources/SectionViewController.swift:337` | Gesture.settle | `_change` | duration | .spring |  | `sections[target].controller.view._change(pos: pageFrame(target).origin, animated: true, duration: duration, timingFunction: .spring, complet` |
| `packages/TGUIKit/Sources/LoginErrorStateView.swift:38` | LoginErrorStateView. | `animateAlpha` | 0.2 |  |  | `self?.layer?.animateAlpha(from: 1, to: 0, duration: 0.2)` |
| `packages/TGUIKit/Sources/LoginErrorStateView.swift:44` | LoginErrorStateView. | `animateAlpha` | 0.2 |  |  | `self?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:37` | LiquidGlassLensAnimation.update | `CABasicAnimation` | duration |  | key | `animation = CABasicAnimation(keyPath: key)` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:38` | LiquidGlassLensAnimation.update | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:41` | LiquidGlassLensAnimation.update | `CASpringAnimation` |  |  | key | `let spring = CASpringAnimation(keyPath: key)` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:42` | LiquidGlassLensAnimation.update | `.mass =` |  |  |  | `spring.mass = 3` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:43` | LiquidGlassLensAnimation.update | `.stiffness =` | 0.5 |  |  | `spring.stiffness = 1000` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:44` | LiquidGlassLensAnimation.update | `.damping =` | 0.5 |  |  | `spring.damping = 500` |
| `packages/TGUIKit/Sources/LiquidGlassLens/LensAnimation.swift:45` | LiquidGlassLensAnimation.update | `.duration =` | 0.5 |  |  | `spring.duration = 0.5` |

## Telegram-Mac (3)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `Telegram-Mac/app/MainViewController.swift:60` | UpdateTabView.updateContent | `change` |  |  |  | `shimmer.change(opacity: isInstalling ? 0 : 1, animated: animated)` |
| `Telegram-Mac/app/MainViewController.swift:65` | UpdateTabView.updateContent | `change` |  | .spring |  | `change(size: NSMakeSize(preferredWidth, frame.height), animated: animated, timingFunction: .spring)` |
| `Telegram-Mac/app/MainViewController.swift:66` | UpdateTabView.updateContent | `change` |  | .spring |  | `change(pos: NSMakePoint(superview.bounds.focus(frame.size).minX, frame.minY), animated: animated, timingFunction: .spring)` |

## TelegramMedia (4)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/TelegramMedia/Sources/AudioWaveformView.swift:198` | AudioWaveformView.updateForegroundClip | `animateBounds` | 0.2 | .easeOut |  | `foregroundClippingLayer.animateBounds(from: previous, to: target, duration: 0.2, timingFunction: .easeOut)` |
| `packages/TelegramMedia/Sources/LottiePlayer.swift:2221` | LottiePlayerView.removeFrozenLayer | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak layer] _ in` |
| `packages/TelegramMedia/Sources/LottiePlayer.swift:2409` | LottiePlayerView.set | `animateAlpha` | 0.2 |  |  | `fallback.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TelegramMedia/Sources/LottiePlayer.swift:2455` | LottiePlayerView.set | `animateAlpha` | 0.2 |  |  | `view.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |

## TelegramMediaUtils (2)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/TelegramMediaUtils/Sources/TelegramMediaUtils/StickerPreviewHandler.swift:184` | PreviewModalView.update | `animateScaleSpring` | 0.2 |  |  | `current?.layer?.animateScaleSpring(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak current] completed in` |
| `packages/TelegramMediaUtils/Sources/TelegramMediaUtils/StickerPreviewHandler.swift:201` | PreviewModalView.update | `animateScaleSpring` | 0.2 |  |  | `contentView?.layer?.animateScaleSpring(from: 0.5, to: 1.0, duration: 0.2)` |

## TelegramShare (16)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `TelegramShare/SELottiePlayer.swift:1387` | SE_LottiePlayerView.set | `animateAlpha` | 0.2 |  |  | `fallback.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `TelegramShare/SELottiePlayer.swift:1400` | SE_LottiePlayerView.set | `animateAlpha` | 0.2 |  |  | `view.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak view] _ in` |
| `TelegramShare/SESelectController.swift:180` | SelectAccountView.layout | `animateAlpha` | 0.2 |  |  | `self.container.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `TelegramShare/SESelectController.swift:181` | SelectAccountView.layout | `animateScaleSpringFrom` | 0.2 |  |  | `self.container.layer?.animateScaleSpringFrom(anchor: NSMakePoint(container.frame.width, 0), from: 0.1, to: 1, duration: 0.2, bounce: false)` |
| `TelegramShare/SESelectController.swift:200` | SelectAccountView.layout | `change` | 0.2 | .spring |  | `self?.change(opacity: 0, animated: true, removeOnCompletion: false, duration: 0.2, timingFunction: .spring, completion: { [weak self] comple` |
| `TelegramShare/SESelectController.swift:296` | ShareModalView.layout | `change` |  |  |  | `cancelView.change(opacity: 1, animated: false)` |
| `TelegramShare/SESelectController.swift:297` | ShareModalView.layout | `change` |  |  |  | `backButton.change(opacity: 0, animated: false)` |
| `TelegramShare/SESelectController.swift:459` | ForumTopicArguments.push | `animatePosition` | 0.35 | .spring |  | `view.layer?.animatePosition(from: NSMakePoint(oneOfThrid * 2, view.frame.minY), to: view.frame.origin, duration: 0.35, timingFunction: .spri` |
| `TelegramShare/SESelectController.swift:460` | ForumTopicArguments.push | `animatePosition` | 0.35 | .spring |  | `sourceView.layer?.animatePosition(from: sourceView.frame.origin, to: NSMakePoint(-oneOfThrid, sourceView.frame.minY), duration: 0.35, timing` |
| `TelegramShare/SESelectController.swift:466` | ForumTopicArguments.pop | `animatePosition` | 0.35 | .spring |  | `view.layer?.animatePosition(from: tableView.frame.origin, to: NSMakePoint(frame.width, view.frame.minY), duration: 0.35, timingFunction: .sp` |
| `TelegramShare/SESelectController.swift:469` | ForumTopicArguments.pop | `animatePosition` | 0.35 | .spring |  | `sourceView.layer?.animatePosition(from: NSMakePoint(-oneOfThrid, sourceView.frame.minY), to: sourceView.frame.origin, duration: 0.35, timing` |
| `TelegramShare/SESelectController.swift:496` | ForumTopicArguments.updateNavigationButtons | `change` |  |  |  | `backButton.change(opacity: inDestinationMode ? 1 : 0, animated: true)` |
| `TelegramShare/SESelectController.swift:497` | ForumTopicArguments.updateNavigationButtons | `change` |  |  |  | `cancelView.change(opacity: inDestinationMode ? 0 : 1, animated: true)` |
| `TelegramShare/SESelectController.swift:538` | ForumTopicArguments.updateWithAccounts | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `TelegramShare/SESelectController.swift:634` | ShareObject.requestIfNeeded | `animateAlpha` | 0.35 |  |  | `self.progressView.layer?.animateAlpha(from: 0, to: 1, duration: 0.35)` |
| `TelegramShare/ShareViewController.swift:164` | ShareViewController.launchExtension | `animateAlpha` | 0.2 |  |  | `context.rootController.view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |

## TelegramTheme (1)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/TelegramTheme/Sources/TelegramTheme/Appearance.swift:2256` | .telegramUpdateTheme | `change` | 0.2 |  |  | `imageView.change(opacity: 0, animated: true, removeOnCompletion: false, duration: 0.2, completion: { [weak imageView] completed in` |

## TextRecognizing (13)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/TextRecognizing/Sources/TextRecognizing/BarcodeOverlay.swift:209` | Chip.reveal | `animateAlpha` | 0.15 |  |  | `layer.animateAlpha(from: from, to: 1, duration: 0.15)` |
| `packages/TextRecognizing/Sources/TextRecognizing/BarcodeOverlay.swift:211` | Chip.reveal | `animateScaleSpring` | 0.3 |  |  | `layer.animateScaleSpring(from: 0.9, to: 1, duration: 0.3, bounce: false)` |
| `packages/TextRecognizing/Sources/TextRecognizing/BarcodeOverlay.swift:215` | Chip.reveal | `animateAlpha` | 0.15 |  |  | `layer.animateAlpha(from: from, to: 0, duration: 0.15, completion: { [weak self] _ in` |
| `packages/TextRecognizing/Sources/TextRecognizing/BarcodeOverlay.swift:244` | Chip.updateHighlight | `animateAlpha` | 0.15 |  |  | `area.outline.animateAlpha(from: from, to: highlighted ? 1 : 0, duration: 0.15)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:85` | DrawingTextLayer.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:111` | DrawingTextLayer.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:129` | DrawingTextLayer.set | `animateAlpha` | 0.2 |  |  | `current.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:372` | DrawingTextLayer.set | `change` |  |  |  | `self.linearProgress.change(opacity: 1)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:374` | DrawingTextLayer.set | `change` |  |  |  | `self.linearProgress.change(opacity: 0)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:454` | DrawingTextLayer.showLiftedSubject | `animateAlpha` | 0.25 |  |  | `dim.animateAlpha(from: 0, to: 1, duration: 0.25)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:455` | DrawingTextLayer.showLiftedSubject | `animateScaleSpring` | 0.4 |  | shadowOpacity | `subject.animateScaleSpring(from: 1, to: 1.04, duration: 0.4, removeOnCompletion: false, bounce: true, center: false)` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:457` | DrawingTextLayer.showLiftedSubject | `CAKeyframeAnimation` |  |  | shadowOpacity | `let glow = CAKeyframeAnimation(keyPath: "shadowOpacity")` |
| `packages/TextRecognizing/Sources/TextRecognizing/ImageTextSelector.swift:468` | DrawingTextLayer.showLiftedSubject | `animateAlpha` | 0.25 |  |  | `container.animateAlpha(from: 1, to: 0, duration: 0.25, removeOnCompletion: false, completion: { [weak self, weak container] _ in` |

## TranslateUI (10)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:263` | TranslateTabItemView.set | `change` |  |  |  | `activeTextView.change(opacity: selected ? 1 : 0, animated: animated)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:264` | TranslateTabItemView.set | `change` |  |  |  | `inactiveTextView.change(opacity: !selected ? 1 : 0, animated: animated)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:341` | TranslateTabRowView.set | `change` |  |  |  | `pill.change(pos: NSMakePoint(pillX, 3), animated: true)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:342` | TranslateTabRowView.set | `change` |  |  |  | `pill.change(size: NSMakeSize(pillW, pillH), animated: false)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:492` | StyleEmojiItemView.set | `change` |  |  |  | `activeLabel.change(opacity: selected ? 1 : 0, animated: animated)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:493` | StyleEmojiItemView.set | `change` |  |  |  | `inactiveLabel.change(opacity: !selected ? 1 : 0, animated: animated)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:661` | StyleEmojiRowView.updateItemLayout | `change` |  |  |  | `pill.change(pos: NSMakePoint(pillX, 3), animated: true)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:662` | StyleEmojiRowView.updateItemLayout | `change` |  |  |  | `pill.change(size: NSMakeSize(pillW, pillH), animated: false)` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:675` | StyleEmojiRowView.updateItemLayout | `NSAnimationContext.runAnimationGroup` | 0.2 |  |  | `NSAnimationContext.runAnimationGroup { ctx in` |
| `packages/TranslateUI/Sources/TranslateUI/TranslateModalController.swift:676` | StyleEmojiRowView.updateItemLayout | `.duration =` | 0.2 |  |  | `ctx.duration = 0.2` |

## UniqueGiftBackground (6)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/UniqueGiftBackground/Sources/UniqueGiftBackground/UniqueGiftBackgroundView.swift:160` | UniqueGiftBackgroundLayer.update | `CATransition` | 0.25 |  |  | `let transition = CATransition()` |
| `packages/UniqueGiftBackground/Sources/UniqueGiftBackground/UniqueGiftBackgroundView.swift:162` | UniqueGiftBackgroundLayer.update | `.duration =` | 0.25 |  |  | `transition.duration = 0.25` |
| `packages/UniqueGiftBackground/Sources/UniqueGiftBackground/UniqueGiftBackgroundView.swift:284` | UniqueGiftBackgroundLayer.show | `CATransition` | 0.25 |  |  | `let transition = CATransition()` |
| `packages/UniqueGiftBackground/Sources/UniqueGiftBackground/UniqueGiftBackgroundView.swift:286` | UniqueGiftBackgroundLayer.show | `.duration =` | 0.25 |  |  | `transition.duration = 0.25` |
| `packages/UniqueGiftBackground/Sources/UniqueGiftBackground/UniqueGiftBackgroundView.swift:343` | UniqueGiftBackgroundLayer.animatePatternTransition | `CAKeyframeAnimation` |  |  | transform.scale | `let animation = CAKeyframeAnimation(keyPath: "transform.scale")` |
| `packages/UniqueGiftBackground/Sources/UniqueGiftBackground/UniqueGiftBackgroundView.swift:346` | UniqueGiftBackgroundLayer.animatePatternTransition | `.duration =` | 0.4 |  |  | `animation.duration = 0.4` |

## WalletUI (68)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/WalletUI/Sources/WalletUI/WalletTransactionController.swift:556` | WalletTransactionCommentRowItem.walletCommentReplace | `animateAlpha` | duration | curve.timingFunction |  | `layer.animateAlpha(from: opacityFrom, to: opacityTo, duration: duration, timingFunction: curve.timingFunction, completion: { _ in` |
| `packages/WalletUI/Sources/WalletUI/WalletTransactionController.swift:559` | WalletTransactionCommentRowItem.walletCommentReplace | `animateScaleCenter` | duration | curve.timingFunction |  | `layer.animateScaleCenter(from: appearing ? walletCommentReplaceScale : 1, to: appearing ? 1 : walletCommentReplaceScale, duration: duration,` |
| `packages/WalletUI/Sources/WalletUI/WalletTransactionController.swift:563` | WalletTransactionCommentRowItem.walletCommentReplace | `animate` | duration | curve.timingFunction | filters.gaussianBlur.inputRadius | `layer.animate(from: blurFrom as NSNumber, to: blurTo as NSNumber, keyPath: "filters.gaussianBlur.inputRadius", timingFunction: curve.timingF` |
| `packages/WalletUI/Sources/WalletUI/WalletTransactionRowItem.swift:686` | WalletTransactionRowView.set | `animateContents` |  |  |  | `amountIconView.layer?.animateContents()` |
| `packages/WalletUI/Sources/WalletUI/WalletCollectables.swift:1629` | WalletCardStickerLayer.apply | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletSendRatePillRowItem.swift:251` | WalletSendRatePillRowView.setShown | `CABasicAnimation` |  |  | opacity | `let opacity = CABasicAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletSendRatePillRowItem.swift:257` | WalletSendRatePillRowView.setShown | `CABasicAnimation` |  |  | transform | `let transform = CABasicAnimation(keyPath: "transform")` |
| `packages/WalletUI/Sources/WalletUI/WalletCollectibleDetailsController.swift:623` | WalletCollectibleActionControl.viewClass | `change` |  |  |  | `control.change(opacity: 0.8, animated: true)` |
| `packages/WalletUI/Sources/WalletUI/WalletCollectibleDetailsController.swift:626` | WalletCollectibleActionControl.viewClass | `change` |  |  |  | `control.change(opacity: 1.0, animated: true)` |
| `packages/WalletUI/Sources/WalletUI/WalletCollectibleDetailsController.swift:629` | WalletCollectibleActionControl.viewClass | `change` |  |  |  | `control.change(opacity: 1.0, animated: true)` |
| `packages/WalletUI/Sources/WalletUI/WalletPeerBalanceController.swift:211` | WalletPeerBalanceView.setNoticeVisible | `animateAlpha` |  |  |  | `ownershipBubble.layer?.animateAlpha(from: CGFloat(previous), to: visible ? 1 : 0, duration: visible ? 0.2 : 0.06)` |
| `packages/WalletUI/Sources/WalletUI/WalletPeerBalanceController.swift:329` | WalletPeerBalanceView.animateOut | `animateAlpha` | 0.15 |  |  | `self.layer?.animateAlpha(from: 1, to: 0, duration: 0.15, removeOnCompletion: false, completion: { _ in completion() })` |
| `packages/WalletUI/Sources/WalletUI/WalletPeerBalanceController.swift:514` | WalletPeerBalanceController.viewWillDisappear | `animateAlpha` | 0.25 |  |  | `backdrop.layer?.animateAlpha(from: CGFloat(opacity), to: 0, duration: 0.25)` |
| `packages/WalletUI/Sources/WalletUI/WalletCardEffects.swift:709` | WalletCardEffectsLayers.installTwinkle | `CABasicAnimation` |  |  | transform.scale | `let animation = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardEffects.swift:712` | WalletCardEffectsLayers.installTwinkle | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletDigitRoll.swift:212` | Column.play | `CAKeyframeAnimation` |  |  | transform | `let transform = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/WalletUI/Sources/WalletUI/WalletDigitRoll.swift:216` | Column.play | `CAKeyframeAnimation` |  |  | opacity | `let opacity = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletDigitRoll.swift:219` | Column.play | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletOpenIntro.swift:169` | WalletAddressReveal.addFade | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveQrRevealView.swift:105` | WalletReceiveQrRevealView.animateIn | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveQrRevealView.swift:121` | WalletReceiveQrRevealView.animateIn | `makeSpringAnimation` |  |  | transform.scale | `let grow = makeSpringAnimation("transform.scale")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveQrRevealView.swift:128` | WalletReceiveQrRevealView.animateIn | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletStickerTrashView.swift:55` | WalletStickerTrashView.setShown | `change` | 0.2 |  |  | `change(opacity: shown ? 1 : 0, animated: true, duration: 0.2)` |
| `packages/WalletUI/Sources/WalletUI/WalletStickerTrashView.swift:65` | WalletStickerTrashView.setHot | `change` | 0.2 | .easeOut |  | `textView.change(opacity: hot ? 1 : 0, animated: true, duration: 0.2)` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:454` | WalletAmountRowItem.walletAmountApplyBlur | `CABasicAnimation` |  |  | filters.gaussianBlur.inputRadius | `let animation = CABasicAnimation(keyPath: "filters.gaussianBlur.inputRadius")` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:457` | WalletAmountRowItem.walletAmountApplyBlur | `.duration =` | walletAmountCurrencyDuration |  |  | `animation.duration = walletAmountCurrencyDuration` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:546` | WalletAmountSymbolTransition.walletAmountAnimateCurrencyChange | `animateAlpha` | walletAmountCurrencyDuration |  |  | `layer.animateAlpha(from: 0.0, to: CGFloat(layer.opacity), duration: walletAmountCurrencyDuration)` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1597` | Layout.inputRejected | `CAKeyframeAnimation` |  |  | transform.translation.x | `let animation = CAKeyframeAnimation(keyPath: "transform.translation.x")` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1604` | Layout.inputRejected | `.duration =` | 0.42 |  |  | `animation.duration = 0.42` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1719` | Layout.switchSymbols | `CAKeyframeAnimation` |  |  | transform | `let transform = CAKeyframeAnimation(keyPath: "transform")` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1721` | Layout.switchSymbols | `CAKeyframeAnimation` |  |  | opacity | `let opacity = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1723` | Layout.switchSymbols | `CAKeyframeAnimation` |  |  | filters.gaussianBlur.inputRadius | `let blur = CAKeyframeAnimation(keyPath: "filters.gaussianBlur.inputRadius")` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1727` | Layout.switchSymbols | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1743` | Layout.switchSymbols | `.duration =` | duration |  |  | `group.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletAmountRowItem.swift:1796` | Layout.pulseSymbols | `CAKeyframeAnimation` |  |  | sublayerTransform | `let pulse = CAKeyframeAnimation(keyPath: "sublayerTransform")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1454` | WalletCardView.walletCardEmphasize | `CABasicAnimation` |  |  | shadowOpacity | `let animation = CABasicAnimation(keyPath: "shadowOpacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1457` | WalletCardView.walletCardEmphasize | `.duration =` | 0.45 |  |  | `animation.duration = 0.45` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1508` | WalletCardView.setStickerHint | `CABasicAnimation` |  |  | lineDashPhase | `let march = CABasicAnimation(keyPath: "lineDashPhase")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1516` | WalletCardView.setStickerHint | `animateAlpha` | 0.35 |  |  | `if !wasVisible { stickerHintLayer.animateAlpha(from: 0, to: 1, duration: 0.35) }` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1520` | WalletCardView.setStickerHint | `animateAlpha` | 0.2 |  |  | `if wasVisible { stickerHintLayer.animateAlpha(from: 1, to: 0, duration: 0.2) }` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1671` | WalletCardView.setStickerGrow | `CABasicAnimation` |  |  | transform | `let animation = CABasicAnimation(keyPath: "transform")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:1674` | WalletCardView.setStickerGrow | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2142` | WalletCardStickerSelectionLayer.setShown | `CABasicAnimation` |  |  | opacity | `let fade = CABasicAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2149` | WalletCardStickerSelectionLayer.setShown | `CABasicAnimation` |  |  | transform.scale | `let grow = CABasicAnimation(keyPath: "transform.scale")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2366` | WalletChatCardShimmerView.animateBand | `CAKeyframeAnimation` |  |  | keyPath | `let animation = CAKeyframeAnimation(keyPath: keyPath)` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2370` | WalletChatCardShimmerView.animateBand | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2373` | WalletChatCardShimmerView.animateBand | `CAKeyframeAnimation` |  |  | opacity | `let opacity = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2382` | WalletChatCardShimmerView.animateBand | `.duration =` | duration |  |  | `group.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletCardView.swift:2621` | BackgroundRotationAnimation.setAwaitingTransferFlight | `animateAlpha` | 0.15 |  |  | `gramDiamondView.layer?.animateAlpha(from: 0, to: 1, duration: 0.15)` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:285` | Layout.applyAnimations | `CAKeyframeAnimation` |  |  | position | `let animation = CAKeyframeAnimation(keyPath: "position")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:289` | Layout.applyAnimations | `.duration =` | duration |  |  | `animation.duration = duration` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:733` | RingGlyphItem.animateCardFlip | `CAKeyframeAnimation` | Self.cardFlipDuration |  | transform.scale | `let scale = CAKeyframeAnimation(keyPath: "transform.scale")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:740` | RingGlyphItem.animateCardFlip | `CAKeyframeAnimation` | Self.cardFlipDuration |  | opacity | `let shade = CAKeyframeAnimation(keyPath: "opacity")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:750` | RingGlyphItem.animateCardFlip | `CABasicAnimation` |  |  | transform.rotation.y | `let rotation = CABasicAnimation(keyPath: "transform.rotation.y")` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:1082` | RingGlyphItem.set | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:1084` | RingGlyphItem.set | `_change` | 0.2 |  |  | `copiedView._change(opacity: item.displaysAddress ? 1 : 0, animated: true, duration: 0.2)` |
| `packages/WalletUI/Sources/WalletUI/WalletReceiveController.swift:1085` | RingGlyphItem.set | `animateAlpha` | 0.2 |  |  | `actionButton.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WalletUI/Sources/WalletUI/WalletTransactionAmountRowItem.swift:283` | WalletPendingAmountShimmerView.addAnimation | `CABasicAnimation` |  |  | position.x | `let animation = CABasicAnimation(keyPath: "position.x")` |
| `packages/WalletUI/Sources/WalletUI/WalletTransactionAmountRowItem.swift:287` | WalletPendingAmountShimmerView.addAnimation | `.duration =` | 1.0 |  |  | `animation.duration = 1.0` |
| `packages/WalletUI/Sources/WalletUI/WalletGiftDepositConfirmationRowItem.swift:138` | WalletGiftDepositConfirmationRowView.set | `animateAlpha` | 0.2 |  |  | `feeView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WalletUI/Sources/WalletUI/WalletGramTooltip.swift:209` | WalletGramTooltipView.animateIn | `animateSpring` | 0.4 | .easeInEaseOut | transform.scale | `layer?.animateSpring(from: NSNumber(value: 0.01), to: NSNumber(value: 1.0), keyPath: "transform.scale", duration: 0.4, damping: 105)` |
| `packages/WalletUI/Sources/WalletUI/WalletGramTooltip.swift:210` | WalletGramTooltipView.animateIn | `animateSpring` | 0.4 | .easeInEaseOut | position | `layer?.animateSpring(from: NSValue(point: arrowOffset), to: NSValue(point: .zero), keyPath: "position", duration: 0.4, damping: 105, additiv` |
| `packages/WalletUI/Sources/WalletUI/WalletGramTooltip.swift:211` | WalletGramTooltipView.animateIn | `animateAlpha` | 0.2 | .easeInEaseOut |  | `layer?.animateAlpha(from: 0, to: 1, duration: 0.2, timingFunction: .easeInEaseOut)` |
| `packages/WalletUI/Sources/WalletUI/WalletGramTooltip.swift:215` | WalletGramTooltipView.animateOut | `animateScale` | 0.2 | .easeInEaseOut |  | `layer?.animateScale(from: 1, to: 0.01, duration: 0.2, removeOnCompletion: false)` |
| `packages/WalletUI/Sources/WalletUI/WalletGramTooltip.swift:216` | WalletGramTooltipView.animateOut | `animatePosition` | 0.2 | .easeInEaseOut |  | `layer?.animatePosition(from: .zero, to: arrowOffset, duration: 0.2, timingFunction: .easeInEaseOut, removeOnCompletion: false, additive: tru` |
| `packages/WalletUI/Sources/WalletUI/WalletGramTooltip.swift:217` | WalletGramTooltipView.animateOut | `animateAlpha` | 0.2 | .easeInEaseOut |  | `layer?.animateAlpha(from: 1, to: 0, duration: 0.2, timingFunction: .easeInEaseOut, removeOnCompletion: false, completion: { [weak self] _ in` |
| `packages/WalletUI/Sources/WalletUI/WalletSendOpening.swift:151` | WalletSendOpening.update | `CAKeyframeAnimation` |  |  | transform.translation.y | `let animation = CAKeyframeAnimation(keyPath: "transform.translation.y")` |
| `packages/WalletUI/Sources/WalletUI/WalletSendOpening.swift:160` | WalletSendOpening.update | `.duration =` | duration |  |  | `animation.duration = duration` |

## WallpaperUI (9)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:47` | Color.update | `animateBackground` |  |  |  | `self.layer?.animateBackground()` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:60` | Color.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:61` | Color.update | `animateScaleSpring` | 0.3 |  |  | `current.layer?.animateScaleSpring(from: 0.1, to: 1.0, duration: 0.3, removeOnCompletion: false, bounce: false)` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:65` | Color.update | `animateBorder` |  |  |  | `current.layer?.animateBorderColor()` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:70` | Color.update | `animateScaleSpring` | 0.3 |  |  | `selection.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.3, bounce: false)` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:121` | Color.update | `animateScaleSpring` | 0.3 |  |  | `view.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.3, removeOnCompletion: false, bounce: false)` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:133` | Color.update | `animateAlpha` | 0.2 |  |  | `color.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperColorPickerContainerView.swift:134` | Color.update | `animateScaleSpring` | 0.3 |  |  | `color.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3, bounce: false)` |
| `packages/WallpaperUI/Sources/WallpaperUI/WallpaperPreviewController.swift:937` | WallpaperPreviewView.updateState | `animateAlpha` | 0.25 | .linear |  | `progressView.layer?.animateAlpha(from: 1, to: 0, duration: 0.25, timingFunction: .linear, removeOnCompletion: false, completion: { [weak pro` |

## WebAppUI (25)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:372` | Left.update | `animateAlpha` | 0.2 |  |  | `button.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:507` | MainButton.update | `change` |  |  |  | `self.textView.change(opacity: loading == nil ? 1 : 0, animated: animated)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:589` | ButtonsBlock.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:614` | ButtonsBlock.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:750` | ButtonsBlock.update | `_change` |  |  |  | `self.webview._change(opacity: inProgress ? 0 : 1, animated: animated)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:813` | ButtonsBlock.set | `change` |  |  |  | `self.loading.change(opacity: 0, animated: animated)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:815` | ButtonsBlock.set | `change` |  |  |  | `self.loading.change(opacity: 1, animated: animated)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:819` | ButtonsBlock.set | `change` |  |  |  | `self.loading.change(opacity: 0, animated: animated)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:838` | ButtonsBlock.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:851` | ButtonsBlock.update | `animatePosition` |  |  |  | `view.layer?.animatePosition(from: view.frame.origin, to: view.frame.origin.offset(dx: 0, dy: view.frame.height), removeOnCompletion: false)` |
| `packages/WebAppUI/Sources/WebAppUI/WebpageModalController.swift:3025` | FetchResult.closeAnyway | `animateAlpha` | 0.2 |  |  | `self.window?.contentView?.layer?.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { [weak self] _ in` |
| `packages/WebAppUI/Sources/WebAppUI/BrowserState.swift:85` | Webapp.show | `animateAlpha` | 0.2 |  |  | `self.contentView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, removeOnCompletion: false)` |
| `packages/WebAppUI/Sources/WebAppUI/BrowserState.swift:86` | Webapp.show | `animateScaleSpring` | 0.2 |  |  | `self.contentView?.layer?.animateScaleSpring(from: 0.8, to: 1.0, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:247` | WebappBrowser.show | `animateAlpha` | 0.2 |  |  | `self.contentView?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2, removeOnCompletion: false)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:248` | WebappBrowser.show | `animateScaleSpring` | 0.2 |  |  | `self.contentView?.layer?.animateScaleSpring(from: 0.8, to: 1.0, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:397` | TabView.update | `animateBackground` | transition.duration |  |  | `self.layer?.animateBackground(duration: transition.duration, function: transition.timingFunction)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:480` | TabView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:511` | TabView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:535` | TabView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:554` | TabView.update | `animateAlpha` | 0.2 |  |  | `statusControl.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:740` | TabsView.merge | `animateAlpha` | transition.duration | transition.timingFunction |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: transition.duration, timingFunction: transition.timingFunction)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:841` | ContentController.update | `animateAlpha` | 0.2 |  |  | `newView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:1616` | WebpageContainerView.update | `animateAlpha` | 0.2 |  |  | `current.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:1633` | WebpageContainerView.setMainView | `animateAlpha` | 0.2 |  |  | `newView.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WebAppUI/Sources/WebAppUI/WebappBrowser.swift:1989` | WebappBrowserController.hide | `animateAlpha` | 0.2 |  |  | `layer.animateAlpha(from: 1, to: 0, duration: 0.2, removeOnCompletion: false, completion: { _ in finish() })` |

## WidgetUI (10)

| file:line | context | call | duration | curve | keyPath | code |
|---|---|---|---|---|---|---|
| `packages/WidgetUI/Sources/WidgetUI/EmptyChatViewController.swift:33` | EmptyChatView.toggleTips | `animateAlpha` | 0.3 | .spring |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.3, timingFunction: .spring)` |
| `packages/WidgetUI/Sources/WidgetUI/EmptyChatViewController.swift:34` | EmptyChatView.toggleTips | `animateScaleSpring` | 0.3 |  |  | `view.layer?.animateScaleSpring(from: 0.1, to: 1, duration: 0.3)` |
| `packages/WidgetUI/Sources/WidgetUI/EmptyChatViewController.swift:39` | EmptyChatView.toggleTips | `animateScaleSpring` | 0.3 |  |  | `view.layer?.animateScaleSpring(from: 1, to: 0.1, duration: 0.3, bounce: false)` |
| `packages/WidgetUI/Sources/WidgetUI/EmptyChatViewController.swift:44` | EmptyChatView.toggleTips | `change` |  |  |  | `containerView.change(opacity: isEnabled ? 0 : 1, animated: animated)` |
| `packages/WidgetUI/Sources/WidgetUI/WidgetStickersController.swift:150` | WidgetStickersContainer.reload | `animateAlpha` | 0.2 |  |  | `view.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WidgetUI/Sources/WidgetUI/WidgetController.swift:133` | PresentMode.present | `_change` | duration | .spring |  | `previous.view._change(opacity: 0, duration: duration, timingFunction: .spring, completion: { [weak previous] completed in` |
| `packages/WidgetUI/Sources/WidgetUI/WidgetController.swift:146` | PresentMode.present | `_change` | duration | .spring |  | `controller.view._change(opacity: 1, animated: mode.animated, duration: duration, timingFunction: .spring)` |
| `packages/WidgetUI/Sources/WidgetUI/WidgetController.swift:158` | PresentMode.present | `animatePosition` | duration | .spring |  | `controller.view.layer?.animatePosition(from: from, to: to, duration: duration, timingFunction: .spring)` |
| `packages/WidgetUI/Sources/WidgetUI/WidgetController.swift:167` | PresentMode.present | `animateAlpha` | 0.2 |  |  | `prev?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
| `packages/WidgetUI/Sources/WidgetUI/WidgetController.swift:183` | PresentMode.present | `animateAlpha` | 0.2 |  |  | `next?.layer?.animateAlpha(from: 0, to: 1, duration: 0.2)` |
