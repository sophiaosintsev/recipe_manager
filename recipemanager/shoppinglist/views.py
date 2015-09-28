from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse, HttpResponse
from .models import ShoppingList
from django.core import serializers


def shoppinglist(request):
    return render(
        request,
        'shoppinglist.html',
    )


@login_required
def get_shoppinglist(request):
    if request.method == 'GET':
        # Check to see if user has shopping list, if yes, send it back
        data = ShoppingList.objects.filter(user=request.user)
        shoppinglist = serializers.serialize("json", data)
        if data:
            return HttpResponse(shoppinglist, content_type='application/json'
            )
        else:
            JsonResponse(
                []
            )
    elif request.method == 'POST':
        shoppinglist = json.loads(request.body)
        data = ShoppingList.objects.filter(user=request.user)
        # This is the users shopping list
        if data:
            data[0].item = shoppinglist
            # Save/Update list
            data[0].save()
            return JsonResponse(
                {"result": "List has been saved!"}
            )
        else:
            # This is the first time user is creating a list
            # Create new model, set the item and save
            shoplist = ShoppingList.objects.create(item='newlist', user=request.user)
            shoplist.save()
            return JsonResponse(
                {"result": "List has been saved!"}
            )
