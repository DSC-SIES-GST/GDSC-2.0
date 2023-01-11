from django.shortcuts import get_object_or_404, render, redirect
from .models import Domain, Member
# Create your views here.


def index(request):
    domains = Domain.objects.filter(is_active=True)
    print(domains)
    context = {
        'domains': domains
    }
    return render(request, 'teams/teams.html', context)


def team(request, slug):
    if (Domain.objects.filter(title=slug, is_active=True)):
        members = Member.objects.filter(slug=slug, is_active=True)
        domain_name = Domain.objects.filter(title=slug, is_active=True).first()
        context = {
            'domain_name': domain_name,
            'members': members
        }
        return render(request, 'teams/team.html', context)
    else:
        return redirect('teams')
