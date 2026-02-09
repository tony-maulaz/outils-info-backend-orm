# Exercice : pratiquer ORM + SQL brut (FastAPI)

Objectif : etendre le mini projet ORM pour manipuler des requetes SQL et ORM, tout en gardant la validation via schemas Pydantic.

## Ce que vous devez produire
Ajoutez de nouveaux endpoints dans des fichiers separes (ou dans les fichiers existants) :
- une requete SQL brute avec filtre
- une requete ORM avec filtre
- une requete ORM avec jointure + aggregation

## Consignes
- Utiliser les schemas Pydantic pour valider les entrees/sorties.
- Garder les routes par theme (raw_sql.py, orm_simple.py, orm_join.py).
- Tester dans Swagger UI (/docs).

## Endpoints a ajouter (suggestion)

### 1) SQL brut avec filtre
`GET /raw/books/search?title=...`
- retourne les livres dont le titre contient le texte
- requete SQL avec `LIKE`
- reponse : liste de `BookSummary`

### 2) ORM simple avec filtre
`GET /orm/books/search?min_pages=...`
- retourne les livres avec `pages >= min_pages`
- reponse : liste de `BookOut`
- valider `min_pages` (>= 1)

### 3) ORM avec jointure + aggregation
`GET /orm/authors-with-count`
- retourne chaque auteur avec le nombre de livres
- utiliser une jointure + `COUNT`
- schema de reponse :
  - `author_id: int`
  - `author_name: str`
  - `book_count: int`

## Checklist de validation
- Les nouveaux endpoints apparaissent dans Swagger UI
- Les validations Pydantic renvoient bien 422 si les donnees sont invalides
- Les endpoints avec filtre retournent les bonnes listes
- L'endpoint d aggregation affiche un comptage correct
