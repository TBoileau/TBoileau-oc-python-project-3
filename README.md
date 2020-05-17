OpenClassrooms - DA Python - Projet 3
=====================================

# Pré-requis

* Python 3.7.7 ou plus

*Note : attention, dans certains cas il est possible que `pygame` ne s'installe pas correctement, car `pygame 1.9.6` n'est pas pris en charge par `Python 3.8`, et il n'existe à ce jour aucune version **LTS** (Long Term Support) pour `Python 3.8`.*

# Installation

Clonez le projet sur votre PC :
```
git clone git@github.com:TBoileau/oc-python-project-3.git
```

Déplacez-vous dans le dossier :
```
cd oc-python-project-3
```

Installez les dépendances avec `pip` :
```
make install
```

# Qualité du code

Lancez `flake8` pour analyser la qualité du code (PEP8) :
```
make coding-style
```

# Tester l'application

Lancez la série de tests unitaires :
```
make test
```

Avec un reporting html :
```
make coverage
```