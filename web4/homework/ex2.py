from river import River
import mlabex1

mlabex1.connect()

rivers_list = River.objects(continent="Africa")
for p in rivers_list:
    print(p.name)
    print(p.continent)
    print(p.length)
    print("* * * * * * * * *") 