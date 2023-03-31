from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import *
from django.http import JsonResponse
from google.cloud import functions_v1
import requests
import json


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'home.html')

def get_cadidates_list():
    gcp_url = 'https://europe-west1-rare-sunrise-381713.cloudfunctions.net/function-2'
    response = requests.get(gcp_url)
    candidates = response.json()['candidates']
    return candidates

def get_candidates(request):
    context={'candidates' : get_cadidates_list()} 
    return render(request, 'candidates.html', context=context)

def get_votes(request):
    # Appeler la fonction get_votes sur GCP
    gcp_url = 'https://europe-west1-rare-sunrise-381713.cloudfunctions.net/function-4'
    print(gcp_url)
    response = requests.get(gcp_url)
    votes = response.json()['votes']
    context={'votes' : votes} 
    return render(request, 'results.html', context=context)

def vote(request):
    if request.method == 'POST':
        candidate_id = int(request.POST['candidate_id'])
        print(candidate_id)
        voter_id = int(request.user.id)
        print(voter_id)
        # Appel de la fonction cloud pour enregistrer le vote
        """functions_client = functions_v1.CloudFunctionsServiceClient()
        parent = functions_client.cloud_function_path('rare-sunrise-381713', 'europe-west1', 'function-3')
        data = {'candidate_id': candidate_id, 'voter_id': voter_id}
        response = functions_client.call_function(name=parent, data=data)"""
        post_data = {"candidate_id": candidate_id, "voter_id": voter_id}
        response = requests.post('https://europe-west1-rare-sunrise-381713.cloudfunctions.net/function-3', json=post_data)
        content = response.content
        
        return redirect('/results')
    
    context={'candidates' : get_cadidates_list()} 
    return render(request, 'vote.html', context=context)