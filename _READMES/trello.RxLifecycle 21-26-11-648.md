rxlifecycle this library allows one to automatically complete sequences based on a second lifecycle stream this capability is useful in android where incomplete subscriptions can cause memory leaks usage you must start with an observable t representing a lifecycle stream then you use rxlifecycle to bind a sequence to that lifecycle you can bind when the lifecycle emits anything java myobservable compose rxlifecycle bind lifecycle subscribe or you can bind to when a specific lifecyle event occurs java myobservable compose rxlifecycle binduntilevent lifecycle activityevent destroy subscribe alternatively you can let rxlifecycle determine the appropriate time to end the sequence java myobservable compose rxlifecycleandroid bindactivity lifecycle subscribe it assumes you want to end the sequence in the opposing lifecycle event e g if subscribing during start it will terminate on stop if you subscribe after pause it will terminate at the next destruction event e g pause will terminate in stop providers where do lifecycles come from generally they are provided by an appropriate lifecycleprovider t but where are those implemented you have a few options for that use rxlifecycle components and subclass the provided rxactivity rxfragment etc classes use navi rxlifecycle navi to generate providers use androids lifecycle rxlifecycle android lifecycle to generate providers write the implementation yourself if you use rxlifecycle components just extend the appropriate class then use the built in bindtolifecycle or binduntilevent methods java public class myactivity extends rxactivity override public void onresume super onresume myobservable compose bindtolifecycle subscribe if you use rxlifecycle navi then you just pass your navicomponent to navilifecycle to generate a provider java public class myactivity extends naviactivity private final lifecycleprovider provider navilifecycle createactivitylifecycleprovider this override public void onresume super onresume myobservable compose provider bindtolifecycle subscribe if you use rxlifecycle android lifecycle then you just pass your lifecycleowner to androidlifecycle to generate a provider java public class myactivity extends lifecycleactivity private final lifecycleprovider provider androidlifecycle createlifecycleprovider this override public void onresume super onresume myobservable compose provider bindtolifecycle subscribe unsubscription rxlifecycle does not actually unsubscribe the sequence instead it terminates the sequence the way in which it does so varies based on the type observable flowable and maybe emits oncompleted single and completable emits onerror cancellationexception if a sequence requires the subscription unsubscribe behavior then it is suggested that you manually handle the subscription yourself and call unsubscribe when appropriate kotlin the rxlifecycle kotlin module provides built in extensions to the base rxjava types kotlin myobservable bindtolifecycle myview subscribe myobservable binduntilevent myrxactivity stop subscribe there is an additional rxlifecycle android lifecycle kotlin module to provider extensions to work with livecycleowners kotlin myobservable binduntilevent mylifecycleactivity on stop subscribe installation gradle compile com trello rxlifecycle2 rxlifecycle 2 2 1 if you want to bind to android specific lifecycles compile com trello rxlifecycle2 rxlifecycle android 2 2 1 if you want pre written activities and fragments you can subclass as providers compile com trello rxlifecycle2 rxlifecycle components 2 2 1 if you want pre written support preference fragments you can subclass as providers compile com trello rxlifecycle2 rxlifecycle components preference 2 2 1 if you want to use navi for providers compile com trello rxlifecycle2 rxlifecycle navi 2 2 1 if you want to use android lifecycle for providers compile com trello rxlifecycle2 rxlifecycle android lifecycle 2 2 1 if you want to use kotlin syntax compile com trello rxlifecycle2 rxlifecycle kotlin 2 2 1 if you want to use kotlin syntax with android lifecycle compile com trello rxlifecycle2 rxlifecycle android lifecycle kotlin 2 2 1 license copyright c 2016 trello licensed under the apache license version 2 0 the license you may not use this file except in compliance with the license you may obtain a copy of the license at http www apache org licenses license 2 0 unless required by applicable law or agreed to in writing software distributed under the license is distributed on an as is basis without warranties or conditions of any kind either express or implied see the license for the specific language governing permissions and limitations under the license