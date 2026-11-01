# Design tokens — Telegram for macOS 13.1

Источник: `refs/Telegram-macOS` (см. `VERSION.md`). Все пути ниже относительно `refs/Telegram-macOS/`. Размеры — в pt (= px в tdesktop .style при 100%).
Шрифт SF Pro **не переносим** → замена **Inter** (см. §3, там же метрики SF для подгонки Inter).

## 0. Как устроена тема (что переносить в tdesktop)

- Палитра = плоский набор ~110 ролей (`ColorPalette`, `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift:905` — init со всеми ролями). Встроенные палитры: `whitePalette` («Day»), `dayClassicPalette` («Day Classic», **дефолт** для светлой), `darkPalette` («Dark»), `nightAccentPalette` («Tinted»/Night Blue, **дефолт** для тёмной), `systemPalette` (системная, Mojave-цвета NSColor).
- Дефолтные настройки: `ThemeSettings.swift:1182` — `palette: dayClassicPalette, bubbled: false, fontSize: 13, defaultDark: .nightAccent, defaultDay: .dayClassic`. ⚠ По умолчанию **пузыри выключены** (режим «list»), пузыри включаются в Settings → Appearance → Chat Mode.
- Акцент: `withAccentColor(_:disableTint:)` (`ColorPalette.swift:1542`) пересчитывает accent/link/accentIcon/bubbleBackground_outgoing и т.д. от выбранного цвета; для tinted-тем (`tinted: true`) фон/разделители тонируются оттенком акцента. Списки акцентов — §1.2.
- Tinted vs non-tinted: `nightAccentPalette.tinted = true` — его фоны (#18222D и т.п.) — это «Night Blue»; при смене акцента фоны перекрашиваются в hue акцента.
- macOS 26 «Liquid Glass»: при наличии `NSGlassEffectView` панели (сайдбар, шапка, поле ввода, меню) — стекло, иначе фолбэк `NSVisualEffectView` (`packages/TGUIKit/Sources/LiquidGlassView.swift:210` — `cornerRadius 16, tintAlpha 0.3`, material `.hudWindow` (dark) / `.titlebar` (light), `:420`). На этой машине (macOS 15) работает фолбэк-блюр. Для Qt: полупрозрачная заливка `background α0.3` + blur 20–30 px.

## 1. Цвета

### 1.1 Палитры (все роли × все встроенные темы)

Значения — hex RGB, `αN` — альфа. `<sub>:N</sub>` — строка в `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift`. Таблица сгенерирована `recon/tools/palettes.py`.

| Палитра | name | isDark | tinted | строка |
|---|---|---|---|---|
| `whitePalette` | "day" | false | false | `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift:1879` |
| `nightAccentPalette` | "nightAccent" | true | true | `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift:2027` |
| `dayClassicPalette` | "dayClassic" | false | false | `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift:2162` |
| `darkPalette` | "Dark" | true | false | `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift:2298` |
| `systemPalette` | "system" | true | false | `packages/ColorPalette/Sources/ColorPalette/ColorPalette.swift:2596` |

| Роль | whitePalette | nightAccentPalette | dayClassicPalette | darkPalette | systemPalette |
|---|---|---|---|---|---|
| `basicAccent` | #2481CC <sub>:1893</sub> | #2EA6FF <sub>:2041</sub> | #2481CC <sub>:2176</sub> | #0088FF <sub>:2312</sub> | #2EA6FF <sub>:2611</sub> |
| `background` | #FFFFFF <sub>:1894</sub> | #18222D <sub>:2042</sub> | #FFFFFF <sub>:2177</sub> | #292B36 <sub>:2313</sub> | #292A2F <sub>:2612</sub> |
| `text` | #000000 <sub>:1895</sub> | #FFFFFF <sub>:2043</sub> | #000000 <sub>:2178</sub> | #E9E9E9 <sub>:2314</sub> | #FFFFFF <sub>:2613</sub> |
| `grayText` | #999999 <sub>:1896</sub> | #B1C3D5 <sub>:2044</sub> | #999999 <sub>:2179</sub> | #8699A3 <sub>:2315</sub> | #B1C3D5 <sub>:2614</sub> |
| `link` | #2481CC <sub>:1897</sub> | #62BCF9 <sub>:2045</sub> | #2481CC <sub>:2180</sub> | #0088FF <sub>:2316</sub> | #2EA6FF <sub>:2615</sub> |
| `accent` | #2481CC <sub>:1898</sub> | #2EA6FF <sub>:2046</sub> | #2481CC <sub>:2181</sub> | #0088FF <sub>:2317</sub> | #2EA6FF <sub>:2616</sub> |
| `redUI` | #FF3B30 <sub>:1899</sub> | #EF5B5B <sub>:2047</sub> | #FF3B30 <sub>:2182</sub> | #EC6657 <sub>:2318</sub> | #EF5B5B <sub>:2617</sub> |
| `greenUI` | #63DA6E <sub>:1900</sub> | #49AD51 <sub>:2048</sub> | #63DA6E <sub>:2183</sub> | #49AD51 <sub>:2319</sub> | #49AD51 <sub>:2618</sub> |
| `blackTransparent` | #000000 α0.6 <sub>:1901</sub> | #000000 α0.6 <sub>:2049</sub> | #000000 α0.6 <sub>:2184</sub> | #000000 α0.6 <sub>:2320</sub> | #000000 α0.6 <sub>:2619</sub> |
| `grayTransparent` | #F4F4F4 α0.4 <sub>:1902</sub> | #2F313D α0.5 <sub>:2050</sub> | #F4F4F4 α0.4 <sub>:2185</sub> | #2F313D α0.5 <sub>:2321</sub> | #3E464C α0.5 <sub>:2620</sub> |
| `grayUI` | #FAFAFA <sub>:1903</sub> | #18222D <sub>:2051</sub> | #FAFAFA <sub>:2186</sub> | #292B36 <sub>:2322</sub> | #292A2F <sub>:2621</sub> |
| `darkGrayText` | #333333 <sub>:1904</sub> | #B1C3D5 <sub>:2052</sub> | #333333 <sub>:2187</sub> | #8699A3 <sub>:2323</sub> | #B1C3D5 <sub>:2622</sub> |
| `accentSelect` | #4C91C7 <sub>:1905</sub> | #3B6BA5 <sub>:2053</sub> | #4C91C7 <sub>:2188</sub> | #1A6CC0 <sub>:2324</sub> | #3B6BA5 <sub>:2623</sub> |
| `selectText` | #EAEAEA <sub>:1906</sub> | #3D6EA3 <sub>:2054</sub> | #EAEAEA <sub>:2189</sub> | #8699A3 <sub>:2325</sub> | #3D6EA3 <sub>:2624</sub> |
| `border` | #EAEAEA <sub>:1907</sub> | #213040 <sub>:2055</sub> | #EAEAEA <sub>:2190</sub> | #464A57 <sub>:2326</sub> | #3D474F <sub>:2625</sub> |
| `grayBackground` | #F4F4F4 <sub>:1908</sub> | #213040 <sub>:2056</sub> | #F4F4F4 <sub>:2191</sub> | #464A57 <sub>:2327</sub> | #3E464C <sub>:2626</sub> |
| `grayForeground` | #E4E4E4 <sub>:1909</sub> | #213040 <sub>:2057</sub> | #E4E4E4 <sub>:2192</sub> | #3D414D <sub>:2328</sub> | #3E464C <sub>:2627</sub> |
| `grayIcon` | #9E9E9E <sub>:1910</sub> | #B1C3D5 <sub>:2058</sub> | #9E9E9E <sub>:2193</sub> | #8699A3 <sub>:2329</sub> | #B1C3D5 <sub>:2628</sub> |
| `accentIcon` | #2481CC <sub>:1911</sub> | #2EA6FF <sub>:2059</sub> | #2481CC <sub>:2194</sub> | #0088FF <sub>:2330</sub> | #2EA6FF <sub>:2629</sub> |
| `badgeMuted` | #D7D7D7 <sub>:1912</sub> | #B1C3D5 <sub>:2060</sub> | #B7B6BD <sub>:2195</sub> | #8699A3 <sub>:2331</sub> | #B1C3D5 <sub>:2630</sub> |
| `badge` | #4BA3E2 <sub>:1913</sub> | #2EA6FF <sub>:2061</sub> | #4BA3E2 <sub>:2196</sub> | #0088FF <sub>:2332</sub> | #2EA6FF <sub>:2631</sub> |
| `indicatorColor` | #464A57 <sub>:1914</sub> | #FFFFFF <sub>:2062</sub> | #464A57 <sub>:2197</sub> | #FFFFFF <sub>:2333</sub> | #FFFFFF <sub>:2632</sub> |
| `selectMessage` | #EAEAEA <sub>:1915</sub> | #0F161E <sub>:2063</sub> | #EAEAEA <sub>:2198</sub> | #3D414D <sub>:2334</sub> | #42444A <sub>:2633</sub> |
| `monospacedPre` | #000000 <sub>:1916</sub> | #2EA6FF <sub>:2064</sub> | #000000 <sub>:2199</sub> | #FFFFFF <sub>:2335</sub> | #FFFFFF <sub>:2634</sub> |
| `monospacedCode` | #FF3B30 <sub>:1917</sub> | #2EA6FF <sub>:2065</sub> | #FF3B30 <sub>:2200</sub> | #FF3B30 <sub>:2336</sub> | #FFFFFF <sub>:2635</sub> |
| `monospacedPreBubble_incoming` | #FF3B30 <sub>:1918</sub> | #FFFFFF <sub>:2066</sub> | #FF3B30 <sub>:2201</sub> | #FFFFFF <sub>:2337</sub> | #FFFFFF <sub>:2636</sub> |
| `monospacedPreBubble_outgoing` | #FFFFFF <sub>:1919</sub> | #FFFFFF <sub>:2067</sub> | #000000 <sub>:2202</sub> | #FFFFFF <sub>:2338</sub> | #FFFFFF <sub>:2637</sub> |
| `monospacedCodeBubble_incoming` | #FF3B30 <sub>:1920</sub> | #FFFFFF <sub>:2068</sub> | #FF3B30 <sub>:2203</sub> | #EC6657 <sub>:2339</sub> | #FFFFFF <sub>:2638</sub> |
| `monospacedCodeBubble_outgoing` | #FFFFFF <sub>:1921</sub> | #FFFFFF <sub>:2069</sub> | #000000 <sub>:2204</sub> | #FFFFFF <sub>:2340</sub> | #FFFFFF <sub>:2639</sub> |
| `selectTextBubble_incoming` | #CCDDEA <sub>:1922</sub> | #3E6B9B <sub>:2070</sub> | #CCDDEA <sub>:2205</sub> | #8699A3 <sub>:2341</sub> | #3E6B9B <sub>:2640</sub> |
| `selectTextBubble_outgoing` | #6DA8D6 <sub>:1923</sub> | #375D8A <sub>:2071</sub> | #CCDDEA <sub>:2206</sub> | #8699A3 <sub>:2342</sub> | #375D8A <sub>:2641</sub> |
| `bubbleBackground_incoming` | #F7F7FA <sub>:1924</sub> | #1E2C3B <sub>:2072</sub> | #FFFFFF <sub>:2207</sub> | #3D414D <sub>:2343</sub> | #4E5058 <sub>:2642</sub> |
| `bubbleBorder_incoming` | #EDEDF2 <sub>:1926</sub> | #293848 <sub>:2074</sub> | #86A9C9 α0.5 <sub>:2209</sub> | #464A57 <sub>:2345</sub> | #4E5058 <sub>:2644</sub> |
| `bubbleBorder_outgoing` | #4D93C9 <sub>:1927</sub> | #3B6BA5 <sub>:2075</sub> | #86A9C9 α0.5 <sub>:2210</sub> | #1A6CC0 <sub>:2346</sub> | #3B6BA5 <sub>:2645</sub> |
| `grayTextBubble_incoming` | #999999 <sub>:1928</sub> | #B1C3D5 <sub>:2076</sub> | #999999 <sub>:2211</sub> | #8699A3 <sub>:2347</sub> | #B1C3D5 <sub>:2646</sub> |
| `grayTextBubble_outgoing` | #EFFAFF α0.8 <sub>:1929</sub> | #EFFAFF α0.8 <sub>:2077</sub> | #008C09 α0.8 <sub>:2212</sub> | #9BBDD8 <sub>:2348</sub> | #EFFAFF α0.8 <sub>:2647</sub> |
| `grayIconBubble_incoming` | #999999 <sub>:1930</sub> | #B1C3D5 <sub>:2078</sub> | #999999 <sub>:2213</sub> | #8699A3 <sub>:2349</sub> | #B1C3D5 <sub>:2648</sub> |
| `grayIconBubble_outgoing` | #EFFAFF α0.8 <sub>:1931</sub> | #B1C3D5 <sub>:2079</sub> | #008C09 α0.8 <sub>:2214</sub> | #9BBDD8 <sub>:2350</sub> | #B1C3D5 <sub>:2649</sub> |
| `accentIconBubble_incoming` | #999999 <sub>:1932</sub> | #B1C3D5 <sub>:2080</sub> | #999999 <sub>:2215</sub> | #8699A3 <sub>:2351</sub> | #B1C3D5 <sub>:2650</sub> |
| `accentIconBubble_outgoing` | #EFFAFF α0.8 <sub>:1933</sub> | #EFFAFF α0.8 <sub>:2081</sub> | #008C09 α0.8 <sub>:2216</sub> | #9BBDD8 <sub>:2352</sub> | #EFFAFF α0.8 <sub>:2651</sub> |
| `linkBubble_incoming` | #2481CC <sub>:1934</sub> | #62BCF9 <sub>:2082</sub> | #2481CC <sub>:2217</sub> | #4DA6FF <sub>:2353</sub> | #2EA6FF <sub>:2652</sub> |
| `linkBubble_outgoing` | #FFFFFF <sub>:1935</sub> | #FFFFFF <sub>:2083</sub> | #004BAD <sub>:2218</sub> | #FFFFFF <sub>:2354</sub> | #FFFFFF <sub>:2653</sub> |
| `textBubble_incoming` | #000000 <sub>:1936</sub> | #FFFFFF <sub>:2084</sub> | #000000 <sub>:2219</sub> | #E9E9E9 <sub>:2355</sub> | #FFFFFF <sub>:2654</sub> |
| `textBubble_outgoing` | #FFFFFF <sub>:1937</sub> | #FFFFFF <sub>:2085</sub> | #000000 <sub>:2220</sub> | #FFFFFF <sub>:2356</sub> | #FFFFFF <sub>:2655</sub> |
| `selectMessageBubble` | #EDF4F9 α0.6 <sub>:1938</sub> | #1E2C3B <sub>:2086</sub> | #EDF4F9 <sub>:2221</sub> | #3D414D <sub>:2357</sub> | #4E5058 <sub>:2656</sub> |
| `fileActivityBackground` | #4BA3E2 <sub>:1939</sub> | #2EA6FF α0.8 <sub>:2087</sub> | #4BA3E2 <sub>:2222</sub> | #0088FF <sub>:2358</sub> | #2EA6FF α0.8 <sub>:2657</sub> |
| `fileActivityForeground` | #FFFFFF <sub>:1940</sub> | #FFFFFF <sub>:2088</sub> | #FFFFFF <sub>:2223</sub> | #FFFFFF <sub>:2359</sub> | #FFFFFF <sub>:2658</sub> |
| `fileActivityBackgroundBubble_incoming` | #4BA3E2 <sub>:1941</sub> | #B1C3D5 <sub>:2089</sub> | #3CA7FE <sub>:2224</sub> | #0088FF <sub>:2360</sub> | #B1C3D5 <sub>:2659</sub> |
| `fileActivityBackgroundBubble_outgoing` | #FFFFFF <sub>:1942</sub> | #FFFFFF <sub>:2090</sub> | #00A700 <sub>:2225</sub> | #FFFFFF <sub>:2361</sub> | #FFFFFF <sub>:2660</sub> |
| `fileActivityForegroundBubble_incoming` | #FFFFFF <sub>:1943</sub> | #1E2C3B <sub>:2091</sub> | #FFFFFF <sub>:2226</sub> | #FFFFFF <sub>:2362</sub> | #4E5058 <sub>:2661</sub> |
| `fileActivityForegroundBubble_outgoing` | #4C91C7 <sub>:1944</sub> | #3B6BA5 <sub>:2092</sub> | #FFFFFF <sub>:2227</sub> | #1A6CC0 <sub>:2363</sub> | #3B6BA5 <sub>:2662</sub> |
| `waveformBackground` | #9E9E9E α0.7 <sub>:1945</sub> | #B1C3D5 α0.7 <sub>:2093</sub> | #9E9E9E α0.7 <sub>:2228</sub> | #8699A3 α0.7 <sub>:2364</sub> | #B1C3D5 α0.7 <sub>:2663</sub> |
| `waveformForeground` | #4BA3E2 <sub>:1946</sub> | #2EA6FF α0.8 <sub>:2094</sub> | #4BA3E2 <sub>:2229</sub> | #0088FF <sub>:2365</sub> | #2EA6FF α0.8 <sub>:2664</sub> |
| `waveformBackgroundBubble_incoming` | #999999 <sub>:1947</sub> | #B1C3D5 <sub>:2095</sub> | #3CA7FE α0.6 <sub>:2230</sub> | #8699A3 <sub>:2366</sub> | #B1C3D5 <sub>:2665</sub> |
| `waveformBackgroundBubble_outgoing` | #FFFFFF <sub>:1948</sub> | #B1C3D5 <sub>:2096</sub> | #00A700 α0.6 <sub>:2231</sub> | #9BBDD8 <sub>:2367</sub> | #B1C3D5 <sub>:2666</sub> |
| `waveformForegroundBubble_incoming` | #4BA3E2 <sub>:1949</sub> | #FFFFFF <sub>:2097</sub> | #3CA7FE <sub>:2232</sub> | #0088FF <sub>:2368</sub> | #FFFFFF <sub>:2667</sub> |
| `waveformForegroundBubble_outgoing` | #EFFAFF <sub>:1950</sub> | #FFFFFF <sub>:2098</sub> | #00A700 <sub>:2233</sub> | #FFFFFF <sub>:2369</sub> | #FFFFFF <sub>:2668</sub> |
| `webPreviewActivity` | #2481CC <sub>:1951</sub> | #62BCF9 <sub>:2099</sub> | #2481CC <sub>:2234</sub> | #0088FF <sub>:2370</sub> | #2EA6FF <sub>:2669</sub> |
| `webPreviewActivityBubble_incoming` | #2481CC <sub>:1952</sub> | #FFFFFF <sub>:2100</sub> | #2481CC <sub>:2235</sub> | #0088FF <sub>:2371</sub> | #FFFFFF <sub>:2670</sub> |
| `webPreviewActivityBubble_outgoing` | #FFFFFF <sub>:1953</sub> | #FFFFFF <sub>:2101</sub> | #00A700 <sub>:2236</sub> | #FFFFFF <sub>:2372</sub> | #FFFFFF <sub>:2671</sub> |
| `redBubble_incoming` | #FF3B30 <sub>:1954</sub> | #EF5B5B <sub>:2102</sub> | #FF3B30 <sub>:2237</sub> | #EC6657 <sub>:2373</sub> | #EF5B5B <sub>:2672</sub> |
| `redBubble_outgoing` | #FF3B30 <sub>:1955</sub> | #EF5B5B <sub>:2103</sub> | #FF3B30 <sub>:2238</sub> | #EC6657 <sub>:2374</sub> | #EF5B5B <sub>:2673</sub> |
| `greenBubble_incoming` | #63DA6E <sub>:1956</sub> | #49AD51 <sub>:2104</sub> | #63DA6E <sub>:2239</sub> | #49AD51 <sub>:2375</sub> | #49AD51 <sub>:2674</sub> |
| `greenBubble_outgoing` | #63DA6E <sub>:1957</sub> | #49AD51 <sub>:2105</sub> | #63DA6E <sub>:2240</sub> | #49AD51 <sub>:2376</sub> | #49AD51 <sub>:2675</sub> |
| `chatReplyTitle` | #2481CC <sub>:1958</sub> | #62BCF9 <sub>:2106</sub> | #2481CC <sub>:2241</sub> | #0088FF <sub>:2377</sub> | #2EA6FF <sub>:2676</sub> |
| `chatReplyTextEnabled` | #000000 <sub>:1959</sub> | #FFFFFF <sub>:2107</sub> | #000000 <sub>:2242</sub> | #E9E9E9 <sub>:2378</sub> | #FFFFFF <sub>:2677</sub> |
| `chatReplyTextDisabled` | #999999 <sub>:1960</sub> | #B1C3D5 <sub>:2108</sub> | #999999 <sub>:2243</sub> | #8699A3 <sub>:2379</sub> | #B1C3D5 <sub>:2678</sub> |
| `chatReplyTitleBubble_incoming` | #2481CC <sub>:1961</sub> | #FFFFFF <sub>:2109</sub> | #2481CC <sub>:2244</sub> | #FFFFFF <sub>:2380</sub> | #FFFFFF <sub>:2679</sub> |
| `chatReplyTitleBubble_outgoing` | #FFFFFF <sub>:1962</sub> | #FFFFFF <sub>:2110</sub> | #00A700 <sub>:2245</sub> | #FFFFFF <sub>:2381</sub> | #FFFFFF <sub>:2680</sub> |
| `chatReplyTextEnabledBubble_incoming` | #000000 <sub>:1963</sub> | #FFFFFF <sub>:2111</sub> | #000000 <sub>:2246</sub> | #FFFFFF <sub>:2382</sub> | #FFFFFF <sub>:2681</sub> |
| `chatReplyTextEnabledBubble_outgoing` | #FFFFFF <sub>:1964</sub> | #FFFFFF <sub>:2112</sub> | #000000 <sub>:2247</sub> | #FFFFFF <sub>:2383</sub> | #FFFFFF <sub>:2682</sub> |
| `chatReplyTextDisabledBubble_incoming` | #999999 <sub>:1965</sub> | #B1C3D5 <sub>:2113</sub> | #999999 <sub>:2248</sub> | #8699A3 <sub>:2384</sub> | #B1C3D5 <sub>:2683</sub> |
| `chatReplyTextDisabledBubble_outgoing` | #EFFAFF α0.8 <sub>:1966</sub> | #B1C3D5 <sub>:2114</sub> | #008C09 α0.8 <sub>:2249</sub> | #9BBDD8 <sub>:2385</sub> | #B1C3D5 <sub>:2684</sub> |
| `groupPeerNameRed` | #FC5C51 <sub>:1967</sub> | #FF8E86 <sub>:2115</sub> | #FC5C51 <sub>:2250</sub> | #FF8E86 <sub>:2386</sub> | #FF8E86 <sub>:2685</sub> |
| `groupPeerNameOrange` | #FA790F <sub>:1968</sub> | #FFA357 <sub>:2116</sub> | #FA790F <sub>:2251</sub> | #FFA357 <sub>:2387</sub> | #FFA357 <sub>:2686</sub> |
| `groupPeerNameViolet` | #895DD5 <sub>:1969</sub> | #BF9AFF <sub>:2117</sub> | #895DD5 <sub>:2252</sub> | #BF9AFF <sub>:2388</sub> | #BF9AFF <sub>:2687</sub> |
| `groupPeerNameGreen` | #0FB297 <sub>:1970</sub> | #4DD6BF <sub>:2118</sub> | #0FB297 <sub>:2253</sub> | #4DD6BF <sub>:2389</sub> | #9CCFC3 <sub>:2688</sub> |
| `groupPeerNameCyan` | #00C1A6 <sub>:1971</sub> | #45E8D1 <sub>:2119</sub> | #00C1A6 <sub>:2254</sub> | #45E8D1 <sub>:2390</sub> | #45E8D1 <sub>:2689</sub> |
| `groupPeerNameLightBlue` | #3CA5EC <sub>:1972</sub> | #7AC9FF <sub>:2120</sub> | #3CA5EC <sub>:2255</sub> | #7AC9FF <sub>:2391</sub> | #7AC9FF <sub>:2690</sub> |
| `groupPeerNameBlue` | #3D72ED <sub>:1973</sub> | #7AA2FF <sub>:2121</sub> | #3D72ED <sub>:2256</sub> | #7AA2FF <sub>:2392</sub> | #7AA2FF <sub>:2691</sub> |
| `peerAvatarRedTop` | #FF885E <sub>:1974</sub> | #FFAC8E <sub>:2122</sub> | #FF885E <sub>:2257</sub> | #FF885E <sub>:2393</sub> | #FFAC8E <sub>:2692</sub> |
| `peerAvatarRedBottom` | #FF516A <sub>:1975</sub> | #FF8597 <sub>:2123</sub> | #FF516A <sub>:2258</sub> | #FF516A <sub>:2394</sub> | #FF8597 <sub>:2693</sub> |
| `peerAvatarOrangeTop` | #FFCD6A <sub>:1976</sub> | #FFDC97 <sub>:2124</sub> | #FFCD6A <sub>:2259</sub> | #FFCD6A <sub>:2395</sub> | #FFDC97 <sub>:2694</sub> |
| `peerAvatarOrangeBottom` | #FFA85C <sub>:1977</sub> | #FFC28D <sub>:2125</sub> | #FFA85C <sub>:2260</sub> | #FFA85C <sub>:2396</sub> | #FFC28D <sub>:2695</sub> |
| `peerAvatarVioletTop` | #82B1FF <sub>:1978</sub> | #A8C8FF <sub>:2126</sub> | #82B1FF <sub>:2261</sub> | #82B1FF <sub>:2397</sub> | #A8C8FF <sub>:2696</sub> |
| `peerAvatarVioletBottom` | #665FFF <sub>:1979</sub> | #948FFF <sub>:2127</sub> | #665FFF <sub>:2262</sub> | #665FFF <sub>:2398</sub> | #948FFF <sub>:2697</sub> |
| `peerAvatarGreenTop` | #A0DE7E <sub>:1980</sub> | #CDFFB2 <sub>:2128</sub> | #A0DE7E <sub>:2263</sub> | #A0DE7E <sub>:2399</sub> | #CDFFB2 <sub>:2698</sub> |
| `peerAvatarGreenBottom` | #54CB68 <sub>:1981</sub> | #90F4A0 <sub>:2129</sub> | #54CB68 <sub>:2264</sub> | #54CB68 <sub>:2400</sub> | #90F4A0 <sub>:2699</sub> |
| `peerAvatarCyanTop` | #53EDD6 <sub>:1982</sub> | #8BFFEE <sub>:2130</sub> | #53EDD6 <sub>:2265</sub> | #53EDD6 <sub>:2401</sub> | #8BFFEE <sub>:2700</sub> |
| `peerAvatarCyanBottom` | #28C9B7 <sub>:1983</sub> | #6AF1E2 <sub>:2131</sub> | #28C9B7 <sub>:2266</sub> | #28C9B7 <sub>:2402</sub> | #6AF1E2 <sub>:2701</sub> |
| `peerAvatarBlueTop` | #72D5FD <sub>:1984</sub> | #9DE3FF <sub>:2132</sub> | #72D5FD <sub>:2267</sub> | #72D5FD <sub>:2403</sub> | #9DE3FF <sub>:2702</sub> |
| `peerAvatarBlueBottom` | #2A9EF1 <sub>:1985</sub> | #6CC2FF <sub>:2133</sub> | #2A9EF1 <sub>:2268</sub> | #2A9EF1 <sub>:2404</sub> | #6CC2FF <sub>:2703</sub> |
| `peerAvatarPinkTop` | #E0A2F3 <sub>:1986</sub> | #F1C4FF <sub>:2134</sub> | #E0A2F3 <sub>:2269</sub> | #E0A2F3 <sub>:2405</sub> | #F1C4FF <sub>:2704</sub> |
| `peerAvatarPinkBottom` | #D669ED <sub>:1987</sub> | #EE9CFF <sub>:2135</sub> | #D669ED <sub>:2270</sub> | #D669ED <sub>:2406</sub> | #EE9CFF <sub>:2705</sub> |
| `bubbleBackgroundHighlight_incoming` | #EAEAEA <sub>:1988</sub> | #283848 <sub>:2136</sub> | #D9F4FF <sub>:2271</sub> | #525768 <sub>:2407</sub> | #42444A <sub>:2706</sub> |
| `bubbleBackgroundHighlight_outgoing` | #5080B0 <sub>:1989</sub> | #5280AA <sub>:2137</sub> | #C8FFA6 <sub>:2272</sub> | #2A5A90 <sub>:2408</sub> | #5280AA <sub>:2707</sub> |
| `chatDateActive` | #FFFFFF <sub>:1990</sub> | #18222D <sub>:2138</sub> | #FFFFFF <sub>:2273</sub> | #292B36 <sub>:2409</sub> | #292A2F <sub>:2708</sub> |
| `chatDateText` | #333333 <sub>:1991</sub> | #B1C3D5 <sub>:2139</sub> | #999999 <sub>:2274</sub> | #8699A3 <sub>:2410</sub> | #B1C3D5 <sub>:2709</sub> |
| `revealAction_neutral1_background` | #4892F2 <sub>:1992</sub> | #007CD6 <sub>:2140</sub> | #4892F2 <sub>:2275</sub> | #555869 <sub>:2411</sub> | #555869 <sub>:2710</sub> |
| `revealAction_neutral1_foreground` | #FFFFFF <sub>:1993</sub> | #FFFFFF <sub>:2141</sub> | #FFFFFF <sub>:2276</sub> | #FFFFFF <sub>:2412</sub> | #FFFFFF <sub>:2711</sub> |
| `revealAction_neutral2_background` | #F09A37 <sub>:1994</sub> | #CD7800 <sub>:2142</sub> | #F09A37 <sub>:2277</sub> | #CD7800 <sub>:2413</sub> | #CD7800 <sub>:2712</sub> |
| `revealAction_neutral2_foreground` | #FFFFFF <sub>:1995</sub> | #FFFFFF <sub>:2143</sub> | #FFFFFF <sub>:2278</sub> | #FFFFFF <sub>:2414</sub> | #FFFFFF <sub>:2713</sub> |
| `revealAction_destructive_background` | #FF3824 <sub>:1996</sub> | #C70C0C <sub>:2144</sub> | #FF3824 <sub>:2279</sub> | #C70C0C <sub>:2415</sub> | #C70C0C <sub>:2714</sub> |
| `revealAction_destructive_foreground` | #FFFFFF <sub>:1997</sub> | #FFFFFF <sub>:2145</sub> | #FFFFFF <sub>:2280</sub> | #FFFFFF <sub>:2416</sub> | #FFFFFF <sub>:2715</sub> |
| `revealAction_constructive_background` | #00C900 <sub>:1998</sub> | #08A723 <sub>:2146</sub> | #00C900 <sub>:2281</sub> | #08A723 <sub>:2417</sub> | #08A723 <sub>:2716</sub> |
| `revealAction_constructive_foreground` | #FFFFFF <sub>:1999</sub> | #FFFFFF <sub>:2147</sub> | #FFFFFF <sub>:2282</sub> | #FFFFFF <sub>:2418</sub> | #FFFFFF <sub>:2717</sub> |
| `revealAction_accent_background` | #2481CC <sub>:2000</sub> | #007CD6 <sub>:2148</sub> | #2481CC <sub>:2283</sub> | #1A5CA0 <sub>:2419</sub> | #3A6E7D <sub>:2718</sub> |
| `revealAction_accent_foreground` | #FFFFFF <sub>:2001</sub> | #FFFFFF <sub>:2149</sub> | #FFFFFF <sub>:2284</sub> | #FFFFFF <sub>:2420</sub> | #FFFFFF <sub>:2719</sub> |
| `revealAction_warning_background` | #FF9500 <sub>:2002</sub> | #CD7800 <sub>:2150</sub> | #FF9500 <sub>:2285</sub> | #CD7800 <sub>:2421</sub> | #CD7800 <sub>:2720</sub> |
| `revealAction_warning_foreground` | #FFFFFF <sub>:2003</sub> | #FFFFFF <sub>:2151</sub> | #FFFFFF <sub>:2286</sub> | #FFFFFF <sub>:2422</sub> | #FFFFFF <sub>:2721</sub> |
| `revealAction_inactive_background` | #BCBCC3 <sub>:2004</sub> | #26384C <sub>:2152</sub> | #BCBCC3 <sub>:2287</sub> | #464A57 <sub>:2423</sub> | #464A57 <sub>:2722</sub> |
| `revealAction_inactive_foreground` | #FFFFFF <sub>:2005</sub> | #FFFFFF <sub>:2153</sub> | #FFFFFF <sub>:2288</sub> | #FFFFFF <sub>:2424</sub> | #FFFFFF <sub>:2723</sub> |
| `chatBackground` | #FFFFFF <sub>:2006</sub> | #18222D <sub>:2154</sub> | #FFFFFF <sub>:2289</sub> | #292B36 <sub>:2425</sub> | #292A2F <sub>:2724</sub> |
| `listBackground` | #EFEFF3 <sub>:2007</sub> | #101820 <sub>:2155</sub> | #EFEFF3 <sub>:2290</sub> | #1E1F26 <sub>:2426</sub> | #1E1F24 <sub>:2725</sub> |
| `listGrayText` | #6D6D71 <sub>:2008</sub> | #B1C3D5 <sub>:2156</sub> | #6D6D71 <sub>:2291</sub> | #8699A3 <sub>:2427</sub> | #B1C3D5 <sub>:2726</sub> |
| `grayHighlight` | #F8F8F8 <sub>:2009</sub> | #18222D <sub>:2157</sub> | #F8F8F8 <sub>:2292</sub> | #292B36 <sub>:2428</sub> | #292A2F <sub>:2727</sub> |
| `focusAnimationColor` | #68A8E2 <sub>:2010</sub> | #68A8E2 <sub>:2158</sub> | #68A8E2 <sub>:2293</sub> | #68A8E2 <sub>:2429</sub> | #68A8E2 <sub>:2728</sub> |
| `premium` | #6B93FF <sub>:2011</sub> | #6B93FF <sub>:2159</sub> | #6B93FF <sub>:2294</sub> | #6B93FF <sub>:2430</sub> | #6B93FF <sub>:2729</sub> |
| `vibrant` | #808080 α0.1 <sub>:2012</sub> | #808080 α0.1 <sub>:2160</sub> | #808080 α0.1 <sub>:2295</sub> | #808080 α0.1 <sub>:2431</sub> | #808080 α0.1 <sub>:2730</sub> |
| `blueText` | — | — | — | — | #009687 <sub>:2740</sub> |
| `blueFill` | — | — | — | — | #20EEDA <sub>:2740</sub> |

### 1.2 Списки акцентов (Settings → Appearance)

| Палитра | Акценты (по порядку) | Строки |
|---|---|---|
| Day (`whitePalette`) | #2481CC, #F83B4C, #FF7519, #EBA239, #29B327, #00C2ED, #7748FF, #FF5DA2 | `ColorPalette.swift:1885` |
| Tinted/Night (`nightAccentPalette`) | #2EA6FF, #F83B4C, #FF7519, #EBA239, #29B327, #00C2ED, #7748FF, #FF5DA2 | `ColorPalette.swift:2033` |
| Day Classic | #2481CC, #5A9E29, #F55783, #7E5FE5, #FF5FA9, #199972, #009EEE (+ bubble-градиенты) | `ColorPalette.swift:2168` |
| Dark (`darkPalette`) | #0088FF, #F83B4C, #FF7519, #EBA239, #29B327, #00C2ED, #7748FF, … | `ColorPalette.swift:2304` |

Для скриншотов: «два акцента по умолчанию» = #2481CC (light) и #2EA6FF (tinted dark); «другой» = #7748FF.

### 1.3 Цвета имён/аватарок (peer colors)
`packages/ColorPalette/Sources/ColorPalette/PeerNamesColor.swift` + `theme.colors.peerColors(n)` — 7 пар градиентов аватарок-заглушек (top/bottom). Перенести в tdesktop `historyPeerN…` / `historyPeerUserpicFg`.

## 2. Радиусы, размеры, толщины

| Токен | Значение | Где |
|---|---|---|
| Базовый `.cornerRadius` | 5 | `packages/TGUIKit/Sources/TGColor.swift:380` |
| `.borderSize` (все разделители) | 1 (1 px при 1x, на Retina тоже 1pt) | `TGColor.swift:384` |
| Пузырь: главный радиус | **16** | `packages/TelegramTheme/Sources/TelegramTheme/ChatMessageBubbleImages.swift:13` |
| Пузырь: вспомогательный (стык в группе) | **8** | `ChatMessageBubbleImages.swift:14` |
| Пузырь: ширина хвоста | 6 | `ChatMessageBubbleImages.swift:15` |
| Пузырь: диаметр шаблона (9-patch) | 32 | `ChatMessageBubbleImages.swift:16` |
| Хвост: эллипсы | нижний 27×17 @ (d−9, d−17); вырез верхний 23×21 @ (d, d−19) | `ChatMessageBubbleImages.swift:97-98, 114-129` |
| Плашка выделения строки списка чатов | radius **14**, continuous corners, inset 3 от строки | `packages/ChatListUI/Sources/ChatListUI/ChatListRowView.swift:701-712, 3332-3336` |
| Плашка в свёрнутом сайдбаре | аватар.insetBy(−7) | `ChatListRowView.swift:3333` |
| Аватар в списке чатов | 50×50, круг; форум — radius 10 | `ChatListRowView.swift:1188, 1546, 2030` |
| Аватар в чате (группы) | 36 зона (аватар 30) | `packages/ChatUI/Sources/ChatUI/ChatRowItem.swift:692-712` |
| Настройки: группа строк (modern) | radius **20**, внутр. отступы 12/14/12/14 | `packages/GeneralRows/Sources/GeneralRows/GeneralRowView.swift:128`, `GeneralRowItem.swift:160-230` |
| Настройки: max ширина блока | 600 | `GeneralRowItem.swift:436-447` |
| Liquid glass панель | radius 16, tint α0.3 | `LiquidGlassView.swift:210` |
| Меню (AppMenu) | radius **18** (покой); при открытии морф «пилюля→18» | `packages/TGUIKit/Sources/AppMenuController.swift:112-115, 138-195` |
| Пункт меню: плашка hover | radius 5 (`.cornerRadius`), leftInset 11, innerInset 4 | `packages/TGUIKit/Sources/AppMenuRowItem.swift:59, 149-150` |
| Тултип (shimmer) | 10 | `packages/TGUIKit/Sources/ShimmerTooltipView.swift:6` |
| Кнопка «свайп-ответ» | 33×33, линия прогресса 2, кольцо успеха r=35 | `packages/ChatUI/Sources/ChatUI/ChatRowView.swift:23-30` |
| Кнопка отправки (поле) | 40×32, inset 4, gap 6 | `packages/ChatUI/Sources/ChatUI/ChatInputSendButton.swift:110-112` |
| Тени меню/свитча | shadowOpacity 0.26, radius 20 | `packages/TGUIKit/Sources/ModalMorphTransition.swift:19-20` |

## 3. Типографика

### 3.1 Шкала (TGFont)
`packages/TGUIKit/Sources/TGFont.swift:295-303`:

| Имя | pt | Типичное использование |
|---|---|---|
| `.small` | 11 | бейджи (medium), подписи, время в списке (part) |
| `.short` | 12 | дата в списке чатов, время в пузыре, подзаголовок шапки (статус), подпись/forward |
| `.text` | **13** | текст сообщений (= `theme.fontSize`, настраивается 11–?), превью сообщения в списке, сервисные сообщения |
| `.title` | 14 | имя чата в списке (**medium**) |
| `.header` | 15 | заголовок в шапке чата (**medium**) |
| `.huge` | 18 | крупные заголовки |

Веса: `.normal`=regular, `.medium`=medium, `.bold` **= semibold** (не bold!), `.semibold`=semibold, `.avatar`=rounded bold (буквы в аватарке, 22pt в списке), `.code`=monospaced medium, `.italic`, `.roundTimer`=rounded. `TGFont.swift:89-293`.

Ключевые текстовые стили:

| Элемент | Шрифт | Цвет-роль | Где |
|---|---|---|---|
| Список: имя чата | medium 14 | `chatList.textColor` (секретный — `secretChatTextColor`) | `ChatListRowItem.swift:925-928` |
| Список: превью | normal 13 | `grayText` / `chatList.peerTextColor` (автор) | `ChatListRowItem.swift:983-997` |
| Список: дата | normal 12 | `grayText` | `ChatListRowItem.swift:959` |
| Список: бейдж | medium 11 | `chatList.badgeTextColor` на `badgeBackgroundColor` / `badgeMutedBackgroundColor` | `ChatListRowItem.swift:1126` |
| Список: вкладки папок в строке | bold(=semibold) 10 UPPERCASE | | `ChatListRowItem.swift:859` |
| Чат: текст | normal `fontSize` (13) | `chat.textColor(isIncoming, bubbled)` | ChatMessageItem |
| Чат: автор | medium 13 | `chat.linkColor` / peer color | `ChatRowItem.swift:2230` |
| Чат: forward/подпись/время | normal 12 | `chat.grayText` | `ChatRowItem.swift:2174, 2384` |
| Дата-разделитель | medium `fontSize` | service color | `packages/ChatUI/Sources/ChatUI/ChatMessageDateHeader.swift:126` |
| Сервисное сообщение | normal/medium 13 | `chatServiceItemTextColor` | `ChatServiceItem.swift:408-522` |
| Шапка чата: заголовок | medium 15 | text | `ChatTitleBarView.swift:28` |
| Шапка чата: статус | normal 12 | grayText / accent (online, typing) | `ChatTitleBarView.swift:782-786` |

### 3.2 Метрики системного шрифта (SF Pro, macOS 15) — для подгонки Inter
Снято `recon/tools/fontm.swift` (NSFont.systemFont). `lineHeight` = `NSLayoutManager.defaultLineHeight` — то, что даёт высоту строки в TextView. Трекинг SF применяется автоматически (оптический, по размеру); ориентир из Apple HIG для SF Pro Text: 11pt +0.06, 12pt 0, 13pt −0.08, 14pt −0.15, 15pt −0.23, 16pt −0.31, 17pt −0.43 (pt). Для Inter при 13px рекомендуем letter-spacing ≈ −0.1px и line-height 16px, чтобы совпасть по высоте строк.

| size pt | weight (TGFont) | family/name | ascender | descender | leading | lineHeight (LM default) | capHeight | xHeight |
|---|---|---|---|---|---|---|---|---|
| 10 | regular(.normal) | .AppleSystemUIFont | 9.67 | -2.11 | 0.00 | 12.00 | 7.05 | 5.26 |
| 10 | medium(.medium) | .AppleSystemUIFontMedium | 9.67 | -2.11 | 0.00 | 12.00 | 7.05 | 5.30 |
| 10 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 9.67 | -2.11 | 0.00 | 12.00 | 7.05 | 5.34 |
| 11 | regular(.normal) | .AppleSystemUIFont | 10.63 | -2.32 | 0.00 | 13.00 | 7.75 | 5.79 |
| 11 | medium(.medium) | .AppleSystemUIFontMedium | 10.63 | -2.32 | 0.00 | 13.00 | 7.75 | 5.83 |
| 11 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 10.63 | -2.32 | 0.00 | 13.00 | 7.75 | 5.87 |
| 12 | regular(.normal) | .AppleSystemUIFont | 11.60 | -2.53 | 0.00 | 15.00 | 8.46 | 6.32 |
| 12 | medium(.medium) | .AppleSystemUIFontMedium | 11.60 | -2.53 | 0.00 | 15.00 | 8.46 | 6.36 |
| 12 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 11.60 | -2.53 | 0.00 | 15.00 | 8.46 | 6.40 |
| 13 | regular(.normal) | .AppleSystemUIFont | 12.57 | -2.74 | 0.00 | 16.00 | 9.16 | 6.84 |
| 13 | medium(.medium) | .AppleSystemUIFontMedium | 12.57 | -2.74 | 0.00 | 16.00 | 9.16 | 6.89 |
| 13 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 12.57 | -2.74 | 0.00 | 16.00 | 9.16 | 6.94 |
| 14 | regular(.normal) | .AppleSystemUIFont | 13.54 | -2.95 | 0.00 | 17.00 | 9.86 | 7.37 |
| 14 | medium(.medium) | .AppleSystemUIFontMedium | 13.54 | -2.95 | 0.00 | 17.00 | 9.86 | 7.42 |
| 14 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 13.54 | -2.95 | 0.00 | 17.00 | 9.86 | 7.47 |
| 15 | regular(.normal) | .AppleSystemUIFont | 14.50 | -3.16 | 0.00 | 18.00 | 10.57 | 7.90 |
| 15 | medium(.medium) | .AppleSystemUIFontMedium | 14.50 | -3.16 | 0.00 | 18.00 | 10.57 | 7.95 |
| 15 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 14.50 | -3.16 | 0.00 | 18.00 | 10.57 | 8.01 |
| 16 | regular(.normal) | .AppleSystemUIFont | 15.47 | -3.38 | 0.00 | 18.00 | 11.27 | 8.42 |
| 16 | medium(.medium) | .AppleSystemUIFontMedium | 15.47 | -3.38 | 0.00 | 18.00 | 11.27 | 8.48 |
| 16 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 15.47 | -3.38 | 0.00 | 18.00 | 11.27 | 8.54 |
| 18 | regular(.normal) | .AppleSystemUIFont | 17.40 | -3.80 | 0.00 | 21.00 | 12.68 | 9.46 |
| 18 | medium(.medium) | .AppleSystemUIFontMedium | 17.40 | -3.80 | 0.00 | 21.00 | 12.68 | 9.54 |
| 18 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 17.40 | -3.80 | 0.00 | 21.00 | 12.68 | 9.59 |
| 22 | regular(.normal) | .AppleSystemUIFont | 21.27 | -4.64 | 0.00 | 26.00 | 15.50 | 11.37 |
| 22 | medium(.medium) | .AppleSystemUIFontMedium | 21.27 | -4.64 | 0.00 | 26.00 | 15.50 | 11.47 |
| 22 | semibold(.semibold/.bold) | .AppleSystemUIFontDemi | 21.27 | -4.64 | 0.00 | 26.00 | 15.50 | 11.56 |

## 4. Высоты строк списков

| Список | Высота | Отступы | Где |
|---|---|---|---|
| Чаты | **70** (аватар 50 @ (10,10), текст с x=70, margin 9) | leftInset = 50+2·10 = 70; разделитель от x=70 (у последнего закреплённого — от 0) | `ChatListRowItem.swift:1192, 1382-1396, 2638-2656`; `ChatListRowView.swift:1459` |
| Чаты: свёрнутый архив | 35 (или 70 при ширине 82) | | `ChatListRowItem.swift:2640-2645` |
| Топик форума | 53 + высота текста (≈17) | | `ChatListRowItem.swift:2654` |
| Настройки (GeneralRowItem) | 40 по умолчанию (+ inner insets 12/14 у modern) | inset 20/20 | `GeneralRowItem.swift:385` |
| Контакты / поиск / участники (ShortPeerRow) | 50 (аватар 36, имя medium 14, статус normal 13 grayText) | inset left 10 | `packages/ShortPeerRow/Sources/ShortPeerRow/ShortPeerRowItem.swift:341` |
| Меню (AppMenuRowItem) | **28** (1 строка), иначе текст+8; разделитель 4–5; текст medium 13, шорткат medium 13 secondary | leftInset 11, innerInset 4 | `packages/TGUIKit/Sources/AppMenuRowItem.swift:36, 95, 149-150, 167-178, 333-339` |
| Навбар (шапка) | **64** | | `packages/TGUIKit/Sources/NavigationBarView.swift:17` |

## 5. Тени, блюр, материалы

| Где | Значение | Ссылка |
|---|---|---|
| Liquid glass/фолбэк | NSVisualEffectView `.hudWindow` (dark) / `.titlebar` (light), blending `.withinWindow`; поверх tint `background α0.3` | `LiquidGlassView.swift:318-430` |
| Модалка-затемнение | dim backdrop, `.ultraDark` material для full-screen модалок | `packages/TGUIKit/Sources/Modal.swift:1101` |
| Прогресс-модалка | `.dark`/`.light` material | `ProgressModal.swift:15` |
| Тень всплывающих (свитч/линза, морф) | opacity 0.26, radius 20 | `ModalMorphTransition.swift:19-20` |
| Пузыри | без тени; outgoing может быть градиентом (`bubbleBackground_outgoing` = массив цветов, blended 0.5) | `ColorPalette.swift:1058-1060` |
