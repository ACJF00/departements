import requests
from PIL import Image
from io import BytesIO
import os

# Your data with the correct field name
images = [
  {"code": "01", "nom": "Ain", "chef_lieu": "Bourg-en-Bresse", "image": "https://office-de-tourisme-de-france.org/wp-content/uploads/2023/08/bourg-en-bresse.webp"},
  {"code": "02", "nom": "Aisne", "chef_lieu": "Laon", "image": "https://enfranceaussi.fr/wp-content/uploads/2020/11/toits-laon.jpg"},
  {"code": "03", "nom": "Allier", "chef_lieu": "Moulins", "image": "https://www.detoursenfrance.fr/patrimoine/destinations/regions/auvergne-rhone-alpes/10-bonnes-raisons-de-visiter-moulins-1043404#public://2023/12/07/moulinsvuegeuneuralejean-marcteissonnierweb-6571e862393e9.jpg-0"},
  {"code": "04", "nom": "Alpes-de-Haute-Provence", "chef_lieu": "Digne-les-Bains", "image": "https://www.ubaye.com/csx/scripts/resizer.php?filename=T003_APP003%2Fsnippetimage%2Fa7%2F57%2Fgfx5t79chqi5&mime=image%252Fjpeg&originalname=Barcelonnette-en-hiver-%28c%29Brendan-Le-Peru.jpg&geometry=730x%3E&crop=x533"},
  {"code": "05", "nom": "Hautes-Alpes", "chef_lieu": "Gap", "image": "https://www.provenceweb.fr/img/containers/images/villages-hd/05/gap/3_g-gap.jpg/feb80e0d0a04925204d0368220905359.jpg"},
  {"code": "06", "nom": "Alpes-Maritimes", "chef_lieu": "Nice", "image": "https://static-cms.routard.com/web-routard/uploads/xlarge_nice_1466255_d6980c20c2.jpg"},
  {"code": "07", "nom": "Ardèche", "chef_lieu": "Privas", "image": "https://media.routard.com/image/58/5/ardeche-vallon-pont-arc.1584585.w740.jpg"},
  {"code": "08", "nom": "Ardennes", "chef_lieu": "Charleville-Mézières", "image": "https://www.charleville-sedan-tourisme.fr/wp-content/uploads/2018/04/la-place-ducale-de-charleville-mezieres-petite-soeur-de-la-place-des-vosges-a-paris-1600x900.jpg"},
  {"code": "09", "nom": "Ariège", "chef_lieu": "Foix", "image": "https://www.jolieslueurs.com/wp-content/uploads/2022/01/SAINT-LIZIER-ARIEGE-13-2048x1152.jpg"},
  {"code": "10", "nom": "Aube", "chef_lieu": "Troyes", "image": "https://www.explore-grandest.com/wp-content/uploads/2021/10/emile-zola-studio-og-6-scaled-1-1024x768.jpg"},
  {"code": "11", "nom": "Aude", "chef_lieu": "Carcassonne", "image": "https://www.leboat.fr/sites/default/files/styles/lbt_imgstyle_gallery_lg/public/info/media/midi-carcassonne-cite-800x430.jpg?itok=NrMisvP_&timestamp=1690298433"},
  {"code": "12", "nom": "Aveyron", "chef_lieu": "Rodez", "image": "https://www.ville-rodez.fr/uploads/2022/02/musee-soulage-cathedrale.webp"},
  {"code": "13", "nom": "Bouches-du-Rhône", "chef_lieu": "Marseille", "image": "https://media.routard.com/image/93/1/vieux-port-de-nuit.1612931.w630.jpg"},
  {"code": "14", "nom": "Calvados", "chef_lieu": "Caen", "image": "https://lp-cms-production.imgix.net/2019-06/a0782b217b230309682ef3dfefdf69fd-caen.jpg?auto=format&w=1920&h=640&fit=crop&crop=faces,edges&q=75"},
  {"code": "15", "nom": "Cantal", "chef_lieu": "Aurillac", "image": "https://img.lamontagne.fr/jgeZDoSpcd37oyxrvYiFPl4PjWUE6Xai4elhBJysc18/fit/657/438/sm/0/bG9jYWw6Ly8vMDAvMDAvMDYvMzgvOTQvMjAwMDAwNjM4OTQ5Ng.jpg"},
  {"code": "16", "nom": "Charente", "chef_lieu": "Angoulême", "image": "https://paris-jetequitte.com/wp-content/uploads/2021/06/vivre-angouleme-J5.-07.-angouleme-ville-rempars-19-Flow-Velo-Aurelie-Stapf-porteurdesonge.com_.jpg.webp"},
  {"code": "17", "nom": "Charente-Maritime", "chef_lieu": "La Rochelle", "image": "https://scontent-mrs2-1.xx.fbcdn.net/v/t39.30808-6/277803057_10159330560323891_6424691961801036095_n.jpg?stp=c0.5000x0.5000f_dst-jpg_e15_p3025x1210_q60_tt1_u&efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV91cmwifQ&_nc_cid=0&_nc_ad=z-m&_nc_ht=scontent-mrs2-1.xx&_nc_cat=103&_nc_ohc=xAY9CsF1ipgQ7kNvgGSsyLc&ccb=1-7&_nc_sid=5f2048&oh=00_AYCh1VnvfWSld9unEJBKVu_PhbCCvcHcwenfrspwxQ72nA&oe=6643FC23"},
  {"code": "18", "nom": "Cher", "chef_lieu": "Bourges", "image": "https://navaway.fr/wp-content/uploads/2022/05/Bourges.jpg"},
  {"code": "19", "nom": "Corrèze", "chef_lieu": "Tulle", "image": "https://i-de.unimedias.fr/2023/12/07/tulle-quai-14-6571e7b36207d.jpg?auto=format%2Ccompress&crop=faces&cs=tinysrgb&fit=max&w=1050"},
  {"code": "21", "nom": "Côte-d'Or", "chef_lieu": "Dijon", "image": "https://i0.wp.com/blog.mappy.com/wp-content/uploads/2023/04/0b98e-istock-1074291938-blog.png?resize=696%2C316&ssl=1"},
  {"code": "22", "nom": "Côtes-d'Armor", "chef_lieu": "Saint-Brieuc", "image": "https://www.hotel-duguesclin.fr/bases/bandeau_image/grande/20/Bsbpc-aa7225_BERTHIER-Emmanuel.jpeg"},
  {"code": "23", "nom": "Creuse", "chef_lieu": "Guéret", "image": "https://i-de.unimedias.fr/2023/12/07/st-vaury-01-6571e288e2857.jpg?auto=format%2Ccompress&crop=faces&cs=tinysrgb&fit=crop&h=501&w=890"},
  {"code": "24", "nom": "Dordogne", "chef_lieu": "Périgueux", "image": "https://www.aquitaineonline.com/images/stories/Dordogne_2021/perigueux-010122A.jpg"},
  {"code": "25", "nom": "Doubs", "chef_lieu": "Besançon", "image": "https://media.lesechos.com/api/v1/images/view/5dc031c2d286c2107f388c06/1280x720-webp/0602180364949-web-tete.webp"},
  {"code": "26", "nom": "Drôme", "chef_lieu": "Valence", "image": "https://www.locabox.fr/media/cache/resolve/optimized/uploads/files/page/625fba7d05547848708764.jpg"},
  {"code": "27", "nom": "Eure", "chef_lieu": "Évreux", "image": "https://partir.ouest-france.fr/magazine/wp-content/uploads/2023/09/evreux-scaled.jpeg"},
  {"code": "28", "nom": "Eure-et-Loir", "chef_lieu": "Chartres", "image": "https://img.olympics.com/images/image/private/t_s_16_9_g_auto/t_s_w2440/f_auto/primary/lgk9krheofjhagar3ivd"},
  {"code": "29", "nom": "Finistère", "chef_lieu": "Quimper", "image": "https://www.trecobois.fr/wp-content/uploads/2021/07/quimper-1536x1028.jpg"},
  {"code": "2A", "nom": "Corse-du-Sud", "chef_lieu": "Ajaccio", "image": "https://www.costacroisieres.fr/content/dam/costa/costa-magazine/articles-magazine/travel/ajaccio-travel/ajaccio_d.jpg.image.1296.974.high.jpg"},
  {"code": "2B", "nom": "Haute-Corse", "chef_lieu": "Bastia", "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/7c/51/8e/belle-vue.jpg?w=2000&h=800&s=1"},
  {"code": "30", "nom": "Gard", "chef_lieu": "Nîmes", "image": "https://images.winalist.com/blog/wp-content/uploads/2021/05/26144008/AdobeStock_277499536-1536x1024.jpeg"},
  {"code": "31", "nom": "Haute-Garonne", "chef_lieu": "Toulouse", "image": "https://cdn.laetis.fr/i/crtocc/full/https://www.tourisme-occitanie.com/uploads/2018/9/les-quais-de-garonne_d-viet-crt-occitanie.jpg"},
  {"code": "32", "nom": "Gers", "chef_lieu": "Auch", "image": "https://www.auch-tourisme.com/wp-content/uploads/2020/09/L-instantc-18-1354x900.jpg"},
  {"code": "33", "nom": "Gironde", "chef_lieu": "Bordeaux", "image": "https://www.bordeauxmarchesolidaire.fr/wp-content/uploads/2021/12/standard_compressed_6080155627_ab87538792_b.jpg"},
  {"code": "34", "nom": "Hérault", "chef_lieu": "Montpellier", "image": "https://cdn.generationvoyage.fr/2020/11/equipe-montpellier-1536x647.jpg"},
  {"code": "35", "nom": "Ille-et-Vilaine", "chef_lieu": "Rennes", "image": "https://www.tourisme-rennes.com/voy_content/uploads/2023/09/Patrimoine-rennes-vuduciel.jpg"},
  {"code": "36", "nom": "Indre", "chef_lieu": "Châteauroux", "image": "https://www.chateauroux-tourisme.com/app/uploads/iris-images/5483/2019-cht-raoul-cp-cm-benjamin-steimes-650x780-f50_50.webp"},
  {"code": "37", "nom": "Indre-et-Loire", "chef_lieu": "Tours", "image": "https://www.tours.fr/app/uploads/2023/01/FL20220802153421-%C2%A9-Ville-de-Tours-F.-Lafite-.jpg"},
  {"code": "38", "nom": "Isère", "chef_lieu": "Grenoble", "image": "https://www.lehub-privilodges.com/wp-content/uploads/2019/05/ville-grenoble.jpg.webp"},
  {"code": "39", "nom": "Jura", "chef_lieu": "Lons-le-Saunier", "image": "https://www.guides-france.com/wp-content/uploads/2021/07/Visite-Guidee-Lons-le-Saunier.jpg"},
  {"code": "40", "nom": "Landes", "chef_lieu": "Mont-de-Marsan", "image": "https://www.guide-des-landes.com/_bibli/articlesPage/40/images/confluence-teddy-bear-photos.jpg?v=ficheArticle&width=819&height=540&pixelRatio=2.0000"},
  {"code": "41", "nom": "Loir-et-Cher", "chef_lieu": "Blois", "image": "https://www.blois.fr/sites/default/files/styles/original/public/media/images/blois-chateauroyal-201506-jpthibault-jdavid_0.jpg?itok=EE0EZoxQ"},
  {"code": "42", "nom": "Loire", "chef_lieu": "Saint-Étienne", "image": "https://www.sncf-connect.com/assets/styles/ratio_2_1_max_width_961/public/media/2022-04/barrage-de-grangent-loire-saint-etienne.jpg?h=5df09f47&itok=i-C5uEBE"},
  {"code": "43", "nom": "Haute-Loire", "chef_lieu": "Le Puy-en-Velay", "image": "https://tribunedelyon.fr/wp-content/uploads/sites/5/2023/10/photo-2-luc-olivier.jpg"},
  {"code": "44", "nom": "Loire-Atlantique", "chef_lieu": "Nantes", "image": "https://institut-superieur-environnement.com/content/uploads/2023/01/nantes-capitale-verte.webp"},
  {"code": "45", "nom": "Loiret", "chef_lieu": "Orléans", "image": "https://bonjourorleans.fr/wp-content/uploads/2016/04/placedumatroi-orleans-statue-jeanne-arc.jpg"},
  {"code": "46", "nom": "Lot", "chef_lieu": "Cahors", "image": "https://www.sncf-connect.com/assets/styles/ratio_2_1_max_width_961/public/media/2022-02/cahors-vue-generale.jpg?h=f101bc3b&itok=OkoNINoL"},
  {"code": "47", "nom": "Lot-et-Garonne", "chef_lieu": "Agen", "image": "https://mediaim.expedia.com/destination/1/aa4738b86051cde869b26325dda062a0.jpg?impolicy=fcrop&w=1040&h=580&q=mediumHigh"},
  {"code": "48", "nom": "Lozère", "chef_lieu": "Mende", "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/0f/2c/c0/vue-du-pont-notre-dame.jpg?w=2400&h=1000&s=1"},
  {"code": "49", "nom": "Maine-et-Loire", "chef_lieu": "Angers", "image": "https://www.tourisme.destination-angers.com/sites/angers-tourisme/files/styles/ratio_16_9_xl/public/content/images/chateau-angers-vue-aerienne-c-alexandre-lamoureux.jpg?itok=R0N6nPOk"},
  {"code": "50", "nom": "Manche", "chef_lieu": "Saint-Lô", "image": "https://www.normandie-tourisme.fr/wp-content/uploads/2022/12/remparts-fortifications-saint-lo-anibas-photography-955x600.jpg"},
  {"code": "51", "nom": "Marne", "chef_lieu": "Châlons-en-Champagne", "image": "https://woody.cloudly.space/app/uploads/chalons-en-champagne/2021/04/thumbs/place-de-la-republique-pan-de-bois-fontaine-teddy-picaude-1920x960.jpg"},
  {"code": "52", "nom": "Haute-Marne", "chef_lieu": "Chaumont", "image": "https://www.bienvenue-hautemarne.fr/wp-content/uploads/2023/05/dsc-1569-1-1280x709.jpg"},
  {"code": "53", "nom": "Mayenne", "chef_lieu": "Laval", "image": "https://woody.cloudly.space/app/uploads/tourisme-mayenne/2019/07/thumbs/chateau-musee-laval-1-1920x960.jpg"},
  {"code": "54", "nom": "Meurthe-et-Moselle", "chef_lieu": "Nancy", "image": "https://i.f1g.fr/media/cms/704x396_cropupscale/2022/11/03/a2c7fc86c6b887959f61fd704ff9d8c2bbc1c34f774d3dc41654207db787be9d.jpg"},
  {"code": "55", "nom": "Meuse", "chef_lieu": "Bar-le-Duc", "image": "https://www.blelorraine.fr/wp-content/uploads/2020/10/pont-Bar-le-Duc.jpg"},
  {"code": "56", "nom": "Morbihan", "chef_lieu": "Vannes", "image": "https://morbihan.com/app/uploads/morbihan/2023/08/thumbs/Patrice-BAISSAC-DSC_7725-Vannes-ok-Presse-13-12-2024-1920x960.jpg"},
  {"code": "57", "nom": "Moselle", "chef_lieu": "Metz", "image": "https://cdn-s-www.leprogres.fr/images/66821704-DA7C-41E1-B48D-E22921BBDDCD/NW_detail/le-jardin-ephemere-installe-sur-la-place-de-la-comedie-fait-partie-d-espaces-verts-couvrant-pres-d-un-quart-de-la-superficie-de-la-ville-photo-philippe-gisselbrecht-ville-de-metz-1620988148.jpg"},
  {"code": "58", "nom": "Nièvre", "chef_lieu": "Nevers", "image": "https://www.nievre-tourisme.com/uploads/2021/02/en-tete-nevers-pont-de-loire-fmr-travel-blog-1600x900.jpg"},
  {"code": "59", "nom": "Nord", "chef_lieu": "Lille", "image": "https://uploads.lebonbon.fr/source/2023/march/2043048/ville-lille_1_2000.jpg"},
  {"code": "60", "nom": "Oise", "chef_lieu": "Beauvais", "image": "https://www.terre.tv/wp-content/uploads/2022/08/que-faire-a-beauvais-1024x679.jpg.webp"},
  {"code": "61", "nom": "Orne", "chef_lieu": "Alençon", "image": "https://www.villes-sanctuaires.com/sites/default/files/styles/page-display-xs/public/alencon-histoire-2.jpg?itok=OETe9XkK"},
  {"code": "62", "nom": "Pas-de-Calais", "chef_lieu": "Arras", "image": "https://woody.cloudly.space/app/uploads/crt-hautsdefrance/2020/12/thumbs/arras-beffroi-ot-arras-pays-dartois-tama66-640x320-crop-1610626064.jpg"},
  {"code": "63", "nom": "Puy-de-Dôme", "chef_lieu": "Clermont-Ferrand", "image": "https://www.chu-clermontferrand.fr/sites/default/files/styles/2220xauto/public/media/2021-03/Angelus%20YODASON%20%28CC%20BY%202.0%29.jpg?itok=veDFn8V2"},
  {"code": "64", "nom": "Pyrénées-Atlantiques", "chef_lieu": "Pau", "image": "https://www.guide-bearn-pyrenees.com/_bibli/articlesPage/154/images/adobestock-jeanmichel-top-10-a-faire-a-pau.jpg?v=ficheArticle&width=819&height=540&pixelRatio=2.0000"},
  {"code": "65", "nom": "Hautes-Pyrénées", "chef_lieu": "Tarbes", "image": "https://homnicity.com/wp-content/uploads/2020/10/homnicity-tarbes.jpg"},
  {"code": "66", "nom": "Pyrénées-Orientales", "chef_lieu": "Perpignan", "image": "https://images.winalist.com/blog/wp-content/uploads/2021/05/26144011/AdobeStock_171790454-1536x1024.jpeg"},
  {"code": "67", "nom": "Bas-Rhin", "chef_lieu": "Strasbourg", "image": "https://content.r9cdn.net/rimg/dimg/ff/d1/b45bd509-city-13597-164c828f0b0.jpg?crop=true&width=1020&height=498"},
  {"code": "68", "nom": "Haut-Rhin", "chef_lieu": "Colmar", "image": "https://www.brithotel.fr/images/resized/categories_minisite_diapo/photos_1280/centre-ville-colmar.jpg"},
  {"code": "69", "nom": "Rhône", "chef_lieu": "Lyon", "image": "https://www.aflyon.org/wp-content/uploads/2023/06/bandeau-lyon-vue-fourviere-1200x497.jpg"},
  {"code": "70", "nom": "Haute-Saône", "chef_lieu": "Vesoul", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Vieux-Vesoul.jpg/560px-Vieux-Vesoul.jpg"},
  {"code": "71", "nom": "Saône-et-Loire", "chef_lieu": "Mâcon", "image": "https://www.meteocity.com/images/cache/large_webp/images/download/blocks/macon-shutterstock-1331677220-6267e646391e2110082732.webp"},
  {"code": "72", "nom": "Sarthe", "chef_lieu": "Le Mans", "image": "https://www.lemans.fr/fileadmin/_processed_files_storage_ajaris/7/3/csm_lm_0093940_098a0d0da9.jpg"},
  {"code": "73", "nom": "Savoie", "chef_lieu": "Chambéry", "image": "https://www.voyageway.com/wp-content/uploads/2019/10/visiter-chambery.jpg"},
  {"code": "74", "nom": "Haute-Savoie", "chef_lieu": "Annecy", "image": "https://onyvatravel.com/wp-content/uploads/2021/03/onyvatravel-france-annecy-vieille-ville-1920x1281.jpg"},
  {"code": "75", "nom": "Paris", "chef_lieu": "Paris", "image": "https://media.routard.com/image/39/2/paris-de-nuit.1564392.w740.jpg"},
  {"code": "76", "nom": "Seine-Maritime", "chef_lieu": "Rouen", "image": "https://cdn.generationvoyage.fr/2020/08/Une-Rouen-S-F.jpg"},
  {"code": "77", "nom": "Seine-et-Marne", "chef_lieu": "Melun", "image": "https://a.travel-assets.com/findyours-php/viewfinder/images/res70/106000/106875-Melun.jpg?impolicy=fcrop&w=1040&h=580&q=mediumHigh"},
  {"code": "78", "nom": "Yvelines", "chef_lieu": "Versailles", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Vue_a%C3%A9rienne_du_domaine_de_Versailles_par_ToucanWings_-_Creative_Commons_By_Sa_3.0_-_073.jpg/2560px-Vue_a%C3%A9rienne_du_domaine_de_Versailles_par_ToucanWings_-_Creative_Commons_By_Sa_3.0_-_073.jpg"},
  {"code": "79", "nom": "Deux-Sèvres", "chef_lieu": "Niort", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/View_of_%C3%89glise_Saint-Andr%C3%A9_and_Les_Vieux_Ponts%2C_Niort.jpg/560px-View_of_%C3%89glise_Saint-Andr%C3%A9_and_Les_Vieux_Ponts%2C_Niort.jpg"},
  {"code": "80", "nom": "Somme", "chef_lieu": "Amiens", "image": "https://i.notretemps.com/1400x787/smart/2022/10/25/amiens-quai-belu.jpeg"},
  {"code": "81", "nom": "Tarn", "chef_lieu": "Albi", "image": "https://www.albi-tourisme.fr/app/uploads/iris-images/2285/4-la-cathei-drale-vue-du-pont-neuf-3-min-1920x1080-f50_50.jpg"},
  {"code": "82", "nom": "Tarn-et-Garonne", "chef_lieu": "Montauban", "image": "https://www.guide-tarn-aveyron.com/_bibli/articlesPage/119/images/adobestock-jackf-montauban.jpg?v=ficheArticle&width=819&height=540&pixelRatio=2.0000"},
  {"code": "83", "nom": "Var", "chef_lieu": "Toulon", "image": "https://ideat.fr/wp-content/thumbnails/uploads/sites/3/2023/08/toulon-1-scaled-tt-width-740-height-474-crop-1-bgcolor-ffffff-except_gif-1.jpg"},
  {"code": "84", "nom": "Vaucluse", "chef_lieu": "Avignon", "image": "https://media.roole.fr/_next/image?url=https%3A%2F%2Fassets.prod.roole.fr%2Fdata%2Fassets%2Fi_Stock_1354233497_66e7ac7831.jpg&w=3840&q=75"},
  {"code": "85", "nom": "Vendée", "chef_lieu": "La Roche-sur-Yon", "image": "https://www.destination-larochesuryon.fr/wp-content/uploads/wpetourisme/La-Roche-sur-Yon--c--Ville-de-La-Roche-sur-Yon-780x560.jpg"},
  {"code": "86", "nom": "Vienne", "chef_lieu": "Poitiers", "image": "https://www.petitfute.com/medias/mag/32070/originale/AdobeStock_605918125-1024x683.jpeg"},
  {"code": "87", "nom": "Haute-Vienne", "chef_lieu": "Limoges", "image": "https://res.cloudinary.com/lastminute-contenthub/s--XygVAslo--/c_limit,h_999999,w_1920/f_auto/q_auto:eco/v1/DAM/Photos/Destinations/Europe/France/Limoges/shutterstock_1831952194"},
  {"code": "88", "nom": "Vosges", "chef_lieu": "Épinal", "image": "https://www.ou-et-quand.net/partir/images/illustration/thumb/300/200/epinal_541.jpg"},
  {"code": "89", "nom": "Yonne", "chef_lieu": "Auxerre", "image": "https://www.bourgogne-tourisme.com/uploads/2023/06/auxerre-vue-sur-la-ville-et-la-cathedrale-saint-etienne-1600x900.jpg"},
  {"code": "90", "nom": "Territoire de Belfort", "chef_lieu": "Belfort", "image": "https://cdn-s-www.estrepublicain.fr/images/70B45E29-D022-4945-81C1-C49B1CE38D68/NW_detail/avec-le-numero-90-le-departement-du-territoire-est-le-plus-recent-de-france-hormis-les-departements-d-ile-de-france-photo-er-isabelle-petitlaurent-1595580241.jpg"},
  {"code": "91", "nom": "Essonne", "chef_lieu": "Évry-Courcouronnes", "image": "https://www.francebleu.fr/s3/cruiser-production/2023/01/0b5bf974-b2f9-4a9f-8b4f-079f9e32ef6d/1200x680_capitale-place-droits-de-homme-et-citoyen-evry-courcouronnes-credit-angelique-mian.jpg"},
  {"code": "92", "nom": "Hauts-de-Seine", "chef_lieu": "Nanterre", "image": "https://content.r9cdn.net/rimg/dimg/dd/45/a2191129-city-16829-170a91c7488.jpg?crop=true&width=2160&height=1215&xhint=2498&yhint=1757&outputtype=webp"},
  {"code": "93", "nom": "Seine-Saint-Denis", "chef_lieu": "Bobigny", "image": "https://www.bobigny.fr/fileadmin/_processed_/b/6/csm_20171018_hp_tram_007_162ae2f268.jpg"},
  {"code": "94", "nom": "Val-de-Marne", "chef_lieu": "Créteil", "image": "https://www.ville-creteil.fr/img/creteil-ville-de-transition-une.jpg"},
  {"code": "95", "nom": "Val-d'Oise", "chef_lieu": "Cergy", "image": "https://imavenir.com/wp-content/uploads/2020/07/investir-immobilier-cergy-pontoise.png"}
]


for image in images:
    try:
        image_url = image["image"]
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()  # Ensure the request was successful
        img = Image.open(BytesIO(response.content))
        
        # Extract the filename from the URL and change extension to `.webp`
        original_name = os.path.basename(image_url)
        base_name, _ = os.path.splitext(original_name)
        webp_name = f"{base_name}.webp"
        
        # Save the image in WEBP format with the original name
        img.save(webp_name, format="WEBP")
        print(f"Saved: {webp_name}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image {image_url}: {e}")
    except Exception as ex:
        print(f"Error processing image {image_url}: {ex}")
