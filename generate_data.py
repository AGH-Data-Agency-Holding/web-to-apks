import urllib.request
import json
from pathlib import Path

apps_data = [
    {"name": "Quran Majeed", "slug": "quran-majeed", "cat": "Spiritualité & Audio", "icon": "fa-book-quran", "desc": "Lecture complète, audio hors-ligne et récitations authentiques."},
    {"name": "Face Editor", "slug": "face-editor", "cat": "AI & Retouche", "icon": "fa-wand-magic-sparkles", "desc": "Retouche photo et filtres IA autonomes sur mobile."},
    {"name": "Winning Items", "slug": "winning-items", "cat": "E-Commerce", "icon": "fa-chart-line", "desc": "Détecteur de produits gagnants et analyse tendances e-commerce."},
    {"name": "Hair Changer", "slug": "hair-changer", "cat": "AI & Beauté", "icon": "fa-scissors", "desc": "Essayage virtuel de coupes de cheveux et styles par IA."},
    {"name": "Prophets Stories", "slug": "prophets-stories", "cat": "Éducation", "icon": "fa-landmark", "desc": "Histoires des prophètes interactives avec audio intégré."},
    {"name": "BIO Skin Care", "slug": "bio-skin-care", "cat": "Santé & Bio", "icon": "fa-spa", "desc": "Diagnostics de peau personnalisés et soins 100% naturels."},
    {"name": "DIET Weight Loss", "slug": "diet-weight-loss", "cat": "Santé & Régime", "icon": "fa-weight-scale", "desc": "Coach minceur, calcul calorique et programmes adaptés."},
    {"name": "Food Recipes", "slug": "food-recipes", "cat": "Cuisine", "icon": "fa-utensils", "desc": "Recettes saines, idées repas rapides et guide nutritionnel."},
    {"name": "Halal Recipes", "slug": "halal-recipes", "cat": "Cuisine & Ramadan", "icon": "fa-bowl-rice", "desc": "Recettes halal certifiées et menus gourmands de Ramadan."},
    {"name": "Study Helper", "slug": "study-helper", "cat": "Éducation & IA", "icon": "fa-graduation-cap", "desc": "Assistant pédagogique IA et tuteur d'étude interactif."},
    {"name": "Therapy AI", "slug": "therapy-ai", "cat": "Bien-être & IA", "icon": "fa-heart-pulse", "desc": "Écoute bienveillante, relaxation et gestion du stress par IA."},
    {"name": "Virtual Try On", "slug": "virtual-tryon", "cat": "Mode & Dressing", "icon": "fa-shirt", "desc": "Essayage virtuel de vêtements et stylisme intelligent."},
    {"name": "Home Design", "slug": "home-design", "cat": "Maison & Déco", "icon": "fa-couch", "desc": "Conception d'intérieurs, aménagement 3D et déco maison."},
    {"name": "Prayer Guide", "slug": "prayer-guide", "cat": "Spiritualité", "icon": "fa-mosque", "desc": "Horaires de prière précis, boussole Qibla et rappels."},
    {"name": "Ruqyah Dua", "slug": "ruqyah-dua", "cat": "Spiritualité & Audio", "icon": "fa-hands-praying", "desc": "Invocations prophétiques, versets de protection et audio."},
    {"name": "Baby Food", "slug": "baby-food", "cat": "Famille & Bébé", "icon": "fa-baby", "desc": "Alimentation infantile, diversification et repas équilibrés."},
    {"name": "Quit Vaping", "slug": "quit-vaping", "cat": "Santé & Sevrage", "icon": "fa-ban-smoking", "desc": "Accompagnement quotidien pour arrêter la vape et tabac."},
    {"name": "Home Workout", "slug": "home-workout", "cat": "Fitness & Sport", "icon": "fa-dumbbell", "desc": "Entraînements à la maison sans matériel et programmes HIIT."},
    {"name": "Medical AI", "slug": "medical-ai", "cat": "Santé & Médecine IA", "icon": "fa-user-doctor", "desc": "Analyse médicale préventive et orientation santé IA."},
    {"name": "Fun Rush", "slug": "fun-rush", "cat": "Jeux & Arcade", "icon": "fa-gamepad", "desc": "Jeux d'arcade et défis réflexes pour toute la famille."},
    {"name": "Tontine", "slug": "tontine", "cat": "Finance & Épargne", "icon": "fa-coins", "desc": "Gestion sécurisée de tontines et épargne communautaire."},
    {"name": "Chbe3ni", "slug": "chbe3ni", "cat": "Restauration", "icon": "fa-burger", "desc": "Guide gourmand, commandes et découvertes culinaires locales."},
    {"name": "Golden Adv", "slug": "golden-adv", "cat": "Business & Pub", "icon": "fa-bullhorn", "desc": "Campagnes publicitaires et leviers d'acquisition marketing."},
    {"name": "MyZine", "slug": "myzine", "cat": "Médias & News", "icon": "fa-newspaper", "desc": "Magazine interactif d'actualités et contenus exclusifs."}
]

out_list = []
print("Audit des 24 applications sur Cloudflare R2...")
for app in apps_data:
    slug = app["slug"]
    url = f"https://download.datagenere.com/apks/{slug}-latest.apk"
    app["url"] = url
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        res = urllib.request.urlopen(req, timeout=5)
        cl = int(res.headers.get("Content-Length", 0))
        lm = res.headers.get("Last-Modified", "")
        app["available"] = True
        app["size_mb"] = round(cl / (1024 * 1024), 1)
        app["last_modified"] = lm
        print(f"  [OK] {app['name']} ({slug}) -> {app['size_mb']} Mo")
    except Exception:
        app["available"] = False
        app["size_mb"] = None
        app["last_modified"] = None
        print(f"  [KO] {app['name']} ({slug}) -> Non disponible")
    out_list.append(app)

dest = Path(r"F:\web-to-apks\apps.json")
with open(dest, "w", encoding="utf-8") as f:
    json.dump(out_list, f, indent=2, ensure_ascii=False)

print(f"Fichier généré avec succès : {dest}")
