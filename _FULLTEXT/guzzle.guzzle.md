Guzzle, PHP HTTP client Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. Simple interface for building query strings, POST requests, streaming large uploads, streaming large downloads, using HTTP cookies, uploading JSON data, etc... Can send both synchronous and asynchronous requests using the same interface. Uses PSR-7 interfaces for requests, responses, and streams. This allows you to utilize other PSR-7 compatible libraries with Guzzle. Abstracts away the underlying HTTP transport, allowing you to write environment and transport agnostic code; i.e., no hard dependency on cURL, PHP streams, sockets, or non-blocking event loops. Middleware system allows you to augment and compose client behavior. ```php $client = new \GuzzleHttp\Client(); $res = $client->request(GET, https://api.github.com/repos/guzzle/guzzle); echo $res->getStatusCode(); // 200 echo $res->getHeaderLine(content-type); // application/json; charset=utf8 echo $res->getBody(); // {"id": 1420053, "name": "guzzle", ...} // Send an asynchronous request. $request = new \GuzzleHttp\Psr7\Request(GET, http://httpbin.org); $promise = $client->sendAsync($request)->then(function ($response) { echo I completed! . $response->getBody(); }); $promise->wait(); ``` Help and docs Documentation Stack Overflow Gitter Installing Guzzle The recommended way to install Guzzle is through Composer. ```bash Install Composer curl -sS https://getcomposer.org/installer | php ``` Next, run the Composer command to install the latest stable version of Guzzle: bash php composer.phar require guzzlehttp/guzzle After installing, you need to require Composers autoloader: php require vendor/autoload.php; You can then later update Guzzle using composer: bash composer.phar update Version Guidance | Version | Status | Packagist | Namespace | Repo | Docs | PSR-7 | PHP Version | |---------|------------|---------------------|--------------|---------------------|---------------------|-------|-------------| | 3.x | EOL | guzzle/guzzle | Guzzle | v3 | v3 | No | >= 5.3.3 | | 4.x | EOL | guzzlehttp/guzzle | GuzzleHttp | v4 | N/A | No | >= 5.4 | | 5.x | Maintained | guzzlehttp/guzzle | GuzzleHttp | v5 | v5 | No | >= 5.4 | | 6.x | Latest | guzzlehttp/guzzle | GuzzleHttp | v6 | v6 | Yes | >= 5.5 |