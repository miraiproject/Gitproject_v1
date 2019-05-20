### GitProject
みんなで開発をして、楽しくプログラミングを勉強していきましょう！

# 皆さんにいじってほしい各ファイルの場所

各々のファイルはgitproject_v1/demo/temprate/demo　の中にhtmlファイルが
gitproject_v1/demo/static/demoの中にCSSファイルが用意されています。
適宜変更して使ってください。
また、htmlファイル内の
```
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'demo/top_page.css' %}">
````
みたいな記述は、cssを呼び出しているので、消さないでください！
