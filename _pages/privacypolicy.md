---
layout: page
title: Privacy policy
description: How Ting Radio handles local settings, radio requests, song services, purchases and website visits.
language: en
permalink: /privacypolicy/
translated: false
english_only: true
translation_key: privacy
---

# Privacy policy

Last updated: 7 October 2026

Ting Radio is developed and maintained by Vonzen. This policy covers the Ting Radio app, its website and support correspondence. For questions or privacy requests, contact [VonzenApp@outlook.com](mailto:VonzenApp@outlook.com).

You can listen without creating a Ting Radio account. The app saves your library and preferences locally and connects to external services to provide radio, song information and purchases. Those services receive the requests described below and connection information, such as your IP address.

We use the information described in this policy to provide and maintain the relevant features, handle purchases and respond to support requests. We do not sell or rent your personal information. Requests to external providers are part of operating these features and are processed under those providers’ own privacy policies; this policy does not replace them.

Listening does not require you to provide your name, phone number, postal address or an account password to Ting Radio. This does not mean that every request is anonymous: network addresses, purchase identifiers and information you send to support are handled as described below.

## 1. Information on your devices

The app stores favourites, custom station addresses, recent stations, listening and song history, search history, discovery preferences, feature allowance state, alarm settings and cached artwork or song information in local settings or files. These support your library, recommendations and app functionality. Song history contains song information; it is not an audio recording.

Your paired iPhone and Apple Watch can exchange station favourites, recent and custom stations, discovery region and Pro status through Apple's WatchConnectivity framework. This is companion synchronisation, rather than a Ting Radio cloud account shared across all devices.

On supported iPhones, radio wake-up uses Apple's AlarmKit. With your permission, the app gives the system the alarm time, repeat schedule and related station information needed to arrange the alarm.

## 2. Radio discovery and playback

Radio Browser supplies community-maintained directory information; the selected broadcaster or stream provider supplies the audio. These are separate services, and each receives the requests directed to it. A connection can reveal your IP address, request time and normal HTTP or device information to the receiving service.

Directory searches send search terms and selected filters, such as genre, country or language, to [Radio Browser](https://www.radio-browser.info/). When you play a directory station, the app reports its station identifier to Radio Browser's click endpoint. Adding a directory station to favourites may also send a vote for that station. Custom stations do not use these directory click or vote reports.

Playback connects to the selected station's stream server. Station validation and artwork loading also contact the relevant stream or image servers. These providers receive your network connection information and the requested address. A custom URL can contain information you include in it; use only addresses you are entitled to access and share.

At startup, the app downloads Ting Radio's station blocklist from this website (vonzen.github.io), which lists stations removed after rights or other reports. The request contains no identifier beyond normal connection information, and the list is cached on your device.

At startup, the app may request an approximate region from [ipwho.is](https://ipwhois.io/) using your network IP address. The response can include country, region, city and time zone. It helps choose discovery content and the network route for purchase services. This does not use GPS or request precise-location permission. The app caches the region result locally without writing the returned IP field to disk.

## 3. Song recognition and artwork

Song recognition uses Apple ShazamKit with audio from the station being played. It can start when you open or use recognition, and may run again to refresh the recognition panel while it is open. A separate tap is not required for every match. It does not record through your microphone. [Apple describes ShazamKit](https://developer.apple.com/shazamkit/) as matching a one-way acoustic signature without sharing the audio with Apple.

The current app does not request online lyrics. Apple's iTunes Search or Lookup services may receive a title, artist or Apple Music identifier to find artwork and song information.

These services and their hosting providers also receive ordinary network request information. Matching results may be cached on your device. Ting Radio does not upload your complete local library or listening history as part of these requests.

Artwork lookups can run automatically when a station supplies song information without a cover image. Requests therefore depend on the features in use and available metadata, rather than requiring a separate confirmation for each lookup.

When you open a song in an external music app, Ting Radio passes a track link or search information to that app. For QQ Music and NetEase Music, it copies the song title and artist to the system clipboard before opening the app's search screen. The clipboard is managed by your operating system. Sharing a song through the system share sheet passes the selected song information and any included link to the destination you choose. Those apps and websites handle the information under their own policies.

## 4. Purchases and Pro access

Apple processes App Store purchases. Ting Radio uses RevenueCat to load purchase options, validate and restore purchases, and maintain Pro access. Its SDK connects when configured at app startup, even before you choose to buy.

The current integration uses a generated anonymous RevenueCat app-user identifier, rather than a Ting Radio account name. This identifier can associate purchase records and service requests even though it does not contain your name. RevenueCat processes purchase receipts or transaction information, purchase history and entitlement status for purchase functionality, fraud prevention and purchase reporting available to us in its dashboard. Some connections may use RevenueCat's backup API at api.rc-backup.com. Payment card or bank-account details are handled by Apple and are not received by Ting Radio. See [RevenueCat's privacy information](https://www.revenuecat.com/privacy) and its [Apple privacy disclosure guidance](https://www.revenuecat.com/docs/platform-resources/apple-platform-resources/apple-app-privacy).

The current app does not integrate an advertising SDK or a general-purpose behaviour or crash-reporting SDK. This does not prevent stations from broadcasting their own advertisements or external services from keeping operational logs.

## 5. Website and support

The website uses an English default entry point and separate addresses for each language. It does not store a language preference in your browser or add advertising cookies, visitor-analysis scripts or tracking pixels.

The website is hosted on GitHub Pages. GitHub may process visitor IP addresses and request logs for hosting and security under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

The in-app contact action opens an email draft containing the app version, build number, operating-system version, device model identifier and selected app language. You can review or edit the draft; opening it does not send a message to us. If you send it, we receive your email address, message and anything you choose to attach. We use these to respond and resolve your request. Please avoid sending unnecessary sensitive information, passwords or private stream-access tokens. Station reports opened from the app add the station name, directory identifier, stream and homepage addresses to the draft. Copyright and privacy requests are also handled as support correspondence.

Apple may separately provide crash reports and app-use statistics according to your system analytics-sharing settings. These are Apple's reporting mechanisms, rather than an analytics SDK added by Ting Radio. You can manage this sharing in your device's Analytics & Improvements settings; see [Apple's App Analytics & Privacy explanation](https://www.apple.com/legal/privacy/data/en/app-analytics/). Local diagnostic events, such as alarm-operation logs, do not themselves send reports to a Ting Radio analytics server.

## 6. Retention, security and your choices

Local information remains until you remove it through available app controls, the cache is replaced or the operating system removes the app's data. You can manage favourites and custom stations, clear search or listening and song history, change preferences, and delete alarms. Clearing history does not clear every separate song-information or artwork cache. Device backups may retain copies under your system settings.

We retain support correspondence as needed to handle the request and meet applicable obligations. Apple, RevenueCat, radio servers and other providers apply their own retention rules; clearing local history does not erase their records. Services may process requests in countries other than yours. We do not promise a single retention period or storage location for these independent services.

Connections use the protocols supported by each provider. Some station streams and custom URLs use unencrypted HTTP. No network or storage system is guaranteed to be completely secure.

You can stop playback and leave the relevant feature, or fully quit the app, to stop subsequent requests for those functions. Moving the app to the background does not stop playback. Changing Apple's analytics-sharing setting does not stop radio, song-information or purchase requests needed for the features you use. You can manage alarm permission in system settings and Apple purchases through your Apple account. Deleting the app does not cancel a subscription.

## 7. Privacy requests and disclosures

Depending on the law that applies to you, you may request access, correction, deletion or a portable copy of personal information, object to or restrict its processing, withdraw consent where processing relies on it, or complain to the relevant privacy authority. Contact [VonzenApp@outlook.com](mailto:VonzenApp@outlook.com) with the request and enough information to locate the relevant records. We may need to verify your authority to make the request and will respond within applicable legal deadlines.

Our ability to act is limited to information we hold or control. We cannot remotely retrieve or erase your device's local library, and independent providers may need to handle requests about their own records. We will explain applicable limits, including information that must be retained to meet legal obligations. Withdrawing consent does not affect processing that was lawful before withdrawal.

We may disclose information we hold when required by law or when necessary and legally permitted to investigate abuse, address a rights claim or protect people and services. Any such disclosure will be limited to information relevant to that purpose.

## 8. Children and minors

Ting Radio is not designed specifically for children. Minors should use it with a parent or guardian’s guidance and any consent required by local law. External broadcasts may contain material unsuitable for children. If you believe a child has provided us with personal information that should not have been collected, contact us so we can review and, where appropriate, delete information within our control.

## 9. Changes and contact

We will update this page when app functionality or information practices change and show the revision date above. For material changes, we will provide notice appropriate to the change and required by applicable law. A policy update does not replace any consent that the law requires us to obtain. For questions, support or privacy requests, email [VonzenApp@outlook.com](mailto:VonzenApp@outlook.com). Our [Terms of Service]({{ '/termsofservice/' | relative_url }}) explain the conditions for using Ting Radio.
