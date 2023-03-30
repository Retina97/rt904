from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    party = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom+' - '+self.party

class Voting_bureau(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Voter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    bureau_id = models.ForeignKey(Voting_bureau, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter =  models.ForeignKey(Voter, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.voter_id.name+' - '+self.candidate_id.nom