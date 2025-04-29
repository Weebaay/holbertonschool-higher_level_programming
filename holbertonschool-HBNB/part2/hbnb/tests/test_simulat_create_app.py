def create_place(self, place_data):
    try:
        # Vérifiez si le propriétaire existe
        owner = self.get_user(place_data['owner_id'])
        if not owner:
            # Créez un utilisateur simulé si le propriétaire n'existe pas
            owner = User(first_name="Simulated", last_name="Owner", email="simulated@example.com")
            owner.id = place_data['owner_id']
            self.user_repo.add(owner)
            print(f"Utilisateur simulé ajouté avec ID={owner.id}")
        
        # Associez le propriétaire au lieu
        place_data['owner'] = owner
        place = Place(**place_data)
        self.place_repo.add(place)
        return place
    except ValueError as e:
        raise ValueError(f"Invalid input data for place: {str(e)}")
