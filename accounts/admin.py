from django.contrib import admin
from sbs.models.Athlete import Athlete
from sbs.models.DirectoryMember import DirectoryMember
from sbs.models.SportClubUser import SportClubUser
from sbs.models.Coach import Coach
from sbs.models.Judge import Judge
from sbs.models.Person import Person

from sbs.models.Abirim import Abirim
from sbs.models.Aevrak import Aevrak
from sbs.models.AbirimParametre import AbirimParametre
from sbs.models.Adosya import Adosya
from sbs.models.Aklasor import Aklasor
from sbs.models.AdosyaParametre import AdosyaParametre

admin.site.site_header = 'Kobiltek Bilisim Kullanici Yönetim Paneli '  # default: "Django Administration"
admin.site.index_title = 'Sistem Yönetimi'  # default: "Site administration"
admin.site.site_title = 'Admin'  # default: "Django site admin"

admin.site.register(Abirim)
admin.site.register(Adosya)
admin.site.register(Aklasor)
admin.site.register(AbirimParametre)
admin.site.register(AdosyaParametre)
admin.site.register(Aevrak)
