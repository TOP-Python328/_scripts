from django.http import HttpResponse


def main(request):
    breakpoint()
    return HttpResponse('<h1>Hello World!</h1>')


page = '''
<html>
<head>
  <title>Страница</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div align="center">
    <h2>Главная страница</h2>
    <p>Какой-то текст, который должен приветствовать посетителя.</p>
    <button onclick="test()">Кнопка</button>
  </div>
  <script>
    function test() {
      console.log("JS работает!")
    }
  </script>
</body>
</html>
'''


def next_page(request):
    return HttpResponse(page)

