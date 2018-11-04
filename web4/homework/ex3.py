from river import River
import mlabex1

mlabex1.connect()

rivers_list = River.objects(continent="Africa", length__lt=1000)
for p in rivers_list:
    print(p.name)
    print(p.continent)
    print(p.length)
    print("* * * * * * * * *") 