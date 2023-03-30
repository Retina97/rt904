from django.contrib import admin

from .models import Candidate, Voter, Vote, Voting_bureau

# Register your models here.
admin.site.register([Candidate, Voter, Voting_bureau])
