from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.
class GetWeapons(APIView):
     def get(self,request,format=None):
        data = [
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "Desert Eagle",
    "skin_name": "Дракон-предводитель",
    "rarity": "classified",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposr-kLAtl7PLZTjlH_9mkgIWKkPvxDLDEm2JS4Mp1mOjG-oLKhF2zowcDPzixc9OLcw82ZlyF8wC8wb251MW4tcifmydi7CEn4HiPlhyy1BxJbeNshqPIHELeWfJvK5CfiA"
  },
  {
    "weapon_name": "M4A4",
    "skin_name": "Звездный крейсер",
    "rarity": "covert",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou-6kejhnwMzFJTwW08y_m46OkuXLP7LWnn9u5MRjjeyPp4j2iwC38kA9N2j7IIeSe1M9ZQrZ-VS3wefv0ZG_tZXOyHo3uSZ34WGdwUJSqpF9BQ"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "★ Bowie Knife",
    "skin_name": "Убийство",
    "rarity": "rare",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJfwObaZzRU7dCJlo-cnvLLMrbujG5T-sROhuDG_ZjKhFWmrBZyYTygdtTEe1RqYQ3Z8lTtkO6-0JC66czAzCdk73Ym7Hjemh20iREYb_sv26KxNysneA"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "Desert Eagle",
    "skin_name": "Дракон-предводитель",
    "rarity": "classified",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposr-kLAtl7PLZTjlH_9mkgIWKkPvxDLDEm2JS4Mp1mOjG-oLKhF2zowcDPzixc9OLcw82ZlyF8wC8wb251MW4tcifmydi7CEn4HiPlhyy1BxJbeNshqPIHELeWfJvK5CfiA"
  },
  {
    "weapon_name": "M4A4",
    "skin_name": "Звездный крейсер",
    "rarity": "covert",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou-6kejhnwMzFJTwW08y_m46OkuXLP7LWnn9u5MRjjeyPp4j2iwC38kA9N2j7IIeSe1M9ZQrZ-VS3wefv0ZG_tZXOyHo3uSZ34WGdwUJSqpF9BQ"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "Desert Eagle",
    "skin_name": "Дракон-предводитель",
    "rarity": "classified",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposr-kLAtl7PLZTjlH_9mkgIWKkPvxDLDEm2JS4Mp1mOjG-oLKhF2zowcDPzixc9OLcw82ZlyF8wC8wb251MW4tcifmydi7CEn4HiPlhyy1BxJbeNshqPIHELeWfJvK5CfiA"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  },
  {
    "weapon_name": "Desert Eagle",
    "skin_name": "Дракон-предводитель",
    "rarity": "classified",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposr-kLAtl7PLZTjlH_9mkgIWKkPvxDLDEm2JS4Mp1mOjG-oLKhF2zowcDPzixc9OLcw82ZlyF8wC8wb251MW4tcifmydi7CEn4HiPlhyy1BxJbeNshqPIHELeWfJvK5CfiA"
  },
  {
    "weapon_name": "FAMAS",
    "skin_name": "Валентность",
    "rarity": "restricted",
    "steam_image": "http://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgposLuoKhRf0uL3dzxP7c-Jl4-Fg_jhIYTdn2xZ_Pp9i_vG8MKj3VDh-kY9MWr3dYDDdwZtaQnV-Fi4k-vph8e0vcmYzXBlvCNw7X7UgVXp1iHYIfHn"
  }
]

        return JsonResponse(data, status=status.HTTP_200_OK)
