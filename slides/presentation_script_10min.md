# Présentation 10 minutes

## Utilisation

- Ce script suit l'ordre actuel de `slides/main.tex`.
- La partie principale tient en environ 9 à 10 minutes si le rythme reste simple.
- La partie `Annexe` est prévue pour les questions ou si vous voulez détailler les modules.

---

## 1. Titre

Bonjour, aujourd'hui on va présenter notre projet de comparaison entre un CNN classique, AlexNet, et une architecture de type transformer, (Dynamic Hybrid Vision Transformer) DHVT, pour la classification d'images.

L'idée générale est de voir comment rendre un modèle de type ViT plus efficace sur un petit dataset.

---

## 2. Plan

La présentation est organisée en trois parties.

D'abord, on rappelle rapidement l'idée du CNN et la logique générale de DHVT.
Ensuite, on montre les résultats principaux.
Enfin, on termine par la conclusion.

---

## 3. Question du projet

Notre objectif est de comparer deux familles de modèles.

D'un côté, AlexNet, qui est un baseline CNN classique.
De l'autre, DHVT, qui est un transformer modifié.

La question centrale est la suivante :
Comment conserver les avantages des Transformers tout en les adaptant à des ensembles de données plus petits, en s’inspirant des convolutions ?

---

## 4. Point de départ : le CNN

On commence par le CNN.

AlexNet repose sur la convolution.
Son point fort est qu'il apprend naturellement des motifs locaux, donc des textures, des contours, et des structures proches dans l'image.

C'est très adapté à la vision.
Mais sa limite, c'est qu'il capture moins directement les relations globales entre régions éloignées.

Donc ici, on peut résumer :
le CNN est naturellement fort pour le local.

---

## 5. Vue d'ensemble de DHVT

Maintenant, on passe à DHVT.

L'idée de transition est simple.

Le CNN est bon pour le local.
Le ViT standard est bon pour le global.
Mais sur de petites images, un ViT standard est souvent trop brutal au début.

DHVT essaie donc de combiner les deux :
garder la partie globale du transformer, tout en réintroduisant une partie de la logique locale du CNN.

Concrètement :

- SOPE(Sequential Overlapping Patch Embedding) ajoute une entrée plus proche d'une logique convolutionnelle
- HI-MHSA(Head-Interacted Multi-Head Self-Attention) garde et organise la partie globale
- DAFF(Dynamic Aggregation Feed Forward) remet de la convolution dans le bloc interne

Autrement dit, DHVT peut être résumé comme :
transformer global + biais local inspiré du CNN.

---

## 6. Résumé de la structure

Cette diapositive résume les trois modifications.

SOPE(Sequential Overlapping Patch Embedding) agit sur l'entrée.
HI-MHSA agit sur l'attention.
DAFF(Dynamic Aggregation Feed Forward) agit sur le bloc interne.

Le message important ici est simple :
DHVT ne supprime pas la logique transformer.
Il la garde, mais il ajoute des éléments qui permettent de mieux traiter les petites images.

---

## 7. Résultat principal

On passe maintenant aux résultats.

Le résultat principal est que DHVT est meilleur qu'AlexNet sur CIFAR-10 et sur CIFAR-100.

Sur CIFAR-10, l'écart existe déjà.
Mais sur CIFAR-100, il devient beaucoup plus grand.

C'est important, parce que CIFAR-100 est une tâche plus difficile.

Un autre point intéressant est que DHVT est aussi beaucoup plus compact qu'AlexNet en nombre de paramètres.

Donc on obtient à la fois de meilleures performances et un modèle plus léger.

---

## 8. Courbes de validation CIFAR-100

Cette figure est probablement la plus importante de toute la présentation.

On voit que DHVT apprend plus vite.
Et surtout, il reste au-dessus d'AlexNet pendant tout l'entraînement.

Donc son avantage n'apparaît pas seulement à la fin.
Il est visible pendant toute la dynamique d'apprentissage.

Cela renforce l'idée que l'architecture elle-même est plus adaptée à cette tâche.

---

## 9. Confiance des prédictions

Ici, on regarde non seulement le score final, mais aussi la qualité des prédictions.

DHVT sépare mieux les bonnes et les mauvaises prédictions.
Donc ses scores de confiance sont plus cohérents.

Autrement dit, quand DHVT prédit avec confiance, cette confiance est plus souvent justifiée.

Cela complète l'analyse du simple accuracy.

---

## 10. Gain par classe

Cette figure montre que le gain de DHVT n'est pas concentré sur seulement quelques classes faciles.

L'écart est positif pour toutes les classes.

Donc l'avantage de DHVT est global.
Ce n'est pas un résultat dû à deux ou trois catégories particulières.

---

## 11. Exemples d'erreurs

Ici, on montre des cas difficiles.

Cette figure est utile parce qu'elle rend la différence entre les deux modèles plus concrète.

Dans plusieurs exemples, DHVT corrige une erreur d'AlexNet.
Mais on voit aussi que certaines erreurs restent difficiles pour tout le monde, surtout quand l'image est petite, floue ou ambiguë.

Donc cette diapositive montre à la fois les gains de DHVT et les limites du problème.

---

## 12. Cartes d'attention

Cette diapositive permet de voir où DHVT regarde.

Sur les bons exemples, l'attention tombe souvent sur l'objet principal ou sur une partie discriminante de l'objet.

Sur les erreurs, l'attention devient souvent plus diffuse.

Cette figure ne prouve pas tout à elle seule, mais elle donne une lecture qualitative cohérente avec les résultats précédents.

---

## 13. Variantes de CIFAR-100

Ici, on a voulu tester si l'avantage de DHVT restait visible quand on modifie la difficulté visuelle.

On a donc construit plusieurs variantes :
`clean`, `texture`, `damaged_occluded` et `long_range`.

Le résultat est clair :
DHVT reste meilleur sur toutes les variantes.

L'avantage est maximal sur `clean`, mais il reste présent dans tous les autres cas.

Donc le gain n'est pas limité à une seule situation.

---

## 14. Conclusion

Pour conclure :

Le CNN est naturellement fort pour le local.
Le ViT est naturellement fort pour le global.
DHVT essaie de combiner les deux.

Et dans nos expériences, cela fonctionne :
DHVT obtient de meilleurs résultats qu'AlexNet, surtout quand la tâche devient plus difficile.

Le message final est donc que DHVT constitue ici une meilleure architecture que le baseline CNN classique pour ce cadre expérimental.

---

## 15. Références

Ici, on peut simplement dire que les trois références principales sont :

- AlexNet
- ViT
- DHVT

Et que les liens sont cliquables dans le PDF.

Ne passez pas de temps ici, sauf si on vous pose une question.

---

## 16. Merci

Merci pour votre attention.
Nous sommes prêts à répondre aux questions.

---

# Annexe

## Comment utiliser l'annexe

- Cette partie n'est pas nécessaire dans les 10 minutes principales.
- Elle sert si l'enseignant demande plus de détails sur l'architecture.
- Vous pouvez ouvrir directement la page correspondante depuis les hyperliens dans la partie principale.

---

## Annexe A. SOPE

Si on me demande ce qu'est SOPE, je peux répondre comme ça :

SOPE modifie l'entrée du modèle.
Au lieu d'envoyer directement des patches trop indépendants, il introduit une entrée plus proche d'une logique convolutionnelle.

Donc on garde davantage d'information locale dès le début.

L'idée est simple :
avant même l'attention, on veut que les tokens d'entrée soient déjà mieux adaptés aux petites images.

---

## Annexe B. HI-MHSA

Si on me demande ce qu'est HI-MHSA, je peux dire :

HI-MHSA modifie le bloc d'attention.
Il garde la logique globale du transformer, mais il organise mieux cette information avec les head tokens.

Donc, parmi les trois modules, c'est celui qui reste le plus du côté transformer.

Son rôle principal est de mieux structurer l'information globale avant la classification finale.

---

## Annexe C. DAFF

Si on me demande ce qu'est DAFF, je peux dire :

DAFF remplace le FFN standard du transformer.
Et surtout, il remet explicitement de la convolution dans le bloc interne.

Donc DAFF est une manière très claire de réintroduire une logique de type CNN à l'intérieur du transformer.

On peut dire que SOPE agit surtout à l'entrée, alors que DAFF agit à l'intérieur du bloc.

---

## Résumé oral très court

Si vous devez résumer toute l'architecture en une phrase :

`DHVT = transformer pour le global + idées inspirées du CNN pour le local.`
