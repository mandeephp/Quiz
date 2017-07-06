from django.conf.urls import url
from django_pdfkit import PDFView
from . import views

urlpatterns=[

	url(r'^index/', views.index,name='index'),	
	url(r'^compare/(?P<id>\d+)/$', views.compare, name='compare'),
	url(r'^solution/', views.Solution, name='solution'),
	url(r'^solutionCSI/', views.SolutionCSI, name='solutionCSI'),
	url(r'^solutionCSA/', views.SolutionCSA, name='solutionCSA'),
	url(r'^solutionNW/', views.SolutionNW, name='solutionNW'),
	url(r'^solutionNWI/', views.SolutionNWI, name='solutionNWI'),
	url(r'^solutionNWA/', views.SolutionNWA, name='solutionNWA'),
	url(r'^solutionLX/', views.SolutionLX, name='solutionLX'),
	url(r'^solutionLXA/', views.SolutionLXA, name='solutionLXA'),
	url(r'^solutionLXI/', views.SolutionLXI, name='solutionLXI'),
	url(r'^solution/', views.Solution, name='solution'),
	url(r'^CS/', views.Computer_Science,name='Computer_Science'),
	url(r'^CSI/', views.Computer_Science_Intermediate,name='Computer_Science_Intermediate'),
	url(r'^CSA/', views.Computer_Science_Advance,name='Computer_Science_Advance'),
	url(r'^NW/', views.Networking,name='Networking'),
	url(r'^NWI/', views.Networking_Intermediate,name='Networking_Intermediate'),
	url(r'^NWA/', views.Networking_Advance,name='Networking_Advance'),
	url(r'^LX/', views.Linux,name='Linux'),
	url(r'^LXI/', views.Linux_Intermediate,name='Linux_Intermediate'),
	url(r'^LXA/', views.Linux_Advance,name='Linux_Advance'),
	url(r'^EP/', views.Electronic_Principal,name='Electronic_Principal'),
	url(r'^login/', views.login_view,name='login'),
	url(r'^signup/', views.register_view,name='signup'),
	url(r'^logout/', views.logout_view,name='logout', ),	
	url(r'^my-pdf/', PDFView.as_view(template_name='my-pdf.html'), name='my-pdf'),
	url(r'^CSO/', views.Computer_Science_Options,name='Computer_Science_Options'),
	url(r'^LXO/', views.Linux_Options,name='Linux_Options'),
	url(r'^NWO/', views.Networking_Options,name='Networking_Options'),
	url(r'^EPO/', views.Electronic_Options,name='Electronic_Options'),
	url(r'^ses/', views.sessionss),
	url(r'^userid/', views.Current_user_id),
	url(r'^ajax/$', views.advert, name ='ajax'),


]
