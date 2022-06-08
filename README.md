# boringssl_mitm
build mitm with boringssl
1. 使用boringssl进行mitmproxy的编译，同时搭配修改tlsconfig进行tls指纹的bypass。
2. 只能针对单个网站的tls指纹进行模拟，在iOS的app上进行过测试。
3. 针对不同的网站的不同的tls指纹还需要看情况进行源码的修改以进行适配。
4. 在进行编译的过程中删去了部分api。
