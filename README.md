# 4-es labor

N-királynő problémája Sosic és Gu 1990-es cikkje alapján

      Az algoritmus N darab királynőt helyez el egy NxN es sakktáblán, úgy hogy egyikük se tudja támadni egymást.
Kezdetben generálunk egy 0 tól ... N-1 ig tartó véletlenszerű számkombinációt. Minden q[i] elem az reprezentál egy királynőt az i-ik oszlop-ba
q[i]-es értékű sorindexel.

      Eleine kiszámoljuk, hogy az elhelyezett királynők közül, hány üti egymást, főátlók és mellékátlókat tekintve. (Összesen 2*N-1 átló)
elmentjük egy listába, hogy hány darab királynő képes támadni. Miután ez megtörtént sorra vesszük a királynőket páronként, azokat amelyek tá-
madva voltak. Ha ezek felcserélésével, csökkenne az ütközések száma akkor végrehajtsuk a cserét máskülönben elvetjük, mindezt addig ismételve amíg egy ütközés se lesz,
ekkor kapjuk meg tulajdonképpen a végeredményt ahol az N darab királynő biztonságosan van elhelyezve.
