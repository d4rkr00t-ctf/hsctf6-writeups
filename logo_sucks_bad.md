We are given following image.

![](./data/logo.png)

The main challenge is to know what tool to analyze the png file with. After trying lots of tools, `zsteg` worked!
```
$ zsteg -l 0 logo.png
...ultricies urna. In fringilla hendrerit purus, tristique aliquam ipsum molestie vitae. Sed efficitur auctor lacus ac luctus.\n\nDonec id viverra augue. Vivamus nullhsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}a neque, iaculis quis urna eget, gravida commodo quam. Vestibulum porttitor justo in suscipit rutrum. Sed id tristique ipsum. Nulla vel porta nisl...
```
Flag - hsctf{th4_l3est_s3gnific3nt_bbbbbbbbbbbbb}
