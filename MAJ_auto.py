import paramiko

# Configuration des serveurs
serveurs = [
    {
        'nom': 'Serveur1',
        'adresse': '192.168.1.100',
        'utilisateur': 'votre_utilisateur_ssh',
        'mot_de_passe': 'votre_mot_de_passe_ssh',
        'commandes': [
            'sudo apt update',
            'sudo apt upgrade -y',
        ]
    },
    # Ajoutez d'autres serveurs ici si nécessaire
]

# Fonction pour exécuter des commandes SSH sur un serveur
def executer_commandes_ssh(adresse, utilisateur, mot_de_passe, commandes):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(adresse, username=utilisateur, password=mot_de_passe)
    for commande in commandes:
        stdin, stdout, stderr = ssh.exec_command(commande)
        print(f"Résultat pour {commande}:")
        print(stdout.read().decode())
        print(stderr.read().decode())
    ssh.close()

# Exécution des commandes sur chaque serveur
for serveur in serveurs:
    print(f"Exécution des commandes de maintenance sur {serveur['nom']} ({serveur['adresse']})")
    executer_commandes_ssh(serveur['adresse'], serveur['utilisateur'], serveur['mot_de_passe'], serveur['commandes'])
    print(f"Terminé la maintenance sur {serveur['nom']} ({serveur['adresse']})")

print("Maintenance terminée sur tous les serveurs.")
