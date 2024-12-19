import bevezetes, sorozat, epuletek, Epulet


"""bevezetes.adatbekeres()

fejek=sorozat.fejek_szama()

sorozat.konzol_kiir(fejek)

sorozat.file_kiir(fejek)"""


epuletek_lista = epuletek.beolvasas()
m = epuletek.magas_epuletek_szama(epuletek_lista)
legoregebb = epuletek.legoregebb_epulet_orszaga(epuletek_lista)
(epuletek_lista, m, legoregebb)
