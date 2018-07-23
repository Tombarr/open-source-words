Universal Image Loader Android library #1 on GitHub. UIL aims to provide a powerful, flexible and highly customizable instrument for image loading, caching and displaying. It provides a lot of configuration options and good control over the image loading and caching process. Project News Really have no time for development... so I stop project maintaining since Nov 27 :( UIL [27.11.2011 - 27.11.2015] Thanks to all developers for your support :) Features Multithread image loading (async or sync) Wide customization of ImageLoaders configuration (thread executors, downloader, decoder, memory and disk cache, display image options, etc.) Many customization options for every display image call (stub images, caching switch, decoding options, Bitmap processing and displaying, etc.) Image caching in memory and/or on disk (devices file system or SD card) Listening loading process (including downloading progress) Android 2.0+ support Downloads universal-image-loader-1.9.5.jar Documentation Quick Setup Configuration Display Options Useful Info - Read it before asking a question User Support - Read it before creating new issue Sample project - Learn it to understand the right way of library usage ChangeLog - Info about API changes is here Usage Acceptable URIs examples java "http://site.com/image.png" // from Web "file:///mnt/sdcard/image.png" // from SD card "file:///mnt/sdcard/video.mp4" // from SD card (video thumbnail) "content://media/external/images/media/13" // from content provider "content://media/external/video/media/13" // from content provider (video thumbnail) "assets://image.png" // from assets "drawable://" + R.drawable.img // from drawables (non-9patch images) NOTE: Use drawable:// only if you really need it! Always consider the native way to load drawables - ImageView.setImageResource(...) instead of using of ImageLoader. Simple java ImageLoader imageLoader = ImageLoader.getInstance(); // Get singleton instance java // Load image, decode it to Bitmap and display Bitmap in ImageView (or any other view // which implements ImageAware interface) imageLoader.displayImage(imageUri, imageView); java // Load image, decode it to Bitmap and return Bitmap to callback imageLoader.loadImage(imageUri, new SimpleImageLoadingListener() { @Override public void onLoadingComplete(String imageUri, View view, Bitmap loadedImage) { // Do whatever you want with Bitmap } }); java // Load image, decode it to Bitmap and return Bitmap synchronously Bitmap bmp = imageLoader.loadImageSync(imageUri); Complete java // Load image, decode it to Bitmap and display Bitmap in ImageView (or any other view // which implements ImageAware interface) imageLoader.displayImage(imageUri, imageView, options, new ImageLoadingListener() { @Override public void onLoadingStarted(String imageUri, View view) { ... } @Override public void onLoadingFailed(String imageUri, View view, FailReason failReason) { ... } @Override public void onLoadingComplete(String imageUri, View view, Bitmap loadedImage) { ... } @Override public void onLoadingCancelled(String imageUri, View view) { ... } }, new ImageLoadingProgressListener() { @Override public void onProgressUpdate(String imageUri, View view, int current, int total) { ... } }); java // Load image, decode it to Bitmap and return Bitmap to callback ImageSize targetSize = new ImageSize(80, 50); // result Bitmap will be fit to this size imageLoader.loadImage(imageUri, targetSize, options, new SimpleImageLoadingListener() { @Override public void onLoadingComplete(String imageUri, View view, Bitmap loadedImage) { // Do whatever you want with Bitmap } }); java // Load image, decode it to Bitmap and return Bitmap synchronously ImageSize targetSize = new ImageSize(80, 50); // result Bitmap will be fit to this size Bitmap bmp = imageLoader.loadImageSync(imageUri, targetSize, options); Load & Display Task Flow Applications using Universal Image Loader MediaHouse, UPnP/DLNA Browser | Prezzi Benzina (AndroidFuel) | ROM Toolbox Lite, Pro | Stadium Astro | Chef Astro | Sporee - Live Soccer Scores | EyeEm - Photo Filter Camera | Topface - meeting is easy | reddit is fun | Diaro - personal diary | Meetup | Vingle - Magazines by Fans | Anime Music Radio | WidgetLocker Theme Viewer | ShortBlogger for Tumblr | SnapDish Food Camera | Twitch | TVShow Time, TV show guide | Planning Center Services | Lapse It | My Cloud Player for SoundCloud | SoundTracking | LoopLR Social Video | Hír24 | Immobilien Scout24 | Lieferheld - Pizza Pasta Sushi | Loocator: free sex datings | 벨팡-개편 이벤트,컬러링,벨소리,무료,최신가요,링투유 | Streambels AirPlay/DLNA Player | Ship Mate - All Cruise Lines | Disk & Storage Analyzer | 糗事百科 | Balance BY | Anti Theft Alarm - Security | XiiaLive™ - Internet Radio | Bandsintown Concerts | Save As Web Archive | MCPE STORE -Download MCPE file | All-In-One Toolbox (29 Tools) | Zaim | Calculator Plus Free | Truedialer by Truecaller | DoggCatcher Podcast Player | PingTools Network Utilities | The Traveler | minube: travel photo album | Wear Store for Wear Apps | Cast Store for Chromecast Apps | WebMoney Keeper Donation You can support the project and thank the author for his hard work :) * PayPal - nostra.uil[at]gmail[dot]com Alternative libraries AndroidQuery : ImageLoading DroidParts : ImageFetcher Fresco Glide Picasso UrlImageViewHelper Volley : ImageLoader License Copyright 2011-2015 Sergey Tarasevich Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.