We are given following url - https://agent-keith.web.chal.hsctf.com

```
$ python
>>> import requests
>>> res = requests.get("https://agent-keith.web.chal.hsctf.com")
>>> print(res.text)
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
        <title>agent-keith</title>
        <link rel="stylesheet" href="http://localhost:8002/static/style.css">
    </head>
    <body>
        <main>
            <h2>If you're not Keith, you won't get the flag!</h2>
            <p><b>Your agent is:</b> python-requests/2.19.1</p>
            <p><b>Flag:</b> Access Denied</p>
            <!-- DEBUG (remove me!!): NCSA_Mosaic/2.0 (Windows 3.1) -->
        </main>
    </body>
</html>
>>> # We just have to change the user agent in the request header to one mentioned in html comment
>>> res = requests.get("https://agent-keith.web.chal.hsctf.com", headers={"User-Agent": "NCSA_Mosaic/2.0 (Windows 3.1)"})
>>> print(res.text)
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
        <title>agent-keith</title>
        <link rel="stylesheet" href="http://localhost:8002/static/style.css">
    </head>
    <body>
        <main>
            <h2>If you're not Keith, you won't get the flag!</h2>
            <p><b>Your agent is:</b> NCSA_Mosaic/2.0 (Windows 3.1)</p>
            <p><b>Flag:</b> hsctf{wow_you_are_agent_keith_now}</p>
            <!-- DEBUG (remove me!!): NCSA_Mosaic/2.0 (Windows 3.1) -->
        </main>
    </body>
</html>
```
Flag - hsctf{wow_you_are_agent_keith_now}
