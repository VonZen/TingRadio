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

Last updated: 5 October 2026

Ting Radio is developed and maintained by Vonzen. This policy covers the Ting Radio app, its website and support correspondence. For questions or privacy requests, contact [VonzenApp@outlook.com](mailto:VonzenApp@outlook.com).

You can listen without creating a Ting Radio account. The app saves your library and preferences locally and connects to external services to provide radio, song information and purchases. Those services receive the requests described below and connection information, such as your IP address.

We use the information described in this policy to provide and maintain the relevant features, handle purchases and respond to support requests. We do not sell or rent your personal information. Requests to external providers are part of operating these features and are processed under those providers’ own privacy policies; this policy does not replace them.

## 1. Information on your devices

The app stores favourites, custom station addresses, recent stations, listening and song history, search history, discovery preferences, feature allowance state, alarm settings and cached artwork or song information in local settings or files. These support your library, recommendations and app functionality. Song history contains song information; it is not an audio recording.

Your paired iPhone and Apple Watch can exchange station favourites, recent and custom stations, discovery region and Pro status through Apple's WatchConnectivity framework. This is companion synchronisation, rather than a Ting Radio cloud account shared across all devices.

On supported iPhones, radio wake-up uses Apple's AlarmKit. With your permission, the app gives the system the alarm time, repeat schedule and related station information needed to arrange the alarm.

## 2. Radio discovery and playback

Directory searches send search terms and selected filters, such as genre, country or language, to [Radio Browser](https://www.radio-browser.info/). When you play a directory station, the app reports its station identifier to Radio Browser's click endpoint. Adding a directory station to favourites may also send a vote for that station. Custom stations do not use these directory click or vote reports.

Playback connects to the selected station's stream server. Station validation and artwork loading also contact the relevant stream or image servers. These providers receive your network connection information and the requested address. A custom URL can contain information you include in it; use only addresses you are entitled to access and share.

At startup, the app may request an approximate region from [ipwho.is](https://ipwhois.io/) using your network IP address. The response can include country, region, city and time zone. It helps choose discovery content and the network route for purchase services. This does not use GPS or request precise-location permission. The app caches the region result locally without writing the returned IP field to disk.

Radio Browser supplies directory information; the selected broadcaster or stream provider supplies the audio. These are separate services, and each receives the requests directed to it.

## 3. Song recognition, lyrics and artwork

Song recognition uses Apple ShazamKit with audio from the station being played, including where recognition helps match lyrics. It does not record through your microphone. [Apple describes ShazamKit](https://developer.apple.com/shazamkit/) as matching a one-way acoustic signature without sharing the audio with Apple.

Lyrics requests may send a song identifier, title, artist and storefront region to SpicyAMLL (api.spicyamll.online); a song identifier to the AMLL lyrics database hosted on GitHub (raw.githubusercontent.com); or the title and artist to [LRCLIB](https://lrclib.net/). Not every request uses every provider. Apple's iTunes Search or Lookup services may receive a title, artist or Apple Music identifier to find artwork and song information.

These services and their hosting providers also receive ordinary network request information. Matching results and lyrics may be cached on your device. Ting Radio does not upload your complete local library or listening history as part of these requests.

## 4. Purchases and Pro access

Apple processes App Store purchases. Ting Radio uses RevenueCat to load purchase options, validate and restore purchases, and maintain Pro access. Its SDK connects when configured at app startup, even before you choose to buy.

The current integration uses a generated anonymous RevenueCat app-user identifier, rather than a Ting Radio account name. RevenueCat processes purchase receipts or transaction information, purchase history and entitlement status for these functions and purchase-service operation. Some connections may use RevenueCat's backup API at api.rc-backup.com. Payment card or bank-account details are handled by Apple and are not received by Ting Radio. See [RevenueCat's privacy information](https://www.revenuecat.com/privacy) and its [Apple privacy disclosure guidance](https://www.revenuecat.com/docs/platform-resources/apple-platform-resources/apple-app-privacy).

The current app does not integrate an advertising SDK or a general-purpose behaviour or crash-reporting SDK. This does not prevent stations from broadcasting their own advertisements or external services from keeping operational logs.

## 5. Website and support

The website uses an English default entry point and separate addresses for each language. It does not store a language preference in your browser or add advertising cookies, visitor-analysis scripts or tracking pixels.

The website is hosted on GitHub Pages. GitHub may process visitor IP addresses and request logs for hosting and security under the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

If you email support, we receive your email address, message and anything you choose to attach. We use these to respond and resolve your request. Please avoid sending unnecessary sensitive information.

## 6. Retention, security and your choices

Local information remains until you remove it through available app controls, the cache is replaced or the operating system removes the app's data. You can manage favourites and custom stations, clear search or listening and song history, change preferences, and delete alarms. Clearing history does not clear every separate song-information or artwork cache. Device backups may retain copies under your system settings.

We retain support correspondence as needed to handle the request and meet applicable obligations. Apple, RevenueCat, radio servers and other providers apply their own retention rules; clearing local history does not erase their records. Services may process requests in countries other than yours. We do not promise a single retention period or storage location for these independent services.

Connections use the protocols supported by each provider. Some station streams and custom URLs use unencrypted HTTP. No network or storage system is guaranteed to be completely secure.

You can stop playback and leave the relevant feature, or fully quit the app, to stop subsequent requests for those functions. Moving the app to the background does not stop playback. You can manage alarm permission in system settings and Apple purchases through your Apple account. Deleting the app does not cancel a subscription. Depending on applicable law, you may have rights to access, correct, delete or restrict processing of personal information. Contact us to make a request; we may need enough information to verify and locate the relevant records. For information held independently by another provider, its own request process may also be necessary.

## 7. Children and minors

Ting Radio is not designed specifically for children. Minors should use it with a parent or guardian’s guidance and any consent required by local law. External broadcasts may contain material unsuitable for children. If you believe a child has provided us with personal information that should not have been collected, contact us so we can review and, where appropriate, delete information within our control.

## 8. Changes and contact

We will update this page when app functionality or information practices change and show the revision date above. Any consent required by applicable law will be requested where relevant. For questions, support or privacy requests, email [VonzenApp@outlook.com](mailto:VonzenApp@outlook.com).
