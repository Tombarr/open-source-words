okhttp utils 由于个人原因，现已停止维护。 对okhttp的封装类，okhttp见：https github com square okhttp 目前对应okhttp版本3 3 1 用法 android studio compile com zhy okhttputils 2 6 2 eclipse 下载最新jar okhttputils 2 6 2 jar 注：需要同时导入okhttp和okio的jar，下载见：https github com square okhttp 目前对以下需求进行了封装 一般的get请求 一般的post请求 基于http post的文件上传（类似表单） 文件下载 加载图片 上传下载的进度回调 支持取消某个请求 支持自定义callback 支持head、delete、patch、put 支持session的保持 支持自签名网站https的访问，提供方法设置下证书就行 配置okhttpclient 默认情况下，将直接使用okhttp默认的配置生成okhttpclient，如果你有任何配置，记得在application中调用initclient方法进行设置。 java public class myapplication extends application override public void oncreate super oncreate okhttpclient okhttpclient new okhttpclient builder addinterceptor new loggerinterceptor tag connecttimeout 10000l timeunit milliseconds readtimeout 10000l timeunit milliseconds 其他配置 build okhttputils initclient okhttpclient 别忘了在androidmanifest中设置。 对于cookie 包含session 对于cookie一样，直接通过cookiejar方法配置，参考上面的配置过程。 cookiejarimpl cookiejar new cookiejarimpl new persistentcookiestore getapplicationcontext okhttpclient okhttpclient new okhttpclient builder cookiejar cookiejar 其他配置 build okhttputils initclient okhttpclient 目前项目中包含： persistentcookiestore 持久化cookie serializablehttpcookie 持久化cookie memorycookiestore cookie信息存在内存中 如果遇到问题，欢迎反馈，当然也可以自己实现cookiejar接口，编写cookie管理相关代码。 此外，对于持久化cookie还可以使用https github com franmontiel persistentcookiejar 相当于框架中只是提供了几个实现类，你可以自行定制或者选择使用。 对于log 初始化okhttpclient时，通过设置拦截器实现，框架中提供了一个loggerinterceptor，当然你可以自行实现一个interceptor 。 okhttpclient okhttpclient new okhttpclient builder addinterceptor new loggerinterceptor tag 其他配置 build okhttputils initclient okhttpclient 对于https 依然是通过配置即可，框架中提供了一个类httpsutils 设置可访问所有的https网站 httpsutils sslparams sslparams httpsutils getsslsocketfactory null null null okhttpclient okhttpclient new okhttpclient builder sslsocketfactory sslparams sslsocketfactory sslparams trustmanager 其他配置 build okhttputils initclient okhttpclient 设置具体的证书 httpsutils sslparams sslparams httpsutils getsslsocketfactory 证书的inputstream null null okhttpclient okhttpclient new okhttpclient builder sslsocketfactory sslparams sslsocketfactory sslparams trustmanager 其他配置 build okhttputils initclient okhttpclient 双向认证 httpsutils getsslsocketfactory 证书的inputstream 本地证书的inputstream 本地证书的密码 同样的，框架中只是提供了几个实现类，你可以自行实现sslsocketfactory，传入sslsocketfactory即可。 其他用法示例 get请求 java string url http www csdn net okhttputils get url url addparams username hyman addparams password 123 build execute new stringcallback override public void onerror request request exception e override public void onresponse string response post请求 java okhttputils post url url addparams username hyman addparams password 123 build execute callback post json java okhttputils poststring url url content new gson tojson new user zhy 123 mediatype mediatype parse application json charset utf 8 build execute new mystringcallback 提交一个gson字符串到服务器端，注意：传递json的时候，不要通过addheader去设置contenttype，而使用 mediatype mediatype parse application json charset utf 8 。 post file java okhttputils postfile url url file file build execute new mystringcallback 将文件作为请求体，发送到服务器。 post表单形式上传文件 java okhttputils post addfile mfile messenger 01 png file addfile mfile test1 txt file2 url url params params headers headers build execute new mystringcallback 支持单个多个文件，addfile的第一个参数为文件的key，即类别表单中 input type file name mfile 的name属性。 自定义callback 目前内部包含stringcallback filecallback bitmapcallback，可以根据自己的需求去自定义callback，例如希望回调user对象： java public abstract class usercallback extends callback override public user parsenetworkresponse response response throws ioexception string string response body string user user new gson fromjson string user class return user okhttputils get url url addparams username hyman addparams password 123 build execute new usercallback override public void onerror request request exception e mtv settext onerror e getmessage override public void onresponse user response mtv settext onresponse response username 通过parsenetworkresponse回调的response进行解析，该方法运行在子线程，所以可以进行任何耗时操作，详细参见sample。 下载文件 java okhttputils get url url build execute new filecallback environment getexternalstoragedirectory getabsolutepath gson 2 2 1 jar override public void inprogress float progress mprogressbar setprogress int 100 progress override public void onerror request request exception e log e tag onerror e getmessage override public void onresponse file file log e tag onresponse file getabsolutepath 注意下载文件可以使用filecallback，需要传入文件需要保存的文件夹以及文件名。 显示图片 java okhttputils get url url build execute new bitmapcallback override public void onerror request request exception e mtv settext onerror e getmessage override public void onresponse bitmap bitmap mimageview setimagebitmap bitmap 显示图片，回调传入bitmapcallback即可。 上传下载的进度显示 java new callback t override public void inprogress float progress use progress 0 1 callback回调中有inprogress方法，直接复写即可。 head、delete、put、patch java okhttputils put also can use delete head patch requestbody requestbody create null may be something build execute new mystringcallback 如果需要requestbody，例如：put、patch，自行构造进行传入。 同步的请求 response response okhttputils get url url tag this build execute execute方法不传入callback即为同步的请求，返回response。 取消单个请求 java requestcall call okhttputils get url url build call cancel 根据tag取消请求 目前对于支持的方法都添加了最后一个参数object tag，取消则通过okhttputils canceltag tag 执行。 例如：在activity中，当activity销毁取消请求： okhttputils get url url tag this build override protected void ondestroy super ondestroy 可以取消同一个tag的 okhttputils canceltag this 取消以activity this作为tag的请求 比如，当前activity页面所有的请求以activity对象作为tag，可以在ondestory里面统一取消。 混淆 okhttputils dontwarn com zhy http keep class com zhy http okhttp dontwarn okhttp3 keep class okhttp3 okio dontwarn okio keep class okio