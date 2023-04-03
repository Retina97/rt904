from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import Candidate, Voter, Vote, Voting_bureau

# Register your models here.
admin.site.register([Candidate, Voter, Voting_bureau])

admin.site.register(User, UserAdmin)